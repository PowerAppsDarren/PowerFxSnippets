#!/usr/bin/env bash
################################################################################
# Claude Reviewer Session Launcher
################################################################################
# PURPOSE: Launch Claude Code with Sonnet 4.5 for CODE REVIEW
#
# WHY SONNET FOR REVIEWS?
#   - Code review requires deep analysis (Sonnet is better at this)
#   - Security vulnerabilities need careful examination
#   - Performance issues require sophisticated reasoning
#   - Worth the extra cost for quality/security assurance
#   - Reviews are typically 5-10% of your work (affordable)
#
# REVIEW FOCUS AREAS:
#   1. Security - SQL injection, XSS, auth bypass, secrets exposure
#   2. Performance - N+1 queries, memory leaks, inefficient algorithms
#   3. Code Quality - Duplication, complexity, maintainability
#   4. Testing - Edge cases, error handling, coverage gaps
#
# WHEN TO USE THIS:
#   ✅ Before merging to production
#   ✅ Security-critical code (auth, payments, data access)
#   ✅ Performance-critical code (APIs, data processing)
#   ✅ Inherited/legacy code you need to understand
#   ✅ Pre-deployment final check
#
# USAGE EXAMPLES:
#   # Review a specific file:
#   ./claude-reviewer.sh src/auth/login.js
#
#   # Review entire directory:
#   ./claude-reviewer.sh src/components/
#
#   # Review with no target (interactive):
#   ./claude-reviewer.sh
#
################################################################################

# BASH SAFETY FLAGS
set -euo pipefail

################################################################################
# ARGUMENT PARSING
################################################################################

# Capture the review target (file or directory)
# ${1:-.} means: use $1 if provided, otherwise "." (current directory)
# This allows reviewing current directory by default
TARGET="${1:-.}"

################################################################################
# USER FEEDBACK
################################################################################

# Make it clear we're using Sonnet for review
# Users should know this is the EXPENSIVE model (worth it for reviews)
echo "🔍 Starting Claude Reviewer (Sonnet 4.5)"

# Show what's being reviewed
echo "📁 Reviewing: $TARGET"
echo ""

# Display the review checklist so user knows what to expect
echo "🎯 Review checklist:"
echo "  ✓ Security vulnerabilities"  # OWASP Top 10, auth issues, etc.
echo "  ✓ Performance issues"        # N+1 queries, memory leaks, etc.
echo "  ✓ Code quality"              # Duplication, complexity, readability
echo "  ✓ Test coverage"             # Edge cases, error handling
echo ""

################################################################################
# EXECUTION MODE DETECTION
################################################################################

# Check if target is a valid file or directory
# -d = is directory, -f = is file
# [ ] || [ ] = OR condition in bash
if [ -d "$TARGET" ] || [ -f "$TARGET" ]; then
    #---------------------------------------------------------------------------
    # STRUCTURED REVIEW MODE: Target specified, use detailed review prompt
    #---------------------------------------------------------------------------
    # User provided a specific file/directory to review
    # We'll create a comprehensive review prompt with specific criteria

    # Build a multi-line review prompt
    # This gives Claude clear instructions on what to look for
    # The more specific we are, the better the review quality
    REVIEW_PROMPT="Perform comprehensive code review of: $TARGET

Focus on:
1. Security - SQL injection, XSS, authentication, secrets exposure
   # Why: Security issues can lead to data breaches, user compromise
   # Look for: Unvalidated input, exposed credentials, weak auth

2. Performance - N+1 queries, memory leaks, inefficient algorithms
   # Why: Performance issues lead to slow apps, high costs, bad UX
   # Look for: Unnecessary loops, redundant API calls, memory growth

3. Maintainability - Code duplication, complexity, documentation
   # Why: Maintainable code = faster feature dev, easier debugging
   # Look for: Copy-pasted code, complex functions, missing docs

4. Testing - Edge cases, error handling, coverage gaps
   # Why: Untested code = production bugs, user-facing errors
   # Look for: Missing error handling, edge cases, happy-path-only tests

Provide:
- Severity rating (Critical/High/Medium/Low)
  # Critical = security vulnerability, data loss risk
  # High = performance issue, major bug
  # Medium = code quality, maintainability
  # Low = minor improvements, style issues

- Specific line numbers
  # Always reference exact locations so fixes are easy

- Recommended fixes
  # Explain HOW to fix, not just WHAT is wrong

- Example corrections
  # Show before/after code when possible"

    # Launch Claude in print mode with the review prompt
    # -p = print mode (execute task and return result)
    # --model = use Sonnet for deep analysis
    #
    # Why Sonnet? Security/performance reviews need sophisticated reasoning
    # Worth the extra cost to catch bugs before production!
    exec claude -p "$REVIEW_PROMPT" --model claude-sonnet-4-5-20250929

else
    #---------------------------------------------------------------------------
    # INTERACTIVE REVIEW MODE: No target, start conversation
    #---------------------------------------------------------------------------
    # User ran: ./claude-reviewer.sh (no file/directory specified)
    # Start interactive session where user can discuss code
    # Useful for exploratory reviews or discussing architecture

    # Launch Claude in interactive mode
    # User can paste code, ask questions, request reviews
    exec claude --model claude-sonnet-4-5-20250929
fi

################################################################################
# IMPORTANT NOTES FOR USERS:
################################################################################
#
# 1. REVIEWS USE SONNET (EXPENSIVE BUT WORTH IT)
#    - Security reviews need deep analysis
#    - Performance issues need sophisticated detection
#    - Better to spend $0.50 on review than $5000 on breach!
#
# 2. WHEN TO REVIEW:
#    - Before production deployment
#    - After significant refactoring
#    - When working with sensitive data (auth, payments, PII)
#    - When performance is critical (APIs, data processing)
#    - When you inherit unfamiliar code
#
# 3. REVIEW BEST PRACTICES:
#    - Review small chunks (one feature at a time)
#    - Focus on critical paths first (auth, payments)
#    - Act on Critical/High issues immediately
#    - Schedule Medium/Low issues for later
#
# 4. COST OPTIMIZATION:
#    - Reviews are ~5-10% of total work
#    - Worth using Sonnet for quality assurance
#    - One caught security bug pays for 1000 reviews!
#
# 5. WHAT GETS REVIEWED:
#    - Code logic and implementation
#    - Security vulnerabilities
#    - Performance bottlenecks
#    - Test coverage gaps
#    - Documentation quality
#    - Error handling completeness
#
# 6. SEVERITY LEVELS EXPLAINED:
#    - Critical: Fix immediately, blocks deployment
#    - High: Fix before merge, could cause issues
#    - Medium: Fix soon, affects maintainability
#    - Low: Nice to have, style/minor improvements
#
################################################################################
