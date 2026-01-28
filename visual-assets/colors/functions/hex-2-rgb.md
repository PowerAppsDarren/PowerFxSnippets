---
title: HEX to RGB Conversion
description: Convert hexadecimal color codes to RGB values in Power Fx
category: colors/functions
tags:
  - color-conversion
  - hex
  - RGB
  - RGBA
credit: https://github.com/matthewdevaney/powerapps-custom-functions
related:
  - ./fxgethexfromcolor
  - ./rgb-2-hsl
  - ./rgb-2-hsv
---

# HEX to RGB

## Table of Contents

- [Add This to Your Application](#add-this-to-your-application)

Credit: https://github.com/matthewdevaney/powerapps-custom-functions/tree/main/custom_functions_hiro

## Add This to Your Application

```PowerFx
With(
    {
        tblColdec: AddColumns(
            ForAll(Split(
                Lower(
                    Right(
                        HEX,
                        6
                    )
                ),
                ""
            ), {Result: ThisRecord.Value}),
            decimal,
            If(
                ThisRecord.Result in Sequence(
                    10,
                    0
                ),
                ThisRecord.Result,
                LookUp(
                    Table(
                        {
                            key: "a",
                            val: 10
                        },
                        {
                            key: "b",
                            val: 11
                        },
                        {
                            key: "c",
                            val: 12
                        },
                        {
                            key: "d",
                            val: 13
                        },
                        {
                            key: "e",
                            val: 14
                        },
                        {
                            key: "f",
                            val: 15
                        }
                    ),
                    key = Result
                ).val
            )
        )
    },
    With(
        {
            R: 16 * First(tblColdec).decimal + Last(
                FirstN(
                    tblColdec,
                    2
                )
            ).decimal,
            G: 16 * Last(
                FirstN(
                    tblColdec,
                    3
                )
            ).decimal + Last(
                FirstN(
                    tblColdec,
                    4
                )
            ).decimal,
            B: 16 * Last(
                FirstN(
                    tblColdec,
                    5
                )
            ).decimal + Last(
                FirstN(
                    tblColdec,
                    6
                )
            ).decimal
        },
        {
            Color: RGBA(
                R,
                G,
                B,
                1
            ),
            R: R,
            G: G,
            B: B
        }
    )
)
```
---

## History

| Date | Author | Changes |
|------|--------|---------|
| 2026-01-27 | Migration | Initial TOC and history section added |
