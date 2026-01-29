---
title: "Theming Patterns"
description: "Theme management, color schemes, and consistent styling patterns for Power Apps"
category: "ui-patterns"
subcategory: "theming"
tags:
  - theming
  - colors
  - styling
  - branding
  - design-system
difficulty: intermediate
products:
  - power-apps-canvas
author: "PowerAppsDarren"
created: 2026-01-27
updated: 2026-01-27
---

# Theming Patterns

## Table of Contents

- [Overview](#overview)
- [Contents](#contents)
- [Theme Structure](#theme-structure)
  - [Color Palette](#color-palette)
  - [Typography](#typography)
  - [Spacing](#spacing)
- [Applying Themes](#applying-themes)
  - [Control Properties](#control-properties)
  - [Dynamic Theming](#dynamic-theming)
- [Best Practices](#best-practices)
- [Related Resources](#related-resources)

Patterns for implementing consistent theming and styling across Power Apps applications.

## Overview

This folder contains patterns for managing themes, color schemes, and visual consistency in Power Apps. Proper theming ensures a professional appearance and makes it easy to update your app's look and feel.

## Contents

| File | Description |
|------|-------------|
| [Theming.md](./Theming.md) | Introduction to theming concepts |
| [Microsoft-Base-Themes.md](./Microsoft-Base-Themes.md) | Built-in Microsoft theme reference |

## Theme Structure

A well-organized theme typically includes:

### Color Palette

```powerfx
// Define in App.Formulas or App.OnStart
fxTheme = {
    // Primary colors
    Primary: ColorValue("#742774"),
    PrimaryLight: ColorValue("#9E3C9E"),
    PrimaryDark: ColorValue("#541F54"),

    // Secondary colors
    Secondary: ColorValue("#0078D4"),
    SecondaryLight: ColorValue("#2899F5"),

    // Semantic colors
    Success: ColorValue("#107C10"),
    Warning: ColorValue("#FFB900"),
    Error: ColorValue("#D83B01"),
    Info: ColorValue("#0078D4"),

    // Neutral colors
    Background: Color.White,
    Surface: ColorValue("#F5F5F5"),
    TextPrimary: ColorValue("#323130"),
    TextSecondary: ColorValue("#605E5C"),
    Border: ColorValue("#E1E1E1")
}
```

### Typography

```powerfx
fxTypography = {
    // Font family
    FontFamily: Font.'Segoe UI',

    // Font sizes
    SizeHeading1: 28,
    SizeHeading2: 24,
    SizeHeading3: 20,
    SizeBody: 14,
    SizeCaption: 12,

    // Font weights
    WeightRegular: FontWeight.Normal,
    WeightMedium: FontWeight.Semibold,
    WeightBold: FontWeight.Bold
}
```

### Spacing

```powerfx
fxSpacing = {
    XS: 4,
    SM: 8,
    MD: 16,
    LG: 24,
    XL: 32,
    XXL: 48
}
```

## Applying Themes

### Control Properties

Use theme values in control properties:

```powerfx
// Button Fill
Fill: =fxTheme.Primary

// Label Color
Color: =fxTheme.TextPrimary

// Container Fill
Fill: =fxTheme.Surface
```

### Dynamic Theming

Support light/dark modes or multiple themes:

```powerfx
// Toggle between themes
If(
    varDarkMode,
    fxDarkTheme,
    fxLightTheme
)
```

## Best Practices

1. **Centralize definitions** - Define all theme values in one place (App.Formulas)
2. **Use semantic names** - Name colors by purpose (Primary, Error) not appearance (Blue, Red)
3. **Maintain consistency** - Apply theme values uniformly across all controls
4. **Document your theme** - Keep a reference of all theme values and their usage
5. **Consider accessibility** - Ensure sufficient contrast ratios

## Related Resources

- [Visual Assets - Colors](../../visual-assets/colors/README.md)
- [UI Patterns Overview](../README.md)
- [Microsoft Fluent Design](https://www.microsoft.com/design/fluent/)

---

## History

| Date       | Author      | Changes                          |
|------------|-------------|----------------------------------|
| 2026-01-27 | Claude      | Created initial README           |
