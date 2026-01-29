# PowerFxSnippets v2.0.0 -- Repository Restructuring Complete

> **468 files. 9 categories. One mission: make Power Fx development faster and easier.**

## What Happened

The PowerFxSnippets repository has undergone a complete restructuring. Every file has been reorganized, standardized, and enhanced to make finding and using Power Fx snippets as frictionless as possible.

This is the largest update in the project's history, touching every file in the repository.

## Key Highlights

- **9 feature-based categories** replace the previous flat/legacy folder structure
- **468 markdown files** with consistent formatting, YAML frontmatter, and table of contents
- **Search indexes** (SEARCH-INDEX.md, TAG-INDEX.md, PRODUCT-INDEX.md) for fast discovery
- **GitHub Actions** that automatically validate snippet metadata on every pull request
- **Contribution infrastructure** with issue templates, PR templates, and a detailed Contributing Guide
- **Developer tools** for validating, migrating, and indexing snippets

## What Changed

### New Category Structure

| Category              | What's Inside                                        |
|-----------------------|------------------------------------------------------|
| `app-lifecycle/`      | App initialization, OnStart, OnError, named formulas |
| `ui-controls/`        | Gallery, buttons, inputs, charts, and more           |
| `ui-patterns/`        | Dialogs, menus, theming, reusable components         |
| `visual-assets/`      | SVGs, icons, colors, fonts, emojis                   |
| `data-operations/`    | Sample data, JSON handling, geocoding                |
| `functions/`          | User-defined functions, algorithms, utilities        |
| `integrations/`       | Office 365, Power Automate connectors                |
| `learning/`           | Tutorials, certification guides, best practices      |
| `utilities/`          | Templates, validation scripts, tools                 |

### Standardized Content

Every snippet now includes:

- **YAML frontmatter** with title, description, category, tags, difficulty, and product metadata
- **Table of Contents** for longer files
- **History section** tracking all changes over time
- **Consistent code fencing** with `powerfx` language tags

### Automation and Quality

- **`validate-snippets.yml`** -- GitHub Action that validates YAML frontmatter on every PR
- **`check-links.yml`** -- Weekly automated link checking with lychee
- **Issue templates** for snippet submissions, bug reports, and feature requests
- **PR template** for consistent contribution reviews

### Developer Tools

Located in `utilities/tools/`:

| Tool                       | Purpose                             |
|----------------------------|-------------------------------------|
| `snippet-validator.py`     | Validate YAML frontmatter           |
| `index-generator.py`       | Generate search indexes             |
| `add-toc-history.py`       | Add TOC and history sections        |
| `migration-helper.py`      | Migrate files with frontmatter      |

## How to Get Started

1. **Browse the new structure** -- Start with the [README](../README.md) and explore the 9 categories
2. **Find snippets by product** -- Use the [Product Index](../PRODUCT-INDEX.md) to filter by Canvas Apps, Model-Driven Apps, or Power Automate
3. **Search by tag** -- Use the [Search Index](../SEARCH-INDEX.md) and [Tag Index](../TAG-INDEX.md)
4. **Check the gotchas** -- Read [Power Fx Gotchas](../Reference/power-fx-gotchas.md) before writing Power Fx code

## For Existing Users

If you had bookmarks to files in the old structure, they have moved. See the **[Migration Guide](../MIGRATION-GUIDE.md)** for a complete mapping of old paths to new locations.

## Call for Contributions

This restructuring creates a solid foundation, but the repository thrives on community contributions. Here's how you can help:

- **Add new snippets** -- Share your Power Fx patterns and solutions
- **Improve existing content** -- Fix errors, add examples, enhance documentation
- **Report issues** -- Found a broken link or incorrect code? [Open an issue](https://github.com/PowerAppsDarren/PowerFxSnippets/issues)
- **Suggest new categories or tags** -- Help us organize better

Read the [Contributing Guide](../CONTRIBUTING.md) to get started.

## Statistics

| Metric                | Count |
|-----------------------|-------|
| Markdown files        | 468   |
| Directories           | 200+  |
| Validated snippets    | 103   |
| SVG files             | 12    |
| GitHub Action workflows | 2   |
| Categories            | 9     |
| Searchable tags       | 200+  |

## Thank You

Thank you to the Power Apps community for the inspiration and contributions that made this repository possible. Special thanks to the Microsoft Power Platform team for creating Power Fx.

---

## History

| Date       | Author  | Changes                             |
|------------|---------|-------------------------------------|
| 2026-01-29 | Phase 6 | Created v2.0.0 launch announcement  |
