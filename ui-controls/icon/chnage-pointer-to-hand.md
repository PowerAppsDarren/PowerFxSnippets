---
title: "Change Pointer to Hand"
description: "An icon control configured to show a hand cursor on hover."
category: "ui-controls"
subcategory: "icon"
tags: ["icon", "cursor", "ui", "ux"]
difficulty: beginner
products:
  - power-apps-canvas
dependencies: []
author: "Darren Neese"
created: 2025-11-19
updated: 2025-11-19
license: "MIT"
related: []
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