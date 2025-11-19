# Tasks: Repository Restructuring

**Input**: Design documents from `/specs/001-repository-restructure/`
**Prerequisites**: spec.md, plan.md

**Organization**: Tasks are grouped by phase to enable independent implementation and tracking.

## Format: `[ID] [Phase] [P?] Description`

- **[Phase]**: Which phase this task belongs to (P1, P2, P3, P4, P5, P6)
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

### Other Category Migrations (Lower Priority)

- [ ] T046 [P2] Migrate Controls/ (remaining 16 control types) to ui-controls/
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

---

## Phase 3: Documentation (Week 3-4)

**Purpose**: Comprehensive navigation and discovery

### README File Creation

- [ ] T063 [P3][P] Complete ui-patterns/README.md
- [ ] T064 [P3][P] Complete visual-assets/README.md
- [ ] T065 [P3][P] Complete data-operations/README.md
- [ ] T066 [P3][P] Complete functions/README.md
- [ ] T067 [P3][P] Complete integrations/README.md
- [ ] T068 [P3][P] Complete learning/README.md
- [ ] T069 [P3][P] Complete utilities/README.md
- [ ] T070 [P3] Write README.md for all second-level directories (estimate 40+ files)
- [ ] T071 [P3] Write README.md for all third-level directories with content (estimate 20+ files)

### Search & Discovery Tools

- [ ] T072 [P3] Generate SEARCH-INDEX.md - Complete searchable snippet catalog with all metadata
- [ ] T073 [P3] Create TAG-INDEX.md - All snippets organized by tags
- [ ] T074 [P3] Create DIFFICULTY-INDEX.md - Snippets organized by difficulty (beginner/intermediate/advanced)
- [ ] T075 [P3] Create PRODUCT-INDEX.md - Snippets organized by Power Platform product
- [ ] T076 [P3] Generate statistics (snippet counts by category, tag frequency, etc.)

### Migration Documentation

- [ ] T077 [P3] Create MIGRATION-GUIDE.md with complete 52-entry old → new path mapping
- [ ] T078 [P3] Add deprecation notices in old directory locations (after archiving)
- [ ] T079 [P3] Update all internal links in migrated snippets to use new paths
- [ ] T080 [P3] Verify no broken internal links using link-checker

---

## Phase 4: Automation (Week 4-5)

**Purpose**: Maintain quality and consistency

### GitHub Actions Workflows

- [ ] T081 [P4][P] Create .github/workflows/validate-snippets.yml - Run snippet-validator.py on every PR
- [ ] T082 [P4][P] Create .github/workflows/generate-indexes.yml - Auto-generate indexes on merge to main
- [ ] T083 [P4][P] Create .github/workflows/check-links.yml - Weekly broken link checking

### GitHub Templates

- [ ] T084 [P4][P] Create .github/ISSUE_TEMPLATE/bug-report.md
- [ ] T085 [P4][P] Create .github/ISSUE_TEMPLATE/feature-request.md
- [ ] T086 [P4][P] Create .github/ISSUE_TEMPLATE/snippet-submission.md
- [ ] T087 [P4][P] Create .github/PULL_REQUEST_TEMPLATE.md with snippet submission checklist

### Contribution Guidelines

- [ ] T088 [P4] Create CONTRIBUTING.md with:
  - How to add new snippets
  - Snippet frontmatter requirements
  - README file standards
  - Testing and validation process
  - PR submission guidelines

### Validation & Testing

- [ ] T089 [P4] Run snippet-validator.py on all snippets - fix any validation errors
- [ ] T090 [P4] Test index-generator.py - verify all indexes generate correctly
- [ ] T091 [P4] Test all GitHub Actions workflows in test repository
- [ ] T092 [P4] Verify validate-all-snippets.sh works on full repository

---

## Phase 5: Cleanup (Week 5-6)

**Purpose**: Remove old structure, finalize

### Verification

- [ ] T093 [P5] Generate file count report: old structure vs new structure (should match)
- [ ] T094 [P5] Identify orphaned files (files not migrated to new structure)
- [ ] T095 [P5] Migrate or archive any orphaned files
- [ ] T096 [P5] Verify all internal links updated in migrated content (no old path references)

### Archive Old Structure

- [ ] T097 [P5] Create --old-structure-archive/ directory
- [ ] T098 [P5] Move all old directories to --old-structure-archive/
- [ ] T099 [P5] Add README.md in --old-structure-archive/ explaining deprecation
- [ ] T100 [P5] Create redirect notes in old locations pointing to new paths

### Final Validation

- [ ] T101 [P5] Run snippet-validator.py on entire repository - 100% pass rate
- [ ] T102 [P5] Generate all search indexes one final time
- [ ] T103 [P5] Review all README files for completeness and accuracy
- [ ] T104 [P5] Verify all GitHub Actions passing on main branch
- [ ] T105 [P5] Final link check - no broken internal links
- [ ] T106 [P5] Test snippet discovery workflow end-to-end

---

## Phase 6: Launch (Week 6)

**Purpose**: Announce and communicate

### Communication

- [ ] T107 [P6] Write launch announcement for GitHub Discussions
- [ ] T108 [P6] Create GitHub Release with changelog
- [ ] T109 [P6] Update main README.md with "What's New" section highlighting restructuring
- [ ] T110 [P6] Notify regular contributors via GitHub mentions or email

### Documentation Updates

- [ ] T111 [P6] Update any external blog posts or articles linking to repository
- [ ] T112 [P6] Update links in any related repositories or projects
- [ ] T113 [P6] Create "Migration Guide for Contributors" documentation

### Monitoring & Feedback

- [ ] T114 [P6] Set up GitHub Discussions category for restructuring feedback
- [ ] T115 [P6] Monitor GitHub Issues for confusion or questions about new structure
- [ ] T116 [P6] Track metrics: search usage, popular categories, contributor feedback
- [ ] T117 [P6] Create feedback survey for community input

---

## Summary Statistics

**Total Tasks**: 117
- **Phase 1** (Foundation): 9 tasks ✅ COMPLETE
- **Phase 2** (Migration): 53 tasks
- **Phase 3** (Documentation): 18 tasks
- **Phase 4** (Automation): 12 tasks
- **Phase 5** (Cleanup): 14 tasks
- **Phase 6** (Launch): 11 tasks

**Parallelizable Tasks**: ~40 tasks marked with [P]

**Current Progress**: 9/117 tasks complete (7.7%)
**Phase 1 Progress**: 9/9 tasks complete (100%) ✅

---

## Critical Path

The following tasks are blocking and must be completed sequentially:

1. **P2 Prerequisites**: T010-T013 (utilities) must complete before migration tasks
2. **P2 → P3**: At least 5 priority categories (T014-T045) must migrate before documentation
3. **P3 → P4**: MIGRATION-GUIDE.md (T077) must complete before automation
4. **P4 → P5**: All GitHub Actions (T081-T083) must work before cleanup
5. **P5 → P6**: Verification (T093-T106) must pass before launch

---

## Next Actions

**Immediate (Week 2):**
1. Create validation utilities (T010-T013)
2. Begin App.Formulas migration (T014-T021)
3. Begin Gallery migration (T022-T029)

**Short-term (Week 2-3):**
4. Complete all priority category migrations
5. Merge duplicate categories
6. Migrate remaining categories

**Medium-term (Week 3-4):**
7. Complete all README files
8. Generate all search indexes
9. Create migration guide

**Long-term (Week 4-6):**
10. Set up automation
11. Clean up old structure
12. Launch and communicate
