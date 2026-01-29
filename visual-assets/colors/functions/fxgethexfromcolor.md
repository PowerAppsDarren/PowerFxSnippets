---
title: fxGetHexFromColor
description: User-defined function to convert a Power Apps Color value to a hex string
category: colors/functions
tags:
  - color-conversion
  - hex
  - user-defined-function
  - JSON
related:
  - ./hex-2-rgb
  - ../palettes/color-collection
---

# fxGetHexFromColor() User-Defined Function

## Table of Contents

Paste this code into your App.Formulas and call it to convert a ColorValue to a hex string.

```PowerFx
    fxGetHexFromColor(ColorValue:Color, IncludeAlpha:Boolean):Text = (
        With( 
            {
                MyVal: Substitute(
                            JSON(ColorValue), 
                            """", 
                            ""
                        )
            },
            Left(MyVal, Len(MyVal) - 2)
        )
    );
    fxGetHexFromColor(ColorValue:Color):Text = Left(
        Substitute(
            JSON(ColorValue, JSONFormat.Compact), 
            """",
            ""
        ), 
        7
    );
```
---

## History

| Date | Author | Changes |
|------|--------|---------|
| 2026-01-27 | Migration | Initial TOC and history section added |
