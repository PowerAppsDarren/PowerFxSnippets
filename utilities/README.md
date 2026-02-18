# Utilities - Development Tools, Templates, and Scripts

## Table of Contents

- [📋 Overview](#overview)
  - [When to Use](#when-to-use)
  - [Related Categories](#related-categories)
- [📁 Subcategories](#subcategories)
  - [Docs](#docs)
  - [PowerShell](#powershell)
  - [Templates](#templates)
  - [Tools](#tools)
- [🔍 Search & Filter](#search-filter)
  - [By Purpose](#by-purpose)
  - [By Technology](#by-technology)
- [📚 Learning Path](#learning-path)
  - [For Beginners](#for-beginners)
  - [For Intermediate Users](#for-intermediate-users)
  - [For Advanced Users](#for-advanced-users)
- [🤝 Contributing](#contributing)
  - [Adding New Utilities](#adding-new-utilities)
  - [Utility Requirements](#utility-requirements)
  - [Category Maintenance](#category-maintenance)
- [🔗 Cross-References](#cross-references)
  - [Prerequisites](#prerequisites)
  - [Related Content](#related-content)
  - [Next Steps](#next-steps)
- [📞 Support & Help](#support-help)
  - [Getting Help](#getting-help)
  - [Community Resources](#community-resources)
- [📈 Recent Updates](#recent-updates)
  - [Latest Additions](#latest-additions)
  - [Recent Improvements](#recent-improvements)
- [📝 Complete Utility Index](#complete-utility-index)
  - [PowerShell](#powershell-1)
  - [Templates](#templates-1)
  - [Tools](#tools-1)

> Development utilities, templates, and automation scripts that support the PowerFxSnippets repository -- including snippet validation, migration helpers, index generation, and standardized templates for creating new content.

## 📋 Overview

This category contains the supporting infrastructure for the PowerFxSnippets repository. Rather than Power Fx code snippets themselves, these are the tools, templates, and scripts that help maintain, validate, and expand the snippet collection. They ensure consistency, quality, and ease of contribution across the entire repository.

### When to Use
- ✅ **Use this category when**: Validating snippets, creating new content from templates, running batch operations, or automating repository maintenance
- ✅ **Best for**: Contributors adding new snippets, maintainers running quality checks, and developers automating repetitive tasks
- ❌ **Don't use for**: Power Fx code patterns -- those belong in their respective category folders (ui-controls, functions, etc.)

### Related Categories
- [**Learning**](../learning) - Tutorials and best practices for contributors
- [**Functions**](../functions) - Power Fx function patterns (what these tools help maintain)

## 📁 Subcategories

### Docs
**Purpose**: Project documentation including release notes, migration guides, analytics, and reports.

**Key Content:**
- [**Release Notes v2.0.0**](docs/RELEASE-NOTES-v2.0.0.md) - Major restructuring release details
- [**Announcement v2.0.0**](docs/ANNOUNCEMENT-v2.0.0.md) - Community announcement
- [**Migration Guide**](docs/MIGRATION-GUIDE.md) - Old-to-new path mapping
- [**Analytics**](docs/analytics/) - Reporting schedule, baselines, dashboards

**When to use**: Referencing release history, understanding migration paths, or reviewing repository analytics.

### PowerShell
**Purpose**: PowerShell scripts and documentation for Power Platform administration, automation, and development workflows.

**Key Content:**
- [**PowerShell Overview**](powershell/PowerShell.md) - Why PowerShell matters for Power Platform development

**When to use**: Automating Power Platform administrative tasks, managing environments, or scripting deployment workflows.

### Templates
**Purpose**: Standardized templates for creating new snippets and README files, plus editor configuration for consistent formatting.

**Key Content:**
- [**Snippet Template**](templates/snippet-template.md) - YAML frontmatter and markdown structure for new snippets
- [**README Template**](templates/readme-template.md) - Standard category README layout
- [**.editorconfig**](templates/.editorconfig) - Editor formatting rules

**When to use**: Creating new snippets or category folders to ensure consistent structure and metadata.

### Tools
**Purpose**: Python and Bash scripts for validating, migrating, renaming, and indexing snippets across the repository.

**Key Scripts:**

| Tool                          | Language   | Purpose                                                    |
|-------------------------------|------------|------------------------------------------------------------|
| `snippet-validator.py`        | Python     | Validates YAML frontmatter and markdown structure          |
| `index-generator.py`          | Python     | Generates searchable indexes from snippet metadata         |
| `migration-helper.py`         | Python     | Migrates files with proper frontmatter and structure       |
| `add-toc-history.py`          | Python     | Adds Table of Contents and History sections to markdown    |
| `rename-dryrun.py`            | Python     | Preview file renames without executing                     |
| `rename-execute.py`           | Python     | Execute file renames (use after dry run)                   |
| `rename-to-lowercase.py`      | Python     | Preview lowercase rename operations                        |
| `rename-to-lowercase-execute.py` | Python  | Execute lowercase renames                                  |
| `validate-all-snippets.sh`    | Bash       | Batch validation of all snippets in the repository         |

**When to use**: Running quality checks before committing, migrating content between structures, or generating indexes after adding new snippets.

## 🔍 Search & Filter

### By Purpose
- **Quality Assurance**: `snippet-validator.py`, `validate-all-snippets.sh`
- **Content Creation**: `snippet-template.md`, `readme-template.md`
- **Migration & Refactoring**: `migration-helper.py`, `rename-*.py`
- **Index Generation**: `index-generator.py`
- **Markdown Maintenance**: `add-toc-history.py`

### By Technology
- **Python 3.11+**: All `.py` scripts
- **Bash**: `validate-all-snippets.sh`
- **PowerShell**: `powershell/` documentation
- **EditorConfig**: `.editorconfig` formatting rules

## 📚 Learning Path

### For Beginners
1. Start with [**Snippet Template**](templates/snippet-template.md) - Understand the expected format
2. Learn [**README Template**](templates/readme-template.md) - See how categories are structured
3. Read [**PowerShell Overview**](powershell/PowerShell.md) - Understand the admin tooling landscape

### For Intermediate Users
1. Run [**Snippet Validator**](tools/snippet-validator.py) - Check your snippet quality
2. Use [**Batch Validation**](tools/validate-all-snippets.sh) - Validate the entire repository
3. Explore [**Index Generator**](tools/index-generator.py) - See how search indexes are built

### For Advanced Users
1. Contribute to [**Migration Helper**](tools/migration-helper.py) - Help with content restructuring
2. Extend [**Rename Tools**](tools/rename-dryrun.py) - Automate batch renaming operations
3. Customize [**TOC Generator**](tools/add-toc-history.py) - Adapt markdown tooling

## 🤝 Contributing

### Adding New Utilities
1. **Check existing tools** to avoid duplication
2. **Use Python 3.11+** for new scripts (preferred language)
3. **Include docstrings and usage examples** in the script header
4. **Test thoroughly** before committing
5. **Update this README** with the new tool entry

### Utility Requirements
- [ ] **Clear purpose** documented in script header
- [ ] **Usage instructions** with example commands
- [ ] **Error handling** for common failure modes
- [ ] **Dry-run option** for destructive operations
- [ ] **No sensitive data** or hardcoded paths

### Category Maintenance
- Keep this README updated as new tools are added
- Ensure cross-references remain valid
- Test scripts periodically against the current repository structure
- Review and improve tooling as the repository evolves

## 🔗 Cross-References

### Prerequisites
Before using utilities in this category, you should understand:
- [**Power Fx Basics**](https://learn.microsoft.com/en-us/power-platform/power-fx/overview) - Fundamental concepts
- [**Python 3.11+**](https://www.python.org/) - Required for running most tools
- [**YAML Syntax**](https://yaml.org/) - Used in snippet frontmatter

### Related Content
- [**Learning**](../learning) - Tutorials, best practices, and reference guides
- [**Reference**](../learning/reference) - Power Fx gotchas and syntax guides

### Next Steps
After familiarizing yourself with utilities, consider:
- [**Contributing Snippets**](../CONTRIBUTING.md) - Use templates to add new content
- [**Running Validations**](tools/validate-all-snippets.sh) - Ensure quality across the repo
- [**Generating Indexes**](tools/index-generator.py) - Keep search up to date

## 📞 Support & Help

### Getting Help
- **❓ Questions**: [GitHub Discussions](https://github.com/PowerAppsDarren/PowerFxSnippets/discussions)
- **🐛 Issues**: [Report problems](https://github.com/PowerAppsDarren/PowerFxSnippets/issues)
- **💡 Suggestions**: [Feature requests](https://github.com/PowerAppsDarren/PowerFxSnippets/issues)

### Community Resources
- [**Power Platform Community**](https://powerplatform.microsoft.com/community/) - General discussions
- [**Microsoft Learn**](https://learn.microsoft.com/en-us/power-platform/) - Official documentation
- [**Power Apps Ideas**](https://powerusers.microsoft.com/t5/Power-Apps-Ideas/idb-p/PowerAppsIdeas) - Feature requests

## 📈 Recent Updates

### Latest Additions
- [**TOC & History Tool**](tools/add-toc-history.py) - Added 2026-01-27 - Automated markdown maintenance
- [**Snippet Validator**](tools/snippet-validator.py) - Updated 2026-01-27 - Enhanced validation rules

### Recent Improvements
- Added standardized templates for snippets and READMEs
- Improved batch validation with comprehensive error reporting
- Added rename tooling with dry-run safety

---

## 📝 Complete Utility Index

### PowerShell
- [PowerShell Overview](powershell/PowerShell.md)

### Templates
- [Snippet Template](templates/snippet-template.md)
- [README Template](templates/readme-template.md)
- [EditorConfig](templates/.editorconfig)

### Tools
- [Snippet Validator](tools/snippet-validator.py)
- [Index Generator](tools/index-generator.py)
- [Migration Helper](tools/migration-helper.py)
- [Add TOC & History](tools/add-toc-history.py)
- [Rename Dry Run](tools/rename-dryrun.py)
- [Rename Execute](tools/rename-execute.py)
- [Rename to Lowercase](tools/rename-to-lowercase.py)
- [Rename to Lowercase Execute](tools/rename-to-lowercase-execute.py)
- [Validate All Snippets](tools/validate-all-snippets.sh)

---

**📊 Last Updated**: 2026-01-29
**📄 Total Utilities**: 12 (3 templates, 9 scripts/tools)
**👥 Maintainers**: PowerAppsDarren

---

*Found this category helpful? ⭐ [Star the repository](https://github.com/PowerAppsDarren/PowerFxSnippets) to show your support!* 🚀

---

## History

| Date       | Author | Changes                                               |
|------------|--------|-------------------------------------------------------|
| 2026-02-18 | Cleanup | Add docs/ subdirectory; update cross-references for new paths |
| 2026-01-29 | Darren | Created utilities README with full tool index         |
