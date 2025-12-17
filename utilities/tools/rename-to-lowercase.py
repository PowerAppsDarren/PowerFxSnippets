#!/usr/bin/env python3
"""
Rename all files and directories to lowercase-with-dashes format.

Rules:
- All lowercase
- Spaces become dashes
- Multiple dashes become single dash
- Preserve special files: CODE_OF_CONDUCT.md, CONTRIBUTING.md, CLAUDE.md, RESUME.md
- Skip hidden directories (.git, .specify, .repo-root, .github, .darren)
"""

import os
import re
from pathlib import Path

# Root directory
ROOT = Path(__file__).parent.parent.parent

# Directories to skip
SKIP_DIRS = {'.git', '.specify', '.repo-root', '.github', '.darren', 'ai-chats', 'node_modules', '__pycache__'}

# Files to preserve exactly as-is (uppercase conventions)
PRESERVE_FILES = {'CODE_OF_CONDUCT.md', 'CONTRIBUTING.md', 'CLAUDE.md', 'RESUME.md', 'LICENSE', 'LICENSE.md'}

def to_lowercase_dashes(name: str) -> str:
    """Convert a name to lowercase-with-dashes format."""
    # Replace spaces with dashes
    result = name.replace(' ', '-')
    # Replace underscores with dashes (except leading underscore)
    if result.startswith('_'):
        result = '_' + result[1:].replace('_', '-')
    else:
        result = result.replace('_', '-')
    # Replace periods in middle of name with dashes (but keep file extension)
    parts = result.rsplit('.', 1)
    if len(parts) == 2 and len(parts[1]) <= 5:  # Has extension
        base = parts[0].replace('.', '-')
        result = f"{base}.{parts[1]}"
    # Convert to lowercase
    result = result.lower()
    # Remove multiple consecutive dashes
    result = re.sub(r'-+', '-', result)
    # Remove leading/trailing dashes (but keep leading underscore)
    if result.startswith('_'):
        result = '_' + result[1:].strip('-')
    else:
        result = result.strip('-')
    return result

def should_skip(path: Path) -> bool:
    """Check if path should be skipped."""
    for part in path.parts:
        if part in SKIP_DIRS:
            return True
    return False

def get_all_paths(root: Path):
    """Get all files and directories, sorted by depth (deepest first for safe renaming)."""
    all_paths = []
    for dirpath, dirnames, filenames in os.walk(root):
        # Skip hidden/excluded directories
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and not d.startswith('.')]

        current = Path(dirpath)
        if should_skip(current):
            continue

        # Add files
        for f in filenames:
            filepath = current / f
            all_paths.append(filepath)

        # Add directories (we'll process them after files)
        for d in dirnames:
            dirpath_full = current / d
            all_paths.append(dirpath_full)

    # Sort by depth (deepest first) to rename children before parents
    all_paths.sort(key=lambda p: len(p.parts), reverse=True)
    return all_paths

def main():
    print(f"Scanning {ROOT}...")
    print("=" * 60)

    renames = []

    for path in get_all_paths(ROOT):
        if not path.exists():
            continue

        name = path.name

        # Check if file should be preserved
        if name in PRESERVE_FILES:
            print(f"PRESERVE: {path.relative_to(ROOT)}")
            continue

        # Calculate new name
        new_name = to_lowercase_dashes(name)

        if new_name != name:
            new_path = path.parent / new_name
            renames.append((path, new_path))

    print(f"\nFound {len(renames)} items to rename:")
    print("=" * 60)

    for old, new in renames[:50]:  # Show first 50
        print(f"  {old.relative_to(ROOT)}")
        print(f"    → {new.relative_to(ROOT)}")

    if len(renames) > 50:
        print(f"  ... and {len(renames) - 50} more")

    print("\n" + "=" * 60)
    response = input(f"Rename {len(renames)} items? [y/N]: ")

    if response.lower() != 'y':
        print("Aborted.")
        return

    # Perform renames
    success = 0
    errors = []

    for old_path, new_path in renames:
        try:
            if old_path.exists():
                old_path.rename(new_path)
                success += 1
                print(f"✓ {old_path.name} → {new_path.name}")
        except Exception as e:
            errors.append((old_path, new_path, str(e)))
            print(f"✗ {old_path.name}: {e}")

    print("\n" + "=" * 60)
    print(f"Renamed: {success}")
    print(f"Errors: {len(errors)}")

    if errors:
        print("\nErrors:")
        for old, new, err in errors:
            print(f"  {old} → {new}: {err}")

if __name__ == '__main__':
    main()
