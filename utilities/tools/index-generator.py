#!/usr/bin/env python3
"""
T011: Index Generator
Generates search indices (SEARCH-INDEX.md, TAG-INDEX.md, DIFFICULTY-INDEX.md)
from all snippet files with YAML frontmatter.

Usage:
    python index-generator.py <snippets_dir> [--output-dir <dir>]
    python index-generator.py --help
"""

import argparse
import sys
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml


@dataclass
class SnippetMetadata:
    """Metadata extracted from a snippet file."""
    title: str
    description: str
    category: str
    subcategory: str
    tags: list[str]
    difficulty: str
    products: list[str]
    author: str
    created: str
    updated: str
    file_path: Path
    relative_path: str


def extract_frontmatter(content: str) -> dict | None:
    """Extract YAML frontmatter from markdown content."""
    lines = content.split("\n")

    if not lines or lines[0].strip() != "---":
        return None

    end_index = -1
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end_index = i
            break

    if end_index == -1:
        return None

    yaml_content = "\n".join(lines[1:end_index])
    try:
        return yaml.safe_load(yaml_content)
    except yaml.YAMLError:
        return None


def normalize_date(date_value: Any) -> str:
    """Normalize date to ISO string format."""
    if date_value is None:
        return ""
    if isinstance(date_value, datetime):
        return date_value.strftime("%Y-%m-%d")
    if hasattr(date_value, 'isoformat'):
        return date_value.isoformat()
    return str(date_value)


def scan_snippets(snippets_dir: Path, base_dir: Path) -> list[SnippetMetadata]:
    """
    Scan directory for markdown files and extract metadata.

    Args:
        snippets_dir: Directory to scan
        base_dir: Base directory for relative path calculation

    Returns:
        List of SnippetMetadata objects
    """
    snippets: list[SnippetMetadata] = []

    # Directories to exclude
    exclude_dirs = {
        ".specify", "ai-chats", "ai-protocols", ".github", ".git",
        ".repo-root", "utilities", "templates", "docs", ".darren"
    }
    exclude_files = {
        "README.md", "CLAUDE.md", "SEARCH-INDEX.md", "TAG-INDEX.md",
        "DIFFICULTY-INDEX.md", "INDEX.md", "RESUME.md", "CODE_OF_CONDUCT.md"
    }

    for md_file in snippets_dir.rglob("*.md"):
        # Skip excluded directories
        if any(part in exclude_dirs for part in md_file.parts):
            continue

        # Skip excluded files
        if md_file.name in exclude_files:
            continue

        try:
            content = md_file.read_text(encoding="utf-8")
        except Exception:
            continue

        frontmatter = extract_frontmatter(content)
        if frontmatter is None:
            continue

        # Extract required fields with defaults
        try:
            relative_path = md_file.relative_to(base_dir).as_posix()
        except ValueError:
            relative_path = md_file.name

        snippet = SnippetMetadata(
            title=frontmatter.get("title", md_file.stem),
            description=frontmatter.get("description", ""),
            category=frontmatter.get("category", "uncategorized"),
            subcategory=frontmatter.get("subcategory", ""),
            tags=frontmatter.get("tags", []) or [],
            difficulty=frontmatter.get("difficulty", ""),
            products=frontmatter.get("products", []) or [],
            author=frontmatter.get("author", ""),
            created=normalize_date(frontmatter.get("created")),
            updated=normalize_date(frontmatter.get("updated")),
            file_path=md_file,
            relative_path=relative_path,
        )
        snippets.append(snippet)

    return snippets


def generate_search_index(snippets: list[SnippetMetadata]) -> str:
    """Generate SEARCH-INDEX.md content."""
    lines = [
        "# Snippet Search Index",
        "",
        f"_Auto-generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}_",
        "",
        f"**Total Snippets:** {len(snippets)}",
        "",
        "## All Snippets",
        "",
        "| Title | Category | Tags | Difficulty | Path |",
        "|-------|----------|------|------------|------|",
    ]

    # Sort alphabetically by title
    sorted_snippets = sorted(snippets, key=lambda s: s.title.lower())

    for snippet in sorted_snippets:
        tags_str = ", ".join(snippet.tags[:5])  # Limit to 5 tags for display
        if len(snippet.tags) > 5:
            tags_str += "..."

        # Create markdown link
        title_link = f"[{snippet.title}]({snippet.relative_path})"

        lines.append(
            f"| {title_link} | {snippet.category} | {tags_str} | {snippet.difficulty} | `{snippet.relative_path}` |"
        )

    lines.extend([
        "",
        "---",
        "",
        "## Quick Stats",
        "",
    ])

    # Category counts
    category_counts: dict[str, int] = defaultdict(int)
    for s in snippets:
        category_counts[s.category] += 1

    lines.append("### By Category")
    lines.append("")
    for cat in sorted(category_counts.keys()):
        lines.append(f"- **{cat}**: {category_counts[cat]}")

    # Difficulty counts
    difficulty_counts: dict[str, int] = defaultdict(int)
    for s in snippets:
        if s.difficulty:
            difficulty_counts[s.difficulty] += 1

    lines.append("")
    lines.append("### By Difficulty")
    lines.append("")
    for diff in ["beginner", "intermediate", "advanced"]:
        if diff in difficulty_counts:
            lines.append(f"- **{diff}**: {difficulty_counts[diff]}")

    return "\n".join(lines)


