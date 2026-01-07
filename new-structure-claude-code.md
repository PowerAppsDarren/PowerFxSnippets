# PowerFxSnippets Repository Restructuring Plan
## World-Class Organization for Developer Experience

**Created:** 2025-11-17
**Author:** Claude Code (Sonnet 4.5)
**Purpose:** Transform PowerFxSnippets into a world-class, developer-friendly snippet repository optimized for GitHub navigation and discoverability

---

## Executive Summary

### Current State Analysis
- **Total Files:** ~1,213 files across 52 directories
- **Primary Issue:** Inconsistent taxonomy with 5+ overlapping organizational schemes
- **Specific Problems:**
  - Mixed naming conventions (spaces, hyphens, dots)
  - Duplicate/overlapping categories (`String Manipulation/` vs `Text-Manipulation/`)
  - No formal metadata or tagging system
  - Variable hierarchy depth (some flat, some 4+ levels deep)
  - Difficult to discover related snippets across categories

### Transformation Goals
1. **Single organizing principle** - Feature-first, use-case-driven structure
2. **Consistent naming** - All kebab-case, GitHub-optimized
3. **Rich metadata** - Searchable tags, difficulty levels, dependencies
4. **Enhanced navigation** - Visual cues, auto-generated indexes, max 3-level depth
5. **Scalable architecture** - Easy to add new snippets and maintain over time

---

## 📁 Proposed New Structure

### Top-Level Architecture

```
PowerFxSnippets/
│
├── 📱 app-lifecycle/                  # App initialization, error handling, global formulas
├── 🎨 ui-controls/                    # Individual control implementations
├── 🎭 ui-patterns/                    # Reusable UI patterns and layouts
├── 🌈 visual-assets/                  # SVGs, icons, colors, fonts, images
├── 📊 data-operations/                # Data sources, transformations, samples
├── 🔧 functions/                      # User-defined functions, types, utilities
├── 🔗 integrations/                   # Connectors, flows, external systems
├── 🎓 learning/                       # Tutorials, best practices, certification
├── 🧰 utilities/                      # Tools, templates, scripts
│
├── .github/                           # GitHub-specific files (ISSUE_TEMPLATE, workflows)
├── .templates/                        # Snippet templates and standards
├── ai-chats/                          # AI session documentation
├── --repo-root/                       # Shared tooling
│
├── README.md                          # Main repository documentation
├── CONTRIBUTING.md                    # Contribution guidelines
├── MIGRATION-GUIDE.md                 # Old → New structure mapping
└── SEARCH-INDEX.md                    # Auto-generated searchable index
```

---

## 📱 app-lifecycle/ Structure

**Purpose:** Everything that happens at the application level - startup, shutdown, error handling, global formulas

```
app-lifecycle/
├── README.md
│
├── formulas/                          # Named formulas (App.Formulas)
│   ├── README.md
│   ├── collections/
│   │   ├── all-controls-collection.md
│   │   ├── all-screens-collection.md
│   │   └── menu-items-collection.md
│   ├── expressions/
│   │   ├── is-studio-mode.md
│   │   ├── current-user-info.md
│   │   └── theme-configuration.md
│   ├── user-defined-functions/        # UDFs from App.Formulas
│   │   ├── color-conversion.md
│   │   ├── string-utilities.md
│   │   └── validation-helpers.md
│   └── user-defined-types/            # UDTs from App.Formulas
│       ├── customer-type.md
│       ├── order-type.md
│       └── table-types.md
│
├── initialization/                    # App.OnStart patterns
│   ├── README.md
│   ├── basic-startup.md
│   ├── data-preload.md
│   ├── theme-initialization.md
│   └── user-authentication-check.md
│
├── error-handling/                    # App.OnError patterns
│   ├── README.md
│   ├── basic-error-logging.md
│   ├── network-error-recovery.md
│   ├── user-friendly-messages.md
│   └── error-kinds-reference.md
│
├── messaging/                         # App.OnMessage patterns
│   ├── README.md
│   └── message-handling-patterns.md
│
└── navigation/                        # App.StartScreen and nav patterns
    ├── README.md
    ├── conditional-start-screen.md
    └── deep-linking-patterns.md
```

---

## 🎨 ui-controls/ Structure

**Purpose:** Control-specific implementations - organized by control type with consistent sub-patterns

