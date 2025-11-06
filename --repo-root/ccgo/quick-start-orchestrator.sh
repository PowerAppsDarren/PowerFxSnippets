#!/usr/bin/env bash
################################################################################
# Quick Start: Orchestrator-Worker Pattern Demo
################################################################################
# PURPOSE: Educational/demo script showing orchestrator-worker cost optimization
#
# WHAT THIS DOES:
#   - Explains the orchestrator-worker pattern visually
#   - Shows cost comparison (Sonnet-only vs Orchestrator+Workers)
#   - Provides workflow examples
#   - Then launches Sonnet orchestrator for hands-on practice
#
# THIS IS A LEARNING TOOL:
#   - Use this your FIRST TIME to understand the pattern
#   - After you understand it, use claude-orchestrator.sh directly
#   - Think of this as an "interactive tutorial"
#
# USAGE:
#   ./quick-start-orchestrator.sh
#   (Just run it - no arguments needed)
#
################################################################################

# BASH SAFETY FLAGS
set -euo pipefail

################################################################################
# TUTORIAL INTRODUCTION
################################################################################

# Display a nice header so user knows this is a demo/tutorial
echo "🚀 Claude Code Orchestrator-Worker Pattern - Quick Start Demo"
echo "============================================================"
echo ""

################################################################################
# EXPLAIN THE COST OPTIMIZATION
################################################################################

# Show the core value proposition: 50-70% cost savings
# This is the "why should I care?" moment
echo "This pattern saves 50-70% on costs by using:"

# Explain the two-tier pricing model
# Sonnet = expensive but smart (for planning)
# Haiku = cheap and fast (for execution)
echo "  • Sonnet 4.5 ($3/$15 per 1M tokens) for planning"
echo "  • Haiku 4.5 ($1/$5 per 1M tokens) for execution"
echo ""

################################################################################
# SHOW CONCRETE COST EXAMPLE
################################################################################

# Numbers speak louder than words!
# Show realistic cost comparison for 100 typical tasks
echo "📊 Cost Comparison:"
echo "  All Sonnet:  100 tasks = ~$50"  # Using expensive model for everything
echo "  Orchestrated: 100 tasks = ~$20  (60% savings!)"  # Smart delegation
echo ""
echo "-----------------------------------------------------------"
echo ""

################################################################################
# PROJECT CONTEXT CHECK (OPTIONAL)
################################################################################

# Check if we're in a recognized project directory
# Not required, but helps user understand best practices
#
# We look for common project markers:
# .git = git repository
# package.json = Node.js project
# requirements.txt = Python project
#
# [ ! -d ".git" ] means: if .git directory does NOT exist
# && = AND operator (all conditions must be true)
if [ ! -d ".git" ] && [ ! -f "package.json" ] && [ ! -f "requirements.txt" ]; then
    # User is not in a project - give a gentle reminder
    # ⚠️  warns but doesn't block (this is optional)
    echo "⚠️  Not in a project directory. Consider cd to a project first."
    echo ""
    # We continue anyway - demo works from anywhere
fi

################################################################################
# EXPLAIN THE WORKFLOW PATTERN
################################################################################

# This is the KEY LEARNING MOMENT
# Show users the exact workflow they'll use

echo "🎯 Example Workflow:"
echo ""

# Step 1: Orchestrator analyzes and breaks down the task
echo "1. Orchestrator (You're here in Sonnet)"
echo "   → Analyzes: 'Add user authentication with JWT'"
echo "   → Breaks into:"
#
# This is where orchestrator shows its value:
# - Takes vague requirement ("add auth")
# - Breaks into specific, parallel tasks
# - Each task is clear enough for cheap Haiku worker
echo "     - Task A: Implement JWT middleware (Worker 1 - Haiku)"
echo "     - Task B: Create auth endpoints (Worker 2 - Haiku)"
echo "     - Task C: Write integration tests (Worker 3 - Haiku)"
echo ""

# Step 2: Workers execute in parallel
# This is where the COST SAVINGS happen!
# 3 workers running Haiku = 80% cheaper than 3 Sonnets
echo "2. Workers execute in parallel (Haiku - cheap!)"
echo ""

# Step 3: Orchestrator integrates results
# Back to Sonnet for the complex task of reviewing and integrating
# Worth the cost for quality assurance and architectural consistency
echo "3. Orchestrator reviews & integrates results"
echo ""
echo "-----------------------------------------------------------"
echo ""

