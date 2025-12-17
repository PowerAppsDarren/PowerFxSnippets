#!/usr/bin/env python3
"""Execute the renaming of all files and directories to lowercase-with-dashes format."""

import os
import re
from pathlib import Path

ROOT = Path(r"C:\src\src-power-platform\PowerFxSnippets")
SKIP_DIRS = {'.git', '.specify', '.repo-root', '.github', '.darren', 'ai-chats', 'node_modules', '__pycache__', 'utilities'}
PRESERVE_FILES = {'CODE_OF_CONDUCT.md', 'CONTRIBUTING.md', 'CLAUDE.md', 'RESUME.md', 'LICENSE', 'LICENSE.md'}

def to_lowercase_dashes(name: str, is_directory: bool = False) -> str:
    """Convert a name to lowercase-with-dashes format."""
    result = name

    # For directories, replace ALL periods with dashes
    # For files, only replace periods that aren't part of the extension
    if is_directory:
        result = result.replace('.', '-')
    else:
        # Split off extension
        parts = result.rsplit('.', 1)
        if len(parts) == 2 and len(parts[1]) <= 5:
            base = parts[0].replace('.', '-')
            ext = parts[1]
            result = f"{base}.{ext}"

    # Replace spaces with dashes
    result = result.replace(' ', '-')

    # Replace underscores with dashes
    result = result.replace('_', '-')

    # Replace plus signs with nothing
    result = result.replace('+', '')

    # Convert to lowercase
    result = result.lower()

    # Remove multiple consecutive dashes
    result = re.sub(r'-+', '-', result)

    # Remove leading/trailing dashes
    result = result.strip('-')

    return result

def should_skip(path: Path) -> bool:
    for part in path.parts:
        if part in SKIP_DIRS:
            return True
    return False

def get_all_items(root: Path):
    """Get all files and directories, organized for safe renaming."""
    files = []
    dirs = []

    for dirpath, dirnames, filenames in os.walk(root):
        # Filter out directories we should skip
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and not d.startswith('.')]
        current = Path(dirpath)

        if should_skip(current):
            continue

        # Collect files
        for f in filenames:
            if f in PRESERVE_FILES:
                continue
            filepath = current / f
            new_name = to_lowercase_dashes(f, is_directory=False)
            if new_name != f:
                files.append((filepath, new_name))

        # Collect directories
        for d in dirnames:
            dirpath_full = current / d
            new_name = to_lowercase_dashes(d, is_directory=True)
            if new_name != d:
                dirs.append((dirpath_full, new_name))

    # Sort directories by depth (deepest first) so we rename children before parents
    dirs.sort(key=lambda x: len(x[0].parts), reverse=True)

    return files, dirs

def main():
    print(f"Scanning {ROOT}...")
    print("=" * 60)

    files, dirs = get_all_items(ROOT)

    print(f"FILES TO RENAME: {len(files)}")
    print(f"DIRECTORIES TO RENAME: {len(dirs)}")
    print("=" * 60)

    # Rename files first
    file_success = 0
    file_errors = []

    print("\nRenaming files...")
    for old_path, new_name in files:
        try:
            if old_path.exists():
                new_path = old_path.parent / new_name
                old_path.rename(new_path)
                file_success += 1
        except Exception as e:
            file_errors.append((old_path, new_name, str(e)))

    print(f"Files renamed: {file_success}")
    if file_errors:
        print(f"File errors: {len(file_errors)}")
        for old, new, err in file_errors[:10]:
            print(f"  ERR: {old.relative_to(ROOT)} -> {new}: {err}")

    # Rename directories (deepest first)
    dir_success = 0
    dir_errors = []

    print("\nRenaming directories...")
    for old_path, new_name in dirs:
        try:
            if old_path.exists():
                new_path = old_path.parent / new_name
                old_path.rename(new_path)
                dir_success += 1
        except Exception as e:
            dir_errors.append((old_path, new_name, str(e)))

    print(f"Directories renamed: {dir_success}")
    if dir_errors:
        print(f"Directory errors: {len(dir_errors)}")
        for old, new, err in dir_errors[:10]:
            print(f"  ERR: {old.relative_to(ROOT)} -> {new}: {err}")

    print("\n" + "=" * 60)
    print(f"TOTAL SUCCESS: {file_success + dir_success}")
    print(f"TOTAL ERRORS: {len(file_errors) + len(dir_errors)}")

if __name__ == '__main__':
    main()
