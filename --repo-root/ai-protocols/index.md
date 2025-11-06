# AI-Protocols Master Index

**Purpose:** Central directory of all mandatory protocols and guidelines for AI-assisted development across all repositories.

**Last Updated:** 2025-10-31

---

## [CRITICAL] Protocol - Read First!

### [MANDATORY] [AI-Chats Session Documentation Protocol](./ai-chats/README.md)
**File:** `ai-chats/README.md` (main protocol)

**What:** Mandatory folder-based documentation system (v3.2) for tracking ALL AI-assisted development sessions
- Split-file architecture (--00 for summary, --01+ for verbatim exchanges)
- Session folder naming: `YYYY-MM-DD-NN-description/`
- Model-specific files: `[Model-Version]--NN.md` (NO SPACES, DOUBLE DASH)
- Master INDEX.md maintenance

**When:** EVERY AI session - before starting ANY work, create session folder and files
**Priority:** [MANDATORY] - Non-negotiable for all AI tools

---

## Protocol Directory

### Core Workflow Protocols

#### [MANDATORY] [AI-Chats Protocol](./ai-chats.md)
- **Description:** Full AI-Chats session documentation protocol (v3.2)
- **When to use:** Every AI interaction - session tracking and verbatim documentation
- **Priority:** [MANDATORY]

---

### Development Philosophy

#### [IMPORTANT] [AI Priorities - Make-It-Work-First](./ai-priorities.md)
- **Description:** Development philosophy emphasizing functional code before defensive programming
- **Core principles:**
  - Build the happy path first
  - No theoretical defenses
  - Learn from real failures
  - Guard only what breaks
  - Keep code readable and honest
- **When to use:** All code development - guides coding approach and priorities
- **Priority:** [IMPORTANT] - Shapes development methodology

---

### Prompt Engineering

#### [IMPORTANT] [AI-PROMPTS Master System Prompt](./prompts.md)
- **Description:** Prompt optimization protocol for transforming imperfect prompts into precise, constraint-driven, testable prompts
- **Features:**
  - Diagnosis of ambiguities and gaps
  - Multiple optimized variants (Structured, Concise, Tool-Using)
  - Model parameter recommendations
  - Test & evaluation kits
  - Safety and compliance checks
- **When to use:** When crafting complex prompts or optimizing AI interactions
- **Priority:** [IMPORTANT] - Improves AI response quality

---

### Technical Standards

#### [REFERENCE] [Port Number Assignment Protocol](./port-numbers.md)
- **Description:** Standard for selecting available port numbers (50000-60000 range)
- **Rules:**
  - Avoid common ports (80, 8080, 3000, etc.)
  - Random selection from 50000-60000 range
  - Verify availability with netstat/lsof/ss
  - Sequential assignment for multi-service apps (e.g., 55123, 55124, 55125)
- **When to use:** Setting up any web services, APIs, or networked applications
- **Priority:** [REFERENCE] - Follow when configuring ports

---

### Quality Assurance

#### [REFERENCE] [Code Review Protocol](./review.md)
- **Description:** Comprehensive multi-stage code review protocol
- **Phases:**
  1. Static Analysis (linting, type checking, dependency audits)
  2. Dynamic Analysis (runtime behavior, error handling)
  3. Security Audit (OWASP checks, input validation)
  4. Performance Profiling (efficiency, bundle size)
  5. Best Practices Alignment (style, accessibility, maintainability)
  6. AI-Driven Refactoring Suggestions
- **Output:** Detailed report saved to `./look-around/YYYY-MM-DD--HH-MM--{MODEL_NAME}`
- **When to use:** First time assisting with repo, after significant changes by other AI tools
- **Priority:** [REFERENCE] - Use when doing comprehensive reviews

---

## Quick Reference

### Starting a New Project Session?
1. Read [`ai-chats/README.md`](./ai-chats/README.md) - AI-Chats protocol
2. Create session folder: `ai-chats/YYYY-MM-DD-01-description/`
3. Create your model file: `[Model-Version]--00.md`
4. Update the session INDEX.md at session end

### Writing Code?
1. Follow [`ai-priorities.md`](./ai-priorities.md) - Make it work first!
2. Check [`port-numbers.md`](./port-numbers.md) if setting up services
3. Document in your session files as you go

### Doing a Code Review?
1. Follow [`review.md`](./review.md) protocol
2. Output to `./look-around/` directory
3. Check `ai-chats/` folder for changes by other AI tools

### Optimizing Prompts?
1. Apply [`prompts.md`](./prompts.md) protocol
2. Generate multiple variants
3. Include test cases and evaluation criteria

---

## Protocol Statistics

- **Total Protocols:** 5
- **Mandatory:** 1 (AI-Chats)
- **Important:** 2 (Make-It-Work-First, Prompts)
- **Reference:** 2 (Port Numbers, Review)

---

## Maintenance

**How to Add New Protocols:**
1. Create new `.md` file in the ai-protocols directory
2. Add entry to this index.md under appropriate category
3. Include: name, description, when to use, priority
4. Update protocol statistics count

**Version History:**
- **v1.0** (2025-10-31): Initial comprehensive index with all existing protocols

---

## File Structure

```
ai-protocols/
├── index.md                          <- YOU ARE HERE
├── readme.md                         <- Overview and timeless message
├── ai-chats.md                       <- AI-Chats protocol (v3.2)
├── ai-priorities.md                  <- Make-It-Work-First philosophy
├── prompts.md                        <- Prompt optimization
├── port-numbers.md                   <- Port assignment rules
├── review.md                         <- Code review protocol
├── mandatory-protocols.md            <- List of mandatory protocols
├── ai-log.md                         <- AI activity logging
└── ai-chats/                         <- Session folder template
    └── README.md                     <- Full AI-Chats protocol documentation
```

---

**Remember:** All protocols in this directory will be copied to every repository you work on. They are meant to ensure consistency, quality, and proper documentation across all AI-assisted development work.
