# Feature Specification: Repository Restructuring

**Feature ID:** 001-repository-restructure
**Created:** 2025-11-17
**Status:** In Progress (Phase 1 Complete)
**Priority:** High
**Effort:** 6 weeks (6 phases)

## Overview

Transform PowerFxSnippets into a world-class, developer-friendly snippet repository optimized for GitHub navigation and discoverability.

### Problem Statement

The current repository has **1,213 files across 52 directories** with multiple critical issues:

1. **Inconsistent Taxonomy**: 5+ overlapping organizational schemes (technical category, app lifecycle, use case, resource type, knowledge/meta)
2. **Duplicate Categories**: `String Manipulation/` vs `Text-Manipulation/`, multiple color directories
3. **No Metadata System**: No tags, difficulty levels, or searchability
4. **Mixed Naming Conventions**: Spaces, hyphens, and dots used inconsistently
5. **Variable Hierarchy Depth**: Some categories flat (1 level), others deeply nested (4+ levels)
6. **Poor Discoverability**: Difficult to find related snippets across categories

### Goals

1. **Single Organizing Principle**: Feature-first, use-case-driven structure
2. **Consistent Naming**: All kebab-case, GitHub-optimized
3. **Rich Metadata**: Searchable tags, difficulty levels, dependencies
4. **Enhanced Navigation**: Visual cues, auto-generated indexes, max 3-level depth
5. **Scalable Architecture**: Easy to add new snippets and maintain

## User Stories

### US1: As a developer, I want to quickly find snippets by use case

**Acceptance Criteria:**
- [ ] Repository organized by what I want to accomplish (not technical categories)
- [ ] Clear top-level categories with emoji visual cues
- [ ] README in every folder with snippet listings
- [ ] Can find any snippet in < 30 seconds

**Priority:** P0 (Must Have)

### US2: As a contributor, I want clear guidelines for adding snippets

**Acceptance Criteria:**
- [ ] Templates for snippets with YAML frontmatter
- [ ] Templates for README files
- [ ] Clear contribution guidelines
- [ ] Automated validation of snippet format

**Priority:** P0 (Must Have)

### US3: As a user, I want to filter snippets by difficulty and tags

**Acceptance Criteria:**
- [ ] Every snippet has YAML frontmatter with metadata
- [ ] Tags are consistent and searchable
- [ ] Difficulty levels (beginner, intermediate, advanced) on all snippets
- [ ] Auto-generated indexes by tag and difficulty

**Priority:** P1 (Should Have)

### US4: As a maintainer, I want automated quality checks

**Acceptance Criteria:**
- [ ] Validation scripts for snippet frontmatter
- [ ] Automated index generation
- [ ] GitHub Actions for CI/CD
- [ ] Link checking automation

**Priority:** P1 (Should Have)

### US5: As a GitHub browser, I want visual navigation aids

**Acceptance Criteria:**
- [ ] Emoji icons for all top-level categories
- [ ] Consistent README structure across all levels
- [ ] Table of contents with quick links
- [ ] Badge system for snippet status

**Priority:** P2 (Nice to Have)

## Proposed Solution

### Architecture

**9 Top-Level Categories** (Feature-First Organization):

```
PowerFxSnippets/
├── 📱 app-lifecycle/          # App initialization, error handling, global formulas
├── 🎨 ui-controls/            # Individual control implementations
├── 🎭 ui-patterns/            # Reusable UI patterns and layouts
├── 🌈 visual-assets/          # SVGs (1000+), icons, colors, fonts
├── 📊 data-operations/        # Data sources, transformations, samples
├── 🔧 functions/              # User-defined functions, types, utilities
├── 🔗 integrations/           # Connectors, flows, external systems
├── 🎓 learning/               # Tutorials, best practices, certification
└── 🧰 utilities/              # Templates, tools, scripts, GitHub configs
```

**Hierarchy Rules:**
- Maximum 3 levels deep
- Kebab-case naming throughout
- README.md in every directory
- Consistent subdirectory patterns

### Metadata Schema

Every snippet includes YAML frontmatter:

```yaml
---
title: "Snippet Title"
description: "Brief description"
category: "ui-controls"
subcategory: "gallery"
tags:
  - gallery
  - responsive
  - filtering
difficulty: beginner|intermediate|advanced
products:
  - power-apps-canvas
  - power-apps-model-driven
dependencies: []
author: "Author Name"
created: YYYY-MM-DD
updated: YYYY-MM-DD
license: "MIT"
related:
  - path/to/related-snippet.md
---
```

### Migration Strategy

**Complete Migration Mapping** (52 old → new paths):

| Current Location | New Location | Action |
|-----------------|--------------|--------|
| `App.Formulas/` | `app-lifecycle/formulas/` | Split into collections/, expressions/, UDFs/, UDTs/ |
| `Controls/Gallery/` | `ui-controls/gallery/` | Split into layouts/, interactions/, styling/, filtering/ |
| `String Manipulation/` + `Text-Manipulation/` | `functions/string-manipulation/` | **MERGE** duplicates |
| `Color/` + `Color Palettes/` + `Themes-Color-Palettes/` | `visual-assets/colors/` | **CONSOLIDATE** |
| `SVGs/` | `visual-assets/svgs/` | Maintain existing sub-structure |
| ... | ... | See plan.md for complete 52-entry mapping |

## Success Criteria

### Developer Experience
- [ ] Any snippet findable in < 30 seconds
- [ ] Clear visual hierarchy in GitHub UI
- [ ] Consistent naming across all directories
- [ ] Every folder has README.md
- [ ] Tags enable cross-category discovery

### Technical Quality
- [ ] All snippets have valid frontmatter
- [ ] No broken internal links
- [ ] Automated validation in CI/CD
- [ ] Search index auto-updates
- [ ] Migration guide 100% complete

### Scalability
- [ ] Easy to add new snippets (template-based)
- [ ] Clear contribution guidelines
- [ ] Automated quality checks
- [ ] Consistent categorization
- [ ] Support for 10x growth

## Non-Goals

- Rewriting snippet content (only reorganizing)
- Changing existing snippet code (preserve as-is)
- Removing old snippets (archive, don't delete)
- Creating new snippets (focus on reorganization)

## Dependencies

- Git (for submodule management)
- Python 3.11+ (for validation scripts)
- GitHub Actions (for automation)

## Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Breaking existing links | High | Create migration guide, redirects in old locations |
| Community confusion | Medium | Clear announcement, phased rollout, documentation |
| Incomplete migration | High | Automated verification, complete file inventory |
| Loss of content | Critical | Backup before migration, version control |

## Timeline

- **Phase 1**: Foundation (Week 1) - ✅ **COMPLETE**
- **Phase 2**: Content Migration (Week 2-3)
- **Phase 3**: Documentation (Week 3-4)
- **Phase 4**: Automation (Week 4-5)
- **Phase 5**: Cleanup (Week 5-6)
- **Phase 6**: Launch (Week 6)

## Open Questions

- [ ] Should migration happen incrementally or all at once?
- [ ] Need approval from PowerFxSnippets maintainers?
- [ ] Create feature branch or work on main?
- [ ] When to announce restructuring to community?

## References

- [Complete Restructuring Plan](../--new-structure-claude-code.md)
- [AI-Chats Session](../../ai-chats/2025-11-17-01-powerfx-snippets-restructure/)
- [PowerFxSnippets Repository](https://github.com/PowerAppsDarren/PowerFxSnippets)
