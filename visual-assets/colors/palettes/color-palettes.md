---
title: Color Palettes
description: Simple color palette configuration for Power Apps with primary, accent, and utility colors
category: colors/palettes
tags:
  - palette
  - ColorValue
  - ColorFade
  - named-formula
related:
  - ./color-palette-pa
  - ../utilities/color-resources
---

# Color Palettes

This is some YAML you can paste into your canvas Power Apps application.

## Add This to Your Application

```PowerFx
fxColorPalette = {
    Primary:            ColorValue("#742774"), 
    Dark:               ColorValue("#BB35A4"),
    Light:              ColorValue("#D467B9"),
    Lighter:            ColorValue("#E48CC7"),
    Lightest:           ColorValue("#E9A1CB"),
    Faint:              ColorFade(ColorValue("#E9A1CB"), 80%),
    LightGray:          ColorValue("#f5f5f5"),
    Background:         RGBA(255, 255, 255, 1),
    Text:               RGBA(0, 0, 0, 1)
}
```

## Links

- https://primer.style/prism/ ‼️

---

## History

| Date | Author | Changes |
|------|--------|---------|
| 2025-12-17 | Claude | Added YAML frontmatter |
