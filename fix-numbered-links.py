#!/usr/bin/env python3
"""
Fix remaining numbered directory references in README and other files.
Specifically targets old 01-, 02-, etc. prefixed paths that don't exist.
"""

import re
from pathlib import Path


# Mapping of old numbered paths to new paths
# Based on the new directory structure
NUMBERED_MAPPINGS = {
    # Main categories
    '01-getting-started': 'learning/tutorials/getting-started',
    '02-app-architecture': 'app-lifecycle',
    '03-user-interface': 'ui-controls',
    '04-data-management': 'data-operations',
    '05-business-logic': 'functions',
    '06-integrations': 'integrations',
    '07-assets-and-media': 'visual-assets',
    '08-advanced-patterns': 'best-practices',
    '09-learning-resources': 'learning',

    # Subcategories
    '02-app-architecture/app-events': 'app-lifecycle',
    '02-app-architecture/navigation-patterns': 'app-lifecycle',
    '02-app-architecture/performance-optimization': 'best-practices',
    '03-user-interface/controls': 'ui-controls',
    '03-user-interface/themes-and-styling': 'design',
    '04-data-management/data-sources': 'data-sources',
    '04-data-management/data-validation': 'data-operations',
    '04-data-management/data-visualization': 'data-operations',
    '04-data-management/offline-capabilities': 'data-operations',
    '05-business-logic/calculations': 'functions',
    '05-business-logic/error-handling': 'app-onerror',
    '05-business-logic/functions': 'functions',
    '06-integrations/microsoft-365': 'integrations',
    '06-integrations/azure-services': 'integrations',
    '06-integrations/power-automate': 'integrations',
    '06-integrations/third-party-apis': 'integrations',
    '07-assets-and-media/icons': 'icons',
    '07-assets-and-media/svgs': 'visual-assets',
    '08-advanced-patterns/custom-components': 'ui-patterns/components',
    '08-advanced-patterns/security-patterns': 'best-practices',
    '09-learning-resources/best-practices': 'best-practices',
    '09-learning-resources/tutorials': 'learning/tutorials',
    '09-learning-resources/certification-prep': 'certification-exams',
}


def fix_numbered_paths(content: str) -> tuple[str, int]:
    """
    Replace all numbered path references with their new equivalents.
    Returns (fixed_content, count_of_fixes)
    """
    fixes = 0

    # Sort mappings by length (longest first) to avoid partial replacements
    sorted_mappings = sorted(NUMBERED_MAPPINGS.items(), key=lambda x: len(x[0]), reverse=True)

    for old_path, new_path in sorted_mappings:
        # Match the path in various link contexts
        patterns = [
            # Markdown links: [text](path) or [text](./path) or [text](../path)
            (rf'\]\((\.\./)?{re.escape(old_path)}([/)])', rf'](\1{new_path}\2'),
            (rf'\]\(\./{re.escape(old_path)}([/)])', rf'](./{new_path}\1'),
        ]

        for pattern, replacement in patterns:
            old_content = content
            content = re.sub(pattern, replacement, content)
            fixes += len(re.findall(pattern, old_content))

    return content, fixes


def main():
    """Main execution."""
    repo_root = Path(__file__).parent

    print("=" * 80)
    print("FIXING REMAINING NUMBERED DIRECTORY REFERENCES")
    print("=" * 80)
    print()

    # Files to process (focus on main documentation files)
    files_to_fix = [
        'README.md',
        'app-lifecycle/readme.md',
        'data-operations/readme.md',
        'ui-controls/readme.md',
        'functions/README.md',
        'learning/tutorials/getting-started/README.md',
    ]

    total_fixes = 0

    for file_rel in files_to_fix:
        file_path = repo_root / file_rel
        if not file_path.exists():
            print(f"[SKIP] {file_rel} - file not found")
            continue

        try:
            content = file_path.read_text(encoding='utf-8')
            fixed_content, fixes = fix_numbered_paths(content)

            if fixes > 0:
                # Write back
                file_path.write_text(fixed_content, encoding='utf-8')
                print(f"[OK] {file_rel}: {fixes} numbered paths fixed")
                total_fixes += fixes
            else:
                print(f"[OK] {file_rel}: no numbered paths found")

        except Exception as e:
            print(f"[ERROR] {file_rel}: {e}")

    print()
    print("=" * 80)
    print(f"TOTAL: {total_fixes} numbered path references fixed")
    print("=" * 80)


if __name__ == "__main__":
    main()
