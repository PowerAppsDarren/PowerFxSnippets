#!/usr/bin/env python3
"""
Fix broken internal markdown links after Phase 0 renaming (T202).
This script handles the comprehensive link fixing after files and directories
were renamed to lowercase-with-dashes format.
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Tuple, Set
import shutil
from datetime import datetime


# Create backup before running
BACKUP_DIR = None

def create_backup(root_dir: Path):
    """Create a timestamped backup of all markdown files."""
    global BACKUP_DIR
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    BACKUP_DIR = root_dir / f"_backup_links_{timestamp}"
    BACKUP_DIR.mkdir(exist_ok=True)
    print(f"Creating backup in: {BACKUP_DIR}")


def normalize_path_to_lowercase_dashes(path: str) -> str:
    """
    Convert path components to lowercase-with-dashes format.
    Examples:
        App.Formulas -> app-formulas
        Best Practices -> best-practices
        Color Enum.md -> color-enum.md
    """
    parts = path.split('/')
    normalized_parts = []

    for part in parts:
        # Skip empty parts
        if not part:
            continue

        # Don't modify file extensions or special files
        if part in ['README.md', 'LICENSE', 'CONTRIBUTING.md', 'CODE_OF_CONDUCT.md']:
            normalized_parts.append(part)
            continue

        # For files with extensions
        if '.' in part:
            name, ext = part.rsplit('.', 1)
            # Handle multiple extensions like .yaml.md
            while '.' in name:
                name, extra_ext = name.rsplit('.', 1)
                ext = extra_ext + '.' + ext

            # Normalize the name part
            normalized_name = name.replace(' ', '-').replace('_', '-').replace('.', '-')
            normalized_name = normalized_name.lower()
            normalized_parts.append(f"{normalized_name}.{ext}")
        else:
            # Directory names
            normalized = part.replace(' ', '-').replace('_', '-').replace('.', '-')
            normalized = normalized.lower()
            normalized_parts.append(normalized)

    return '/'.join(normalized_parts)


def find_best_match(broken_path: str, root_dir: Path) -> str:
    """
    Try to find the best matching actual path for a broken link.
    Uses various strategies to locate renamed files/directories.
    """
    # Strategy 1: Direct normalization
    normalized = normalize_path_to_lowercase_dashes(broken_path)
    if (root_dir / normalized).exists():
        return normalized

    # Strategy 2: Try without numbered prefixes (01-, 02-, etc.)
    # Remove patterns like "01-", "02-", etc. from path
    no_prefix = re.sub(r'\b\d{2}-', '', broken_path)
    normalized_no_prefix = normalize_path_to_lowercase_dashes(no_prefix)
    if (root_dir / normalized_no_prefix).exists():
        return normalized_no_prefix

    # Strategy 3: Look for similar paths in the file system
    # Extract the filename or last directory
    parts = broken_path.rstrip('/').split('/')
    if parts:
        target = parts[-1]
        normalized_target = normalize_path_to_lowercase_dashes(target)

        # Search for files/dirs with this name
        for item in root_dir.rglob('*'):
            if item.name.lower() == normalized_target.lower():
                rel_path = item.relative_to(root_dir)
                return str(rel_path).replace('\\', '/')

    # Strategy 4: Common mappings based on known restructuring
    mappings = {
        # Old numbered structure to new structure
        '01-getting-started': 'learning/tutorials/getting-started',
        '02-app-architecture': 'app-lifecycle',
        '03-user-interface': 'ui-controls',
        '04-data-management': 'data-operations',
        '05-business-logic': 'functions',
        '06-integrations': 'integrations',
        '07-assets-and-media': 'visual-assets',
        '08-advanced-patterns': 'best-practices',
        '09-learning-resources': 'learning',

        # Specific file mappings
        'App.Formulas': 'app-lifecycle/formulas',
        'App.OnStart': 'app-onstart',
        'App.OnError': 'app-onerror',
        'App.OnMessage': 'app-onmessage',
        'App.StartScreen': 'app-startscreen',
    }

    for old_prefix, new_prefix in mappings.items():
        if broken_path.startswith(old_prefix):
            potential_path = broken_path.replace(old_prefix, new_prefix, 1)
            normalized_potential = normalize_path_to_lowercase_dashes(potential_path)
            if (root_dir / normalized_potential).exists():
                return normalized_potential

    # If all strategies fail, return the normalized version anyway
    return normalized


def extract_internal_links(content: str) -> List[Tuple[str, int, int]]:
    """
    Extract internal markdown links from content.
    Returns list of (link_path, start_pos, end_pos) tuples.
    Excludes http/https links.
    """
    # Pattern: ](path) where path doesn't start with http:// or https://
    pattern = r'\]\(([^)]*?)\)'
    matches = []

    for match in re.finditer(pattern, content):
        link = match.group(1)
        # Skip external links
        if link.startswith('http://') or link.startswith('https://'):
            continue
        # Skip mailto links
        if link.startswith('mailto:'):
            continue
        # Skip anchor-only links
        if link.startswith('#'):
            continue

        matches.append((link, match.start(1), match.end(1)))

    return matches


def fix_link(link: str, source_file: Path, root_dir: Path) -> str:
    """
    Fix a single link path.
    Handles relative paths (../, ./) and absolute paths.
    """
    # Preserve anchor if present
    anchor = ''
    if '#' in link:
        link, anchor = link.split('#', 1)
        anchor = '#' + anchor

    # Remove leading ./
    if link.startswith('./'):
        link = link[2:]

    # Handle relative paths
    if link.startswith('../'):
        # Calculate absolute path from source file
        source_dir = source_file.parent
        parts = link.split('/')
        current_dir = source_dir

        for part in parts:
            if part == '..':
                current_dir = current_dir.parent
            elif part and part != '.':
                current_dir = current_dir / part

        try:
            link = str(current_dir.relative_to(root_dir)).replace('\\', '/')
        except ValueError:
            # Path is outside root, leave as is
            pass

    # Find the best match for this path
    fixed_path = find_best_match(link, root_dir)

    # Make it relative to the source file
    source_dir = source_file.parent
    try:
        # Calculate relative path from source to target
        target_path = root_dir / fixed_path
        if target_path.exists():
            if source_dir == root_dir:
                rel_path = fixed_path
            else:
                rel_path = os.path.relpath(target_path, source_dir).replace('\\', '/')
        else:
            rel_path = fixed_path
    except ValueError:
        rel_path = fixed_path

    # Add ./ prefix if it's just a filename
    if '/' not in rel_path and not rel_path.startswith('.'):
        rel_path = './' + rel_path

    return rel_path + anchor


def fix_file_links(file_path: Path, root_dir: Path, dry_run: bool = True) -> Dict:
    """
    Fix all broken links in a single file.
    Returns statistics about fixes.
    """
    stats = {
        'file': str(file_path.relative_to(root_dir)),
        'links_found': 0,
        'links_fixed': 0,
        'fixes': []
    }

    try:
        content = file_path.read_text(encoding='utf-8')
        original_content = content
        links = extract_internal_links(content)
        stats['links_found'] = len(links)

        # Process links in reverse order to preserve positions
        for link, start_pos, end_pos in reversed(links):
            fixed_link = fix_link(link, file_path, root_dir)

            if fixed_link != link:
                # Replace the link
                content = content[:start_pos] + fixed_link + content[end_pos:]
                stats['links_fixed'] += 1
                stats['fixes'].append({
                    'old': link,
                    'new': fixed_link
                })

        # Write back if not dry run and if there were changes
        if not dry_run and content != original_content:
            # Backup original
            if BACKUP_DIR:
                backup_path = BACKUP_DIR / file_path.relative_to(root_dir)
                backup_path.parent.mkdir(parents=True, exist_ok=True)
                backup_path.write_text(original_content, encoding='utf-8')

            file_path.write_text(content, encoding='utf-8')

    except Exception as e:
        stats['error'] = str(e)

    return stats


def main():
    """Main execution."""
    import sys
    import io

    # Fix Windows console encoding
    if sys.stdout.encoding != 'utf-8':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

    repo_root = Path(__file__).parent
    dry_run = '--apply' not in sys.argv

    print("=" * 80)
    print("BROKEN LINK FIXER - Phase 0 Post-Renaming (T202)")
    print("=" * 80)
    print()

    if dry_run:
        print("DRY RUN MODE - No files will be modified")
        print("Run with --apply to actually fix links")
    else:
        print("APPLY MODE - Files will be modified!")
        create_backup(repo_root)

    print()

    # Find all markdown files
    md_files = list(repo_root.rglob("*.md"))
    # Exclude backup directory and node_modules
    md_files = [f for f in md_files if '_backup_' not in str(f) and 'node_modules' not in str(f)]

    print(f"Found {len(md_files)} markdown files to process")
    print()

    # Process all files
    total_stats = {
        'files_processed': 0,
        'files_with_fixes': 0,
        'total_links': 0,
        'total_fixes': 0,
        'all_fixes': []
    }

    for md_file in md_files:
        stats = fix_file_links(md_file, repo_root, dry_run)
        total_stats['files_processed'] += 1
        total_stats['total_links'] += stats['links_found']
        total_stats['total_fixes'] += stats['links_fixed']

        if stats['links_fixed'] > 0:
            total_stats['files_with_fixes'] += 1
            total_stats['all_fixes'].append(stats)

            if len(total_stats['all_fixes']) <= 10:  # Show first 10 files
                rel_path = md_file.relative_to(repo_root)
                print(f"[OK] {rel_path}: {stats['links_fixed']} links fixed")

    print()
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Files processed: {total_stats['files_processed']}")
    print(f"Files with fixes: {total_stats['files_with_fixes']}")
    print(f"Total links found: {total_stats['total_links']}")
    print(f"Total links fixed: {total_stats['total_fixes']}")
    print()

    if dry_run:
        print("This was a DRY RUN. No files were modified.")
        print("Run with --apply to actually fix the links.")
    else:
        print(f"[DONE] Links have been fixed!")
        if BACKUP_DIR:
            print(f"[BACKUP] Backups saved to: {BACKUP_DIR}")

    # Generate detailed report
    report_path = repo_root / f"link-fix-report-{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(f"# Link Fix Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"## Summary\n\n")
        f.write(f"- Files processed: {total_stats['files_processed']}\n")
        f.write(f"- Files with fixes: {total_stats['files_with_fixes']}\n")
        f.write(f"- Total links found: {total_stats['total_links']}\n")
        f.write(f"- Total links fixed: {total_stats['total_fixes']}\n\n")
        f.write(f"## Files Modified\n\n")

        for file_stats in total_stats['all_fixes']:
            f.write(f"### {file_stats['file']}\n\n")
            f.write(f"Fixed {file_stats['links_fixed']} links:\n\n")
            for fix in file_stats['fixes'][:10]:  # Limit to first 10 per file
                f.write(f"- `{fix['old']}` → `{fix['new']}`\n")
            if len(file_stats['fixes']) > 10:
                f.write(f"- ... and {len(file_stats['fixes']) - 10} more\n")
            f.write("\n")

    print(f"[REPORT] Detailed report: {report_path}")


if __name__ == "__main__":
    main()
