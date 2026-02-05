---
title: "Icons Index"
description: "Searchable catalog of all Power Apps icon resources and documentation"
category: "visual-assets"
subcategory: "icons"
tags: [icons, gallery, visual-assets, enumeration, catalog]
difficulty: "beginner"
products: ["power-apps-canvas"]
author: "PowerAppsDarren"
created: "2024-01-01"
updated: "2026-01-22"
license: "MIT"
related: [visual-assets/svgs, ui-patterns/components]
---

# Icons Index

## Table of Contents

- [Icons Index](#icons-index)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
    - [When to Use](#when-to-use)
  - [Documentation Files](#documentation-files)
  - [Icon Collections](#icon-collections)
    - [Power Apps Built-in Icons](#power-apps-built-in-icons)
  - [Usage Patterns](#usage-patterns)
    - [Basic Icon Display](#basic-icon-display)
    - [Icon Gallery Implementation](#icon-gallery-implementation)
  - [External Resources](#external-resources)
  - [Related Sections](#related-sections)

A searchable catalog of all icon-related resources in this repository.

**Total Documentation Files**: 2
**Total Icon Resources**: 1
**Categories**: Icon Gallery, Icon Collections

---

## Overview

This section contains documentation and resources for working with icons in Power Apps. It includes galleries of built-in icons, collections from various icon packs, and usage patterns for implementing icon-based interfaces.

### When to Use

- **Use this section when**: Displaying icon galleries, creating icon-based navigation, or managing icon resources in your Power Apps
- **Best for**: UI designers, developers building icon-heavy interfaces, teams maintaining visual consistency
- **Related**: [SVGs](./svgs) for vector graphics, [Colors](./colors) for theming

---

## Documentation Files

| File | Description |
|------|-------------|
| [`all-icons-in-gallery.md`](./all-icons-in-gallery.md) | Complete gallery displaying all Power Apps built-in icons |
| [`README.md`](./README.md) | Comprehensive guide to icon resources and external icon packs |

---

## Icon Collections

### Power Apps Built-in Icons

The [`all-icons-in-gallery.md`](./all-icons-in-gallery.md) file provides a complete collection of all Power Apps built-in icons displayed in a gallery control. This includes:

- Category-based icon organization
- Searchable icon catalog
- Copy-ready icon names for use in formulas
- Visual preview of each icon

---

## Usage Patterns

### Basic Icon Display

```powerfx
// Display an icon in an Image control
Image: =Icon.IconName
```

### Icon Gallery Implementation

```powerfx
// Gallery showing all icons
galIcons.Items = fxIcons
galIcons.WrapCount = 4
```

---

## External Resources

The [`README.md`](./README.md) contains links to numerous external icon resources:

| Resource | Description |
|----------|-------------|
| Fluent System Icons | Microsoft's official icon set |
| Font Awesome | Popular icon library |
| Material Design Icons | Google's material icons |
| Simple Icons | Brand and technology icons |

---

## Related Sections

- [SVGs](./svgs) - Scalable vector graphics
- [Colors](./colors) - Color palettes and theming
- [UI Controls](../ui-controls) - Control styling
- [UI Patterns](../ui-patterns) - Design patterns

---

**Last Updated**: 2026-01-22
**Total Files**: 2
**Maintainers**: PowerAppsDarren