def generate_tag_index(snippets: list[SnippetMetadata]) -> str:
    """Generate TAG-INDEX.md content."""
    # Build tag -> snippets mapping
    tag_map: dict[str, list[SnippetMetadata]] = defaultdict(list)
    for snippet in snippets:
        for tag in snippet.tags:
            # Convert tag to string in case it's not (e.g., integer tags)
            tag_str = str(tag).lower() if tag else ""
            if tag_str:
                tag_map[tag_str].append(snippet)

    lines = [
        "# Tag Index",
        "",
        f"_Auto-generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}_",
        "",
        f"**Total Tags:** {len(tag_map)}",
        "",
        "## Tags",
        "",
    ]

    # Sort tags alphabetically
    for tag in sorted(tag_map.keys()):
        tag_snippets = sorted(tag_map[tag], key=lambda s: s.title.lower())
        lines.append(f"### {tag} ({len(tag_snippets)})")
        lines.append("")
        for snippet in tag_snippets:
            lines.append(f"- [{snippet.title}]({snippet.relative_path})")
        lines.append("")

    return "\n".join(lines)


def generate_difficulty_index(snippets: list[SnippetMetadata]) -> str:
    """Generate DIFFICULTY-INDEX.md content."""
    # Build difficulty -> snippets mapping
    diff_map: dict[str, list[SnippetMetadata]] = defaultdict(list)
    for snippet in snippets:
        if snippet.difficulty:
            diff_map[snippet.difficulty.lower()].append(snippet)

    lines = [
        "# Difficulty Index",
        "",
        f"_Auto-generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}_",
        "",
        "Navigate snippets by difficulty level.",
        "",
    ]

    # Order: beginner, intermediate, advanced
    difficulty_order = ["beginner", "intermediate", "advanced"]
    difficulty_emoji = {
        "beginner": "Beginner",
        "intermediate": "Intermediate",
        "advanced": "Advanced"
    }

    for diff in difficulty_order:
        if diff in diff_map:
            diff_snippets = sorted(diff_map[diff], key=lambda s: s.title.lower())
            lines.append(f"## {difficulty_emoji.get(diff, diff.title())} ({len(diff_snippets)})")
            lines.append("")
            lines.append("| Title | Category | Description |")
            lines.append("|-------|----------|-------------|")
            for snippet in diff_snippets:
                desc = snippet.description[:80] + "..." if len(snippet.description) > 80 else snippet.description
                lines.append(f"| [{snippet.title}]({snippet.relative_path}) | {snippet.category} | {desc} |")
            lines.append("")

    # Handle uncategorized difficulty
    no_diff = [s for s in snippets if not s.difficulty]
    if no_diff:
        lines.append("## Uncategorized")
        lines.append("")
        for snippet in sorted(no_diff, key=lambda s: s.title.lower()):
            lines.append(f"- [{snippet.title}]({snippet.relative_path})")
        lines.append("")

    return "\n".join(lines)


def main() -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Generate search indices from snippet files.",
        epilog="""
Generated files:
  SEARCH-INDEX.md    - Searchable table with all snippets
  TAG-INDEX.md       - Snippets organized by tags
  DIFFICULTY-INDEX.md - Snippets organized by difficulty level

The generator scans for .md files with valid YAML frontmatter and
extracts metadata to build the indices. Files in .specify/, ai-chats/,
.github/, and utilities/ directories are excluded.
        """
    )
    parser.add_argument(
        "snippets_dir",
        type=Path,
        help="Directory containing snippet files to index"
    )
    parser.add_argument(
        "-o", "--output-dir",
        type=Path,
        default=None,
        help="Output directory for index files (default: snippets_dir)"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Show verbose output"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be generated without writing files"
    )

    args = parser.parse_args()

    snippets_dir = args.snippets_dir.resolve()
    output_dir = (args.output_dir or snippets_dir).resolve()

    if not snippets_dir.exists():
        print(f"Error: Snippets directory does not exist: {snippets_dir}", file=sys.stderr)
        return 1

    if args.verbose:
        print(f"Scanning: {snippets_dir}")

    # Scan for snippets
    snippets = scan_snippets(snippets_dir, snippets_dir)

    if args.verbose:
        print(f"Found {len(snippets)} snippet(s) with valid frontmatter")

    if not snippets:
        print("Warning: No snippets found with valid YAML frontmatter", file=sys.stderr)

    # Generate indices
    indices = [
        ("SEARCH-INDEX.md", generate_search_index(snippets)),
        ("TAG-INDEX.md", generate_tag_index(snippets)),
        ("DIFFICULTY-INDEX.md", generate_difficulty_index(snippets)),
    ]

    # Write files
    if not args.dry_run:
        output_dir.mkdir(parents=True, exist_ok=True)

    for filename, content in indices:
        output_path = output_dir / filename
        if args.dry_run:
            print(f"Would write: {output_path}")
            if args.verbose:
                print(f"  Content length: {len(content)} characters")
        else:
            output_path.write_text(content, encoding="utf-8")
            if args.verbose:
                print(f"Generated: {output_path}")

    if not args.dry_run:
        print(f"Successfully generated {len(indices)} index file(s) in {output_dir}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
