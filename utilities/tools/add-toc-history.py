#!/usr/bin/env python3
"""
T204-T205: Add Table of Contents and History Sections
Adds TOC after the first H1 heading and History section at the bottom of all markdown files.

Usage:
    python add-toc-history.py                    # Dry-run on current directory
    python add-toc-history.py --execute          # Execute on current directory
    python add-toc-history.py --path /path/to/dir --execute
    python add-toc-history.py --help

Exit codes:
    0 - Success
    1 - Error
"""

import argparse
import re
import sys
from datetime import date
from pathlib import Path
from typing import NamedTuple


class ProcessingResult(NamedTuple):
    """Represents the result of processing a file."""
    file_path: str
    toc_added: bool
    history_added: bool
    skipped_toc: bool
    skipped_history: bool
    error: str | None


# Directories to exclude
EXCLUDED_DIRS = [
    "node_modules",
    ".git",
    "_backup",
    "--old-structure",
]


def should_exclude_path(path: Path) -> bool:
    """Check if the path should be excluded based on directory patterns."""
    path_str = str(path).replace("\\", "/")
    for excluded in EXCLUDED_DIRS:
        if excluded in path_str:
            return True
    return False


def extract_headings(content: str) -> list[tuple[int, str, str]]:
    """
    Extract H2 and H3 headings from markdown content.

    Returns:
        List of tuples: (level, heading_text, anchor_id)
    """
    headings = []
    # Match ## and ### headings (not inside code blocks)
    in_code_block = False

    for line in content.split("\n"):
        # Track code blocks
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            continue

        if in_code_block:
            continue

        # Match H2 and H3
        h2_match = re.match(r"^##\s+(.+)$", line)
        h3_match = re.match(r"^###\s+(.+)$", line)

        if h2_match:
            heading_text = h2_match.group(1).strip()
            anchor = generate_anchor(heading_text)
            headings.append((2, heading_text, anchor))
        elif h3_match:
            heading_text = h3_match.group(1).strip()
            anchor = generate_anchor(heading_text)
            headings.append((3, heading_text, anchor))

    return headings


def generate_anchor(heading: str) -> str:
    """
    Generate a GitHub-compatible anchor ID from a heading.

    Removes emojis, special characters, converts to lowercase,
    and replaces spaces with hyphens.
    """
    # Remove emojis and special characters (keep alphanumeric, spaces, hyphens)
    anchor = re.sub(r"[^\w\s-]", "", heading, flags=re.UNICODE)
    # Remove extra whitespace
    anchor = " ".join(anchor.split())
    # Convert to lowercase and replace spaces with hyphens
    anchor = anchor.lower().replace(" ", "-")
    # Remove consecutive hyphens
    anchor = re.sub(r"-+", "-", anchor)
    # Strip leading/trailing hyphens
    anchor = anchor.strip("-")
    return anchor


def generate_toc(headings: list[tuple[int, str, str]]) -> str:
    """
    Generate a Table of Contents markdown section.

    Args:
        headings: List of (level, heading_text, anchor) tuples

    Returns:
        TOC markdown string
    """
    if not headings:
        return ""

    lines = ["", "## Table of Contents", ""]

    for level, text, anchor in headings:
        # Skip the Table of Contents heading itself and History section
        if text.lower() in ["table of contents", "history"]:
            continue

        # Indent H3 headings
        indent = "  " if level == 3 else ""
        lines.append(f"{indent}- [{text}](#{anchor})")

    lines.append("")
    return "\n".join(lines)


def generate_history_section() -> str:
    """Generate the History section markdown."""
    today = date.today().isoformat()
    return f"""
---

## History

| Date | Author | Changes |
|------|--------|---------|
| {today} | Migration | Initial TOC and history section added |
"""


def has_toc(content: str) -> bool:
    """Check if the content already has a Table of Contents section."""
    # Look for ## Table of Contents (case-insensitive, allows emojis/prefixes)
    return bool(re.search(r"^##\s+.*Table\s+of\s+Contents", content, re.MULTILINE | re.IGNORECASE))


def has_history(content: str) -> bool:
    """Check if the content already has a History section."""
    # Look for ## History (case-insensitive)
    return bool(re.search(r"^##\s+History", content, re.MULTILINE | re.IGNORECASE))


def find_first_h1_position(content: str) -> tuple[int, int] | None:
    """
    Find the position after the first H1 heading.

    Returns:
        Tuple of (line_index, char_position) after the H1 line, or None if not found.
    """
    lines = content.split("\n")
    in_frontmatter = False
    frontmatter_ended = False

    for i, line in enumerate(lines):
        # Handle YAML frontmatter
        if i == 0 and line.strip() == "---":
            in_frontmatter = True
            continue
        if in_frontmatter:
            if line.strip() == "---":
                in_frontmatter = False
                frontmatter_ended = True
            continue

        # Look for H1 (# Heading)
        if re.match(r"^#\s+.+$", line):
            # Return position after this line
            return i, sum(len(l) + 1 for l in lines[:i+1])

    return None


