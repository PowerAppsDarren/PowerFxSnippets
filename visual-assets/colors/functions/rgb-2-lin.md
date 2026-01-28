---
title: RGB to Linear Conversion
description: Convert sRGB color values to linearized values for accurate color calculations
category: colors/functions
tags:
  - color-conversion
  - RGB
  - linear
  - sRGB
credit: https://github.com/P3N-101/color-functions
related:
  - ./luminance
  - ./color-functions
---

# RGB to Linear (sRGBtoLIN)

## Table of Contents

Credit: https://github.com/P3N-101/color-functions

```PowerFx
RGBA(
      (R * 61.8 / 100.0 + G * 32 / 100.0 + B * 6.2 / 100.0),
      (R * 16.3 / 100.0 + G * 77.5 / 100.0 + B * 6.2 / 100.0),
      (R * 16.3 / 100.0 + G * 32.0 / 100.0 + B * 51.6 / 100.0),1
  )
/*
    Achromatomaly:
        R:[61.8, 32,    6.2]
        G:[16.3, 77.5,  6.2]
        B:[16.3, 32.0, 51.6]
*/
```

---

## History

| Date | Author | Changes |
|------|--------|---------|
| 2025-12-17 | Claude | Added YAML frontmatter |
