---
title: "Image Grid Gallery"
description: "A responsive image gallery/grid with wrap count, category badges, and selection overlays"
category: "ui-controls"
subcategory: "gallery"
tags:
  - gallery
  - images
  - grid
  - responsive
  - photos
  - layout
difficulty: intermediate
products:
  - power-apps-canvas
author: "PowerAppsDarren"
created: 2024-01-01
updated: 2024-01-01
---

# Image Grid Gallery

A responsive image gallery/grid style component with automatic wrap count calculation, category badges, and selection overlays.

## Features

- Vertical responsive container layout
- Bold drop shadow on main content container
- Heading "Photo Gallery" outside the gallery
- Summary row with image count and view toggle icons
- Responsive grid layout using WrapCount
- Square/4:3 aspect ratio image tiles
- Overlay on selection with semi-transparent background
- Title text at bottom of each image
- Category badge visible on selection
- Checkmark icon for selected items
- Rounded corners
- Auto-calculates height based on wrap count

## Sample Data Structure

```powerfx
Items: =[
    {Title: "Mountain Vista", Category: "Nature", Image: SampleImage},
    {Title: "City Lights", Category: "Urban", Image: SampleImage}
]
```

## Add This to Your Application

```yaml
- cImageGridWrapper:
    Control: GroupContainer
    Variant: verticalAutoLayoutContainer
    Properties:
      Fill: =RGBA(248, 249, 250, 1)
      Height: =Parent.Height
      Width: =Parent.Width
      LayoutDirection: =LayoutDirection.Vertical
      LayoutMode: =LayoutMode.Auto
      LayoutGap: =16
      PaddingTop: =24
      PaddingBottom: =24
      PaddingLeft: =24
      PaddingRight: =24
    Children:

    # Heading - Outside the gallery
    - lblPhotoGalleryHeading:
        Control: Label
        Properties:
          Text: ="Photo Gallery"
          FontWeight: =FontWeight.Bold
          Size: =24
          Color: =RGBA(32, 33, 36, 1)
          Height: =40
          Width: =Parent.Width - 48
          PaddingLeft: =0
          Align: =Align.Left

    # Summary Row - Outside the gallery
    - cSummaryRow:
        Control: GroupContainer
        Variant: horizontalAutoLayoutContainer
        Properties:
          Height: =48
          Width: =Parent.Width - 48
          Fill: =RGBA(0, 0, 0, 0)
          LayoutMode: =LayoutMode.Auto
          LayoutGap: =16
          LayoutAlignItems: =LayoutAlignItems.Center
        Children:
        # Photo Count
        - lblPhotoCount:
            Control: Label
            Properties:
              Text: =CountRows(galImageGrid.AllItems) & " photos"
              Size: =14
              Color: =RGBA(96, 98, 102, 1)
              Height: =36
              Width: =100
              VerticalAlign: =VerticalAlign.Middle

        # Spacer
        - rectSpacer:
            Control: Rectangle
            Properties:
              Fill: =RGBA(0, 0, 0, 0)
              Height: =1
              Width: =Parent.Width - 280

        # View Toggle Icons
        - cViewToggle:
            Control: GroupContainer
            Variant: horizontalAutoLayoutContainer
            Properties:
              Height: =40
              Width: =80
              Fill: =RGBA(0, 0, 0, 0)
              LayoutMode: =LayoutMode.Auto
              LayoutGap: =8
              LayoutAlignItems: =LayoutAlignItems.Center
            Children:
            - icoGridView:
                Control: Classic/Icon
                Properties:
                  Icon: =Icon.Waffle
                  Color: =RGBA(0, 120, 212, 1)
                  Height: =28
                  Width: =28
            - icoListView:
                Control: Classic/Icon
                Properties:
                  Icon: =Icon.DetailList
                  Color: =RGBA(150, 152, 156, 1)
                  Height: =28
                  Width: =28

    # Main Content Container with Bold Drop Shadow
    - cImageGridContent:
        Control: GroupContainer
        Variant: verticalAutoLayoutContainer
        Properties:
          DropShadow: =DropShadow.Bold
          Fill: =RGBA(255, 255, 255, 1)
          Height: =Parent.Height - 160
          Width: =Parent.Width - 48
          RadiusTopLeft: =12
          RadiusTopRight: =12
          RadiusBottomLeft: =12
          RadiusBottomRight: =12
          LayoutMode: =LayoutMode.Auto
          PaddingTop: =16
          PaddingBottom: =16
          PaddingLeft: =16
          PaddingRight: =16
        Children:

        # Gallery with WrapCount for Grid Layout
        - galImageGrid:
            Control: Gallery
            Variant: galleryVertical
            Properties:
              Items: |
                =[
                    {Title: "Mountain Vista", Category: "Nature", Image: SampleImage},
                    {Title: "City Lights", Category: "Urban", Image: SampleImage},
                    {Title: "Ocean Sunset", Category: "Nature", Image: SampleImage},
                    {Title: "Forest Trail", Category: "Nature", Image: SampleImage},
                    {Title: "Desert Dunes", Category: "Nature", Image: SampleImage},
                    {Title: "Urban Architecture", Category: "Urban", Image: SampleImage},
                    {Title: "Coastal Waves", Category: "Nature", Image: SampleImage},
                    {Title: "Street Art", Category: "Urban", Image: SampleImage}
                ]
              Height: =Parent.Height - 32
              Width: =Parent.Width - 32
              Layout: =Layout.Vertical
              TemplatePadding: =8
              TemplateSize: =200
              WrapCount: =Max(1, RoundDown((Parent.Width - 64) / 200, 0))
              TemplateFill: =RGBA(0, 0, 0, 0)
              ShowScrollbar: =true
            Children:

            # Image Card Container
            - cImageCard:
                Control: GroupContainer
                Variant: manualLayoutContainer
                Properties:
                  Height: =192
                  Width: =192
                  Fill: =RGBA(0, 0, 0, 0)
                  RadiusTopLeft: =8
                  RadiusTopRight: =8
                  RadiusBottomLeft: =8
                  RadiusBottomRight: =8
                Children:

                # Main Image
                - imgPhoto:
                    Control: Image
                    Properties:
                      Image: =ThisItem.Image
                      ImagePosition: =ImagePosition.Fill
                      Height: =150
                      Width: =192
                      X: =0
                      Y: =0
                      RadiusTopLeft: =8
                      RadiusTopRight: =8
                      RadiusBottomLeft: =0
                      RadiusBottomRight: =0

                # Hover/Selection Overlay
                - rectOverlay:
                    Control: Rectangle
                    Properties:
                      Fill: =If(ThisItem.IsSelected, RGBA(0, 0, 0, 0.35), RGBA(0, 0, 0, 0))
                      Height: =150
                      Width: =192
                      X: =0
                      Y: =0
                      RadiusTopLeft: =8
                      RadiusTopRight: =8
                      RadiusBottomLeft: =0
                      RadiusBottomRight: =0

                # Category Badge (visible on selection)
                - lblCategoryBadge:
                    Control: Label
                    Properties:
                      Text: =ThisItem.Category
                      Size: =10
                      FontWeight: =FontWeight.Semibold
                      Color: =RGBA(255, 255, 255, 1)
                      Fill: =RGBA(0, 0, 0, 0.6)
                      Height: =22
                      Width: =70
                      X: =8
                      Y: =8
                      Align: =Align.Center
                      VerticalAlign: =VerticalAlign.Middle
                      RadiusTopLeft: =4
                      RadiusTopRight: =4
                      RadiusBottomLeft: =4
                      RadiusBottomRight: =4
                      Visible: =ThisItem.IsSelected

                # Selection Checkmark (visible on selection)
                - icoSelected:
                    Control: Classic/Icon
                    Properties:
                      Icon: =Icon.CheckBadge
                      Color: =RGBA(255, 255, 255, 1)
                      Height: =28
                      Width: =28
                      X: =156
                      Y: =8
                      Visible: =ThisItem.IsSelected

                # Title Background
                - rectTitleBg:
                    Control: Rectangle
                    Properties:
                      Fill: =If(ThisItem.IsSelected, RGBA(0, 120, 212, 1), RGBA(255, 255, 255, 1))
                      Height: =42
                      Width: =192
                      X: =0
                      Y: =150
                      RadiusTopLeft: =0
                      RadiusTopRight: =0
                      RadiusBottomLeft: =8
                      RadiusBottomRight: =8

                # Title Text
                - lblImageTitle:
                    Control: Label
                    Properties:
                      Text: =ThisItem.Title
                      Size: =13
                      FontWeight: =FontWeight.Semibold
                      Color: =If(ThisItem.IsSelected, RGBA(255, 255, 255, 1), RGBA(32, 33, 36, 1))
                      Height: =42
                      Width: =180
                      X: =6
                      Y: =150
                      VerticalAlign: =VerticalAlign.Middle
                      PaddingLeft: =6
```

## Key Formula: Responsive WrapCount

```powerfx
WrapCount: =Max(1, RoundDown((Parent.Width - 64) / 200, 0))
```

This formula calculates how many columns fit based on:
- Parent container width minus padding (64px)
- Each tile is 200px wide
- Minimum of 1 column


---

## History

| Date | Author | Changes |
|------|--------|---------|
| 2025-12-17 | Claude | Converted from YAML to markdown, added to layouts/ |