def process_file(file_path: Path, execute: bool = False) -> ProcessingResult:
    """
    Process a single markdown file to add TOC and History sections.

    Args:
        file_path: Path to the markdown file
        execute: If True, actually modify the file; if False, dry-run

    Returns:
        ProcessingResult with details of what was/would be done
    """
    file_str = str(file_path)

    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception as e:
        return ProcessingResult(
            file_path=file_str,
            toc_added=False,
            history_added=False,
            skipped_toc=False,
            skipped_history=False,
            error=f"Could not read file: {e}"
        )

    toc_added = False
    history_added = False
    skipped_toc = has_toc(content)
    skipped_history = has_history(content)

    modified_content = content

    # Add TOC if not present
    if not skipped_toc:
        h1_pos = find_first_h1_position(content)
        if h1_pos is not None:
            headings = extract_headings(content)
            # Filter out headings that come before the TOC would be inserted
            toc = generate_toc(headings)

            if toc:  # Only add if there are headings to list
                line_idx, char_pos = h1_pos
                lines = modified_content.split("\n")
                # Insert TOC after the H1 line
                lines.insert(line_idx + 1, toc.rstrip())
                modified_content = "\n".join(lines)
                toc_added = True

    # Add History section if not present
    if not skipped_history:
        history = generate_history_section()
        # Ensure we don't double up on newlines at the end
        modified_content = modified_content.rstrip() + history
        history_added = True

    # Write if executing and changes were made
    if execute and (toc_added or history_added):
        try:
            file_path.write_text(modified_content, encoding="utf-8")
        except Exception as e:
            return ProcessingResult(
                file_path=file_str,
                toc_added=False,
                history_added=False,
                skipped_toc=skipped_toc,
                skipped_history=skipped_history,
                error=f"Could not write file: {e}"
            )

    return ProcessingResult(
        file_path=file_str,
        toc_added=toc_added,
        history_added=history_added,
        skipped_toc=skipped_toc,
        skipped_history=skipped_history,
        error=None
    )


def find_markdown_files(directory: Path) -> list[Path]:
    """
    Find all markdown files in a directory, excluding specified patterns.

    Args:
        directory: Root directory to search

    Returns:
        List of Path objects for markdown files
    """
    md_files = []

    for md_file in directory.rglob("*.md"):
        if not should_exclude_path(md_file):
            md_files.append(md_file)

    return sorted(md_files)


def main() -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Add Table of Contents and History sections to markdown files.",
        epilog="""
Examples:
  python add-toc-history.py                          # Dry-run in current directory
  python add-toc-history.py --execute                # Execute in current directory
  python add-toc-history.py --path ./docs --execute  # Execute in specific directory
  python add-toc-history.py --verbose                # Show detailed output

Behavior:
  - TOC is added after the first H1 heading
  - TOC is generated from H2 and H3 headings
  - History section is added at the bottom of the file
  - Files already containing these sections are skipped

Excluded directories:
  node_modules, .git, _backup*, --old-structure*
        """
    )
    parser.add_argument(
        "--path",
        type=Path,
        default=Path.cwd(),
        help="Directory to process (default: current directory)"
    )
    parser.add_argument(
        "--execute",
        action="store_true",
        help="Actually modify files (default is dry-run)"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Show verbose output including per-file details"
    )
    parser.add_argument(
        "-q", "--quiet",
        action="store_true",
        help="Suppress all output except errors"
    )

    args = parser.parse_args()

    if not args.path.is_dir():
        print(f"Error: {args.path} is not a directory")
        return 1

    mode = "EXECUTE" if args.execute else "DRY-RUN"

    if not args.quiet:
        print(f"{'='*60}")
        print(f"Add TOC and History Sections - {mode} Mode")
        print(f"{'='*60}")
        print(f"Directory: {args.path.absolute()}")
        print()

    # Find all markdown files
    md_files = find_markdown_files(args.path)

    if not args.quiet:
        print(f"Found {len(md_files)} markdown files to process")
        print()

    # Process each file
    results: list[ProcessingResult] = []
    for md_file in md_files:
        result = process_file(md_file, execute=args.execute)
        results.append(result)

        if args.verbose and not args.quiet:
            status_parts = []
            if result.toc_added:
                status_parts.append("TOC added")
            elif result.skipped_toc:
                status_parts.append("TOC exists")
            else:
                status_parts.append("No H1/headings")

            if result.history_added:
                status_parts.append("History added")
            elif result.skipped_history:
                status_parts.append("History exists")

            if result.error:
                status_parts.append(f"ERROR: {result.error}")

            print(f"  {md_file}: {', '.join(status_parts)}")

    # Calculate statistics
    toc_added_count = sum(1 for r in results if r.toc_added)
    history_added_count = sum(1 for r in results if r.history_added)
    toc_skipped_count = sum(1 for r in results if r.skipped_toc)
    history_skipped_count = sum(1 for r in results if r.skipped_history)
    error_count = sum(1 for r in results if r.error)

    if not args.quiet:
        print()
        print(f"{'='*60}")
        print("Summary")
        print(f"{'='*60}")
        print(f"Total files processed: {len(results)}")
        print()
        print("Table of Contents:")
        print(f"  - Added:   {toc_added_count}")
        print(f"  - Skipped (already exists): {toc_skipped_count}")
        print(f"  - No H1/headings: {len(results) - toc_added_count - toc_skipped_count}")
        print()
        print("History Section:")
        print(f"  - Added:   {history_added_count}")
        print(f"  - Skipped (already exists): {history_skipped_count}")
        print()
        if error_count > 0:
            print(f"Errors: {error_count}")
            for r in results:
                if r.error:
                    print(f"  - {r.file_path}: {r.error}")

        if not args.execute:
            print()
            print("NOTE: This was a DRY-RUN. No files were modified.")
            print("      Run with --execute to apply changes.")

    return 0 if error_count == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
