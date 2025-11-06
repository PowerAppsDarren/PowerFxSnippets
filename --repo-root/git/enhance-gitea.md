Enhance the `git-tea-server.sh` script located in `~/dotfiles/` to make it fully interactive and user-friendly, while preserving its core functionality for setting up Git repositories for Tea server projects. The script should handle project initialization, Git setup, and remote pushes securely and efficiently. Follow these detailed steps precisely, without altering existing variable defaults unless specified. Output the complete enhanced script at the end, with clear comments explaining each interactive section and change.

### Interactive Initialization (At Script Start)
- Upon first execution, prompt the user for the project name (e.g., "Enter the project name: ") and store it in the environment variable `GIT_PROJECT_NAME`. Use this variable throughout the script for dynamic naming (e.g., in commit messages, remote names).
- Do not prompt for or modify any other existing variables (e.g., remote URLs, paths, or defaults). Retain their current values as-is to avoid unnecessary changes.

### Working Directory Confirmation
- After setting `GIT_PROJECT_NAME`, interactively confirm the working directory with the user. Present two clear options:
  1. Use the same directory as the script file (current path).
  2. Use the parent directory (one level up, e.g., if the script is in a `scripts/` folder, default to the project root).
- Display the paths for both options (e.g., "Option 1: Current script dir - /path/to/scripts/ | Option 2: Parent dir - /path/to/project/"). Let the user select via numbered input (1 or 2), with validation for invalid choices (loop until valid).
- If the user selects Option 1 (script's directory), follow up with a yes/no prompt: "Should the script be copied to a 'scripts/' folder in the working directory? (This folder may be created if it doesn't exist.) [y/N]". If 'y', create the `scripts/` folder if needed and copy `git-tea-server.sh` there, then cd into the working directory.

### Git Repository Check and Initialization (Before Line ~20, e.g., Before "🔧 Configuring Git remotes")
- Before any remote configuration (specifically before the echo statement like "🔧 Configuring Git remotes for $GIT_PROJECT_NAME"), check if the current working directory is already a Git repository (e.g., via `git rev-parse --git-dir` or checking for `.git/`).
- If not initialized, run `git init` silently and output a confirmation message: "Initialized new Git repository."
- Regardless of initialization status, run `git status` and display its output to the user for transparency (e.g., "Current Git status:").
- Handle any errors gracefully (e.g., if not in a valid dir, prompt to confirm and proceed).

### .gitignore Handling
- Check if a `.gitignore` file exists in the working directory.
- If it doesn't exist or is empty (file size 0), create/touch `.gitignore` and populate it with common ignore patterns for a Tea server project. Include standard entries like:
  - `node_modules/`
  - `*.log`
  - `dist/`
  - `build/`
  - `coverage/`
  - `*.tmp`
  - `.DS_Store`
  - `Thumbs.db`
  - `*.swp`
  - `*.swo`
- **Critically important**: Do NOT include any patterns related to `.env` files (e.g., no `.env`, `.env*`, or `*.env`). The user intentionally commits `.env` files to private SSH-secured repos; do not add, suggest, or debate this.
- After creating/updating, display the contents of `.gitignore` for user confirmation: "Generated/updated .gitignore with the following entries: [list them]. Proceed? [y/N]". If 'N', allow manual edit via an editor (e.g., open with `nano .gitignore`) before continuing.

### Staging, Committing, and Pushing
- Once `.gitignore` is in place, automatically stage all files (including the new/updated `.gitignore`) using `git add .`.
- Create a descriptive initial commit with a message incorporating `GIT_PROJECT_NAME`, e.g.: `git commit -m "Initial commit: Set up ${GIT_PROJECT_NAME} project with .gitignore and basic structure"`.
- If there are no changes to commit (e.g., empty repo), skip the commit and inform the user: "No changes to commit; proceeding to remotes."
- Proceed with the existing remote configuration logic (around line 20+), then push to both remote repositories:
  - Assume the script already defines two remotes (e.g., main and backup); use `git remote add` if needed, `git push -u origin main` (or equivalent branch), and repeat for the second remote.
  - Handle authentication securely (e.g., assume SSH keys are set up; no password prompts).
  - Output success messages for each push, e.g., "Pushed ${GIT_PROJECT_NAME} to remote1 and remote2 successfully."

### General Enhancements
- Add a colorful, welcoming header at the script start: e.g., using `echo -e "\e[32m🚀 Git Tea Server Setup for ${GIT_PROJECT_NAME}\e[0m"`.
- Include input validation everywhere (e.g., non-empty project name, numeric choices).
- Use `read` with prompts for all interactions, and set `set -e` for error handling (exit on failures).
- End the script with a summary: e.g., "Setup complete! Your ${GIT_PROJECT_NAME} repo is ready at [working dir]. Run `git status` to verify."
- Ensure the script is POSIX-compliant, shebang `#!/bin/bash`, and executable.
- Do not overwrite or remove any existing script logic unrelated to these changes; integrate seamlessly.
