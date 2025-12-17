---
title: "Responsive Hero Cards Gallery"
description: "A responsive gallery with hero card layout that automatically adjusts wrap count based on container width"
category: "ui-controls"
subcategory: "gallery"
tags:
  - gallery
  - responsive
  - hero-cards
  - adaptive
  - layout
difficulty: intermediate
products:
  - power-apps-canvas
author: "Scott Durow (modified by PowerAppsDarren)"
created: 2024-01-01
updated: 2024-01-01
---

# Responsive Hero Cards Gallery

This code was originally created by Scott Durow and shared via the PnP Power Platform Snippets repository. It demonstrates a responsive gallery with hero cards that automatically adjust their layout based on the available width.

**Original source:** https://github.com/pnp/powerplatform-snippets/blob/main/power-apps/responsive-hero-cards-gallery/source/responsive-hero-card-gallery.yaml

## Features

- Automatic wrap count calculation based on container width
- Hero card design with image, title, and description
- Responsive height calculation
- Clean card styling with rounded corners
- Clickable overlay for item selection
- FluentV8 label components for modern styling

## Add This to Your Application

```yaml
- cCards:
    Control: GroupContainer
    Variant: verticalAutoLayoutContainer
    Properties:
      Fill: =RGBA(250, 249, 248, 1)
      Height: =Parent.Height
      LayoutDirection: =LayoutDirection.Vertical
      LayoutMode: =LayoutMode.Auto
      PaddingTop: =20
      Width: =Parent.Width
    Children:
    - cCardsHeader:
        Control: GroupContainer
        Variant: manualLayoutContainer
        Properties:
          DropShadow: =DropShadow.None
          FillPortions: =0
          Height: =24
          LayoutMinHeight: =20
          LayoutMinWidth: =0
        Children:
        - lblCardHeader:
            Control: Label
            Properties:
              Text: ="Things you can do with this app"
              FontWeight: =FontWeight.Semibold
              Height: =Parent.Height
              PaddingBottom: =0
              PaddingLeft: =0
              PaddingRight: =0
              PaddingTop: =0
              Width: =Parent.Width-Self.X
              X: =16
    - galHeroCards:
        Control: Gallery
        Variant: BrowseLayout_Vertical_TwoTextOneImageVariant_ver5.0
        Properties:
          Items: |-
            =[
                {Title:"Card Title 1",Description:"Aliquam dictum neque orci, eu convallis ligula tincidunt quis. Quisque.",Image:SampleImage},
                {Title:"Card Title 2",Description:"Nam sollicitudin mattis tellus vel pulvinar. Nulla sed arcu a diam sollicitudin tincidunt. Quisque eleifend.",Image:SampleImage},
                {Title:"Card Title 3",Description:"Donec vel velit venenatis, vestibulum diam quis, lobortis.",Image:SampleImage},
                {Title:"Card Title 4",Description:"Curabitur dictum arcu vitae hendrerit luctus. Integer id sapien ac eros bibendum.",Image:SampleImage}
            ]
          Selectable: =false
          WrapCount: |-
            =IfError(RoundDown(
                Self.Width/
                Max(350,(Self.Width/Self.AllItemsCount))
            ,0),3)
          BorderColor: =RGBA(0, 0, 0, 0)
          DelayItemLoading: =true
          Fill: =RGBA(250, 249, 248, 1)
          FillPortions: =0
          Height: |-
            =RoundUp(
                IfError(Self.AllItemsCount/
                    (RoundDown(Self.Width/Max(350,(Self.Width/Self.AllItemsCount)),0))
                ,1)
            ,0)
            * (Self.TemplateHeight+Self.TemplatePadding)+16
          Layout: =Layout.Vertical
          ShowScrollbar: =false
          TemplatePadding: =16
          TemplateSize: =100
          Width: =Parent.Width
          Y: =4
        Children:
        - cCard:
            Control: GroupContainer
            Variant: manualLayoutContainer
            Properties:
              Fill: =RGBA(255, 255, 255, 1)
              Height: =100
              RadiusBottomLeft: =8
              RadiusBottomRight: =8
              RadiusTopLeft: =8
              RadiusTopRight: =8
              Width: =Parent.TemplateWidth
            Children:
            - cCardContentContainer:
                Control: GroupContainer
                Variant: horizontalAutoLayoutContainer
                Properties:
                  DropShadow: =DropShadow.None
                  Height: =cCardText.Height
                  LayoutAlignItems: =LayoutAlignItems.Center
                  LayoutGap: =12
                  LayoutMode: =LayoutMode.Auto
                  Width: =Parent.Width - Self.X*2
                  X: =20
                  Y: =(Parent.Height - Self.Height)/2
                Children:
                - imgCard:
                    Control: Image
                    Properties:
                      Image: =ThisItem.Image
                      Height: =48
                      Width: =48
                      Y: =34
                - cCardText:
                    Control: GroupContainer
                    Variant: verticalAutoLayoutContainer
                    Properties:
                      AlignInContainer: =AlignInContainer.SetByContainer
                      DropShadow: =DropShadow.None
                      Height: =txtCardTitle.Height + txtCardSubTitle.Height
                      LayoutDirection: =LayoutDirection.Vertical
                      LayoutMinWidth: =10
                      LayoutMode: =LayoutMode.Auto
                      PaddingRight: =16
                    Children:
                    - txtCardTitle:
                        Control: FluentV8/Label
                        Properties:
                          FontSize: =12
                          FontWeight: =FontWeight.Semibold
                          Overflow: ='Label.Overflow'.Hidden
                          Text: =ThisItem.Title
                          TextRole: ='Label.TextRole'.Heading2
                          VerticalAlignment: =VerticalAlign.Top
                          AlignInContainer: =AlignInContainer.Stretch
                          LayoutMinWidth: =200
                    - txtCardSubTitle:
                        Control: FluentV8/Label
                        Properties:
                          AutoHeight: =true
                          Color: =RGBA(97, 97, 97, 1)
                          FontSize: =10
                          Text: =ThisItem.Description
                          VerticalAlignment: =VerticalAlign.Top
                          AlignInContainer: =AlignInContainer.Stretch
                          DisplayMode: =DisplayMode.View
                          Height: =42
                          LayoutMinWidth: =10
                          Width: =353
            - btnCardOverlay:
                Control: Image
                Properties:
                  OnSelect: =Notify(ThisItem.Title)
                  AccessibleLabel: =
                  Image: =
                  Tooltip: =Self.AccessibleLabel
                  BorderColor: =RGBA(250, 249, 248, 1)
                  BorderThickness: =1
                  FocusedBorderColor: =Color.Black
                  FocusedBorderThickness: =1
                  Height: =Parent.Height - 1
                  HoverBorderColor: =RGBA(230, 230, 230, 1)
                  PressedBorderColor: =RGBA(0, 0, 0, 1)
                  RadiusBottomLeft: =8
                  RadiusBottomRight: =8
                  RadiusTopLeft: =8
                  RadiusTopRight: =8
                  TabIndex: =0
                  Width: =Parent.Width-1
    - cMainContent:
        Control: GroupContainer
        Variant: manualLayoutContainer
        Properties:
          DropShadow: =DropShadow.None
        Children:
        - lblPlaceholder:
            Control: Label
            Properties:
              Text: ="Content Placeholder"
              Color: =RGBA(160, 160, 160, 1)
              Fill: =RGBA(140, 140, 140, 0)
              Height: =30
              Width: =300
              X: =20
              Y: =20
```

## Key Formula: Responsive WrapCount

The magic of this gallery is in the WrapCount formula:

```powerfx
IfError(
    RoundDown(
        Self.Width / Max(350, (Self.Width / Self.AllItemsCount))
    , 0),
    3
)
```

This calculates how many cards fit per row based on:
- Minimum card width of 350 pixels
- Available container width
- Number of items in the gallery

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
