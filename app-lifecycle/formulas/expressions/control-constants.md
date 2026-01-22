---
title: "Helpful Constants"
description: "A set of standard constants for spacing, screen defaults, and control properties."
category: "app-architecture"
subcategory: "formulas"
tags:
  - constants
  - design
  - layout
  - standardization
  - expression
difficulty: beginner
products:
  - power-apps-canvas
author: "Darren Neese"
created: 2025-11-19
updated: 2025-11-19
license: "MIT"
---

# Helpful Constants

This is a helpful canvas Power Apps code snippet.

## Add This to Your Application

```PowerFx
    fxConstants = {
        //
        // Spacing values when you need a consistent way of
        // spacing things out.
        //
        Spacing: {
            SpacingSm: 10,
            SpacingMd: 20,
            SpacingLg: 40,
            SpacingXL: 50
        },
        //
        // Screen Defaults
        //
        Screen: {
            Fill: Color.White,
            ShowFullNavAt: 3
        },
        //
        // These will be applied to controls in general
        //
        ControlsInGeneral: {
            BorderRadius: 4,
            Height: 32
        },
        //
        // These will be container defaults
        //
        Container: {
            GapSm: 8,
            GapMd: 16,
            GapLg: 24,
            GapXL: 32,
            GapForLayout: 12,
            PaddingForLayout: 2,
            PaddingSm: 2,
            PaddingMd: 8,
            PaddingLg: 8,
            PaddingXL: 8,
            DropShadowDefault: DropShadow.Regular,
            DropShadowForLayout: DropShadow.Light,
            BorderRadiusNone: 0,
            BorderRadiusSm: 4,
            BorderRadiusMd: 8,
            BorderRadiusLg: 12
        },
        //
        // These will be applied to labels in general
        //
        Label: {
            BorderRadius: 4,
            Height: 30
        }
    };
```
