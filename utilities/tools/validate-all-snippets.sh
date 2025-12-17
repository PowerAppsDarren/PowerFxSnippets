#!/bin/bash
# T013: Validate All Snippets
# Runs snippet-validator.py on all markdown files in the repository.
#
# Usage:
#   ./validate-all-snippets.sh [--verbose] [--quiet] [--help]
#
# Exit codes:
#   0 - All snippets valid
#   1 - One or more validation failures

set -euo pipefail

# Script directory (for finding validator)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VALIDATOR="${SCRIPT_DIR}/snippet-validator.py"

# Repository root (parent of utilities/tools)
REPO_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"

# Options
VERBOSE=false
QUIET=false

# Counters
TOTAL=0
VALID=0
INVALID=0
SKIPPED=0

# Colors (if terminal supports it)
if [[ -t 1 ]]; then
    RED='\033[0;31m'
    GREEN='\033[0;32m'
    YELLOW='\033[0;33m'
    BLUE='\033[0;34m'
    NC='\033[0m' # No Color
else
    RED=''
    GREEN=''
    YELLOW=''
    BLUE=''
    NC=''
fi

# Usage
usage() {
    cat << EOF
Usage: $(basename "$0") [OPTIONS]

Validate YAML frontmatter in all markdown snippet files.

Options:
    -v, --verbose    Show detailed output for each file
    -q, --quiet      Only show summary (no per-file output)
    -h, --help       Show this help message

Excluded paths:
    - README.md, CLAUDE.md files
    - .specify/, ai-chats/, .github/, .git/ directories
    - utilities/ directory

Exit codes:
    0 - All snippets valid
    1 - One or more validation failures
EOF
}

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -v|--verbose)
            VERBOSE=true
            shift
            ;;
        -q|--quiet)
            QUIET=true
            shift
            ;;
        -h|--help)
            usage
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            usage
            exit 1
            ;;
    esac
done

# Check validator exists
if [[ ! -f "$VALIDATOR" ]]; then
    echo -e "${RED}Error: Validator script not found: ${VALIDATOR}${NC}"
    exit 1
fi

# Check Python is available
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Error: python3 is required but not found${NC}"
    exit 1
fi

# Function to check if path should be excluded
should_exclude() {
    local file_path="$1"
    local rel_path="${file_path#$REPO_ROOT/}"

    # Exclude specific filenames
    local filename
    filename=$(basename "$file_path")
    case "$filename" in
        README.md|CLAUDE.md|SEARCH-INDEX.md|TAG-INDEX.md|DIFFICULTY-INDEX.md|INDEX.md)
            return 0
            ;;
    esac

    # Exclude specific directories
    if [[ "$rel_path" == .specify/* ]] || \
       [[ "$rel_path" == ai-chats/* ]] || \
       [[ "$rel_path" == ai-protocols/* ]] || \
       [[ "$rel_path" == .github/* ]] || \
       [[ "$rel_path" == .git/* ]] || \
       [[ "$rel_path" == .repo-root/* ]] || \
       [[ "$rel_path" == utilities/* ]] || \
       [[ "$rel_path" == templates/* ]] || \
       [[ "$rel_path" == docs/* ]] || \
       [[ "$rel_path" == .darren/* ]]; then
        return 0
    fi

    return 1
}

# Header
if [[ "$QUIET" != true ]]; then
    echo -e "${BLUE}=== Snippet Validation Report ===${NC}"
    echo -e "Repository: ${REPO_ROOT}"
    echo ""
fi

# Find and validate all markdown files
FAILED_FILES=()

while IFS= read -r -d '' file; do
    # Check exclusions
    if should_exclude "$file"; then
        ((SKIPPED++)) || true
        if [[ "$VERBOSE" == true ]]; then
            echo -e "${YELLOW}SKIP${NC}: $file"
        fi
        continue
    fi

    ((TOTAL++)) || true

    # Run validator
    if python3 "$VALIDATOR" "$file" -q 2>/dev/null; then
        ((VALID++)) || true
        if [[ "$VERBOSE" == true ]]; then
            echo -e "${GREEN}PASS${NC}: $file"
        fi
    else
        ((INVALID++)) || true
        FAILED_FILES+=("$file")
        if [[ "$QUIET" != true ]]; then
            echo -e "${RED}FAIL${NC}: $file"
            if [[ "$VERBOSE" == true ]]; then
                # Run again without quiet to show errors
                python3 "$VALIDATOR" "$file" 2>&1 | sed 's/^/  /'
            fi
        fi
    fi
done < <(find "$REPO_ROOT" -type f -name "*.md" -print0 2>/dev/null)

# Summary
echo ""
echo -e "${BLUE}=== Summary ===${NC}"
echo -e "Total files scanned: ${TOTAL}"
echo -e "  ${GREEN}Valid${NC}:   ${VALID}"
echo -e "  ${RED}Invalid${NC}: ${INVALID}"
echo -e "  ${YELLOW}Skipped${NC}: ${SKIPPED}"

# List failed files if any
if [[ ${#FAILED_FILES[@]} -gt 0 ]]; then
    echo ""
    echo -e "${RED}Failed files:${NC}"
    for file in "${FAILED_FILES[@]}"; do
        echo "  - $file"
    done
fi

# Exit code
if [[ $INVALID -gt 0 ]]; then
    echo ""
    echo -e "${RED}Validation FAILED${NC}: ${INVALID} file(s) have invalid frontmatter"
    exit 1
else
    echo ""
    echo -e "${GREEN}Validation PASSED${NC}: All ${VALID} snippet(s) are valid"
    exit 0
fi
