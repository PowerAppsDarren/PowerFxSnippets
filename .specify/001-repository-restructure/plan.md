# Implementation Plan: Repository Restructuring

**Feature:** 001-repository-restructure
**Input:** spec.md
**Timeline:** 6 weeks (6 phases)
**Current Status:** Phase 1 Complete ✅

## Architecture Overview

### Technology Stack

- **Git**: Version control and submodule management
- **Python 3.11+**: Validation scripts, index generation
- **Markdown**: All documentation and snippets
- **YAML**: Frontmatter metadata
- **GitHub Actions**: Automated validation and CI/CD

### Directory Structure

```
PowerFxSnippets/
│
├── app-lifecycle/              # Phase 1 ✅ COMPLETE
│   ├── formulas/
│   │   ├── collections/
│   │   ├── expressions/
│   │   ├── user-defined-functions/
│   │   └── user-defined-types/
│   ├── initialization/
│   ├── error-handling/
│   ├── messaging/
│   └── navigation/
│
├── ui-controls/                # Phase 1 ✅ COMPLETE
│   ├── gallery/
│   │   ├── layouts/
│   │   ├── interactions/
│   │   ├── styling/
│   │   └── filtering/
│   ├── text-input/
│   │   ├── validation/
│   │   ├── formatting/
│   │   └── behaviors/
│   └── [15 more control types]/
│
├── ui-patterns/                # Phase 1 ✅ COMPLETE
├── visual-assets/              # Phase 1 ✅ COMPLETE
├── data-operations/            # Phase 1 ✅ COMPLETE
├── functions/                  # Phase 1 ✅ COMPLETE
├── integrations/               # Phase 1 ✅ COMPLETE
├── learning/                   # Phase 1 ✅ COMPLETE
│
├── utilities/                  # Phase 1 ✅ COMPLETE
│   ├── templates/
│   │   ├── snippet-template.md      ✅ Created
│   │   ├── readme-template.md       ✅ Created
│   │   └── .editorconfig            ✅ Created
│   ├── tools/                  # Phase 1: Scripts to create
│   │   ├── snippet-validator.py
│   │   ├── index-generator.py
│   │   └── migration-helper.py
│   ├── scripts/
│   └── github/
│       ├── ISSUE_TEMPLATE/
│       └── workflows/
│
├── --new-structure-claude-code.md   ✅ Complete restructuring plan
├── --old-structure-archive/         # Phase 5: Archive location
└── README.md                         ✅ Updated with restructuring notice
```

## Implementation Phases

### ✅ Phase 1: Foundation (Week 1) - COMPLETE

**Status:** ✅ Complete (2025-11-17)

**Deliverables:**
- [x] Created 9 top-level directories
- [x] Created 141 subdirectories (complete 3-level hierarchy)
- [x] Created templates (snippet-template.md, readme-template.md, .editorconfig)
- [x] Created README files for top-level categories
- [x] Updated main README with restructuring announcement
- [x] Defined metadata schema (YAML frontmatter)
- [x] Created comprehensive restructuring plan (40KB document)

**Artifacts:**
- New directory structure (9 categories, 141 total directories)
- `utilities/templates/snippet-template.md`
- `utilities/templates/readme-template.md`
- `utilities/templates/.editorconfig`
- `--new-structure-claude-code.md`
- Updated `README.md`

---

### 📋 Phase 2: Content Migration (Week 2-3)

**Goal:** Move and enhance existing content

**Priority Categories for Migration:**

