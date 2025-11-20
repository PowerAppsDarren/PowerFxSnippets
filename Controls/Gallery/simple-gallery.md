---
title: "Simple Gallery"
description: "A basic vertical gallery implementation."
category: "Controls"
tags: ["gallery", "basic", "ui", "list"]
difficulty: beginner
author: "Darren Neese"
created: 2025-11-19
updated: 2025-11-19
license: "MIT"
---

# Simple Gallery

```PowerFx
- galFieldTypes:
    Control: Gallery
    Variant: galleryVertical
    Properties:
      BorderColor: =Self.Fill
      BorderThickness: =2
      DelayItemLoading: =true
      Fill: =RGBA(170, 170, 170, 1)
      Height: =400
      Layout: =Layout.Vertical
      LoadingSpinner: =LoadingSpinner.Data
      TemplateFill: =If(ThisItem.IsSelected, Color.LightYellow, Color.White)
      TemplatePadding: =3
      TemplateSize: =40
      Width: =300
      X: =21
      Y: =27
    Children:
    - lblGalleryItemLabel:
        Control: Text
        Properties:
          PaddingLeft: =10
          Text: =ThisItem.SampleHeading
          Height: =Parent.TemplateHeight
          Width: =Parent.TemplateWidth
```
