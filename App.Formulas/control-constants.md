---
title: "Helpful Constants"
description: "A set of standard constants for spacing, screen defaults, and control properties."
category: "App.Formulas"
tags: ["constants", "design", "layout", "standardization"]
difficulty: beginner
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

## Free Community & Course Materials
🆓 Get access to our free Power Apps crash course (and our community) here: 
- https://tinyurl.com/DarrensStuffFree 🔗

## Support

I hope you have found this helpful. If you need any help with the Power Platform, don't hesitate to email us at 
* [support@superpowerlabs.co](support@superpowerlabs.co).
* https://powerplatformlinks.com 

## Disclaimer

THIS CODE IS PROVIDED AS IS WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING ANY IMPLIED WARRANTIES OF FITNESS FOR A PARTICULAR PURPOSE, MERCHANTABILITY, OR NON-INFRINGEMENT.

