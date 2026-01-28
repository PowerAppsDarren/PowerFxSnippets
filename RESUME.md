# RESUME.md - Project State

## Table of Contents

- [Last Session](#last-session)
- [Current State](#current-state)
- [What Was Accomplished This Session (2026-01-21)](#what-was-accomplished-this-session-2026-01-21)
  - [AI Chats Migration to Private Repo](#ai-chats-migration-to-private-repo)
- [Previous Session (2025-12-18 - Latest)](#previous-session-2025-12-18-latest)
  - [Error Kind Tooltip Feature](#error-kind-tooltip-feature)
- [Previous Session (2025-12-18 - Late)](#previous-session-2025-12-18-late)
  - [Mermaid Diagram Fix](#mermaid-diagram-fix)
- [Previous Session (2025-12-18 - Earlier)](#previous-session-2025-12-18-earlier)
  - [1. Error Handler Cooldown Feature](#1-error-handler-cooldown-feature)
  - [2. Created Power Fx Gotchas Reference](#2-created-power-fx-gotchas-reference)
  - [3. Updated CLAUDE.md with Verification Workflow](#3-updated-claudemd-with-verification-workflow)
  - [4. Updated README.md](#4-updated-readmemd)
  - [5. Updated User Profile (~/.claude/CLAUDE.md)](#5-updated-user-profile-claudeclaudemd)
  - [Key Decisions](#key-decisions)
- [Previous Session (2025-12-18 earlier)](#previous-session-2025-12-18-earlier)
  - [Created Environment Variables & ALM Guide](#created-environment-variables-alm-guide)
- [Folder Structure](#folder-structure)
- [Next Steps (Pick Up Here)](#next-steps-pick-up-here)
- [Git Remotes](#git-remotes)

## Last Session
- **Date:** 2026-01-21
- **Model:** Claude Opus 4.5

## Current State

Moved ai-chats folder to private repo. All remotes in sync.

**Branch:** `main`

## What Was Accomplished This Session (2026-01-21)

### AI Chats Migration to Private Repo
- **Moved:** `ai-chats/` folder (12 session folders, 49 files) → `PowerFxSnippets-Private/.ai-chats/`
- **Reason:** AI chat history should not be in public repository
- **Updated:** INDEX.md in private repo with all 13 sessions
- **Commits:** `8f62a8e` (public), `6d54fad` (private)

---

## Previous Session (2025-12-18 - Latest)

### Error Kind Tooltip Feature
- **File:** `errors/catch-all-errors.md`
- **Feature:** Hover tooltips on Kind badges in error emails show description
- **Implementation:** Added `fxErrorKinds` lookup table with all 28 error kinds
- **Fix:** Used `Substitute()` to escape apostrophes in descriptions for HTML attribute safety

---

## Previous Session (2025-12-18 - Late)

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
---

## History

| Date | Author | Changes |
|------|--------|---------|
| 2026-01-27 | Migration | Initial TOC and history section added |
