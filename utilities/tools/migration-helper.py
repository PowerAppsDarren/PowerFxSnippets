#!/usr/bin/env python3
"""
T012: Migration Helper
Assists with file migrations, adding/updating YAML frontmatter and fixing links.

Usage:
    python migration-helper.py <source_path> <dest_path> [--category <cat>]
    python migration-helper.py --help
"""

import argparse
import re
import shutil
import sys
from datetime import date
from pathlib import Path
from typing import Any

import yaml


# Default frontmatter template
DEFAULT_FRONTMATTER = {
    "title": "",
    "description": "",
    "category": "",
    "subcategory": "",
    "tags": [],
    "difficulty": "intermediate",
    "products": ["power-apps-canvas"],
    "dependencies": [],
    "author": "",
    "created": "",
    "updated": "",
    "license": "MIT",
    "related": [],
}


def extract_frontmatter(content: str) -> tuple[dict | None, str]:
    """
    Extract YAML frontmatter from markdown content.

    Returns:
        Tuple of (frontmatter_dict, body_content)
    """
    lines = content.split("\n")

    if not lines or lines[0].strip() != "---":
        return None, content

    end_index = -1
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end_index = i
            break

    if end_index == -1:
        return None, content

    yaml_content = "\n".join(lines[1:end_index])
    body_content = "\n".join(lines[end_index + 1:])

    try:
        frontmatter = yaml.safe_load(yaml_content)
        return frontmatter, body_content
    except yaml.YAMLError:
        return None, content


def generate_frontmatter_yaml(frontmatter: dict) -> str:
    """Generate YAML frontmatter string."""
    # Custom YAML dumper for better formatting
    class CustomDumper(yaml.SafeDumper):
        pass

    def str_representer(dumper: yaml.SafeDumper, data: str) -> yaml.ScalarNode:
        if "\n" in data:
            return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")
        if any(c in data for c in [":", "#", "'", '"', "{", "}", "[", "]"]):
            return dumper.represent_scalar("tag:yaml.org,2002:str", data, style='"')
        return dumper.represent_scalar("tag:yaml.org,2002:str", data)

    CustomDumper.add_representer(str, str_representer)

    yaml_str = yaml.dump(
        frontmatter,
        Dumper=CustomDumper,
        default_flow_style=False,
        allow_unicode=True,
        sort_keys=False,
        width=120,
    )

    return f"---\n{yaml_str}---\n"


def infer_title(file_path: Path, body_content: str) -> str:
    """Infer title from file name or first heading."""
    # Try to find first H1 heading
    h1_match = re.search(r"^#\s+(.+)$", body_content, re.MULTILINE)
    if h1_match:
        return h1_match.group(1).strip()

    # Fall back to filename
    return file_path.stem.replace("-", " ").replace("_", " ").title()


def infer_category(dest_path: Path) -> str:
    """Infer category from destination path."""
    parts = dest_path.parts

    # Look for common category indicators
    category_keywords = [
        "ui-controls", "functions", "data-operations", "patterns",
        "connectors", "components", "formulas", "errors", "controls"
    ]

    for part in parts:
        part_lower = part.lower().replace(" ", "-")
        if part_lower in category_keywords:
            return part_lower

    # Use parent directory name
    if len(parts) > 1:
        return parts[-2].lower().replace(" ", "-")

    return "uncategorized"


def infer_subcategory(dest_path: Path, category: str) -> str:
    """Infer subcategory from destination path."""
    parts = dest_path.parts

    # Find the part after the category
    try:
        cat_index = -1
        for i, part in enumerate(parts):
            if part.lower().replace(" ", "-") == category:
                cat_index = i
                break

        if cat_index >= 0 and cat_index < len(parts) - 2:
            return parts[cat_index + 1].lower().replace(" ", "-")
    except (ValueError, IndexError):
        pass

    return ""


def infer_tags(body_content: str, title: str, category: str) -> list[str]:
    """Infer tags from content."""
    tags = set()

    # Add category as tag
    if category and category != "uncategorized":
        tags.add(category.replace("-", " "))

    # Look for Power Fx keywords in content
    powerfx_keywords = [
        "Filter", "LookUp", "Collect", "Patch", "Navigate",
        "Set", "UpdateContext", "Concurrent", "ForAll",
        "Gallery", "DataTable", "Form", "Button", "TextInput",
        "OnSelect", "OnStart", "OnError", "OnVisible",
        "JSON", "ParseJSON", "Table", "Record",
    ]

    content_lower = body_content.lower()
    for keyword in powerfx_keywords:
        if keyword.lower() in content_lower:
            tags.add(keyword.lower())

    # Limit to 10 tags
    return sorted(list(tags))[:10]


