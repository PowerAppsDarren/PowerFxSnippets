#!/bin/bash
set -e

# Script to fork a GitHub repo locally
# Usage: ./fork-repo.sh <github-url> [target-directory]

if [ -z "$1" ]; then
    echo "Error: No repository URL provided"
    echo "Usage: $0 <github-url> [target-directory]"
    echo "Example: $0 https://github.com/user/repo [my-fork]"
    exit 1
fi

REPO_URL="$1"
TARGET_DIR="$2"

# Extract repository name from URL if no target directory specified
if [ -z "$TARGET_DIR" ]; then
    TARGET_DIR=$(basename "$REPO_URL" .git)
fi

echo "Cloning repository: $REPO_URL"
echo "Target directory: $TARGET_DIR"

# Clone the repository
git clone "$REPO_URL" "$TARGET_DIR"

# Navigate into the cloned repository
cd "$TARGET_DIR"

# Rename origin to upstream
echo "Setting up remotes..."
git remote rename origin upstream

echo ""
echo "✓ Repository forked successfully!"
echo ""
echo "Repository details:"
echo "  Directory: $TARGET_DIR"
echo "  Upstream: $(git remote get-url upstream)"
echo ""
echo "Next steps:"
echo "  1. Add your own remote: git remote add origin <your-repo-url>"
echo "  2. Push to your remote: git push -u origin main"
echo "  3. Pull upstream changes: git pull upstream main"
