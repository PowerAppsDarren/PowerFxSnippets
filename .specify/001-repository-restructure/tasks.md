# Tasks: Repository Restructuring

**Input**: Design documents from `/specs/001-repository-restructure/`
**Prerequisites**: spec.md, plan.md

**Organization**: Tasks are grouped by phase to enable independent implementation and tracking.

## Format: `[ID] [Phase] [P?] Description`

- **[Phase]**: Which implementation phase this task belongs to (Phase1, Phase2, Phase3, Phase4, Phase5, Phase6)
  _Note: Phase labels (Phase1-6) are distinct from user story priorities (P0/P1/P2) in spec.md_
- **[P]**: Can run in parallel (different files, no dependencies)
- Include exact paths in descriptions

---

## ✅ Phase 1: Foundation (COMPLETE)

**Purpose**: Project initialization and basic structure

**Status**: ✅ All tasks complete (2025-11-17)

- [x] T001 [P1] Create 9 top-level directories (app-lifecycle/, ui-controls/, ui-patterns/, visual-assets/, data-operations/, functions/, integrations/, learning/, utilities/)
- [x] T002 [P1] Create complete 3-level subdirectory hierarchy (141 total directories)
- [x] T003 [P1][P] Create utilities/templates/snippet-template.md with YAML frontmatter schema
- [x] T004 [P1][P] Create utilities/templates/readme-template.md with standard README structure
- [x] T005 [P1][P] Create utilities/templates/.editorconfig for consistent formatting
- [x] T006 [P1][P] Create app-lifecycle/README.md with category overview
- [x] T007 [P1][P] Create ui-controls/README.md with control type listings
- [x] T008 [P1] Update main README.md with restructuring announcement and new structure links
- [x] T009 [P1][P] Create --new-structure-claude-code.md with comprehensive restructuring plan (40KB)

---

## Phase 2: Content Migration (Week 2-3)

**Purpose**: Move existing content to new structure with metadata

### Utilities Setup (Prerequisites for Migration)

- [ ] T010 [P2] Create utilities/tools/snippet-validator.py - Validates YAML frontmatter format
- [ ] T011 [P2] Create utilities/tools/index-generator.py - Auto-generates search indexes from snippets
- [ ] T012 [P2] Create utilities/tools/migration-helper.py - Assists with file moves and frontmatter addition
- [ ] T013 [P2][P] Create utilities/scripts/validate-all-snippets.sh - Batch validation script

### Priority Category: App.Formulas Migration

- [ ] T014 [P2] Analyze App.Formulas/ contents - categorize into collections/, expressions/, UDFs/, UDTs/
- [ ] T015 [P2] Migrate collection-related files to app-lifecycle/formulas/collections/
- [ ] T016 [P2][P] Migrate expression files to app-lifecycle/formulas/expressions/
- [ ] T017 [P2][P] Migrate UDF files to app-lifecycle/formulas/user-defined-functions/
- [ ] T018 [P2][P] Migrate UDT files to app-lifecycle/formulas/user-defined-types/
- [ ] T019 [P2] Add YAML frontmatter to all migrated App.Formulas files (~19 files)
- [ ] T020 [P2] Create app-lifecycle/formulas/README.md with complete file listing
- [ ] T021 [P2] Validate all App.Formulas migrations with snippet-validator.py

### Priority Category: Controls/Gallery Migration

- [ ] T022 [P2] Analyze Controls/Gallery/ contents - categorize into layouts/, interactions/, styling/, filtering/
- [ ] T023 [P2] Migrate layout files to ui-controls/gallery/layouts/
- [ ] T024 [P2][P] Migrate interaction files to ui-controls/gallery/interactions/
- [ ] T025 [P2][P] Migrate styling files to ui-controls/gallery/styling/
- [ ] T026 [P2][P] Migrate filtering files to ui-controls/gallery/filtering/
- [ ] T027 [P2] Add YAML frontmatter to all migrated Gallery files (~24 files)
- [ ] T028 [P2] Create ui-controls/gallery/README.md with subcategory descriptions
- [ ] T029 [P2] Validate all Gallery migrations with snippet-validator.py

### Priority Category: Data Samples Migration

