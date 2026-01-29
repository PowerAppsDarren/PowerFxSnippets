# PowerFx Snippets - Migration Guide (v2.0)

This guide documents the directory restructuring performed in the v2.0 repository reorganization. If you previously bookmarked or referenced files using the old directory structure, use this guide to find their new locations.

**Last Updated:** 2026-01-29

---

## Table of Contents

- [Overview](#overview)
- [Directory Mapping Table](#directory-mapping-table)
- [Detailed Migration Notes](#detailed-migration-notes)
- [Updating Your Bookmarks and Links](#updating-your-bookmarks-and-links)
- [Removed Directories](#removed-directories)
- [History](#history)

---

## Overview

The repository was restructured to provide a clearer, more consistent organization of Power Fx snippets. The old flat directory structure has been replaced with a hierarchical layout that groups related content together.

**Key changes:**
- Control-related content consolidated under `ui-controls/` and `ui-patterns/`
- Data-related content organized under `data-operations/`
- Function-related content grouped under `functions/`
- Learning materials centralized under `learning/`
- Old directories have been removed; all content has been migrated

---

## Directory Mapping Table

| Old Path                    | New Path                                 | Notes                                              |
|-----------------------------|------------------------------------------|----------------------------------------------------|
| `controls/`                 | `ui-controls/`                           | All control snippets moved here                    |
| `components/`               | `ui-patterns/components/`                | Custom and code components                         |
| `code-components/`          | `ui-patterns/components/code-components/`| PCF and code component references                  |
| `data-sources/`             | `data-operations/sources/`               | Database schemas, DrawSQL, MSSQL sources           |
| `user-defined-functions/`   | `functions/`                             | UDFs now under broader functions directory          |
| `user-defined-types/`       | `functions/`                             | UDTs grouped with other function patterns           |
| `encode-decode/`            | `functions/encoding-decoding/`           | Encoding/decoding functions                        |
| `msapp-files/`              | *(archived)*                             | MSAPP file content moved to separate toolkit repo  |
| `certification-exams/`      | `learning/certification/`                | PL-900, PL-200, and other cert resources           |
| `App.Formulas/`             | `app-lifecycle/formulas/`                | Named formulas, expressions, collections           |
| `App.OnError/`              | `app-onerror/`                           | Error handling patterns                            |
| `App.OnMessage/`            | `app-onmessage/`                         | Message handling patterns                          |
| `App.OnStart/`              | `app-onstart/`                           | App initialization patterns                        |
| `App.StartScreen/`          | `app-startscreen/`                       | Start screen configurations                        |
| `Algorithms/`               | `functions/algorithms/`                  | Algorithm implementations                          |
| `Connectors/`               | `integrations/connectors/`               | Connector-specific patterns                        |
| `Controls/`                 | `ui-controls/`                           | Same as `controls/` above                          |
| `Data Sources/`             | `data-operations/sources/`               | Same as `data-sources/` above                      |
| `Data Samples/`             | `data-operations/samples/`               | Sample data files and datasets                     |
| `SVGs/`                     | `visual-assets/svgs/`                    | SVG graphics and icons                             |
| `Fonts/`                    | `visual-assets/fonts/`                   | Font resources and configurations                  |
| `Icons/`                    | `visual-assets/icons/`                   | Icon collections                                   |
| `Components/`               | `ui-patterns/components/`                | Same as `components/` above                        |

---

## Detailed Migration Notes

### Controls to UI Controls

The `controls/` directory (and its capitalized variant `Controls/`) has been renamed and reorganized as `ui-controls/`. All control-specific snippets (gallery, label, button, chart, etc.) are now grouped by control type:

```
ui-controls/
├── add-media/
├── attachment/
├── calendar/
├── canvas/
├── chart/
├── container/
├── datacard/
├── drop-down-list/
├── gallery/
│   ├── interactions/
│   ├── layouts/
│   └── styling/
├── icon/
├── image/
├── label-or-text/
├── naming-controls/
├── rectangle/
├── sliders/
└── text-input/
```

### Components to UI Patterns

Both `components/` and `code-components/` have been merged into `ui-patterns/components/`:

```
ui-patterns/
├── components/
│   ├── code-components/     (formerly code-components/)
│   └── custom-components/   (formerly components/)
├── dialogs/
├── menus/
└── theming/
```

### Data Sources to Data Operations

All data-related content is now under `data-operations/`:

```
data-operations/
├── geocoding/
├── json/
├── samples/        (formerly Data Samples/)
│   ├── 538-data/
│   ├── jokes/
│   ├── lorem-ipsum/
│   ├── people/
│   ├── schemas/
│   ├── vehicles/
│   └── world-wide/
└── sources/        (formerly data-sources/ and Data Sources/)
    ├── drawsql/
    └── mssql/
```

### Functions Consolidation

User-defined functions, types, and encoding utilities are now grouped:

```
functions/
├── algorithms/           (formerly Algorithms/)
├── built-in/
│   └── forall/
├── encoding-decoding/    (formerly encode-decode/)
├── string-manipulation/
│   ├── padding/
│   ├── parsing/
│   ├── transformations/
│   └── validation/
├── user-defined-functions/  (formerly user-defined-functions/)
└── user-defined-types/      (formerly user-defined-types/)
```

### Learning and Certification

Certification exam resources have been consolidated with other learning materials:

```
learning/
├── best-practices/
├── certification/     (formerly certification-exams/)
│   ├── pl-200/
│   └── pl-900/
├── README.md
└── tutorials/
    └── getting-started/
```

---

## Updating Your Bookmarks and Links

1. **GitHub bookmarks:** Replace the old directory path with the new path in your browser bookmarks
2. **Internal references:** If you have Power Apps documentation referencing these snippets, update the file paths using the mapping table above
3. **Cloned repositories:** After pulling the latest changes, all old paths will automatically reflect the new structure
4. **Search indexes:** The repository includes updated `SEARCH-INDEX.md`, `TAG-INDEX.md`, `DIFFICULTY-INDEX.md`, and `PRODUCT-INDEX.md` for finding snippets

---

## Removed Directories

The following old directories no longer exist in the repository. All content has been migrated to the new locations shown in the mapping table above:

- `controls/` and `Controls/`
- `components/` and `Components/`
- `code-components/`
- `data-sources/` and `Data Sources/`
- `Data Samples/`
- `user-defined-functions/`
- `user-defined-types/`
- `encode-decode/`
- `msapp-files/`
- `certification-exams/`
- `Algorithms/`
- `Connectors/`
- `SVGs/`
- `Fonts/`
- `Icons/`

**Note:** These old paths will return 404 errors if accessed directly. Use the migration table to find the new locations.

---

## History

| Date       | Author | Changes                                                     |
|------------|--------|-------------------------------------------------------------|
| 2026-01-29 | Claude | Created migration guide documenting v2.0 path restructuring |
