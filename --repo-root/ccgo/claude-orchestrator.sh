#!/usr/bin/env bash
################################################################################
# Claude Orchestrator Session Launcher
################################################################################
# PURPOSE: Launch Claude Code using Sonnet 4.5 for PLANNING and DELEGATION
#
# COST STRATEGY:
#   - This uses Sonnet ($3/$15 per 1M tokens) - EXPENSIVE!
#   - But only for 20-30% of your work (planning/architecture)
#   - It delegates execution to cheap Haiku workers (80% savings)
#   - Overall: 50-70% cost reduction despite using expensive model
#
# WHEN TO USE THIS (20-30% of work):
#   ✅ Complex multi-step features (need to break down)
#   ✅ Architecture decisions (which approach to take?)
#   ✅ Breaking down vague requirements into specific tasks
#   ✅ Integrating results from multiple workers
#   ✅ Strategic refactoring decisions
#   ❌ Simple implementation tasks (use worker instead)
#   ❌ Writing tests (use tester instead)
#   ❌ Bug fixes (use worker instead)
#
# TYPICAL WORKFLOW:
#   1. Start orchestrator (this script)
#   2. Ask: "Break down: Add user authentication with JWT"
#   3. Orchestrator plans 3 subtasks
#   4. Open 3 terminals, run: ~/scripts/claude-worker.sh "Task 1"
#   5. Workers execute in parallel (cheap Haiku!)
#   6. Return to orchestrator to review & integrate
#
# USAGE EXAMPLES:
#   # Start in current directory:
#   ./claude-orchestrator.sh
#
#   # Start in specific project:
#   ./claude-orchestrator.sh ~/src/my-project
#
################################################################################

# BASH SAFETY FLAGS
# -e: Exit on any error
# -u: Treat unset variables as errors
# -o pipefail: Catch errors in pipes
set -euo pipefail

################################################################################
# ARGUMENT PARSING
################################################################################

# Get project directory from first argument, default to current directory
# ${1:-.} means: use $1 if provided, otherwise "." (current dir)
PROJECT_DIR="${1:-.}"

# Change to the project directory
# Why: Orchestrator needs context of the project to plan effectively
cd "$PROJECT_DIR"

################################################################################
# USER GUIDANCE
################################################################################

# Make it VERY CLEAR which model is running
# Users need to know this is the EXPENSIVE Sonnet model
echo "🎯 Starting Claude Orchestrator (Sonnet 4.5)"

# Show which project we're working in
echo "📁 Project: $(basename "$PWD")"
echo ""

# Display orchestrator tips
# This helps users understand the orchestrator-worker pattern
echo "💡 Tips:"

# Tip 1: When to use orchestrator
# Complex = can't describe in one sentence
# Multi-step = needs to be broken down into subtasks
echo "  - Use orchestrator for complex, multi-step tasks"

# Tip 2: The cost optimization strategy
# Orchestrator (Sonnet) plans, then delegates to Haiku workers
# This is THE KEY to 50-70% cost savings!
echo "  - Delegate focused work to Haiku workers for cost savings"

# Tip 3: How to spawn workers from command line
# Show exact command so users know how to create workers
# This is useful when orchestrator says "now create 3 workers"
echo "  - Spawn workers with: claude -p 'task description' --model claude-haiku-4-5-20250514"

echo ""

# Tip 4: Monitor your costs in real-time
# Users should watch their spending to verify savings
echo "📊 Monitor usage: npx ccusage --live"
echo ""

################################################################################
# LAUNCH ORCHESTRATOR
################################################################################

# Launch Claude with Sonnet 4.5 model
# --model claude-sonnet-4-5-20250929 = EXPENSIVE Sonnet for planning
#
# Why Sonnet for orchestrator?
# - Better at complex reasoning and breaking down tasks
# - Better at architectural decisions
# - Worth the extra cost for 20-30% of work (planning)
#
# Why exec?
# - Replaces shell process with Claude (clean exit)
# - When Claude exits, script exits
# - Slightly more efficient than subprocess
exec claude --model claude-sonnet-4-5-20250929

################################################################################
# IMPORTANT NOTES FOR USERS:
################################################################################
#
# 1. THIS SCRIPT USES SONNET (EXPENSIVE)
#    - Only use for planning and complex decisions
#    - Should be 20-30% of your total Claude usage
#    - $0.60 for planning vs $3.00 for implementing
#
# 2. THE ORCHESTRATOR-WORKER PATTERN:
#    Step 1: Orchestrator breaks down task (Sonnet - $$)
#    Step 2: Workers execute in parallel (Haiku - $)
#    Step 3: Orchestrator integrates results (Sonnet - $$)
#    Total cost: 50-70% less than doing everything in Sonnet!
#
# 3. EXAMPLE SESSION:
#    You: "I need to add payment processing to my app"
#    Orchestrator: "I recommend:
#      - Task A: Research payment gateway (Worker 1)
#      - Task B: Create API endpoints (Worker 2)
#      - Task C: Build frontend form (Worker 3)"
#
#    Then you spawn 3 workers for A, B, C (cheap Haiku!)
#    Then return to orchestrator to review integration
#
# 4. WHEN IN DOUBT:
#    - Can you describe task in one sentence? → Use worker
#    - Need to figure out HOW to approach it? → Use orchestrator
#
# 5. MONITORING YOUR PATTERN:
#    - Run: npx ccusage --daily
#    - Check Sonnet vs Haiku ratio
#    - Goal: 20-30% Sonnet, 70-80% Haiku
#    - If too much Sonnet → use workers more!
#
################################################################################
