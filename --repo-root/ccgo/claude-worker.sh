#!/usr/bin/env bash
################################################################################
# Claude Worker Session Launcher
################################################################################
# PURPOSE: Launch Claude Code using the CHEAP Haiku 4.5 model for task execution
#
# COST OPTIMIZATION:
#   - Haiku costs $1 input / $5 output per 1M tokens
#   - Sonnet costs $3 input / $15 output per 1M tokens
#   - Using Haiku = 80% cost savings!
#
# WHEN TO USE THIS:
#   ✅ Implementing specific features (clear requirements)
#   ✅ Writing tests (well-defined scope)
#   ✅ Code refactoring (focused changes)
#   ✅ Documentation generation
#   ✅ Bug fixes (specific issue)
#   ✅ Routine analysis tasks
#   ❌ Complex architecture decisions (use orchestrator instead)
#   ❌ Breaking down vague requirements (use orchestrator instead)
#
# USAGE EXAMPLES:
#   # With task description (one-shot mode):
#   ./claude-worker.sh "Add validation to email field"
#
#   # Interactive mode (start conversation):
#   ./claude-worker.sh
#
#   # Specify project directory:
#   ./claude-worker.sh "Fix login bug" ~/src/my-project
#
################################################################################

# BASH SAFETY FLAGS
# -e: Exit immediately if any command fails (don't continue on errors)
# -u: Treat unset variables as errors (catch typos in variable names)
# -o pipefail: Exit if any command in a pipeline fails (not just the last one)
# Why: These prevent silent failures and make debugging easier
set -euo pipefail

################################################################################
# ARGUMENT PARSING
################################################################################

# Capture the first argument as the task description
# ${1:-} means: use $1 if provided, otherwise use empty string
# This prevents "unbound variable" errors when no argument is given
TASK="${1:-}"

# Capture the second argument as the project directory
# ${2:-.} means: use $2 if provided, otherwise use "." (current directory)
PROJECT_DIR="${2:-.}"

# Change to the project directory
# This ensures Claude operates in the correct context
# Even if user runs script from ~/scripts/, we cd to the project
cd "$PROJECT_DIR"

################################################################################
# USER FEEDBACK
################################################################################

# Display what's happening so user knows which model is being used
# This is important because Haiku vs Sonnet = 80% cost difference!
echo "⚙️  Starting Claude Worker (Haiku 4.5)"

# Show which project we're working in
# basename extracts just the folder name (not full path)
echo "📁 Project: $(basename "$PWD")"
echo ""

################################################################################
# EXECUTION MODE DETECTION
################################################################################

# Check if user provided a task description
# [ -n "$TASK" ] means: if TASK is not empty
if [ -n "$TASK" ]; then
    #---------------------------------------------------------------------------
    # ONE-SHOT MODE: Execute single task and exit
    #---------------------------------------------------------------------------
    # User provided a task like: ./claude-worker.sh "Add validation"
    # This mode is perfect for quick tasks in scripts or automation

    echo "📋 Task: $TASK"
    echo ""

    # Launch Claude with:
    # -p "$TASK" = print mode (execute task and return result)
    # --model claude-haiku-4-5-20250514 = use CHEAP Haiku model (80% savings!)
    #
    # Why exec? Replaces current shell process with Claude
    # This means when Claude exits, the script exits (clean termination)
    # Also slightly faster and uses less memory than spawning subprocess
    exec claude -p "$TASK" --model claude-haiku-4-5-20250514

else
    #---------------------------------------------------------------------------
    # INTERACTIVE MODE: Start conversation with Claude
    #---------------------------------------------------------------------------
    # User ran: ./claude-worker.sh (no task description)
    # This starts a back-and-forth conversation session

    echo "💡 Running in interactive mode"
    echo "🎯 Focus on completing your assigned task efficiently"
    echo ""

    # Launch Claude with:
    # --model claude-haiku-4-5-20250514 = use CHEAP Haiku model
    # No -p flag = interactive conversation mode
    #
    # Why exec? Same reason as above - clean process replacement
    exec claude --model claude-haiku-4-5-20250514
fi

################################################################################
# IMPORTANT NOTES FOR USERS:
################################################################################
#
# 1. THIS SCRIPT USES HAIKU (CHEAP)
#    - Perfect for 70-80% of your daily work
#    - Implementation, tests, docs, bug fixes
#    - $0.08 for a typical task vs $0.40 with Sonnet
#
# 2. WHEN TO USE ORCHESTRATOR INSTEAD:
#    - When you can't describe the task in one sentence
#    - When you need to plan or make architecture decisions
#    - When breaking down a complex feature
#    - Use: ~/scripts/claude-orchestrator.sh
#
# 3. MONITORING COSTS:
#    - Run: npx ccusage --daily
#    - Compare Haiku vs Sonnet usage
#    - You should see 70-80% Haiku, 20-30% Sonnet
#
# 4. THE MODEL FLAG IS CRITICAL:
#    - --model claude-haiku-4-5-20250514 = cheap Haiku
#    - --model claude-sonnet-4-5-20250929 = expensive Sonnet
#    - This flag determines your cost!
#
################################################################################
