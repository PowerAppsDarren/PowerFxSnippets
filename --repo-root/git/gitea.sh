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
# Initialize Git repository
git init

# Add all files and make initial commit
# "git add ." stages all files in current directory and subdirectories
git add .

# Create the first commit with all staged files
# This commit creates the "main" branch
git commit -m "Initial commit"

# Show current remotes (should be empty at this point)
git remote -v

# ==============================================================================
# STEP 3: Configure remote repositories
# ==============================================================================
# Configure remotes with SSH and correct port (2222)
# ${REPO_NAME} gets replaced with the variable value (e.g., "browser-data")
# These repos must exist on the Gitea servers before pushing

# Primary remote: External server
git remote add origin ssh://git@git.superpowerlabs.app:2222/darren/${REPO_NAME}.git

# Alternate remote: Local/pool server
git remote add alt ssh://git@pool:2222/darren/${REPO_NAME}.git

# Display configured remotes to verify they're correct
git remote -v

# ==============================================================================
# STEP 4: SSH authentication setup
# ==============================================================================
# SSH agent setup (needed for SSH authentication)
# eval executes the output of ssh-agent, which sets environment variables
eval "$(ssh-agent -s)"

# Add SSH private key to agent
# This allows git to use your SSH key for authentication
ssh-add ~/.ssh/id_ed25519

# ==============================================================================
# STEP 5: Push to remote repositories
# ==============================================================================
# Push to both remotes
# These commands will fail if the repositories don't exist on the Gitea servers
git push origin main
git push alt main

# ==============================================================================
# Done!
# ==============================================================================