- [ ] T030 [P2] Migrate Data Samples/ to data-operations/samples/ (maintain existing structure)
- [ ] T031 [P2] Add README.md files for each sample dataset subdirectory
- [ ] T032 [P2] Add metadata to sample CSV files (frontmatter in accompanying .md files)
- [ ] T033 [P2] Create data-operations/samples/README.md with sample catalog

### Priority Category: SVGs Migration

- [ ] T034 [P2] Migrate SVGs/ to visual-assets/svgs/ (maintain 4-level structure)
- [ ] T035 [P2] Create visual-assets/svgs/INDEX.md with searchable SVG catalog
- [ ] T036 [P2][P] Add README.md files for Azure/, Fabric/, Power BI/, Power Platform/ subdirectories
- [ ] T037 [P2] Generate SVG preview thumbnails or descriptions

### Duplicate Category Merges

- [ ] T038 [P2] Merge String Manipulation/ + Text-Manipulation/ → functions/string-manipulation/
- [ ] T039 [P2] Categorize merged string files into padding/, transformations/, parsing/, validation/
- [ ] T040 [P2] Add frontmatter to all merged string manipulation files
- [ ] T041 [P2] Create functions/string-manipulation/README.md
- [ ] T042 [P2] Merge Color/ + Color Palettes/ + Themes-Color-Palettes/ → visual-assets/colors/
- [ ] T043 [P2] Split into functions/, palettes/, utilities/ subdirectories
- [ ] T044 [P2] Add frontmatter to all color-related files
- [ ] T045 [P2] Create visual-assets/colors/README.md

### High-Quality Content Migration (Based on repository review)

- [ ] T046 [P2] Migrate Controls/ (remaining 16 control types) to ui-controls/ with priority on well-documented examples
- [ ] T047 [P2] Migrate Components/ to ui-patterns/components/custom-components/
- [ ] T048 [P2] Migrate Code Components/ to ui-patterns/components/code-components/
- [ ] T049 [P2] Migrate Menu-Related/ to ui-patterns/menus/
- [ ] T050 [P2] Migrate Dialogs/ to ui-patterns/dialogs/
- [ ] T051 [P2] Migrate Theming/ to ui-patterns/theming/
- [ ] T052 [P2] Migrate Data Sources/ to data-operations/sources/ (split by source type)
- [ ] T053 [P2] Migrate Connectors/ to integrations/connectors/office365/
- [ ] T054 [P2] Migrate Flows/ to integrations/power-automate/
- [ ] T055 [P2] Migrate Functions/ to functions/user-defined-functions/ (categorize by type)
- [ ] T056 [P2] Migrate User Defined Functions/ to functions/user-defined-functions/
- [ ] T057 [P2] Migrate User Defined Types/ to functions/user-defined-types/
- [ ] T058 [P2] Migrate Algorithms/ to functions/algorithms/
- [ ] T059 [P2] Migrate Encode Decode/ to functions/encoding-decoding/
- [ ] T060 [P2] Migrate Best Practices/ to learning/best-practices/
- [ ] T061 [P2] Migrate Certification Exams/ to learning/certification/
- [ ] T062 [P2] Migrate Learning/ + Content for Learning/ to learning/tutorials/
- [ ] T063 [P2] Migrate 01-getting-started/ (high-priority foundational content) to learning/getting-started/
- [ ] T064 [P2] Migrate 02-app-architecture/ to app-lifecycle/ (core functionality)
- [ ] T065 [P2] Migrate 03-user-interface/ to ui-controls/ and ui-patterns/ as appropriate
- [ ] T066 [P2] Migrate 04-data-management/ to data-operations/ (critical data operations)
- [ ] T067 [P2] Migrate 05-business-logic/ to functions/ and app-lifecycle/ as appropriate
- [ ] T068 [P2] Migrate 06-integrations/ to integrations/ (connectors and flows)
- [ ] T069 [P2] Migrate 07-assets-and-media/ to visual-assets/ (media and assets)
- [ ] T070 [P2] Migrate 08-advanced-patterns/ to appropriate categories in new structure
- [ ] T071 [P2] Migrate 09-learning-resources/ to learning/ (comprehensive learning content)

---

## Phase 3: Documentation (Week 3-4)

**Purpose**: Comprehensive navigation and discovery

### README File Creation

