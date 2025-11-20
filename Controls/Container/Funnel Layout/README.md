---
title: "Funnel Layout Container"
description: "A responsive funnel layout with containers having decreasing numbers of columns (4, 3, 2, 1) for canvas apps"
category: "ui-controls"
subcategory: "container"
tags:
  - container
  - layout
  - funnel
  - responsive
difficulty: intermediate
products:
  - power-apps-canvas
dependencies: []
author: "PowerFxSnippets Community"
created: 2025-11-20
updated: 2025-11-20
license: "MIT"
related: []
---

# Funnel Layout for Power Apps

This snippet provides a responsive funnel layout with containers having decreasing numbers of columns (4, 3, 2, 1) for canvas apps.

All credit goes to Daniel Laskewitz	GitHub (@Laskewitz )
- https://github.com/laskewitz
- https://github.com/pnp/powerplatform-snippets/tree/main/power-apps/layout-funnel

<img src='img/funnel.png'>
<img src='https://github.com/laskewitz.png'>

## Add This to Your Application

```YAML
- MainContainerFunnelScreen:
    Control: GroupContainer
    Variant: verticalAutoLayoutContainer
    Properties:
      Height: =Parent.Height
      LayoutAlignItems: =LayoutAlignItems.Stretch
      LayoutDirection: =LayoutDirection.Vertical
      LayoutJustifyContent: =LayoutJustifyContent.Center
      LayoutMode: =LayoutMode.Auto
      Width: =Parent.Width
    Children:
    - Container1FunnelScreen:
        Control: GroupContainer
        Variant: horizontalAutoLayoutContainer
        Properties:
          LayoutMode: =LayoutMode.Auto
        Children:
        - Container11FunnelScreen:
            Control: GroupContainer
            Variant: horizontalAutoLayoutContainer
            Properties:
              LayoutMode: =LayoutMode.Auto
        - Container12FunnelScreen:
            Control: GroupContainer
            Variant: horizontalAutoLayoutContainer
            Properties:
              LayoutMode: =LayoutMode.Auto
        - Container13FunnelScreen:
            Control: GroupContainer
            Variant: horizontalAutoLayoutContainer
            Properties:
              LayoutMode: =LayoutMode.Auto
        - Container14FunnelScreen:
            Control: GroupContainer
            Variant: horizontalAutoLayoutContainer
            Properties:
              LayoutMode: =LayoutMode.Auto
    - Container2FunnelScreen:
        Control: GroupContainer
        Variant: horizontalAutoLayoutContainer
        Properties:
          LayoutMode: =LayoutMode.Auto
        Children:
        - Container21FunnelScreen:
            Control: GroupContainer
            Variant: horizontalAutoLayoutContainer
            Properties:
              LayoutMode: =LayoutMode.Auto
        - Container22FunnelScreen:
            Control: GroupContainer
            Variant: horizontalAutoLayoutContainer
            Properties:
              LayoutMode: =LayoutMode.Auto
        - Container23FunnelScreen:
            Control: GroupContainer
            Variant: horizontalAutoLayoutContainer
            Properties:
              LayoutMode: =LayoutMode.Auto
    - Container3FunnelScreen:
        Control: GroupContainer
        Variant: horizontalAutoLayoutContainer
        Properties:
          LayoutMode: =LayoutMode.Auto
        Children:
        - Container31FunnelScreen:
            Control: GroupContainer
            Variant: horizontalAutoLayoutContainer
            Properties:
              LayoutMode: =LayoutMode.Auto
        - Container32FunnelScreen:
            Control: GroupContainer
            Variant: horizontalAutoLayoutContainer
            Properties:
              LayoutMode: =LayoutMode.Auto
    - Container4FunnelScreen:
        Control: GroupContainer
        Variant: horizontalAutoLayoutContainer
        Properties:
          LayoutMode: =LayoutMode.Auto
```

## Free Community & Course Materials 

🆓 Get access to our free Power Apps crash course (and our community) here: 
- https://tinyurl.com/DarrensStuffFree 🔗

## Support

I hope you have found this helpful. If you need any help with the Power Platform, don't hesitate to email us at 
* [support@superpowerlabs.co](support@superpowerlabs.co)
* https://superpowerlabs.co 

---

## Disclaimer

**THIS CODE IS PROVIDED AS IS WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING ANY IMPLIED WARRANTIES OF FITNESS FOR A PARTICULAR PURPOSE, MERCHANTABILITY, OR NON-INFRINGEMENT.**


