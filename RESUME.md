# RESUME.md - Project State

## Last Session
- **Date:** 2025-12-18
- **Model:** Claude Opus 4.5

## Current State

Fixed Mermaid diagram rendering issue in error handler docs. All remotes in sync.

**Branch:** `main`

## What Was Accomplished This Session (2025-12-18 - Late)

### Mermaid Diagram Fix
- **File:** `errors/catch-all-errors.md`
- **Issue:** GitHub unable to render Mermaid diagram - parse error on pipe characters
- **Fix:** Replaced `|` with `&#124;` HTML entities in flowchart node text
- **Root cause:** Mermaid uses `|` for edge labels, so `Screen | Source | Message` inside a node was misinterpreted

---

## Previous Session (2025-12-18 - Earlier)

### 1. Error Handler Cooldown Feature
- **File:** `errors/catch-all-errors.md`
- **New config:** `fxErrorEmailCooldownSeconds = 10` (configurable)
- **New field:** `LastEmailSentTime` in collection for cooldown tracking
- **Behavior:** Same error can trigger new email after cooldown elapses
- **Documentation:** Added Mermaid flowchart, timeline examples, behavior matrix

### 2. Created Power Fx Gotchas Reference
- **File:** `Reference/power-fx-gotchas.md`
- **Purpose:** Document Power Fx quirks that differ from .NET/Excel/JavaScript
- **Key content:**
  - Date formatting rules (lowercase `mmm` not `MMM`)
  - CRITICAL: `m`/`mm` is context-sensitive (month vs minutes based on position)
  - Official docs link and verification workflow

### 3. Updated CLAUDE.md with Verification Workflow
- Added mandatory check for gotchas before writing ANY Power Fx code
- Added 4-step verification workflow using `ref_search_documentation`
- Added official docs URL

### 4. Updated README.md
- Added link to Power Fx Gotchas in Repository Tools section

### 5. Updated User Profile (~/.claude/CLAUDE.md)
- Added rule: "Lead with recommended option first when presenting choices"

### Key Decisions
- PDF docs (54MB) exceeds 32MB limit - cannot be used
- URL-based verification via `ref_search_documentation` is the best approach
- Custom MCP deemed overkill - existing tools work well

---

## Previous Session (2025-12-18 earlier)

### Created Environment Variables & ALM Guide
- **File:** `app-lifecycle/environment-variables-sharepoint-alm-guide.md`
- Complete deployment checklist for Power Platform solutions

---

## Folder Structure

```
PowerFxSnippets/
├── app-lifecycle/          # App formulas, OnStart, OnError, ALM guides
├── data-operations/        # Data sources and samples
├── functions/              # Algorithms, built-in, user-defined
├── integrations/           # Connectors, Power Automate
├── learning/               # Best practices, certification, tutorials
├── Reference/              # Power Fx gotchas and syntax references (NEW)
├── ui-controls/            # Gallery, buttons, inputs, etc.
├── ui-patterns/            # Components, dialogs, menus, theming
├── utilities/              # Tools and scripts
└── visual-assets/          # Colors, SVGs
```

## Next Steps (Pick Up Here)

1. **Add more gotchas** to `Reference/power-fx-gotchas.md` as discovered
2. **Test error handler cooldown** in a real Power App
3. **Continue Phase 2 migrations** from spec kit tasks
4. **Fix broken internal links** (T202)

## Git Remotes

| Remote | URL                                                              |
|--------|------------------------------------------------------------------|
| origin | ssh://git@git.superpowerlabs.app:2222/darren/PowerFxSnippets.git |
| alt    | ssh://git@pool:2222/darren/PowerFxSnippets.git                   |
| github | git@github.com:PowerAppsDarren/PowerFxSnippets.git               |