```
ui-controls/
├── README.md
│
├── attachments/
│   ├── README.md
│   ├── basic-file-upload.md
│   └── multi-file-management.md
│
├── button/
│   ├── README.md
│   ├── icon-button.md
│   ├── loading-state-button.md
│   └── confirmation-button.md
│
├── calendar/
│   ├── README.md
│   ├── custom-date-picker.md
│   └── date-range-selector.md
│
├── canvas/
│   ├── README.md
│   ├── drawing-canvas.md
│   └── signature-capture.md
│
├── chart/
│   ├── README.md
│   ├── dynamic-chart-data.md
│   └── custom-chart-colors.md
│
├── combobox/
│   ├── README.md
│   ├── searchable-dropdown.md
│   ├── multi-select-combobox.md
│   └── dependent-dropdowns.md
│
├── container/
│   ├── README.md
│   ├── responsive-container.md
│   ├── funnel-layout.md
│   └── card-container.md
│
├── datacard/
│   ├── README.md
│   ├── custom-datacard-layouts.md
│   └── datacard-validation.md
│
├── date-picker/
│   ├── README.md
│   ├── date-validation.md
│   └── business-days-only.md
│
├── dropdown/
│   ├── README.md
│   ├── filtered-dropdown.md
│   └── cascading-dropdown.md
│
├── form/
│   ├── README.md
│   ├── edit-form-patterns.md
│   ├── display-form-patterns.md
│   └── form-validation.md
│
├── gallery/
│   ├── README.md
│   ├── layouts/
│   │   ├── responsive-gallery.md
│   │   ├── nested-gallery.md
│   │   ├── horizontal-gallery.md
│   │   └── card-layout-gallery.md
│   ├── interactions/
│   │   ├── select-deselect.md
│   │   ├── multi-select.md
│   │   └── swipe-actions.md
│   ├── styling/
│   │   ├── alternating-row-colors.md
│   │   ├── gallery-headers.md
│   │   └── loading-indicators.md
│   └── filtering/
│       ├── search-filter.md
│       ├── multi-field-filter.md
│       └── dynamic-sorting.md
│
├── html-text/
│   ├── README.md
│   ├── rich-text-display.md
│   └── custom-html-rendering.md
│
├── label/
│   ├── README.md
│   ├── dynamic-text-sizing.md
│   ├── multi-line-labels.md
│   └── clickable-label.md
│
├── pen-input/
│   ├── README.md
│   └── signature-field.md
│
├── text-input/
│   ├── README.md
│   ├── validation/
│   │   ├── email-validation.md
│   │   ├── phone-validation.md
│   │   └── regex-validation.md
│   ├── formatting/
│   │   ├── currency-input.md
│   │   ├── auto-capitalize.md
│   │   └── masked-input.md
│   └── behaviors/
│       ├── auto-save.md
│       ├── character-counter.md
│       └── placeholder-hints.md
│
└── timer/
    ├── README.md
    ├── countdown-timer.md
    └── auto-refresh-timer.md
```

---

## 🎭 ui-patterns/ Structure

**Purpose:** Reusable UI/UX patterns that span multiple controls

```
ui-patterns/
├── README.md
│
├── navigation/
│   ├── README.md
│   ├── hamburger-menu.md
│   ├── tab-navigation.md
│   ├── breadcrumb-navigation.md
│   └── sidebar-menu.md
│
├── menus/
│   ├── README.md
│   ├── context-menu.md
│   ├── dropdown-menu.md
│   ├── menu-schema.md
│   └── dynamic-menu-generation.md
│
├── dialogs/
│   ├── README.md
│   ├── confirmation-dialog.md
│   ├── modal-dialog.md
│   └── toast-notifications.md
│
├── theming/
│   ├── README.md
│   ├── dark-mode-toggle.md
│   ├── dynamic-theme-switching.md
│   ├── microsoft-theme-palettes.md
│   └── custom-brand-themes.md
│
├── layouts/
│   ├── README.md
│   ├── responsive-layouts/
│   │   ├── mobile-first-design.md
│   │   ├── tablet-optimization.md
│   │   └── desktop-layouts.md
│   ├── positioning/
│   │   ├── center-self.md
│   │   ├── absolute-positioning.md
│   │   └── relative-positioning.md
│   └── patterns/
│       ├── master-detail.md
│       ├── dashboard-grid.md
│       └── wireframing-templates.md
│
├── components/
│   ├── README.md
│   ├── custom-components/
│   │   ├── loading-spinner.md
│   │   ├── progress-bar.md
│   │   └── rating-stars.md
│   └── code-components/
│       ├── pcf-integration.md
│       └── react-components.md
│
├── accessibility/
│   ├── README.md
│   ├── screen-reader-support.md
│   ├── keyboard-navigation.md
│   └── color-contrast.md
│
└── responsive-design/
    ├── README.md
    ├── breakpoint-patterns.md
    ├── fluid-typography.md
    └── flexible-containers.md
```

---

## 🌈 visual-assets/ Structure

**Purpose:** All visual resources - icons, colors, fonts, images

