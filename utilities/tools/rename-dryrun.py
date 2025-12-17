#!/usr/bin/env python3
"""Dry run to see what would be renamed."""

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

    # Replace plus signs with nothing (or could use 'and')
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

# Collect all items
files_to_rename = []
dirs_to_rename = []

for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and not d.startswith('.')]
    current = Path(dirpath)

    if should_skip(current):
        continue

    # Files
    for f in filenames:
        if f in PRESERVE_FILES:
            continue
        new_name = to_lowercase_dashes(f, is_directory=False)
        if new_name != f:
            files_to_rename.append((current / f, new_name))

    # Directories
    for d in dirnames:
        new_name = to_lowercase_dashes(d, is_directory=True)
        if new_name != d:
            dirs_to_rename.append((current / d, new_name))

print(f"FILES TO RENAME: {len(files_to_rename)}")
print("=" * 60)
for old, new in files_to_rename[:30]:
    print(f"  {old.relative_to(ROOT)} -> {new}")
if len(files_to_rename) > 30:
    print(f"  ... and {len(files_to_rename) - 30} more files")

print(f"\nDIRECTORIES TO RENAME: {len(dirs_to_rename)}")
print("=" * 60)
for old, new in sorted(dirs_to_rename, key=lambda x: str(x[0])):
    print(f"  {old.relative_to(ROOT)} -> {new}")
