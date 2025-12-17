---
title: "Gallery with Column Headings"
description: "A gallery layout with column headers for displaying tabular data with selection highlighting"
category: "ui-controls"
subcategory: "gallery"
tags:
  - gallery
  - headers
  - columns
  - tabular
  - layout
difficulty: beginner
products:
  - power-apps-canvas
author: "PowerAppsDarren"
created: 2024-01-01
updated: 2024-01-01
---

# Gallery with Column Headings

A gallery layout featuring column headers for displaying structured data. Includes a styled header row with customizable column labels and a selection highlight on row interaction.

## Features

- Column header row with primary theme color
- Three configurable column labels
- Selection highlighting (light yellow)
- Responsive width/height based on parent container
- Template padding for clean spacing

## Add This to Your Application

```yaml
- cntGalleryGrouping:
    Control: GroupContainer
    Variant: manualLayoutContainer
    Properties:
      BorderColor: =App.Theme.Colors.Primary
      BorderThickness: =2
      Height: =Parent.Height - Self.Y * 2
      Width: =Parent.Width - Self.X * 2
      X: =20
      Y: =20
    Children:
    - galListing:
        Control: Gallery
        Variant: galleryVertical
        Properties:
          BorderColor: =App.Theme.Colors.Primary
          BorderThickness: =2
          DelayItemLoading: =true
          Fill: =ColorValue("#f5f5f5")
          Height: =Parent.Height - Self.Y
          Layout: =Layout.Vertical
          LoadingSpinner: =LoadingSpinner.Data
          TemplateFill: =If(ThisItem.IsSelected, Color.LightYellow, Color.White)
          TemplatePadding: =2
          TemplateSize: =50
          Width: =Parent.Width - Self.X
          Y: =cntGalleryHeader.Height + cntGalleryHeader.Y
        Children:
        - lblField03:
            Control: Label
            Properties:
              OnSelect: =Select(Parent)
              Text: =ThisItem.SampleHeading
              Height: =Parent.TemplateHeight
              PaddingLeft: =10
              Width: =lblHeading03.Width
              X: =lblHeading03.X
        - lblField02:
            Control: Label
            Properties:
              OnSelect: =Select(Parent)
              Text: =ThisItem.SampleText
              Height: =Parent.TemplateHeight
              PaddingLeft: =10
              Width: =lblHeading02.Width
              X: =lblHeading02.X
        - lblField01:
            Control: Label
            Properties:
              OnSelect: =Select(Parent)
              Text: =ThisItem.SampleHeading
              Height: =Parent.TemplateHeight
              PaddingLeft: =10
              Width: =lblHeading01.Width
              X: =lblHeading01.X
    - cntGalleryHeader:
        Control: GroupContainer
        Variant: manualLayoutContainer
        Properties:
          Fill: =App.Theme.Colors.Primary
          Height: =50
          RadiusBottomLeft: =0
          RadiusBottomRight: =0
          RadiusTopLeft: =0
          RadiusTopRight: =0
          Width: =Parent.Width
        Children:
        - lblHeading01:
            Control: Label
            Properties:
              Text: ="HEADING 01"
              Color: =RGBA(255, 255, 255, 1)
              FontWeight: =FontWeight.Semibold
              Height: =Parent.Height
              PaddingLeft: =10
              Size: =15
        - lblHeading02:
            Control: Label
            Properties:
              Text: ="HEADING 02"
              Color: =RGBA(255, 255, 255, 1)
              FontWeight: =FontWeight.Semibold
              Height: =Parent.Height
              PaddingLeft: =10
              Size: =15
              Width: =600
              X: =lblHeading01.X + lblHeading01.Width
        - lblHeading03:
            Control: Label
            Properties:
              Text: ="HEADING 03"
              Color: =RGBA(255, 255, 255, 1)
              FontWeight: =FontWeight.Semibold
              Height: =Parent.Height
              PaddingLeft: =10
              Size: =15
              Width: =300
              X: =lblHeading02.X + lblHeading02.Width
```

## Free Community & Course Materials

Get access to our free Power Apps crash course (and our community) here:
- https://tinyurl.com/DarrensStuffFree

## Support

If you need any help with the Power Platform, don't hesitate to email us at:
- support@superpowerlabs.co
- https://powerplatformlinks.com

## Disclaimer

THIS CODE IS PROVIDED AS IS WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING ANY IMPLIED WARRANTIES OF FITNESS FOR A PARTICULAR PURPOSE, MERCHANTABILITY, OR NON-INFRINGEMENT.

---

## History

| Date | Author | Changes |
|------|--------|---------|
| 2025-12-17 | Claude | Converted from YAML to markdown, added to layouts/ |
