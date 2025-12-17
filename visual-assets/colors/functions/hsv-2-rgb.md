---
title: HSV to RGB Conversion
description: Convert HSV (Hue, Saturation, Value) color values to RGB in Power Fx
category: colors/functions
tags:
  - color-conversion
  - HSV
  - RGB
  - RGBA
credit: https://github.com/matthewdevaney/powerapps-custom-functions
related:
  - ./rgb-2-hsv
  - ./hex-2-rgb
  - ./rgb-2-hsl
---

# HSV to RGB

Credit: https://github.com/matthewdevaney/powerapps-custom-functions/tree/main/custom_functions_hiro

## Add This to Your Application

```PowerFx
With(
    {
        SVMax: value,
        SVMin: value - (Saturation / 255*value),
        Hvalue: Mod(
            360 + Hue,
            360
        )
    },
    With(
        Switch(
            RoundDown(
                Hvalue / 60,
                0
            ),
            0,
            {
                R: SVMax,
                G: (Hvalue / 60 * (SVMax - SVMin) + SVMin),
                B: SVMin
            },
            1,
            {
                R: ((120 - Hvalue) / 60 * (SVMax - SVMin) + SVMin),
                G: SVMax,
                B: SVMin
            },
            2,
            {
                R: SVMin,
                G: SVMax,
                B: ((120 - Hvalue) / 60 * (SVMax - SVMin) + SVMin)
            },
            3,
            {
                R: SVMin,
                G: ((240 - Hvalue) / 60 * (SVMax - SVMin) + SVMin),
                B: SVMax
            },
            4,
            {
                R: ((Hvalue - 240) / 60 * (SVMax - SVMin) + SVMin),
                G: SVMin,
                B: SVMax
            },
            {
                R: SVMax,
                G: SVMin,
                B: ((360 - Hvalue) / 60 * (SVMax - SVMin) + SVMin)
            }
        ),
        {
            R: R,
            G: G,
            B: B,
            Color: RGBA(
                R,
                G,
                B,
                1
            )
        }
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