```
visual-assets/
├── README.md
│
├── svgs/
│   ├── README.md
│   ├── INDEX.md                       # Searchable catalog with previews
│   ├── azure/
│   │   ├── README.md
│   │   ├── ai-machine-learning/
│   │   ├── analytics/
│   │   ├── compute/
│   │   ├── containers/
│   │   ├── databases/
│   │   ├── devops/
│   │   ├── identity/
│   │   ├── integration/
│   │   ├── iot/
│   │   ├── management/
│   │   ├── migrate/
│   │   ├── mixed-reality/
│   │   ├── mobile/
│   │   ├── networking/
│   │   ├── security/
│   │   ├── storage/
│   │   └── web/
│   ├── fabric/
│   │   ├── README.md
│   │   └── [Fabric icon categories]
│   ├── power-bi/
│   │   ├── README.md
│   │   └── [Power BI icons]
│   └── power-platform/
│       ├── README.md
│       └── [Power Platform icons]
│
├── icons/
│   ├── README.md
│   ├── fluent-ui-icons.md
│   └── custom-icon-fonts.md
│
├── colors/
│   ├── README.md
│   ├── functions/
│   │   ├── hex-to-rgb.md
│   │   ├── rgb-to-hsl.md
│   │   ├── rgb-to-hsv.md
│   │   ├── hsv-to-rgb.md
│   │   └── color-interpolation.md
│   ├── palettes/
│   │   ├── microsoft-brand-colors.md
│   │   ├── accessible-color-palettes.md
│   │   ├── data-viz-colors.md
│   │   └── theme-color-schemes.md
│   └── utilities/
│       ├── color-enum-reference.md
│       ├── rgba-to-hex.md
│       └── contrast-checker.md
│
├── fonts/
│   ├── README.md
│   ├── font-families.md
│   ├── font-loading.md
│   ├── custom-fonts.msapp
│   └── web-safe-fonts.md
│
├── emojis/
│   ├── README.md
│   ├── emoji-picker-data.json
│   └── emoji-in-powerapps.md
│
├── images/
│   ├── README.md
│   ├── image-optimization.md
│   └── base64-encoding.md
│
└── unicode/
    ├── README.md
    ├── special-characters.md
    └── unicode-magic.md
```

---

## 📊 data-operations/ Structure

**Purpose:** Everything data - sources, transformations, samples, schemas

```
data-operations/
├── README.md
│
├── sources/
│   ├── README.md
│   ├── sharepoint/
│   │   ├── list-connections.md
│   │   ├── library-operations.md
│   │   └── sharepoint-formulas.md
│   ├── sql/
│   │   ├── mssql-connections.md
│   │   ├── query-patterns.md
│   │   └── stored-procedures.md
│   ├── dataverse/
│   │   ├── table-connections.md
│   │   ├── relationships.md
│   │   └── choice-columns.md
│   ├── excel/
│   │   ├── excel-as-datasource.md
│   │   └── table-refresh.md
│   └── custom-api/
│       ├── rest-api-connections.md
│       └── authentication-patterns.md
│
├── transformations/
│   ├── README.md
│   ├── collections/
│   │   ├── collect-patterns.md
│   │   ├── clearcollect-vs-collect.md
│   │   └── collection-manipulation.md
│   ├── filtering/
│   │   ├── filter-functions.md
│   │   ├── search-patterns.md
│   │   └── advanced-filtering.md
│   ├── aggregations/
│   │   ├── groupby-patterns.md
│   │   ├── summarize-data.md
│   │   └── pivot-tables.md
│   └── joins/
│       ├── lookup-patterns.md
│       ├── left-join.md
│       └── merge-data.md
│
├── validation/
│   ├── README.md
│   ├── json-validation.md
│   ├── schema-validation.md
│   └── data-quality-checks.md
│
├── samples/
│   ├── README.md
│   ├── employees/
│   │   ├── README.md
│   │   ├── 5k-employees.csv
│   │   └── employee-schema.json
│   ├── jokes/
│   │   ├── README.md
│   │   └── jokes-dataset.csv
│   ├── lorem-ipsum/
│   │   ├── README.md
│   │   └── text-samples.md
│   ├── vehicles/
│   │   ├── README.md
│   │   └── vehicle-data.csv
│   ├── world-data/
│   │   ├── README.md
│   │   ├── countries.csv
│   │   ├── nationalities.csv
│   │   └── world-schemas.json
│   └── 538-data/
│       ├── README.md
│       └── [538 datasets]
│
└── schemas/
    ├── README.md
    ├── erds/
    │   ├── sample-erd.md
    │   └── dataverse-erds.md
    └── json-schemas/
        ├── schema-definitions.md
        └── validation-patterns.md
```

---

## 🔧 functions/ Structure

**Purpose:** Reusable functions, utilities, algorithms, string manipulation

