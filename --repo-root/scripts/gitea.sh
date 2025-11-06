#!/bin/bash
# ==============================================================================
# Gitea Repository Setup Script
# ==============================================================================
# This script initializes a git repository and pushes it to two Gitea remotes:
# - origin: External Gitea server (git.superpowerlabs.app)
# - alt: Local/pool Gitea server
#
# Usage: Run this script from your project directory
#        ./gitea.sh
# ==============================================================================

# Exit on error
set -e

# Error handler
trap 'echo "Error on line $LINENO. Exiting."; exit 1' ERR

# ==============================================================================
# STEP 0: Prerequisite checks
# ==============================================================================
# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "Error: git is not installed. Please install git first."
    exit 1
fi

echo "✓ Git is installed"
echo ""

# ==============================================================================
# STEP 1: Get repository name
# ==============================================================================
# Get the current directory name as default (e.g., if in /home/user/my-project, uses "my-project")
# $PWD is the current working directory, basename extracts just the folder name
DEFAULT_REPO_NAME=$(basename "$PWD")

# Prompt user for repository name
# If user presses Enter without typing, REPO_NAME will be empty
read -p "Enter repository name (or press Enter to use '$DEFAULT_REPO_NAME'): " REPO_NAME

# Use default if empty
# -z checks if string is empty (zero length)
if [ -z "$REPO_NAME" ]; then
    REPO_NAME="$DEFAULT_REPO_NAME"
fi

echo "Using repository name: $REPO_NAME"
echo ""

# ==============================================================================
# STEP 2: Initialize Git and create first commit
# ==============================================================================
# Check if already a git repository
if git rev-parse --git-dir &>/dev/null 2>&1; then
    echo "✓ Git repository already initialized"
else
    echo "Initializing new git repository..."
    # Initialize Git repository
    git init
    echo "✓ Git repository initialized"
fi

# Ensure we're on the main branch (older git defaults to master)
git branch -M main
echo "✓ Branch set to 'main'"
echo ""

# Add all files and make initial commit
# "git add ." stages all files in current directory and subdirectories
git add .

# Create the first commit with all staged files (only if there are changes)
# Check if there are staged changes or if this is a new repo with no commits
if git diff --staged --quiet && git rev-parse HEAD &>/dev/null 2>&1; then
    echo "ℹ No changes to commit, skipping initial commit"
else
    echo "Creating initial commit..."
    git commit -m "Initial commit"
    echo "✓ Initial commit created"
fi
echo ""

# Show current remotes
echo "Current remotes:"
git remote -v
echo ""

# ==============================================================================
# STEP 3: Configure remote repositories
# ==============================================================================
# Configure remotes with SSH and correct port (2222)
# ${REPO_NAME} gets replaced with the variable value (e.g., "browser-data")
# These repos must exist on the Gitea servers before pushing

echo "Configuring remotes..."

# Primary remote: External server
if git remote get-url origin &>/dev/null 2>&1; then
    echo "ℹ Remote 'origin' already exists, updating URL..."
    git remote set-url origin ssh://git@git.superpowerlabs.app:2222/darren/${REPO_NAME}.git
else
    git remote add origin ssh://git@git.superpowerlabs.app:2222/darren/${REPO_NAME}.git
    echo "✓ Added remote 'origin'"
fi

# Alternate remote: Local/pool server
if git remote get-url alt &>/dev/null 2>&1; then
    echo "ℹ Remote 'alt' already exists, updating URL..."
    git remote set-url alt ssh://git@pool:2222/darren/${REPO_NAME}.git
else
    git remote add alt ssh://git@pool:2222/darren/${REPO_NAME}.git
    echo "✓ Added remote 'alt'"
fi

echo ""
# Display configured remotes to verify they're correct
echo "Configured remotes:"
git remote -v
echo ""

# ==============================================================================
# STEP 4: SSH authentication setup
# ==============================================================================
echo "Setting up SSH authentication..."

# Check if SSH key exists
SSH_KEY="$HOME/.ssh/id_ed25519"
if [ ! -f "$SSH_KEY" ]; then
    echo "Error: SSH key not found at $SSH_KEY"
    echo "Please generate an SSH key first with: ssh-keygen -t ed25519"
    exit 1
fi

# Check if ssh-agent is already running and has our key
if ssh-add -l | grep -q "$SSH_KEY"; then
    echo "✓ SSH key already loaded in ssh-agent"
else
    # Start ssh-agent if not running
    if [ -z "$SSH_AUTH_SOCK" ]; then
        echo "Starting ssh-agent..."
        eval "$(ssh-agent -s)"
    fi

    # Add SSH private key to agent
    echo "Adding SSH key to agent..."
    ssh-add "$SSH_KEY"
    echo "✓ SSH key added to agent"
fi
echo ""

# ==============================================================================
# STEP 5: Push to remote repositories
# ==============================================================================
echo "Pushing to remote repositories..."
echo "Note: These commands will fail if the repositories don't exist on the Gitea servers"
echo ""

# Push to both remotes
# Use -u flag to set upstream tracking
if git push -u origin main; then
    echo "✓ Successfully pushed to origin (git.superpowerlabs.app)"
else
    echo "✗ Failed to push to origin. Make sure the repository exists on git.superpowerlabs.app"
    exit 1
fi

if git push -u alt main; then
    echo "✓ Successfully pushed to alt (pool)"
else
    echo "✗ Failed to push to alt. Make sure the repository exists on pool"
    exit 1
fi

# ==============================================================================
# Done!
# ==============================================================================
echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "✓ Repository setup complete!"
echo "═══════════════════════════════════════════════════════════════"
echo "Repository: $REPO_NAME"
echo "Branch: main"
echo "Remotes configured:"
echo "  - origin: git.superpowerlabs.app"
echo "  - alt: pool"
echo "═══════════════════════════════════════════════════════════════"
