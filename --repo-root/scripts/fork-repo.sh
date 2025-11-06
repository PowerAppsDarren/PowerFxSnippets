#!/bin/bash
set -e

# Script to fork a GitHub repo locally
# Usage: ./fork-repo.sh <github-url> [target-directory]
#        ./fork-repo.sh --sync [target-directory]

# Get the directory where the script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Get the project root (parent of scripts folder)
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# Get the clones directory (parent of project root - where sibling repos live)
CLONES_DIR="$(dirname "$PROJECT_ROOT")"

# Check for --sync flag
if [ "$1" = "--sync" ]; then
    SYNC_MODE=true
    TARGET_DIR="$2"

    # If no directory specified, prompt for it
    if [ -z "$TARGET_DIR" ]; then
        echo "Enter the directory name to sync:"
        read -r TARGET_DIR
        if [ -z "$TARGET_DIR" ]; then
            echo "Error: No directory provided"
            exit 1
        fi
    fi

    # Make target directory path absolute (relative to clones directory)
    if [[ ! "$TARGET_DIR" = /* ]]; then
        TARGET_DIR="$CLONES_DIR/$TARGET_DIR"
    fi

    # Check if directory exists
    if [ ! -d "$TARGET_DIR" ]; then
        echo "Error: Directory '$TARGET_DIR' does not exist"
        exit 1
    fi

    # Navigate to the directory
    cd "$TARGET_DIR"

    # Check if it's a git repository
    if [ ! -d ".git" ]; then
        echo "Error: '$TARGET_DIR' is not a git repository"
        exit 1
    fi

    # Check if upstream remote exists
    if ! git remote get-url upstream &>/dev/null; then
        echo "Error: No 'upstream' remote configured"
        echo "Configure it with: git remote add upstream <upstream-url>"
        exit 1
    fi

    # Get current branch
    CURRENT_BRANCH=$(git branch --show-current)

    # Check for uncommitted changes
    if [ -n "$(git status --porcelain)" ]; then
        echo "Warning: You have uncommitted changes"
        read -p "Stash changes and continue? (y/N): " stash_confirm
        if [[ "$stash_confirm" =~ ^[Yy]$ ]]; then
            git stash
            STASHED=true
        else
            echo "Aborting. Commit or stash your changes first."
            exit 1
        fi
    fi

    echo "Syncing with upstream..."
    echo "Repository: $TARGET_DIR"
    echo "Current branch: $CURRENT_BRANCH"
    echo "Upstream: $(git remote get-url upstream)"
    echo ""

    # Fetch from upstream
    echo "Fetching from upstream..."
    git fetch upstream

    # Get the default branch from upstream
    DEFAULT_BRANCH=$(git remote show upstream | grep 'HEAD branch' | cut -d' ' -f5)

    echo "Default upstream branch: $DEFAULT_BRANCH"
    echo ""

    # Ask how to sync
    echo "Sync options:"
    echo "  1. Merge upstream/$DEFAULT_BRANCH into current branch ($CURRENT_BRANCH)"
    echo "  2. Rebase current branch ($CURRENT_BRANCH) onto upstream/$DEFAULT_BRANCH"
    echo "  3. Reset current branch to upstream/$DEFAULT_BRANCH (destructive!)"
    echo "  4. Just fetch (already done, will exit)"
    read -p "Choose (1-4): " sync_choice

    case $sync_choice in
        1)
            echo "Merging upstream/$DEFAULT_BRANCH..."
            git merge upstream/$DEFAULT_BRANCH
            ;;
        2)
            echo "Rebasing onto upstream/$DEFAULT_BRANCH..."
            git rebase upstream/$DEFAULT_BRANCH
            ;;
        3)
            read -p "Are you SURE? This will discard local commits! (yes/N): " confirm_reset
            if [ "$confirm_reset" = "yes" ]; then
                git reset --hard upstream/$DEFAULT_BRANCH
                echo "Branch reset to upstream/$DEFAULT_BRANCH"
            else
                echo "Cancelled."
            fi
            ;;
        4)
            echo "Fetch complete. No merge/rebase performed."
            ;;
        *)
            echo "Invalid choice. Fetch complete, no merge/rebase performed."
            ;;
    esac

    # Restore stashed changes if any
    if [ "$STASHED" = true ]; then
        echo ""
        read -p "Restore stashed changes? (y/N): " restore_confirm
        if [[ "$restore_confirm" =~ ^[Yy]$ ]]; then
            git stash pop
        else
            echo "Changes remain stashed. Use 'git stash pop' to restore them."
        fi
    fi

    echo ""
    echo "✓ Sync complete!"
    echo ""
    echo "To push updates to your fork:"
    echo "  git push origin $CURRENT_BRANCH"

    exit 0
fi

if [ -z "$1" ]; then
    echo "Enter the GitHub repository URL to fork:"
    read -r REPO_URL
    if [ -z "$REPO_URL" ]; then
        echo "Error: No repository URL provided"
        exit 1
    fi
else
    REPO_URL="$1"
fi

TARGET_DIR="$2"

# Extract repository name from URL if no target directory specified
if [ -z "$TARGET_DIR" ]; then
    TARGET_DIR=$(basename "$REPO_URL" .git)
fi

# Make target directory path absolute (relative to clones directory)
if [[ ! "$TARGET_DIR" = /* ]]; then
    TARGET_DIR="$CLONES_DIR/$TARGET_DIR"
fi

# Check if target directory already exists
if [ -d "$TARGET_DIR" ]; then
    echo "Warning: Directory '$TARGET_DIR' already exists"

    # Check if it's a git repository
    if [ -d "$TARGET_DIR/.git" ]; then
        echo "This appears to be an existing git repository."
        echo "Options:"
        echo "  1. Abort and handle manually"
        echo "  2. Add upstream remote to existing repo (if not already set)"
        echo "  3. Delete and re-clone"
        read -p "Choose (1-3): " choice

        case $choice in
            2)
                cd "$TARGET_DIR"
                if git remote get-url upstream &>/dev/null; then
                    echo "Upstream remote already exists: $(git remote get-url upstream)"
                else
                    git remote add upstream "$REPO_URL"
                    echo "Added upstream remote: $REPO_URL"
                fi

                # Fetch from upstream
                echo "Fetching from upstream..."
                git fetch upstream

                DEFAULT_BRANCH=$(git remote show upstream | grep 'HEAD branch' | cut -d' ' -f5)
                echo ""
                echo "✓ Upstream configured successfully!"
                echo ""
                echo "Repository details:"
                echo "  Directory: $TARGET_DIR"
                echo "  Upstream: $(git remote get-url upstream)"
                echo "  Default branch: $DEFAULT_BRANCH"
                echo ""
                echo "To merge upstream changes into your current branch:"
                echo "  git merge upstream/$DEFAULT_BRANCH"
                exit 0
                ;;
            3)
                echo "Removing existing directory..."
                rm -rf "$TARGET_DIR"
                ;;
            *)
                echo "Aborting."
                exit 1
                ;;
        esac
    else
        echo "Directory exists but is not a git repository."
        read -p "Delete and continue? (y/N): " confirm
        if [[ ! "$confirm" =~ ^[Yy]$ ]]; then
            echo "Aborting."
            exit 1
        fi
        rm -rf "$TARGET_DIR"
    fi
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

# Detect the default branch
DEFAULT_BRANCH=$(git branch --show-current)

echo ""
echo "✓ Repository forked successfully!"
echo ""
echo "Repository details:"
echo "  Directory: $TARGET_DIR"
echo "  Upstream: $(git remote get-url upstream)"
echo "  Default branch: $DEFAULT_BRANCH"
echo ""
echo "Next steps:"
echo "  1. Create your fork on GitHub (via web UI or 'gh repo fork')"
echo "  2. Add your fork as origin: git remote add origin <your-fork-url>"
echo "  3. Push to your fork: git push -u origin $DEFAULT_BRANCH"
echo "  4. Pull upstream changes anytime: git pull upstream $DEFAULT_BRANCH"
echo ""
echo "Optional: Create GitHub fork now? (requires 'gh' CLI)"
read -p "(y/N): " create_fork
if [[ "$create_fork" =~ ^[Yy]$ ]]; then
    if command -v gh &> /dev/null; then
        echo "Creating fork on GitHub..."
        gh repo fork --remote=true --remote-name=origin
        echo "✓ Fork created and origin remote added!"
        echo ""
        read -p "Push to your fork now? (y/N): " push_now
        if [[ "$push_now" =~ ^[Yy]$ ]]; then
            git push -u origin $DEFAULT_BRANCH
            echo "✓ Pushed to your fork!"
        fi
    else
        echo "GitHub CLI (gh) not found. Install from: https://cli.github.com/"
    fi
fi

# ==============================================================================
# Optional: Initialize spec-kit
# ==============================================================================
echo ""
echo "Optional: Initialize spec-kit for spec-driven development?"
read -p "(y/N): " init_speckit
if [[ "$init_speckit" =~ ^[Yy]$ ]]; then
    if command -v uvx &> /dev/null; then
        echo "Initializing spec-kit..."
        uvx --from git+https://github.com/github/spec-kit.git specify init .
        echo "✓ Spec-kit initialized!"
    else
        echo "uvx not found. Install uv from: https://github.com/astral-sh/uv"
        echo "Skipping spec-kit setup."
    fi
fi

# ==============================================================================
# Optional: Run Gitea setup
# ==============================================================================
echo ""
echo "Optional: Setup Gitea remotes? (requires gitea.sh script)"
read -p "(y/N): " setup_gitea
if [[ "$setup_gitea" =~ ^[Yy]$ ]]; then
    # Path to gitea.sh relative to this script's location
    GITEA_SCRIPT="$(dirname "$PROJECT_ROOT")/scripts/gitea.sh"

    if [ -f "$GITEA_SCRIPT" ]; then
        echo "Running Gitea setup script..."
        bash "$GITEA_SCRIPT"
    else
        echo "Error: gitea.sh script not found at: $GITEA_SCRIPT"
        echo "Skipping Gitea setup."
    fi
fi