################################################################################
# PROVIDE ACTIONABLE GUIDANCE
################################################################################

# Tell users EXACTLY what to do next
echo "💡 Try this workflow:"
echo ""

# Option 1: Manual workflow (educational - see the pattern in action)
echo "Current terminal (Orchestrator - Sonnet):"
echo "  Ask: 'Break down this task into 3 parallel subtasks: [your task]'"
echo ""
echo "Open 3 new terminals and run:"
echo "  Terminal 2: ~/scripts/claude-worker.sh 'Task A description'"
echo "  Terminal 3: ~/scripts/claude-worker.sh 'Task B description'"
echo "  Terminal 4: ~/scripts/claude-worker.sh 'Task C description'"
echo ""

# Option 2: Automated workflow with Zellij (advanced - when you're ready)
echo "Or use Zellij for automatic layout:"
echo "  zellij --layout orchestrator"
#
# Zellij layout = automatic window management
# Opens 1 orchestrator + 3 workers + monitor in one command
# Advanced users will love this for efficiency
echo ""
echo "-----------------------------------------------------------"
echo ""

################################################################################
# MONITORING TIP
################################################################################

# Always remind users to monitor their costs
# This validates the savings and builds good habits
echo "📈 Monitor costs in real-time:"
echo "  npx ccusage --live"
#
# ccusage --live shows:
# - Tokens used by each model
# - Cost per model
# - Total daily/weekly/monthly spend
# - Verification that Haiku is being used!
echo ""

################################################################################
# INTERACTIVE PAUSE (USER CONSENT)
################################################################################

# Wait for user to read and understand before launching
# This prevents accidental Claude sessions
echo "Ready to start? Press Enter to launch orchestrator..."
read  # Waits for Enter key press
#
# Why pause here?
# - User has time to read the tutorial
# - User explicitly chooses to continue
# - Prevents accidental expensive Sonnet sessions
# - Creates a mental "checkpoint" - user knows they're starting orchestrator

################################################################################
# LAUNCH ORCHESTRATOR
################################################################################

# Now launch the actual orchestrator with Sonnet
# exec = replace this shell with Claude (clean exit when Claude exits)
# --model = use expensive Sonnet for orchestrator role
#
# User is now in an interactive Sonnet session
# They can practice breaking down tasks
# They can spawn workers using the commands shown above
exec claude --model claude-sonnet-4-5-20250929

################################################################################
# IMPORTANT NOTES FOR USERS:
################################################################################
#
# 1. THIS IS A LEARNING TOOL
#    - First time: Run this script to understand the pattern
#    - After learning: Use ~/scripts/claude-orchestrator.sh directly
#    - This script shows HOW, the other script is for daily use
#
# 2. WHAT HAPPENS NEXT (after you press Enter):
#    - Sonnet orchestrator starts (expensive but necessary)
#    - You ask it to break down a complex task
#    - It gives you 3 specific subtasks
#    - You open new terminals and run workers for each subtask
#    - Workers use Haiku (cheap!) to execute
#    - You return to orchestrator to integrate results
#
# 3. EXAMPLE PRACTICE SESSION:
#    You: "Break down: Add payment processing with Stripe"
#    Orchestrator: "I recommend 3 parallel tasks:
#      1. Set up Stripe SDK and API keys (Worker 1)
#      2. Create payment form component (Worker 2)
#      3. Implement webhook handlers (Worker 3)"
#
#    Then in 3 terminals:
#      Terminal 2: ~/scripts/claude-worker.sh "Set up Stripe SDK..."
#      Terminal 3: ~/scripts/claude-worker.sh "Create payment form..."
#      Terminal 4: ~/scripts/claude-worker.sh "Implement webhooks..."
#
#    Each worker costs ~$0.10 (Haiku)
#    vs ~$0.50 each with Sonnet
#    Savings: $1.20 per feature!
#
# 4. WHEN TO USE THIS DEMO SCRIPT:
#    ✅ Your first time learning the pattern
#    ✅ Teaching someone else the pattern
#    ✅ When you forget the workflow
#    ❌ Daily work (use claude-orchestrator.sh instead)
#
# 5. THE ZELLIJ OPTION:
#    After you're comfortable with manual workflow:
#    - Run: cd ~/your-project && zellij --layout orchestrator
#    - This automatically opens:
#      * 1 orchestrator pane (top)
#      * 3 worker panes (middle)
#      * 1 monitor pane (bottom)
#    - All in one window, perfect for complex features!
#
################################################################################
