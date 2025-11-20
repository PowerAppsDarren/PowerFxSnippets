

---
title: "Change Pointer to Hand"
description: "An icon control configured to show a hand cursor on hover."
category: "Controls"
tags: ["icon", "cursor", "ui", "ux"]
difficulty: beginner
author: "Darren Neese"
created: 2025-11-19
updated: 2025-11-19
license: "MIT"
---

# Change Pointer to Hand

```PowerFx
- icoChangePointerToHand:
    Control: Classic/Icon
    Variant: 3DPrinting
    Properties:
      OnSelect: =Select(Parent)
      Color: =Color.Transparent
      Height: =Parent.TemplateHeight
      Icon: =Icon.Printing3D
      Width: =Parent.TemplateWidth
```