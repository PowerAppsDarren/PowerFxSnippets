---
title: RGB to HSL Conversion
description: Convert RGB color values to HSL (Hue, Saturation, Lightness) in Power Fx
category: colors/functions
tags:
  - color-conversion
  - RGB
  - HSL
credit: https://github.com/matthewdevaney/powerapps-custom-functions
related:
  - ./rgb-2-hsv
  - ./hex-2-rgb
  - ./hsv-2-rgb
---

# RGB to HSL

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
        ),
        CNT: (Max(
            Red,
            Green,
            Blue
        ) + Min(
            Red,
            Green,
            Blue
        )) / 2
    },
    If(
        CNT < 128,
        Switch(
            CMAX,
            Red,
            {
                H: Mod(
                    360 + 60 * ((Green - Blue) / (CMAX - CMIN)),
                    360
                ),
                S: (CMAX - CMIN) / (CMAX + CMIN) * 255,
                L: (CMAX + CMIN) / 2
            },
            Green,
            {
                H: Mod(
                    360 + 60 * ((Blue - Red) / (CMAX - CMIN)) + 120,
                    360
                ),
                S: (CMAX - CMIN) / (CMAX + CMIN) * 255,
                L: (CMAX + CMIN) / 2
            },
            Blue,
            {
                H: Mod(
                    360 + 60 * ((Red - Green) / (CMAX - CMIN)) + 240,
                    360
                ),
                S: (CMAX - CMIN) / (CMAX + CMIN) * 255,
                L: (CMAX + CMIN) / 2
            }
        ),
        Switch(
            CMAX,
            Red,
            {
                H: Mod(
                    360 + 60 * ((Green - Blue) / (CMAX - CMIN)),
                    360
                ),
                S: (CMAX - CMIN) / (510 - CMAX - CMIN) * 255,
                L: (CMAX + CMIN) / 2
            },
            Green,
            {
                H: Mod(
                    360 + 60 * ((Blue - Red) / (CMAX - CMIN)) + 120,
                    360
                ),
                S: (CMAX - CMIN) / (510 - CMAX - CMIN) * 255,
                L: (CMAX + CMIN) / 2
            },
            Blue,
            {
                H: Mod(
                    360 + 60 * ((Red - Green) / (CMAX - CMIN)) + 240,
                    360
                ),
                S: (CMAX - CMIN) / (510 - CMAX - CMIN) * 255,
                L: (CMAX + CMIN) / 2
            }
        )
    )
)
```

## Free Community & Course Materials 

🆓 Get access to our free Power Apps crash course (and our community) here: 
- https://tinyurl.com/DarrensStuffFree 🔗

## Support

I hope you have found this helpful. If you need any help with the Power Platform, don't hesitate to email us at 
* [support@superpowerlabs.co](support@superpowerlabs.co)
* https://superpowerlabs.co 

---

## Disclaimer

**THIS CODE IS PROVIDED AS IS WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING ANY IMPLIED WARRANTIES OF FITNESS FOR A PARTICULAR PURPOSE, MERCHANTABILITY, OR NON-INFRINGEMENT.**

---

## History

| Date | Author | Changes |
|------|--------|---------|
| 2025-12-17 | Claude | Added YAML frontmatter |