```
functions/
├── README.md
│
├── user-defined-functions/
│   ├── README.md
│   ├── INDEX.md                       # Categorized UDF catalog
│   ├── date-time/
│   │   ├── add-business-days.md
│   │   ├── format-date-custom.md
│   │   └── timezone-conversion.md
│   ├── math/
│   │   ├── round-to-decimal.md
│   │   ├── percentage-calculations.md
│   │   └── statistical-functions.md
│   ├── text/
│   │   ├── capitalize-words.md
│   │   ├── trim-whitespace.md
│   │   └── parse-name-parts.md
│   ├── validation/
│   │   ├── is-valid-email.md
│   │   ├── is-valid-phone.md
│   │   └── is-valid-url.md
│   └── utilities/
│       ├── generate-guid.md
│       ├── deep-clone-table.md
│       └── safe-divide.md
│
├── user-defined-types/
│   ├── README.md
│   ├── INDEX.md
│   ├── business-types/
│   │   ├── customer.md
│   │   ├── order.md
│   │   ├── invoice.md
│   │   └── product.md
│   ├── common-types/
│   │   ├── address.md
│   │   ├── contact-info.md
│   │   └── currency-value.md
│   └── table-types/
│       ├── customer-table.md
│       └── order-table.md
│
├── string-manipulation/
│   ├── README.md
│   ├── padding/
│   │   ├── left-pad.md
│   │   ├── right-pad.md
│   │   └── center-text.md
│   ├── transformations/
│   │   ├── camel-case.md
│   │   ├── kebab-case.md
│   │   ├── snake-case.md
│   │   └── title-case.md
│   ├── parsing/
│   │   ├── split-delimited.md
│   │   ├── extract-numbers.md
│   │   └── parse-json.md
│   └── validation/
│       ├── is-empty-check.md
│       ├── contains-pattern.md
│       └── regex-patterns.md
│
├── algorithms/
│   ├── README.md
│   ├── sorting/
│   │   ├── custom-sort-order.md
│   │   └── multi-field-sort.md
│   ├── searching/
│   │   ├── binary-search.md
│   │   └── fuzzy-search.md
│   └── optimization/
│       ├── quick-mass-updates.md
│       └── batch-processing.md
│
├── encoding-decoding/
│   ├── README.md
│   ├── base64-encode.md
│   ├── base64-decode.md
│   ├── url-encoding.md
│   └── json-stringify.md
│
└── constants/
    ├── README.md
    ├── common-constants.md
    └── configuration-values.md
```

---

## 🔗 integrations/ Structure

**Purpose:** Connectors, flows, external systems, APIs

```
integrations/
├── README.md
│
├── connectors/
│   ├── README.md
│   ├── office365/
│   │   ├── outlook/
│   │   │   ├── send-email.md
│   │   │   ├── read-emails.md
│   │   │   ├── calendar-events.md
│   │   │   └── attachment-handling.md
│   │   ├── users/
│   │   │   ├── get-user-profile.md
│   │   │   ├── search-users.md
│   │   │   └── user-photo.md
│   │   ├── sharepoint/
│   │   │   ├── file-operations.md
│   │   │   ├── list-items.md
│   │   │   └── permissions.md
│   │   └── teams/
│   │       ├── post-message.md
│   │       ├── create-channel.md
│   │       └── teams-notifications.md
│   │
│   ├── custom-connectors/
│   │   ├── README.md
│   │   ├── api-authentication.md
│   │   ├── swagger-definition.md
│   │   └── custom-connector-examples.md
│   │
│   └── premium-connectors/
│       ├── README.md
│       ├── dataverse-connector.md
│       └── http-connector.md
│
├── power-automate/
│   ├── README.md
│   ├── flow-patterns/
│   │   ├── approval-flows.md
│   │   ├── scheduled-flows.md
│   │   └── instant-flows.md
│   ├── sharepoint-flows/
│   │   ├── item-created-flow.md
│   │   ├── item-updated-flow.md
│   │   └── file-upload-flow.md
│   └── integration-patterns/
│       ├── powerapps-to-flow.md
│       ├── flow-to-powerapps.md
│       └── error-handling-flows.md
│
├── external-systems/
│   ├── README.md
│   ├── model-driven-apps/
│   │   ├── javascript-integration.md
│   │   └── form-scripts.md
│   ├── powershell/
│   │   ├── admin-scripts.md
│   │   └── bulk-operations.md
│   └── git-github/
│       ├── version-control.md
│       └── ci-cd-integration.md
│
└── apis/
    ├── README.md
    ├── rest-apis/
    │   ├── get-requests.md
    │   ├── post-requests.md
    │   └── authentication.md
    └── third-party/
        ├── geocoding-apis.md
        └── payment-gateways.md
```

---

## 🎓 learning/ Structure

**Purpose:** Educational resources, best practices, tutorials, certification prep

```
learning/
├── README.md
│
├── getting-started/
│   ├── README.md
│   ├── power-fx-basics.md
│   ├── first-app-tutorial.md
│   └── common-patterns.md
│
├── best-practices/
│   ├── README.md
│   ├── performance-optimization.md
│   ├── naming-conventions.md
│   ├── code-organization.md
│   ├── error-handling-strategies.md
│   └── delegation-best-practices.md
│
├── tutorials/
│   ├── README.md
│   ├── beginner/
│   │   ├── your-first-gallery.md
│   │   ├── simple-forms.md
│   │   └── basic-navigation.md
│   ├── intermediate/
│   │   ├── complex-galleries.md
│   │   ├── custom-components.md
│   │   └── data-modeling.md
│   └── advanced/
│       ├── advanced-formulas.md
│       ├── performance-tuning.md
│       └── enterprise-patterns.md
│
├── certification/
│   ├── README.md
│   ├── pl-100/
│   │   ├── README.md
│   │   └── exam-topics.md
│   ├── pl-200/
│   │   ├── README.md
│   │   └── study-guide.md
│   ├── pl-400/
│   │   ├── README.md
│   │   └── practice-scenarios.md
│   └── pl-900/
│       ├── README.md
│       └── fundamentals.md
│
├── design-patterns/
│   ├── README.md
│   ├── mvvm-pattern.md
│   ├── repository-pattern.md
│   └── factory-pattern.md
│
├── community/
│   ├── README.md
│   ├── community-resources.md
│   ├── rock-stars.md
│   ├── forums-and-groups.md
│   └── events-and-conferences.md
│
└── licensing/
    ├── README.md
    ├── license-types.md
    └── feature-comparison.md
```

