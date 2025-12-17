---
title: "Modern Card-Style Gallery"
description: "A modern card gallery with responsive layout, bold shadows, status indicators, and summary row"
category: "ui-controls"
subcategory: "gallery"
tags:
  - gallery
  - cards
  - modern
  - status
  - icons
  - layout
difficulty: intermediate
products:
  - power-apps-canvas
author: "PowerAppsDarren"
created: 2024-01-01
updated: 2024-01-01
---

# Modern Card-Style Gallery

A gallery with modern card design featuring bold drop shadows, status-colored icons, and a summary row showing record counts.

## Features

- Vertical responsive container wrapper
- Bold drop shadow on card containers
- Static heading label above gallery
- Summary row showing record count and active status count
- Modern card design with:
  - Rounded corners (8px radius)
  - Icon on left side with status-based colors
  - Title and subtitle stacked vertically
  - Status indicator icon
  - Hover and selection states with color transitions

## Structure

```
cModernCardsWrapper (verticalAutoLayoutContainer)
  |- lblGalleryHeading (static header)
  |- cGallerySummary (summary row with record count)
  +- galModernCards (gallery with card items)
       +- cCard (each card container)
            |- cCardContent (content layout)
            |   |- imgCardIcon (icon/image)
            |   +- cCardTextStack (text container)
            |       |- lblCardTitle (title)
            |       +- lblCardSubtitle (subtitle)
            +- btnCardOverlay (invisible clickable overlay)
```

## Sample Data Structure

```powerfx
Items: =[
    {Title: "Project Alpha", Subtitle: "Marketing Campaign", Icon: Icon.Globe, Status: "Active"},
    {Title: "Project Beta", Subtitle: "Sales Initiative", Icon: Icon.People, Status: "Pending"},
    {Title: "Project Gamma", Subtitle: "Engineering Sprint", Icon: Icon.Settings, Status: "Complete"}
]
```

## Add This to Your Application

