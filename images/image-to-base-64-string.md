# Image to Base 64 String

## Table of Contents

- [Add This to Your Application](#add-this-to-your-application)

This is some YAML you can paste into your canvas Power Apps applciation that will 

## Add This to Your Application

```PowerFx
Substitute(
    JSON(
        imgUpdatedImage.Image,
        JSONFormat.IncludeBinaryData
    ),
    """",
    ""
)
```
---

## History

| Date | Author | Changes |
|------|--------|---------|
| 2026-01-27 | Migration | Initial TOC and history section added |
