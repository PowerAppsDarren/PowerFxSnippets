---
title: "Simple Gallery"
description: "A basic vertical gallery implementation with selection highlighting"
category: "ui-controls"
subcategory: "gallery"
tags:
  - gallery
  - basic
  - vertical
  - beginner
  - layout
difficulty: beginner
products:
  - power-apps-canvas
dependencies: []
related: []
author: "PowerAppsDarren"
created: 2024-01-01
updated: 2024-01-01
---

# Simple Gallery

## Table of Contents

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

---

## History

| Date       | Author | Changes                                                 |
|------------|----|-------------------------------------------------------------|
| 2025-12-17 | Claude | Converted from YAML to markdown, added to layouts/      |