---

## 🧰 utilities/ Structure

**Purpose:** Meta files, templates, tools, scripts

```
utilities/
├── README.md
│
├── templates/
│   ├── README.md
│   ├── snippet-template.md           # Standard snippet format
│   ├── readme-template.md            # Category README format
│   └── .editorconfig                 # Editor configuration
│
├── tools/
│   ├── README.md
│   ├── snippet-validator.py          # Validates snippet frontmatter
│   ├── index-generator.py            # Auto-generates search indexes
│   └── migration-helper.py           # Assists with restructuring
│
├── scripts/
│   ├── README.md
│   └── validate-all-snippets.sh
│
└── github/
    ├── ISSUE_TEMPLATE/
    │   ├── bug-report.md
    │   ├── feature-request.md
    │   └── snippet-submission.md
    ├── workflows/
    │   ├── validate-snippets.yml
    │   └── generate-index.yml
    └── PULL_REQUEST_TEMPLATE.md
```

---

## 📝 Metadata Schema

### YAML Frontmatter Standard

Every snippet file should include YAML frontmatter with the following structure:

```yaml
---
title: "Snippet Title"
description: "Brief description of what this snippet does"
category: "primary-category"                    # e.g., ui-controls, functions, data-operations
subcategory: "subcategory"                      # e.g., gallery, string-manipulation
tags:
  - tag1                                        # Searchable tags
  - tag2
  - tag3
difficulty: beginner|intermediate|advanced      # Skill level required
products:
  - power-apps-canvas                           # Power Platform products
  - power-apps-model-driven
  - power-automate
  - power-pages
  - power-bi
dependencies:
  - dependency1                                 # Required features/connectors
  - dependency2
author: "Author Name"                           # Optional: snippet author
contributors:
  - "Contributor 1"                             # Optional: other contributors
  - "Contributor 2"
created: YYYY-MM-DD                             # Creation date
updated: YYYY-MM-DD                             # Last update date
tested_with: "Power Apps version"               # Optional: tested version
license: "MIT"                                  # License type
related:
  - path/to/related-snippet.md                  # Related snippets
  - path/to/another-related.md
---
```

### Example Snippet with Frontmatter

```markdown
---
title: "Alternating Row Colors in Gallery"
description: "Apply alternating background colors to gallery rows for better readability"
category: "ui-controls"
subcategory: "gallery"
tags:
  - gallery
  - styling
  - ux
  - accessibility
difficulty: beginner
products:
  - power-apps-canvas
dependencies: []
author: "Power Apps Community"
created: 2024-01-15
updated: 2025-11-17
tested_with: "Power Apps 3.24"
license: "MIT"
related:
  - ui-controls/gallery/styling/gallery-headers.md
  - visual-assets/colors/palettes/accessible-color-palettes.md
---

# Alternating Row Colors in Gallery

## Why It Matters

Alternating row colors (zebra striping) improve readability in data-dense galleries by providing visual separation between rows. This is especially important for:
- Long lists of data
- Tables with many columns
- Accessibility compliance (WCAG 2.1)

## Implementation

### Gallery Template Fill Property

```powerfx
If(
    Mod(ThisItem.Value, 2) = 0,
    RGBA(245, 245, 245, 1),  // Even rows - light gray
    RGBA(255, 255, 255, 1)    // Odd rows - white
)
```

### Alternative Using Theme Colors

```powerfx
If(
    Mod(ThisItem.Value, 2) = 0,
    ColorFade(RGBA(0, 120, 212, 1), 90%),  // Even - faded primary
    RGBA(255, 255, 255, 1)                  // Odd - white
)
```

### Accessible High-Contrast Version

```powerfx
If(
    Mod(ThisItem.Value, 2) = 0,
    RGBA(240, 240, 240, 1),  // 4.5:1 contrast ratio
    RGBA(255, 255, 255, 1)
)
```

## Best Practices

- Ensure sufficient contrast ratio (minimum 4.5:1 for WCAG AA)
- Use subtle color differences to avoid visual fatigue
- Test in both light and dark themes
- Consider colorblind-safe palettes

## Related Patterns

- [Gallery Headers](./gallery-headers.md)
- [Accessible Color Palettes](../../visual-assets/colors/palettes/accessible-color-palettes.md)
- [Responsive Gallery Layouts](ui-controls/gallery/layouts/responsive-gallery.md)

## Credits

Community contribution - adapted from Power Apps forums

---
```

