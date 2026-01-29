---
title: "Themed Chart Control"
description: "A themed BarChart control inside a container with custom styling."
category: "ui-controls"
subcategory: "chart"
tags: ["chart", "bar-chart", "theme", "visualization"]
difficulty: intermediate
products:
  - power-apps-canvas
dependencies: []
related: []
author: "Darren Neese"
created: 2025-11-19
updated: 2025-11-19
license: "MIT"
---

# Chart-Controls

## Table of Contents

```PowerFx
- cntChartContainer:
    Control: GroupContainer
    Variant: manualLayoutContainer
    Properties:
      DropShadow: =DropShadow.Regular
      Fill: =Color.WhiteSmoke
      Height: =Parent.Height - Self.Y * 2
      Width: =Parent.Width - Self.X * 2
      X: =40
      Y: =40
    Children:
    - chrBarChart:
        Control: BarChart
        Properties:
          Items: |-
            =FirstN(
                ColumnChartSample,
                5
            )
          GridStyle: =GridStyle.All
          Height: =Parent.Height - Self.X * 1.5
          ItemColorSet: |-
            =[
                App.Theme.Colors.Primary,
                App.Theme.Colors.Lighter30,
                App.Theme.Colors.Darker30,
                App.Theme.Colors.Lighter60,
                App.Theme.Colors.Lighter10
            ]
          ItemsGap: =15
          PaddingLeft: =20
          PaddingRight: =0
          Size: =20
          Width: =Parent.Width - Self.X * 2
          X: =10
          XLabelAngle: =20
          Y: =20
```
---

## History

| Date | Author | Changes |
|------|--------|---------|
| 2026-01-27 | Migration | Initial TOC and history section added |