1. **App.Formulas/** → **app-lifecycle/formulas/**
   - Split into collections/, expressions/, user-defined-functions/, user-defined-types/
   - Add YAML frontmatter to each file
   - ~19 files

2. **Controls/Gallery/** → **ui-controls/gallery/**
   - Reorganize into layouts/, interactions/, styling/, filtering/
   - Add metadata
   - ~24 files

3. **Data Samples/** → **data-operations/samples/**
   - Maintain existing structure
   - Add README files
   - ~50+ files

4. **SVGs/** → **visual-assets/svgs/**
   - Maintain existing 4-level structure (Azure/, Fabric/, Power BI/, Power Platform/)
   - Add index with previews
   - ~1000+ SVG files

5. **Merge Duplicates:**
   - `String Manipulation/` + `Text-Manipulation/` → `functions/string-manipulation/`
   - `Color/` + `Color Palettes/` + `Themes-Color-Palettes/` → `visual-assets/colors/`

**Deliverables:**
- [ ] Migrate high-priority categories (above 5)
- [ ] Add YAML frontmatter to all migrated snippets
- [ ] Validate frontmatter with snippet-validator.py
- [ ] Merge duplicate categories
- [ ] Create README files for migrated categories

**Tools Required:**
- `utilities/tools/migration-helper.py` - Assists with file moves and frontmatter addition
- `utilities/tools/snippet-validator.py` - Validates YAML frontmatter

---

### 📝 Phase 3: Documentation (Week 3-4)

**Goal:** Comprehensive navigation and discovery

**Top-Level README Files:**
- [ ] Complete all 9 top-level category README files
- [ ] Include snippet counts, tags, quick start guides
- [ ] Add navigation links to related categories

**Subcategory README Files:**
- [ ] Write README for every second-level directory
- [ ] Include snippet listings with descriptions
- [ ] Add difficulty-level filtering
- [ ] Include tag clouds

**Search & Discovery:**
- [ ] Generate `SEARCH-INDEX.md` - Complete searchable index
- [ ] Create tag-based indexes
- [ ] Create difficulty-based navigation
- [ ] Generate statistics (snippet counts by category)

**Migration Guide:**
- [ ] Create `MIGRATION-GUIDE.md`
- [ ] Document all 52 old → new path mappings
- [ ] Add redirects or notes in old locations
- [ ] Update all internal links in migrated content

**Deliverables:**
- [ ] README.md in every directory (100% coverage)
- [ ] `SEARCH-INDEX.md` - Auto-generated searchable catalog
- [ ] `MIGRATION-GUIDE.md` - Complete old → new mapping
- [ ] Tag-based and difficulty-based indexes

**Tools Required:**
- `utilities/tools/index-generator.py` - Auto-generates search indexes

---

### 🤖 Phase 4: Automation (Week 4-5)

**Goal:** Maintain quality and consistency

**GitHub Actions Workflows:**

1. **Validate Snippets** (`.github/workflows/validate-snippets.yml`)
   - Run on every PR
   - Check frontmatter format
   - Validate required fields
   - Fail if validation errors

2. **Generate Indexes** (`.github/workflows/generate-indexes.yml`)
   - Run on merge to main
   - Auto-generate SEARCH-INDEX.md
   - Update tag indexes
   - Update statistics
   - Commit changes back

3. **Check Links** (`.github/workflows/check-links.yml`)
   - Run weekly
   - Check for broken internal links
   - Report issues

**Validation Scripts:**
- [ ] `utilities/tools/snippet-validator.py` - Validate frontmatter
- [ ] `utilities/tools/index-generator.py` - Generate search indexes
- [ ] `utilities/scripts/validate-all-snippets.sh` - Batch validation

**Templates & Guidelines:**
- [ ] Issue templates (bug-report.md, feature-request.md, snippet-submission.md)
- [ ] PR template with checklist
- [ ] `CONTRIBUTING.md` - Contribution guidelines

**Deliverables:**
- [ ] 3 GitHub Actions workflows
- [ ] Complete validation tooling
- [ ] Contribution guidelines and templates

---

### 🧹 Phase 5: Cleanup (Week 5-6)

**Goal:** Remove old structure, finalize

**Verification:**
- [ ] Compare old vs new file counts (should match)
- [ ] Check for orphaned files (files not migrated)
- [ ] Verify all links updated in migrated content
- [ ] Test all validation scripts

**Archive Old Structure:**
- [ ] Move old directories to `--old-structure-archive/`
- [ ] Add deprecation notices in old locations
- [ ] Update any external documentation with new paths

**Final Validation:**
- [ ] Run all validation scripts on entire repository
- [ ] Generate final search indexes
- [ ] Review all README files for completeness
- [ ] Verify GitHub Actions working correctly

**Deliverables:**
- [ ] Old structure archived in `--old-structure-archive/`
- [ ] Deprecation notices in place
- [ ] 100% validation pass rate
- [ ] Final search indexes generated

---

### 🚀 Phase 6: Launch (Week 6)

**Goal:** Announce and communicate

**Community Communication:**
- [ ] Write announcement post for GitHub Discussions
- [ ] Update main README with launch announcement
- [ ] Create migration guide for contributors
- [ ] Document new contribution workflow

**Documentation Updates:**
- [ ] Update all external links to repository
- [ ] Update any blog posts or articles
- [ ] Notify regular contributors

**Monitoring:**
- [ ] Monitor GitHub issues for confusion
- [ ] Track usage of new structure
- [ ] Collect community feedback

**Deliverables:**
- [ ] Launch announcement
- [ ] Complete migration guide
- [ ] Updated external documentation
- [ ] Feedback collection system

---

## Migration Mapping Reference

### Complete Old → New Path Conversions (52 entries)

| Current Location | New Location | Migration Action |
|-----------------|--------------|------------------|
| `App.Formulas/` | `app-lifecycle/formulas/` | Split into 4 subdirs |
| `App.OnError/` | `app-lifecycle/error-handling/` | Move directly |
| `App.OnMessage/` | `app-lifecycle/messaging/` | Move directly |
| `App.OnStart/` | `app-lifecycle/initialization/` | Move directly |
| `App.StartScreen/` | `app-lifecycle/navigation/` | Move directly |
| `Controls/Gallery/` | `ui-controls/gallery/` | Split into 4 subdirs |
| `Controls/Text Input/` | `ui-controls/text-input/` | Split into 3 subdirs |
| `String Manipulation/` | `functions/string-manipulation/` | **MERGE with Text-Manipulation** |
| `Text-Manipulation/` | `functions/string-manipulation/` | **MERGE with String Manipulation** |
| `Color/` | `visual-assets/colors/functions/` | **CONSOLIDATE** |
| `Color Palettes/` | `visual-assets/colors/palettes/` | **CONSOLIDATE** |
| `Themes-Color-Palettes/` | `visual-assets/colors/palettes/` | **CONSOLIDATE** |
| `SVGs/` | `visual-assets/svgs/` | Maintain sub-structure |
| `Data Samples/` | `data-operations/samples/` | Maintain sub-structure |
| `Connectors/` | `integrations/connectors/office365/` | Split by type |
| ... | ... | [See --new-structure-claude-code.md for all 52] |

---

## Success Metrics

### Phase Completion Criteria

**Phase 1** ✅:
- [x] All directories created (9 top-level, 141 total)
- [x] Templates created (3 files)
- [x] Main README updated

**Phase 2**:
- [ ] 5 high-priority categories migrated
- [ ] 100% of migrated files have frontmatter
- [ ] Duplicate categories merged

**Phase 3**:
- [ ] 100% README coverage (all directories)
- [ ] SEARCH-INDEX.md generated
- [ ] MIGRATION-GUIDE.md complete

**Phase 4**:
- [ ] All GitHub Actions passing
- [ ] Validation scripts working
- [ ] CONTRIBUTING.md published

**Phase 5**:
- [ ] Old structure archived
- [ ] 100% validation pass
- [ ] No orphaned files

**Phase 6**:
- [ ] Launch announcement published
- [ ] Community notified
- [ ] Feedback collection active

---

## Risk Management

### High-Priority Risks

1. **Breaking External Links**
   - **Mitigation**: Create MIGRATION-GUIDE.md with redirects
   - **Validation**: Check all known external references

2. **Content Loss**
   - **Mitigation**: Git history preserves everything
   - **Validation**: File count comparison before/after

3. **Community Confusion**
   - **Mitigation**: Clear communication, phased rollout
   - **Validation**: Monitor GitHub issues and discussions

---

## Next Steps After Plan Approval

1. Execute Phase 2: Content Migration
2. Build migration-helper.py and snippet-validator.py
3. Migrate App.Formulas/ as first priority
4. Validate and iterate on migration process
