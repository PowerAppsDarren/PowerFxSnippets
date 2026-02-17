#!/usr/bin/env python3
"""
Fix broken internal markdown links after Phase 0 renaming.
Maps old numbered directory structure to new lowercase-with-dashes structure.
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Tuple

# Mapping of old paths to new paths based on README analysis and current structure
PATH_MAPPING = {
    # Old numbered structure -> New structure
    "01-getting-started": None,  # Need to find replacement
    "02-app-architecture": None,  # Need to find replacement
    "03-user-interface": None,  # Need to find replacement
    "04-data-management": None,  # Need to find replacement
    "05-business-logic": None,  # Need to find replacement
    "06-integrations": "integrations",
    "07-assets-and-media": "visual-assets",  # Likely mapping
    "08-advanced-patterns": None,  # Need to find replacement
    "09-learning-resources": "learning",

    # Sub-path mappings
    "02-app-architecture/app-events": "app-lifecycle",  # Best guess
    "02-app-architecture/navigation-patterns": "app-lifecycle",  # May need adjustment
    "02-app-architecture/performance-optimization": "best-practices",  # May need adjustment
    "03-user-interface/controls": "controls",
    "03-user-interface/themes-and-styling": "design",  # Best guess
    "04-data-management/data-sources": "data-sources",
    "04-data-management/data-validation": "data-operations",  # May need adjustment
    "04-data-management/data-visualization": "data-operations",  # May need adjustment
    "04-data-management/offline-capabilities": "data-operations",  # May need adjustment
    "05-business-logic/calculations": "functions",  # May need adjustment
    "05-business-logic/error-handling": "app-onerror",
    "05-business-logic/functions": "functions",
    "06-integrations/azure-services": "integrations",  # May have subdirectory
    "06-integrations/microsoft-365": "integrations",  # May have subdirectory
    "06-integrations/power-automate": "integrations",  # May have subdirectory
    "06-integrations/third-party-apis": "integrations",  # May have subdirectory
    "07-assets-and-media/icons": "icons",
    "07-assets-and-media/svgs": "visual-assets",  # May need adjustment
    "08-advanced-patterns/custom-components": "components",
    "08-advanced-patterns/security-patterns": "best-practices",  # May need adjustment
    "09-learning-resources/best-practices": "best-practices",
    "09-learning-resources/tutorials": "learning",
}


def find_all_markdown_files(root_dir: str) -> List[Path]:
    """Find all markdown files in the repository."""
    root = Path(root_dir)
    files = []
    for md_file in root.rglob("*.md"):
        # Skip backup directories and node_modules
        if '_backup_' in str(md_file) or 'node_modules' in str(md_file):
            continue
        files.append(md_file)
    return files


def extract_internal_links(content: str) -> List[Tuple[str, str]]:
    """
    Extract internal markdown links from content.
    Returns list of (full_match, link_path) tuples.
    """
    # Pattern: ](relative/path) - exclude http/https links
    pattern = r'\]\((\./[^)]+|(?!https?://)[^)]+)\)'
    matches = re.finditer(pattern, content)

    results = []
    for match in matches:
        full_match = match.group(0)
        link_path = match.group(1)
        # Normalize path - remove leading ./
        if link_path.startswith('./'):
            link_path = link_path[2:]
        results.append((full_match, link_path))

    return results


def check_if_path_exists(base_dir: Path, link_path: str) -> bool:
    """Check if a given path exists relative to base directory."""
    full_path = base_dir / link_path
    return full_path.exists()


def fix_link_path(link_path: str, mapping: Dict[str, str]) -> str:
    """
    Attempt to fix a broken link path using the mapping.
    Returns the fixed path or original if no mapping found.
    """
    # Try exact match first
    if link_path in mapping and mapping[link_path]:
        return mapping[link_path]

    # Try partial path matching (longest match wins)
    for old_path, new_path in sorted(mapping.items(), key=lambda x: len(x[0]), reverse=True):
        if link_path.startswith(old_path) and new_path:
            # Replace the old prefix with new prefix
            return link_path.replace(old_path, new_path, 1)

    return link_path  # Return original if no fix found


def analyze_broken_links(root_dir: str) -> Dict:
    """
    Analyze all markdown files and identify broken links.
    Returns statistics and broken link details.
    """
    root = Path(root_dir)
    md_files = find_all_markdown_files(root_dir)

    stats = {
        "total_files": len(md_files),
        "total_links": 0,
        "broken_links": 0,
        "files_with_broken_links": 0,
        "broken_by_file": {},
        "unique_broken_paths": set()
    }

    for md_file in md_files:
        try:
            content = md_file.read_text(encoding='utf-8')
            links = extract_internal_links(content)
            stats["total_links"] += len(links)

            broken_in_this_file = []
            for full_match, link_path in links:
                # Skip anchor-only links
                if link_path.startswith('#'):
                    continue

                # Extract path without anchor
                path_without_anchor = link_path.split('#')[0]
                if not path_without_anchor:
                    continue

                # Check if path exists
                if not check_if_path_exists(root, path_without_anchor):
                    stats["broken_links"] += 1
                    stats["unique_broken_paths"].add(path_without_anchor)
                    broken_in_this_file.append((full_match, link_path))

            if broken_in_this_file:
                stats["files_with_broken_links"] += 1
                rel_path = md_file.relative_to(root)
                stats["broken_by_file"][str(rel_path)] = broken_in_this_file

        except Exception as e:
            print(f"Error processing {md_file}: {e}")

    return stats


def main():
    """Main execution."""
    repo_root = Path(__file__).parent

    print("=" * 80)
    print("ANALYZING BROKEN LINKS IN POWERFXSNIPPETS")
    print("=" * 80)
    print()

    stats = analyze_broken_links(repo_root)

    print(f"Total markdown files: {stats['total_files']}")
    print(f"Total internal links: {stats['total_links']}")
    print(f"Broken links: {stats['broken_links']}")
    print(f"Files with broken links: {stats['files_with_broken_links']}")
    print()

    print("=" * 80)
    print("UNIQUE BROKEN PATHS (first 30):")
    print("=" * 80)
    for i, path in enumerate(sorted(stats['unique_broken_paths'])[:30], 1):
        print(f"{i:3d}. {path}")

    print()
    print("=" * 80)
    print("FILES WITH MOST BROKEN LINKS (top 10):")
    print("=" * 80)
    sorted_files = sorted(
        stats['broken_by_file'].items(),
        key=lambda x: len(x[1]),
        reverse=True
    )
    for file_path, broken in sorted_files[:10]:
        print(f"{file_path}: {len(broken)} broken links")


if __name__ == "__main__":
    main()