- [ ] T072 [P3][P] Complete ui-patterns/README.md
- [ ] T073 [P3][P] Complete visual-assets/README.md
- [ ] T074 [P3][P] Complete data-operations/README.md
- [ ] T075 [P3][P] Complete functions/README.md
- [ ] T076 [P3][P] Complete integrations/README.md
- [ ] T077 [P3][P] Complete learning/README.md
- [ ] T078 [P3][P] Complete utilities/README.md
- [ ] T079 [P3] Write README.md for all second-level directories (estimate 40+ files)
- [ ] T080 [P3] Write README.md for all third-level directories with content (estimate 20+ files)

### Content Quality Enhancement (Based on repository review)

- [ ] T081 [P3] Add visual examples (screenshots/diagrams) where appropriate to enhance understanding
- [ ] T082 [P3] Review and enhance existing documentation standards in all migrated content
- [ ] T083 [P3] Ensure troubleshooting sections are present in all complex snippets
- [ ] T084 [P3] Verify that next steps and related snippet references are updated
- [ ] T085 [P3] Add comprehensive usage examples for all migrated snippets

### Search & Discovery Tools

- [ ] T086 [P3] Generate SEARCH-INDEX.md - Complete searchable snippet catalog with all metadata
- [ ] T087 [P3] Create TAG-INDEX.md - All snippets organized by tags
- [ ] T088 [P3] Create DIFFICULTY-INDEX.md - Snippets organized by difficulty (beginner/intermediate/advanced)
- [ ] T089 [P3] Create PRODUCT-INDEX.md - Snippets organized by Power Platform product
- [ ] T090 [P3] Generate statistics (snippet counts by category, tag frequency, etc.)

### Migration Documentation

- [ ] T091 [P3] Create MIGRATION-GUIDE.md with complete 52-entry old → new path mapping
- [ ] T092 [P3] Add deprecation notices in old directory locations (after archiving)
- [ ] T093 [P3] Update all internal links in migrated snippets to use new paths
- [ ] T094 [P3] Verify no broken internal links using link-checker

---

## Phase 4: Automation (Week 4-5)

**Purpose**: Maintain quality and consistency

### GitHub Actions Workflows

- [ ] T095 [P4][P] Create .github/workflows/validate-snippets.yml - Run snippet-validator.py on every PR
- [ ] T096 [P4][P] Create .github/workflows/generate-indexes.yml - Auto-generate indexes on merge to main
- [ ] T097 [P4][P] Create .github/workflows/check-links.yml - Weekly broken link checking
- [ ] T098 [P4][P] Create .github/workflows/content-completeness.yml - Verify content completeness

### GitHub Templates

- [ ] T099 [P4][P] Create .github/ISSUE_TEMPLATE/bug-report.md
- [ ] T100 [P4][P] Create .github/ISSUE_TEMPLATE/feature-request.md
- [ ] T101 [P4][P] Create .github/ISSUE_TEMPLATE/snippet-submission.md
- [ ] T102 [P4][P] Create .github/PULL_REQUEST_TEMPLATE.md with snippet submission checklist

### Contribution Guidelines

- [ ] T103 [P4] Create CONTRIBUTING.md with:
  - How to add new snippets
  - Snippet frontmatter requirements
  - README file standards
  - Testing and validation process
  - PR submission guidelines
  - SLA commitment: Feedback provided within 48 hours on pull requests
  - Recognition system for contributors
  - Documentation quality standards from repository review

### Validation & Testing

- [ ] T104 [P4] Run snippet-validator.py on all snippets - fix any validation errors
- [ ] T105 [P4] Test index-generator.py - verify all indexes generate correctly
- [ ] T106 [P4] Test all GitHub Actions workflows in test repository
- [ ] T107 [P4] Verify validate-all-snippets.sh works on full repository

---

## Phase 5: Cleanup (Week 5-6)

**Purpose**: Remove old structure, finalize

### Verification

- [ ] T108 [P5] Generate file count report: old structure vs new structure (should match)
- [ ] T109 [P5] Identify orphaned files (files not migrated to new structure)
- [ ] T110 [P5] Migrate or archive any orphaned files
- [ ] T111 [P5] Verify all internal links updated in migrated content (no old path references)

### Archive Old Structure

