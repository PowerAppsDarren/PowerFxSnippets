---
title: RGB to HSV Conversion
description: Convert RGB color values to HSV (Hue, Saturation, Value) in Power Fx
category: colors/functions
tags:
  - color-conversion
  - RGB
  - HSV
credit: https://github.com/matthewdevaney/powerapps-custom-functions
related:
  - ./hsv-2-rgb
  - ./rgb-2-hsl
  - ./hex-2-rgb
---

# RGB to HSV

Credit: https://github.com/matthewdevaney/powerapps-custom-functions/tree/main/custom_functions_hiro

## Add This to Your Application

```PowerFx
With(
    {
        CMAX: Max(
            Red,
            Green,
            Blue
        ),
        CMIN: Min(
            Red,
            Green,
            Blue
        )
    },
    Switch(
        CMAX,
        Red,
        {
            H: Mod(
                360 + 60 * ((Green - Blue) / (CMAX - CMIN)),
                360
            ),
            S: (CMAX - CMIN) / CMAX * 255,
            V: CMAX
        },
        Green,
        {
            H: Mod(
                360 + 60 * ((Blue - Red) / (CMAX - CMIN)) + 120,
                360
            ),
            S: (CMAX - CMIN) / CMAX * 255,
            V: CMAX
        },
        Blue,
        {
            H: Mod(
                360 + 60 * ((Red - Green) / (CMAX - CMIN)) + 240,
                360
            ),
            S: (CMAX - CMIN) / CMAX * 255,
            V: CMAX
        }
    )
)
```


---

## History

| Date | Author | Changes |
|------|--------|---------|
| 2025-12-17 | Claude | Added YAML frontmatter |
