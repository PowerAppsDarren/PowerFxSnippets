

---
title: "Handling Vertical Sliders"
description: "Example of using vertical sliders to control image position."
category: "Controls"
tags: ["slider", "vertical", "layout", "position"]
difficulty: intermediate
author: "Darren Neese"
created: 2025-11-19
updated: 2025-11-19
license: "MIT"
---

# Handling Vertical Sliders

```PowerFx
- Label2:
    Control: Label
    Properties:
      Text: =imgMe.Y
      BorderThickness: =2
      X: =imgMe.X + imgMe.Width
      Y: =imgMe.Y
- Label1_1:
    Control: Label
    Properties:
      Text: =sldX.Value
      X: =579
      Y: =106
- Label1:
    Control: Label
    Properties:
      Text: =sldY.Value
      X: =110
      Y: =366
- sldY:
    Control: Classic/Slider
    Properties:
      Default: =Parent.Height / 2
      Max: =Parent.Height - imgMe.Height
      Height: =282
      Layout: =Layout.Vertical
      Width: =44
      X: =42
      Y: =245
- sldX:
    Control: Classic/Slider
    Properties:
      Default: =Parent.Width / 2
      Max: =Parent.Width - imgMe.Width
      X: =494
      Y: =38
- imgMe:
    Control: Image
    Properties:
      Image: =User().Image
      Height: =200
      Width: =200
      X: =sldX.Value
      Y: =Parent.Height - Self.Height - sldY.Value

```