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
7. **Incomplete Migration**: New structure directories created but lack content, leading to inconsistent user experience
8. **Uneven Content Distribution**: Some categories have more content than others
9. **Missing Visual Elements**: Lack of screenshots or visual examples in many snippets

### Goals

1. **Single Organizing Principle**: Feature-first, use-case-driven structure
2. **Consistent Naming**: All kebab-case, GitHub-optimized
3. **Rich Metadata**: Searchable tags, difficulty levels, dependencies
4. **Enhanced Navigation**: Visual cues, auto-generated indexes, max 3-level depth
5. **Scalable Architecture**: Easy to add new snippets and maintain
6. **Complete Migration**: Ensure all content from old structure is properly migrated
7. **Community-Driven**: Maintain strong documentation and contribution guidelines
8. **Quality Standards**: Preserve and enhance the high documentation standards

## User Stories

### US1: As a developer, I want to quickly find snippets by use case

**Acceptance Criteria:**
- [ ] Repository organized by what I want to accomplish (not technical categories)
- [ ] Clear top-level categories with emoji visual cues
- [ ] README in every folder with snippet listings
- [ ] Can find any snippet in < 30 seconds
- [ ] Rich metadata enables advanced filtering and search
- [ ] Search indexes and tag-based navigation available

**Priority:** P0 (Must Have)

### US2: As a contributor, I want clear guidelines for adding snippets

**Acceptance Criteria:**
- [ ] Templates for snippets with YAML frontmatter
- [ ] Templates for README files
- [ ] Clear contribution guidelines
- [ ] Automated validation of snippet format
- [ ] Consistent documentation standards preserved
- [ ] Learning resources for new contributors

**Priority:** P0 (Must Have)

### US3: As a user, I want to filter snippets by difficulty and tags

**Acceptance Criteria:**
- [ ] Every snippet has YAML frontmatter with metadata
- [ ] Tags are consistent and searchable
- [ ] Difficulty levels (beginner, intermediate, advanced) on all snippets
- [ ] Auto-generated indexes by tag and difficulty
- [ ] Cross-category discovery through tags

**Priority:** P0 (Must Have)

### US4: As a maintainer, I want automated quality checks

**Acceptance Criteria:**
- [ ] Validation scripts for snippet frontmatter (required fields, valid values, ISO dates)
- [ ] Internal link integrity checking (no broken cross-references)
- [ ] Markdown formatting consistency validation
- [ ] Category placement verification (files in correct directories)
- [ ] Automated index generation from snippet metadata
- [ ] GitHub Actions for CI/CD running all validations on PR
- [ ] Content completeness verification

**Priority:** P1 (Should Have)

### US5: As a GitHub browser, I want visual navigation aids

**Acceptance Criteria:**
- [ ] Emoji icons for all top-level categories
- [ ] Consistent README structure across all levels
- [ ] Table of contents with quick links
- [ ] Badge system for snippet status
- [ ] Visual examples where applicable

**Priority:** P2 (Nice to Have)

### US6: As a community member, I want consistent, high-quality documentation

**Acceptance Criteria:**
- [ ] Preserve existing high-quality documentation standards
- [ ] Consistent format across all snippets
- [ ] Comprehensive implementation examples
- [ ] Troubleshooting and common issues sections
- [ ] Next steps and related snippet references

**Priority:** P1 (Should Have)

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
| ... | ... | See [complete 52-entry mapping](../../--new-structure-claude-code.md#migration-mapping) |

### Migration Priorities

Based on repository analysis, prioritize the following content areas for migration:

1. **High-Value Content**: Categories with the most comprehensive and high-quality documentation
2. **Most-Used Content**: Snippets that appear to be most accessed based on structure and naming
3. **Foundation Content**: Core concepts like 01-getting-started that new users depend on
4. **Visual Content**: SVGs and other visual assets that are already properly structured

## Success Criteria

### Developer Experience
- [ ] Any snippet findable in < 30 seconds
- [ ] Clear visual hierarchy in GitHub UI
- [ ] Consistent naming across all directories
- [ ] Every folder has README.md
- [ ] Tags enable cross-category discovery
- [ ] Rich search and filtering capabilities

### Technical Quality
- [ ] All snippets have valid frontmatter
- [ ] No broken internal links
- [ ] Automated validation in CI/CD
- [ ] Search index auto-updates
- [ ] Migration guide 100% complete
- [ ] High-quality documentation standards preserved

### Scalability
- [ ] Easy to add new snippets (template-based, <10 min using provided templates)
- [ ] Clear contribution guidelines (<5 steps to submit PR)
- [ ] Automated quality checks (validation completes in <30 seconds)
- [ ] Consistent categorization
- [ ] Support for 10x growth (current: 1,213 files → target: 12,000+ files without performance degradation)
- [ ] Index generation completes in <30 seconds for full repository
- [ ] Community contribution enabled

### Content Completeness
- [ ] All content from old structure properly migrated
- [ ] No content gaps in new structure
- [ ] Complete README coverage in new directories
- [ ] All metadata fields properly populated
- [ ] Cross-references and related snippets updated

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
| Quality degradation | Medium | Preserve existing high documentation standards |
| Content gaps in new structure | High | Complete content audit before migration |

## Timeline

- **Phase 1**: Foundation (Week 1) - ✅ **COMPLETE**
- **Phase 2**: Content Migration (Week 2-3) - Prioritize high-quality content
- **Phase 3**: Documentation (Week 3-4) - Focus on README completeness
- **Phase 4**: Automation (Week 4-5) - Quality checks and validation
- **Phase 5**: Cleanup (Week 5-6) - Archive old structure, verify completeness
- **Phase 6**: Launch (Week 6) - Community announcement and feedback

## Open Questions

- [ ] Should migration happen incrementally or all at once?
- [ ] Need approval from PowerFxSnippets maintainers?
- [ ] Create feature branch or work on main?
- [ ] When to announce restructuring to community?
- [ ] How to handle existing content gaps during migration?

## References

- [Complete Restructuring Plan](../--new-structure-claude-code.md)
- [AI-Chats Session](../../ai-chats/2025-11-17-01-powerfx-snippets-restructure/)
- [PowerFxSnippets Repository](https://github.com/PowerAppsDarren/PowerFxSnippets)
- [Comprehensive Repository Review](./findings-review.md)