---
title: "Random Screen Transition"
description: "A function to return a random screen transition effect."
category: "app-architecture"
subcategory: "formulas"
tags:
  - navigation
  - transition
  - random
  - ui
  - udf
difficulty: beginner
products:
  - power-apps-canvas
author: "Darren Neese"
created: 2025-11-19
updated: 2025-11-19
license: "MIT"
---

# Random Screen Transition

This function will return one of the 5 screen transitions randomly.
It is a user defined function (UDF) and not a named formula
so that it will return a fresh value.

## Add This to Your Application

```JavaScript
    //
    // This function will return one of the 5 screen transitions randomly.
    // It is a user defined function (UDF) and not a named formula
    // so that it will return a fresh value.
    //
    fxRandomScreenTransition():Text =
        With(
            {
                RandomNumber: RandBetween(1, 5)
            },
            Switch(
                RandomNumber,
                1, ScreenTransition.Cover,
                2, ScreenTransition.CoverRight,
                3, ScreenTransition.Fade,
                4, ScreenTransition.UnCover,
                5, ScreenTransition.UnCoverRight,
                ScreenTransition.None
            )
        );
```