```yaml
- cModernCardsWrapper:
    Control: GroupContainer
    Variant: verticalAutoLayoutContainer
    Properties:
      Fill: =RGBA(248, 249, 250, 1)
      Height: =Parent.Height
      LayoutDirection: =LayoutDirection.Vertical
      LayoutMode: =LayoutMode.Auto
      PaddingBottom: =20
      PaddingLeft: =24
      PaddingRight: =24
      PaddingTop: =20
      Width: =Parent.Width
    Children:
    - lblGalleryHeading:
        Control: Label
        Properties:
          Text: ="Modern Cards Gallery"
          Color: =RGBA(32, 33, 36, 1)
          FontWeight: =FontWeight.Bold
          Height: =32
          PaddingBottom: =0
          PaddingLeft: =0
          PaddingRight: =0
          PaddingTop: =0
          Size: =20
          Width: =Parent.Width - Parent.PaddingLeft - Parent.PaddingRight
    - cGallerySummary:
        Control: GroupContainer
        Variant: horizontalAutoLayoutContainer
        Properties:
          DropShadow: =DropShadow.None
          Fill: =RGBA(0, 0, 0, 0)
          FillPortions: =0
          Height: =24
          LayoutAlignItems: =LayoutAlignItems.Center
          LayoutGap: =12
          LayoutMode: =LayoutMode.Auto
          PaddingBottom: =8
          PaddingTop: =8
          Width: =Parent.Width - Parent.PaddingLeft - Parent.PaddingRight
        Children:
        - lblRecordCount:
            Control: Label
            Properties:
              Text: =CountRows(galModernCards.AllItems) & " items"
              Color: =RGBA(95, 99, 104, 1)
              FontWeight: =FontWeight.Semibold
              Height: =Self.Size * 1.5
              Size: =13
              Width: =100
        - lblSummaryDivider:
            Control: Label
            Properties:
              Text: ="|"
              Color: =RGBA(218, 220, 224, 1)
              Height: =Self.Size * 1.5
              Size: =13
              Width: =20
        - lblActiveCount:
            Control: Label
            Properties:
              Text: =CountIf(galModernCards.AllItems, Status = "Active") & " active"
              Color: =RGBA(95, 99, 104, 1)
              Height: =Self.Size * 1.5
              Size: =13
              Width: =100
    - galModernCards:
        Control: Gallery
        Variant: galleryVertical
        Properties:
          Items: |-
            =[
                {Title: "Project Alpha", Subtitle: "Marketing Campaign", Icon: Icon.Globe, Status: "Active"},
                {Title: "Project Beta", Subtitle: "Sales Initiative", Icon: Icon.People, Status: "Pending"},
                {Title: "Project Gamma", Subtitle: "Engineering Sprint", Icon: Icon.Settings, Status: "Complete"},
                {Title: "Project Delta", Subtitle: "Customer Success", Icon: Icon.Heart, Status: "Active"},
                {Title: "Project Epsilon", Subtitle: "Research & Development", Icon: Icon.Lightbulb, Status: "Active"}
            ]
          DelayItemLoading: =true
          Fill: =RGBA(0, 0, 0, 0)
          FillPortions: =1
          Height: =500
          Layout: =Layout.Vertical
          LoadingSpinner: =LoadingSpinner.Data
          ShowScrollbar: =true
          TemplatePadding: =12
          TemplateSize: =100
          Width: =Parent.Width - Parent.PaddingLeft - Parent.PaddingRight
        Children:
        - cCard:
            Control: GroupContainer
            Variant: manualLayoutContainer
            Properties:
              DropShadow: =DropShadow.Bold
              Fill: =If(ThisItem.IsSelected, RGBA(232, 240, 254, 1), RGBA(255, 255, 255, 1))
              Height: =Parent.TemplateHeight
              RadiusBottomLeft: =8
              RadiusBottomRight: =8
              RadiusTopLeft: =8
              RadiusTopRight: =8
              Width: =Parent.TemplateWidth
            Children:
            - cCardContent:
                Control: GroupContainer
                Variant: horizontalAutoLayoutContainer
                Properties:
                  DropShadow: =DropShadow.None
                  Fill: =RGBA(0, 0, 0, 0)
                  Height: =cCardTextStack.Height
                  LayoutAlignItems: =LayoutAlignItems.Center
                  LayoutGap: =16
                  LayoutMode: =LayoutMode.Auto
                  Width: =Parent.Width - (Self.X * 2)
                  X: =16
                  Y: =(Parent.Height - Self.Height) / 2
                Children:
                - imgCardIcon:
                    Control: Icon
                    Properties:
                      Icon: =ThisItem.Icon
                      Color: =If(ThisItem.Status = "Active", RGBA(26, 115, 232, 1), If(ThisItem.Status = "Pending", RGBA(242, 139, 13, 1), RGBA(95, 99, 104, 1)))
                      Height: =48
                      Width: =48
                - cCardTextStack:
                    Control: GroupContainer
                    Variant: verticalAutoLayoutContainer
                    Properties:
                      AlignInContainer: =AlignInContainer.SetByContainer
                      DropShadow: =DropShadow.None
                      Fill: =RGBA(0, 0, 0, 0)
                      Height: =lblCardTitle.Height + lblCardSubtitle.Height
                      LayoutDirection: =LayoutDirection.Vertical
                      LayoutGap: =4
                      LayoutMinWidth: =200
                      LayoutMode: =LayoutMode.Auto
                    Children:
                    - lblCardTitle:
                        Control: Label
                        Properties:
                          Text: =ThisItem.Title
                          AlignInContainer: =AlignInContainer.Stretch
                          Color: =RGBA(32, 33, 36, 1)
                          FontWeight: =FontWeight.Semibold
                          Height: =Self.Size * 1.5
                          PaddingBottom: =0
                          PaddingLeft: =0
                          PaddingRight: =0
                          PaddingTop: =0
                          Size: =14
                          VerticalAlign: =VerticalAlign.Top
                    - lblCardSubtitle:
                        Control: Label
                        Properties:
                          Text: =ThisItem.Subtitle
                          AlignInContainer: =AlignInContainer.Stretch
                          Color: =RGBA(95, 99, 104, 1)
                          Height: =Self.Size * 1.5
                          PaddingBottom: =0
                          PaddingLeft: =0
                          PaddingRight: =0
                          PaddingTop: =0
                          Size: =12
                          VerticalAlign: =VerticalAlign.Top
                - imgStatusIndicator:
                    Control: Icon
                    Properties:
                      Icon: =If(ThisItem.Status = "Active", Icon.CheckBadge, If(ThisItem.Status = "Pending", Icon.Clock, Icon.Checkmark))
                      AccessibleLabel: =ThisItem.Status
                      Color: =If(ThisItem.Status = "Active", RGBA(52, 168, 83, 1), If(ThisItem.Status = "Pending", RGBA(242, 139, 13, 1), RGBA(95, 99, 104, 1)))
                      Height: =24
                      Width: =24
            - btnCardOverlay:
                Control: Rectangle
                Properties:
                  OnSelect: =Select(Parent); Notify("Selected: " & ThisItem.Title, NotificationType.Information)
                  BorderColor: =If(Self.Pressed, RGBA(26, 115, 232, 1), If(Self.Hover, RGBA(218, 220, 224, 1), RGBA(0, 0, 0, 0)))
                  BorderThickness: =2
                  Fill: =RGBA(0, 0, 0, 0)
                  FocusedBorderColor: =RGBA(26, 115, 232, 1)
                  FocusedBorderThickness: =2
                  Height: =Parent.Height
                  HoverFill: =RGBA(32, 33, 36, 0.04)
                  PressedFill: =RGBA(26, 115, 232, 0.08)
                  RadiusBottomLeft: =8
                  RadiusBottomRight: =8
                  RadiusTopLeft: =8
                  RadiusTopRight: =8
                  Width: =Parent.Width
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