---

## 🗺️ Migration Mapping (Old → New)

### Complete Path Conversions

| Current Location            | New Location                                     | Notes                                                                         |
|-----------------------------|--------------------------------------------------|-------------------------------------------------------------------------------|
| `App.Formulas/`             | `app-lifecycle/formulas/`                        | Split into collections/, expressions/, user-defined-functions/, user-defined-types/ |
| `App.OnError/`              | `app-lifecycle/error-handling/`                  | Consolidate error patterns                                                    |
| `App.OnMessage/`            | `app-lifecycle/messaging/`                       |                                                                               |
| `App.OnStart/`              | `app-lifecycle/initialization/`                  |                                                                               |
| `App.StartScreen/`          | `app-lifecycle/navigation/`                      |                                                                               |
| `Controls/Gallery/`         | `ui-controls/gallery/`                           | Split into layouts/, interactions/, styling/, filtering/                      |
| `Controls/Container/`       | `ui-controls/container/`                         |                                                                               |
| `Controls/Label or Text/`   | `ui-controls/label/`                             | Rename (remove "or Text")                                                     |
| `Controls/Text Input/`      | `ui-controls/text-input/`                        | Split into validation/, formatting/, behaviors/                               |
| `Controls/Combobox-Classic/`| `ui-controls/combobox/`                          | Rename (remove "-Classic")                                                    |
| `Controls/Attachments/`     | `ui-controls/attachments/`                       |                                                                               |
| `Controls/Calendar/`        | `ui-controls/calendar/`                          |                                                                               |
| `Controls/Canvas/`          | `ui-controls/canvas/`                            |                                                                               |
| `Controls/Chart/`           | `ui-controls/chart/`                             |                                                                               |
| `Controls/DataCard/`        | `ui-controls/datacard/`                          |                                                                               |
| `Controls/Date Picker/`     | `ui-controls/date-picker/`                       |                                                                               |
| `Controls/Drop down/`       | `ui-controls/dropdown/`                          |                                                                               |
| `Controls/Form/`            | `ui-controls/form/`                              |                                                                               |
| `Controls/HTML text/`       | `ui-controls/html-text/`                         |                                                                               |
| `Controls/Pen input/`       | `ui-controls/pen-input/`                         |                                                                               |
| `Controls/Timer/`           | `ui-controls/timer/`                             |                                                                               |
| `Components/`               | `ui-patterns/components/custom-components/`      |                                                                               |
| `Code Components/`          | `ui-patterns/components/code-components/`        | Merge with Components                                                         |
| `Menu-Related/`             | `ui-patterns/menus/`                             |                                                                               |
| `Dialogs/`                  | `ui-patterns/dialogs/`                           |                                                                               |
| `Center Self/`              | `ui-patterns/layouts/positioning/`               |                                                                               |
| `Wire Framing/`             | `ui-patterns/layouts/patterns/`                  |                                                                               |
| `Color/`                    | `visual-assets/colors/functions/`                | Split functions vs palettes                                                   |
| `Color Palettes/`           | `visual-assets/colors/palettes/`                 |                                                                               |
| `Themes-Color-Palettes/`    | `visual-assets/colors/palettes/`                 | Merge with Color Palettes                                                     |
| `Theming/`                  | `ui-patterns/theming/`                           |                                                                               |
| `SVGs/`                     | `visual-assets/svgs/`                            | Maintain sub-structure                                                        |
| `Icons/`                    | `visual-assets/icons/`                           |                                                                               |
| `Fonts/`                    | `visual-assets/fonts/`                           |                                                                               |
| `Images/`                   | `visual-assets/images/`                          |                                                                               |
| `Emojis/`                   | `visual-assets/emojis/`                          |                                                                               |
| `Charts/`                   | `ui-controls/chart/`                             | Merge with Controls/Chart                                                     |
| `Unicode-Magic/`            | `visual-assets/unicode/`                         |                                                                               |
| `Data Samples/`             | `data-operations/samples/`                       | Maintain sub-structure                                                        |
| `Data Sources/`             | `data-operations/sources/`                       | Split by source type                                                          |
| `Data ERDs/`                | `data-operations/schemas/erds/`                  |                                                                               |
| `Connectors/`               | `integrations/connectors/office365/`             | Split by connector type                                                       |
| `Custom Connectors APIs/`   | `integrations/connectors/custom-connectors/`     |                                                                               |
| `Flows/`                    | `integrations/power-automate/`                   |                                                                               |
| `Functions/`                | `functions/`                                     | Split into subdirectories                                                     |
| `User Defined Functions/`   | `functions/user-defined-functions/`              | Split by category                                                             |
| `User Defined Types/`       | `functions/user-defined-types/`                  | Split by category                                                             |
| `Algorithms/`               | `functions/algorithms/`                          |                                                                               |
| `String Manipulation/`      | `functions/string-manipulation/`                 |                                                                               |
| `Text-Manipulation/`        | `functions/string-manipulation/`                 | DUPLICATE - merge                                                             |
| `Encode Decode/`            | `functions/encoding-decoding/`                   |                                                                               |
| `Constants/`                | `functions/constants/`                           |                                                                               |
| `Errors/`                   | `app-lifecycle/error-handling/`                  | Merge with App.OnError                                                        |
| `Code Comments/`            | `learning/best-practices/`                       |                                                                               |
| `JSON/`                     | `data-operations/validation/`                    |                                                                               |
| `Best Practices/`           | `learning/best-practices/`                       |                                                                               |
| `Content for Learning/`     | `learning/getting-started/`                      |                                                                               |
| `Learning/`                 | `learning/tutorials/`                            |                                                                               |
| `Certification Exams/`      | `learning/certification/`                        | Maintain sub-structure                                                        |
| `Communities/`              | `learning/community/`                            |                                                                               |
| `Power Apps Rock Stars/`    | `learning/community/`                            |                                                                               |
| `Licensing/`                | `learning/licensing/`                            |                                                                               |
| `Design/`                   | `learning/design-patterns/`                      |                                                                               |
| `Model Driven/`             | `integrations/external-systems/model-driven-apps/` |                                                                               |
| `PowerShell/`               | `integrations/external-systems/powershell/`      |                                                                               |
| `Git or GitHub/`            | `integrations/external-systems/git-github/`      |                                                                               |
| `Geocoding/`                | `integrations/apis/third-party/`                 |                                                                               |
| `.templates/`               | `utilities/templates/`                           |                                                                               |
| `--new-structure/`          | DELETE                                           | Empty, being replaced                                                         |