def update_internal_links(content: str, source_path: Path, dest_path: Path) -> str:
    """Update relative links in content based on new file location."""
    # Find all markdown links: [text](path)
    link_pattern = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

    def update_link(match: re.Match) -> str:
        text = match.group(1)
        link_path = match.group(2)

        # Skip external links and anchors
        if link_path.startswith(("http://", "https://", "#", "mailto:")):
            return match.group(0)

        # Try to resolve and update relative path
        try:
            # Resolve the original link relative to source
            original_target = (source_path.parent / link_path).resolve()

            # Calculate new relative path from destination
            try:
                new_relative = original_target.relative_to(dest_path.parent.resolve())
                new_link = new_relative.as_posix()
            except ValueError:
                # Can't make relative, use absolute
                new_link = original_target.as_posix()

            return f"[{text}]({new_link})"
        except Exception:
            return match.group(0)

    return link_pattern.sub(update_link, content)


def migrate_file(
    source_path: Path,
    dest_path: Path,
    category: str | None = None,
    subcategory: str | None = None,
    author: str | None = None,
    force: bool = False,
    dry_run: bool = False,
    verbose: bool = False,
) -> tuple[bool, str]:
    """
    Migrate a file from source to destination.

    Returns:
        Tuple of (success, message)
    """
    # Validate source
    if not source_path.exists():
        return False, f"Source file does not exist: {source_path}"

    if not source_path.is_file():
        return False, f"Source is not a file: {source_path}"

    # Check destination
    if dest_path.exists() and not force:
        return False, f"Destination already exists: {dest_path}. Use --force to overwrite."

    # Read source content
    try:
        content = source_path.read_text(encoding="utf-8")
    except Exception as e:
        return False, f"Could not read source file: {e}"

    # Extract existing frontmatter
    existing_frontmatter, body_content = extract_frontmatter(content)

    # Build new frontmatter
    frontmatter = dict(DEFAULT_FRONTMATTER)

    if existing_frontmatter:
        # Merge with existing
        for key, value in existing_frontmatter.items():
            if value is not None:
                frontmatter[key] = value

    # Infer missing values
    if not frontmatter.get("title"):
        frontmatter["title"] = infer_title(dest_path, body_content)

    if not frontmatter.get("category"):
        frontmatter["category"] = category or infer_category(dest_path)
    elif category:
        frontmatter["category"] = category

    if not frontmatter.get("subcategory"):
        frontmatter["subcategory"] = subcategory or infer_subcategory(dest_path, frontmatter["category"])
    elif subcategory:
        frontmatter["subcategory"] = subcategory

    if not frontmatter.get("tags"):
        frontmatter["tags"] = infer_tags(body_content, frontmatter["title"], frontmatter["category"])

    if not frontmatter.get("author") and author:
        frontmatter["author"] = author

    # Set dates
    today = date.today().isoformat()
    if not frontmatter.get("created"):
        frontmatter["created"] = today
    frontmatter["updated"] = today

    # Update internal links
    updated_body = update_internal_links(body_content, source_path, dest_path)

    # Generate new content
    new_content = generate_frontmatter_yaml(frontmatter) + "\n" + updated_body.lstrip("\n")

    if dry_run:
        if verbose:
            print("=" * 60)
            print(f"Source: {source_path}")
            print(f"Destination: {dest_path}")
            print("=" * 60)
            print("Generated frontmatter:")
            print(generate_frontmatter_yaml(frontmatter))
            print("=" * 60)
        return True, f"Would migrate: {source_path} -> {dest_path}"

    # Create parent directories
    try:
        dest_path.parent.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        return False, f"Could not create destination directory: {e}"

    # Write destination file
    try:
        dest_path.write_text(new_content, encoding="utf-8")
    except Exception as e:
        return False, f"Could not write destination file: {e}"

    return True, f"Successfully migrated: {source_path} -> {dest_path}"


def main() -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Migrate markdown snippet files with frontmatter handling.",
        epilog="""
This tool helps migrate snippet files by:
  1. Moving the file to the new location
  2. Adding/updating YAML frontmatter if missing
  3. Creating parent directories as needed
  4. Updating internal relative links

Examples:
  # Basic migration
  python migration-helper.py old/snippet.md new/category/snippet.md

  # With explicit category
  python migration-helper.py snippet.md ui-controls/gallery/snippet.md --category ui-controls

  # Dry run to preview
  python migration-helper.py snippet.md new/path.md --dry-run --verbose
        """
    )
    parser.add_argument(
        "source",
        type=Path,
        help="Source file path"
    )
    parser.add_argument(
        "dest",
        type=Path,
        help="Destination file path"
    )
    parser.add_argument(
        "-c", "--category",
        help="Override category value"
    )
    parser.add_argument(
        "-s", "--subcategory",
        help="Override subcategory value"
    )
    parser.add_argument(
        "-a", "--author",
        help="Set author if not present"
    )
    parser.add_argument(
        "-f", "--force",
        action="store_true",
        help="Overwrite destination if it exists"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview migration without making changes"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Show verbose output"
    )

    args = parser.parse_args()

    source_path = args.source.resolve()
    dest_path = args.dest.resolve()

    success, message = migrate_file(
        source_path=source_path,
        dest_path=dest_path,
        category=args.category,
        subcategory=args.subcategory,
        author=args.author,
        force=args.force,
        dry_run=args.dry_run,
        verbose=args.verbose,
    )

    print(message)
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