- [ ] T112 [P5] Create --old-structure-archive/ directory
- [ ] T113 [P5] Move all old directories to --old-structure-archive/
- [ ] T114 [P5] Add README.md in --old-structure-archive/ explaining deprecation
- [ ] T115 [P5] Create redirect notes in old locations pointing to new paths

### Final Validation

- [ ] T116 [P5] Run snippet-validator.py on entire repository - 100% pass rate
- [ ] T117 [P5] Generate all search indexes one final time
- [ ] T118 [P5] Review all README files for completeness and accuracy
- [ ] T119 [P5] Verify all GitHub Actions passing on main branch
- [ ] T120 [P5] Final link check - no broken internal links
- [ ] T121 [P5] Test snippet discovery workflow end-to-end
- [ ] T122 [P5] Verify content quality standards are maintained throughout repository

---

## Phase 6: Launch (Week 6)

**Purpose**: Announce and communicate

### Communication

- [ ] T123 [P6] Write launch announcement for GitHub Discussions
- [ ] T124 [P6] Create GitHub Release with changelog
- [ ] T125 [P6] Update main README.md with "What's New" section highlighting restructuring
- [ ] T126 [P6] Notify regular contributors via GitHub mentions or email

### Documentation Updates

- [ ] T127 [P6] Update any external blog posts or articles linking to repository
- [ ] T128 [P6] Update links in any related repositories or projects
- [ ] T129 [P6] Create "Migration Guide for Contributors" documentation

### Monitoring & Feedback

- [ ] T130 [P6] Set up GitHub Discussions category for restructuring feedback
- [ ] T131 [P6] Monitor GitHub Issues for confusion or questions about new structure
- [ ] T132 [P6] Track metrics: search usage, popular categories, contributor feedback
- [ ] T133 [P6] Create feedback survey for community input

---

## Summary Statistics

**Total Tasks**: 133 (increased from 117 based on repository review findings)
- **Phase 1** (Foundation): 9 tasks ✅ COMPLETE
- **Phase 2** (Migration): 53 tasks (increased from 53 based on comprehensive content migration)
- **Phase 3** (Documentation): 18 tasks (increased from 18 with quality enhancements)
- **Phase 4** (Automation): 15 tasks (increased from 12 with content completeness validation)
- **Phase 5** (Cleanup): 15 tasks (increased from 14 with quality verification)
- **Phase 6** (Launch): 11 tasks

**Parallelizable Tasks**: ~45 tasks marked with [P]

**Current Progress**: 9/133 tasks complete (6.8%)
**Phase 1 Progress**: 9/9 tasks complete (100%) ✅

---

## Critical Path

The following tasks are blocking and must be completed sequentially:

1. **P2 Prerequisites**: T010-T013 (utilities) must complete before migration tasks
2. **P2 → P3**: At least 5 priority categories (T014-T045) must migrate before documentation
3. **P2 Content Migration**: T063-T070 (high-priority content) must complete before full docs
4. **P3 → P4**: MIGRATION-GUIDE.md (T091) must complete before automation
5. **P4 → P5**: All GitHub Actions (T095-T098) must work before cleanup
6. **P5 → P6**: Verification (T116-T122) must pass before launch

---

## Next Actions

**Immediate (Week 2):**
1. Create validation utilities (T010-T013)
2. Begin App.Formulas migration (T014-T021)
3. Begin Gallery migration (T022-T029)
4. Begin high-priority content migration (T063-T070)

**Short-term (Week 2-3):**
5. Complete all priority category migrations
6. Merge duplicate categories
7. Migrate remaining categories

**Medium-term (Week 3-4):**
8. Complete all README files
9. Generate all search indexes
10. Create migration guide
11. Enhance content quality based on repository review

**Long-term (Week 4-6):**
12. Set up automation
13. Clean up old structure
14. Launch and communicate
15. Monitor and collect feedback

---

## Repository Review Insights

Based on comprehensive repository analysis, these enhancements have been incorporated:

1. **Content Completeness**: Added tasks for comprehensive content migration across all 01-09 categories
2. **Quality Standards**: Added documentation quality enhancement tasks (T081-T085)
3. **Visual Content**: Added tasks for visual examples and screenshots (T081)
4. **High-Priority Content**: Identified and prioritized foundational content like 01-getting-started
5. **Validation**: Added content completeness validation in automation phase (T098)
6. **Quality Verification**: Added final quality verification in cleanup phase (T122)