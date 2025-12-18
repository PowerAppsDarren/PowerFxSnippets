---
title: "Random Profile Photo"
description: "An Image control that displays a random person's face using an external service."
category: "ui-controls"
subcategory: "image"
tags: ["image", "random", "profile", "avatar"]
difficulty: beginner
products:
  - power-apps-canvas
dependencies: []
related: []
author: "Darren Neese"
created: 2025-11-19
updated: 2025-11-19
license: "MIT"
---

# Need a Random Profile Photo

This is really nice if you want to have a photo for each row in your gallery control for people.

## Add This to Your Application

```JavaScript
// Paste this in as YAML into your canvas Power Apps application
- imgRandomPerson:
    Control: Image
    Properties:
      AccessibleLabel: ="A photo of a person. Just their face."
      Image: ="https://thispersondoesnotexist.com/"
      Tooltip: =Self.AccessibleLabel
      BorderColor: =Self.Fill
      DisabledFill: =Self.Fill
      HoverBorderColor: =Self.Fill
      PressedBorderColor: =Self.Fill
      Fill: =Color.Transparent
      RadiusBottomLeft: =Average(Self.Height, Self.Width) * 10%
      RadiusBottomRight: =Average(Self.Height, Self.Width) * 10%
      RadiusTopLeft: =Average(Self.Height, Self.Width) * 10%
      RadiusTopRight: =Average(Self.Height, Self.Width) * 10%
```