---

## 📋 README Template Examples

### Top-Level Category README

```markdown
# 🎨 UI Controls

Control-specific Power Fx snippets organized by control type.

## 📂 Categories

| Control Type              | Description                  | Snippet Count |
|---------------------------|------------------------------|---------------|
| [Gallery](components/gallery)     | Data display with templates  | 24            |
| [Text Input](controls/text-input) | User input fields          | 15            |
| [Combobox](./combobox)   | Dropdown selections          | 12            |
| [Button](./button)       | Action triggers              | 8             |
| [Form](./form)           | Data entry forms             | 18            |
| ...                       | ...                          | ...           |

## 🏷️ Browse by Tag

- [#validation](#validation) (23 snippets)
- [#responsive](#responsive) (18 snippets)
- [#accessibility](#accessibility) (14 snippets)
- [#performance](#performance) (9 snippets)

## 🎯 Quick Start

New to UI Controls in Power Fx? Start here:

1. [Basic Gallery Setup](ui-controls/gallery/layouts/responsive-gallery.md)
2. [Form Validation Patterns](form/form-validation.md)
3. [Input Field Best Practices](text-input/validation/email-validation.md)

## 📖 Related Resources

- [UI Patterns](./ui-patterns) - Multi-control patterns
- [Visual Assets](./visual-assets) - Colors, icons, themes
- [Best Practices](./best-practices) - Code quality guidelines

---

*Last updated: 2025-11-17 | [Contribute](./CONTRIBUTING.md)*
```

### Subcategory README

```markdown
# Gallery Snippets

Reusable Power Fx patterns for Gallery controls.

## 📂 Sub-Categories

### [Layouts](ui-controls/gallery/layouts)
Gallery arrangement and structure patterns

- [Responsive Gallery](ui-controls/gallery/layouts/responsive-gallery.md) ⭐
- [Nested Gallery](layouts/nested-gallery.md)
- [Horizontal Gallery](layouts/horizontal-gallery.md)
- [Card Layout Gallery](layouts/card-layout-gallery.md)

### [Interactions](ui-controls/gallery/interactions)
User interaction patterns

- [Select/Deselect](interactions/select-deselect.md) ⭐
- [Multi-Select](interactions/multi-select.md)
- [Swipe Actions](interactions/swipe-actions.md)

### [Styling](ui-controls/gallery/styling)
Visual appearance and theming

- [Alternating Row Colors](ui-controls/gallery/styling/alternating-row-colors.md) ⭐
- [Gallery Headers](styling/gallery-headers.md)
- [Loading Indicators](styling/loading-indicators.md)

### [Filtering](./filtering)
Data filtering and search

- [Search Filter](filtering/search-filter.md) ⭐
- [Multi-Field Filter](filtering/multi-field-filter.md)
- [Dynamic Sorting](filtering/dynamic-sorting.md)

## 🔍 Browse by Difficulty

| Difficulty        | Snippets                     |
|-------------------|------------------------------|
| 🟢 Beginner       | [8 snippets](#beginner)      |
| 🟡 Intermediate   | [12 snippets](#intermediate) |
| 🔴 Advanced       | [4 snippets](#advanced)      |

## 🏷️ Tags

`#gallery` `#responsive` `#nested` `#filtering` `#styling` `#select` `#multi-select` `#search` `#sorting` `#loading`

