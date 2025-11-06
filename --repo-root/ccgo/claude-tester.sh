#!/usr/bin/env bash
################################################################################
# Claude Tester Session Launcher
################################################################################
# PURPOSE: Launch Claude Code with Haiku 4.5 for TEST GENERATION
#
# COST OPTIMIZATION:
#   - Test generation is well-defined, repetitive work
#   - Perfect for cheap Haiku model ($1/$5 vs $3/$15)
#   - Saves 80% on test generation costs!
#   - Example: Generating tests for 10 files:
#     * Sonnet: $6.00
#     * Haiku:  $1.20
#     * Savings: $4.80 (80%)!
#
# WHAT THIS GENERATES:
#   - Unit tests (test individual functions)
#   - Integration tests (test component interactions)
#   - Edge case coverage (boundary conditions, nulls, etc.)
#   - Error handling tests (what happens when things fail)
#   - Mocked external dependencies (APIs, databases, etc.)
#
# WHEN TO USE THIS:
#   ✅ After implementing new features
#   ✅ When test coverage is low
#   ✅ Before refactoring (tests = safety net)
#   ✅ For TDD (test-driven development)
#   ✅ When adding to legacy code (tests = documentation)
#
# USAGE EXAMPLES:
#   # Generate tests for specific file:
#   ./claude-tester.sh src/utils/validation.js
#
#   # Generate tests for component:
#   ./claude-tester.sh src/components/LoginForm.tsx
#
#   # Interactive mode (discuss testing strategy):
#   ./claude-tester.sh
#
################################################################################

# BASH SAFETY FLAGS
set -euo pipefail

################################################################################
# ARGUMENT PARSING
################################################################################

# Capture the file to generate tests for
# ${1:-} means: use $1 if provided, otherwise empty string
FILE="${1:-}"

################################################################################
# USER FEEDBACK
################################################################################

# Make it clear we're using Haiku (the CHEAP model)
# Test generation is perfect for Haiku - well-defined, repetitive
echo "🧪 Starting Claude Tester (Haiku 4.5)"
echo ""

################################################################################
# EXECUTION MODE DETECTION
################################################################################

# Check if user provided a file to test
# [ -n "$FILE" ] means: if FILE is not empty
if [ -n "$FILE" ]; then
    #---------------------------------------------------------------------------
    # TARGETED TEST GENERATION: Generate tests for specific file
    #---------------------------------------------------------------------------
    # User provided a file like: ./claude-tester.sh src/auth.js
    # We'll create comprehensive tests for that file

    echo "📝 Generating tests for: $FILE"
    echo ""

    # Build a detailed test generation prompt
    # The more specific our requirements, the better the tests
    TEST_PROMPT="Generate comprehensive tests for: $FILE

Requirements:
- Test all exported functions/classes
  # Why: Public API needs thorough testing
  # Make sure every function has at least one test

- Include edge cases and error handling
  # Why: Most bugs happen at boundaries
  # Test: null, undefined, empty strings, max values, min values
  # Test: What happens when API fails, network errors, etc.

- Mock external dependencies appropriately
  # Why: Tests should be fast, isolated, deterministic
  # Mock: API calls, database queries, file system, timers
  # Don't: Make real network requests, touch real databases

- Use project's testing framework conventions
  # Why: Consistency with existing tests
  # Check existing tests to match style
  # Use same test runner (Jest, Mocha, pytest, etc.)

- Aim for 90%+ code coverage
  # Why: High coverage = fewer production bugs
  # Cover: All code paths, branches, error conditions
  # Don't obsess: 100% is often overkill

- Add descriptive test names
  # Why: Tests serve as documentation
  # Good: 'should return 401 when token is expired'
  # Bad:  'test1', 'testAuth', 'test_function'
  # Format: 'should [expected behavior] when [condition]'"

    # Launch Claude with:
    # -p = print mode (generate tests and exit)
    # --model = use CHEAP Haiku model (perfect for test generation!)
    #
    # Why Haiku? Test generation is:
    # - Well-defined (clear requirements)
    # - Repetitive (similar patterns)
    # - Lower risk (tests don't ship to production)
    # - High volume (many files need tests)
    # = Perfect for cheap model!
    exec claude -p "$TEST_PROMPT" --model claude-haiku-4-5-20250514

else
    #---------------------------------------------------------------------------
    # INTERACTIVE TEST MODE: Discuss testing strategy
    #---------------------------------------------------------------------------
    # User ran: ./claude-tester.sh (no file specified)
    # Start conversation about testing approach, strategies, etc.
    # Useful for planning test suites, discussing coverage goals

    echo "💡 Interactive test generation mode"
    echo ""

    # Launch Claude in interactive mode with Haiku
    # User can ask about testing strategies, get advice, etc.
    exec claude --model claude-haiku-4-5-20250514
fi

################################################################################
# IMPORTANT NOTES FOR USERS:
################################################################################
#
# 1. THIS USES HAIKU (CHEAP!)
#    - Test generation is perfect for Haiku
#    - 80% cost savings vs Sonnet
#    - Same quality for this well-defined task
#
# 2. TYPICAL WORKFLOW:
#    Step 1: Implement feature with worker
#      ~/scripts/claude-worker.sh "Add login validation"
#
#    Step 2: Generate tests with tester
#      ~/scripts/claude-tester.sh src/auth/validation.js
#
#    Step 3: Run tests
#      npm test (or pytest, cargo test, etc.)
#
#    Step 4: Iterate if needed
#      If tests fail, fix implementation or tests
#
# 3. WHAT GETS GENERATED:
#    - Test file in correct location (e.g., __tests__/, test_*.py)
#    - Test suite structure (describe/it or test_* functions)
#    - Setup/teardown (beforeEach, afterEach, fixtures)
#    - Mocks for external dependencies
#    - Edge case coverage
#    - Error condition tests
#    - Assertions for expected behavior
#
# 4. COST EXAMPLE (REAL SAVINGS):
#    Scenario: Generate tests for 20 files
#
#    With Sonnet (old way):
#      20 files × $0.30 per file = $6.00
#
#    With Haiku (new way):
#      20 files × $0.06 per file = $1.20
#
#    Savings: $4.80 (80%)!
#    Over a year (1 test/day): $1,752 saved!
#
# 5. TEST BEST PRACTICES:
#    - Test behavior, not implementation
#    - One assertion per test (mostly)
#    - Test names should read like documentation
#    - Mock external dependencies
#    - Aim for fast tests (< 100ms each)
#    - Test happy path AND error cases
#
# 6. TESTING PYRAMID:
#    - Lots of unit tests (fast, cheap, focused)
#    - Some integration tests (medium speed/cost)
#    - Few E2E tests (slow, expensive, fragile)
#    This tester is best for unit/integration tests
#
# 7. FRAMEWORKS SUPPORTED:
#    - JavaScript/TypeScript: Jest, Mocha, Vitest
#    - Python: pytest, unittest
#    - Rust: cargo test
#    - Go: testing package
#    - Ruby: RSpec, Minitest
#    - Java: JUnit, TestNG
#    (Haiku knows all major testing frameworks!)
#
################################################################################