---

⭐ = Most popular snippets
```

---

## 🚀 Implementation Plan

### Phase 1: Foundation (Week 1)
**Goal:** Set up new structure without breaking existing

1. **Create new directory structure**
   - Create all top-level folders (`app-lifecycle/`, `ui-controls/`, etc.)
   - Create all second-level subdirectories
   - Create placeholder README.md files

2. **Define templates and standards**
   - Finalize snippet template with frontmatter
   - Create README templates for each level
   - Set up `.editorconfig` for consistency

3. **Build utilities**
   - Write `snippet-validator.py` (validates frontmatter)
   - Write `index-generator.py` (auto-generates search indexes)
   - Write `migration-helper.py` (assists with file moves and updates)

### Phase 2: Content Migration (Week 2-3)
**Goal:** Move and enhance existing content

1. **Migrate high-priority categories first**
   - `App.Formulas/` → `app-lifecycle/formulas/`
   - `Controls/Gallery/` → `ui-controls/gallery/`
   - `Data Samples/` → `data-operations/samples/`
   - `SVGs/` → `visual-assets/svgs/`

2. **Add frontmatter to migrated files**
   - Use validation script to ensure consistency
   - Add tags, difficulty levels, metadata

3. **Merge duplicate categories**
   - `String Manipulation/` + `Text-Manipulation/` → `functions/string-manipulation/`
   - `Color/` + `Color Palettes/` + `Themes-Color-Palettes/` → `visual-assets/colors/`

### Phase 3: Documentation (Week 3-4)
**Goal:** Comprehensive navigation and discovery

1. **Write all README files**
   - Top-level category READMEs with overviews
   - Subcategory READMEs with snippet lists
   - Main repository README with new structure

2. **Generate indexes**
   - Auto-generate `SEARCH-INDEX.md` with all snippets
   - Create tag-based indexes
   - Build difficulty-based navigation

3. **Create migration guide**
   - `MIGRATION-GUIDE.md` with old → new path mappings
   - Redirects or notes in old locations
   - Update links in existing content

### Phase 4: Automation (Week 4-5)
**Goal:** Maintain quality and consistency

1. **GitHub Actions**
   - Validate all snippets on PR (check frontmatter)
   - Auto-generate indexes on merge
   - Check for broken links

2. **Templates and contribution guides**
   - Issue templates for snippet submissions
   - PR template with checklist
   - `CONTRIBUTING.md` with guidelines

### Phase 5: Cleanup (Week 5-6)
**Goal:** Remove old structure, finalize

1. **Verify all content migrated**
   - Compare old vs new file counts
   - Check for orphaned files
   - Verify all links updated

2. **Archive old structure**
   - Move old directories to `--old-structure-archive/`
   - Add deprecation notices
   - Update all external links

3. **Final validation**
   - Run all validation scripts
   - Generate final search indexes
   - Review all README files

---

## ✅ Success Criteria

### Developer Experience
- [ ] Any snippet findable in < 30 seconds
- [ ] Clear visual hierarchy in GitHub UI
- [ ] Consistent naming across all directories
- [ ] Every folder has a README.md
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
- [ ] Support for future growth (100+ snippets per category)

### Discoverability
- [ ] Tag-based navigation
- [ ] Difficulty-level filtering
- [ ] Related snippets linked
- [ ] Product-specific views
- [ ] Full-text search support

---

## 🎯 Key Benefits

### For Contributors
- **Clear structure** - Know exactly where new snippets belong
- **Templates** - Consistent format reduces decision fatigue
- **Automated validation** - Catch errors before merge
- **Easy to navigate** - Find related snippets quickly

### For Users
- **Faster discovery** - Multiple paths to find snippets (category, tag, difficulty)
- **Better organization** - Logical grouping by use case
- **Rich metadata** - Know difficulty, dependencies, products before opening
- **Visual navigation** - Emoji icons for quick scanning

### For Maintainers
- **Automated tools** - Index generation, validation, link checking
- **Scalable** - Structure supports 10x growth
- **Consistent** - Enforced standards reduce tech debt
- **Documented** - Clear migration path and contribution guide

---

## 🔄 Maintenance Strategy

### Weekly
- Review new snippet submissions
- Update search indexes
- Check for broken links

### Monthly
- Review tag taxonomy (add/merge tags as needed)
- Update difficulty ratings based on feedback
- Archive obsolete snippets

### Quarterly
- Analyze usage metrics (if available)
- Update contribution guidelines
- Review and update templates
- Community feedback survey

---

## 📞 Questions & Feedback

For questions about this restructuring plan:
- Open a GitHub Discussion
- Tag maintainers in issues
- Join the Power Platform community forums

---

**Document Version:** 1.0
**Last Updated:** 2025-11-17
**Author:** Claude Code (Sonnet 4.5)
**Status:** Proposed - Awaiting Review
