---
title: "Spacer Rectangle"
description: "A rectangle control used as a visual spacer or guide during development."
category: "Controls"
tags: ["rectangle", "spacer", "layout", "guide"]
difficulty: beginner
author: "Darren Neese"
created: 2025-11-19
updated: 2025-11-19
license: "MIT"
---

# Spacer Medium Rectangle

This is a helpful canvas Power Apps code snippet.

## Add This to Your Application

```PowerFx
- retSpacerGuide:
    Control: Rectangle
    Properties:
      AccessibleLabel: ="This is just a spacer guide control."
      Tooltip: ="This is just a spacer guide control."
      BorderColor: =Color.Red // An annoying color that stands out
      BorderThickness: =1
      Fill: =RGBA(0, 255, 0, 1) // An annoying color that stands out
      Height: =fxConstants.Spacing.SpacingMd // 20
      Visible: =fxIsStudioMode // StartsWith(Host.Version, "PowerApps-Studio")
      Width: =fxConstants.Spacing.SpacingMd // 20
      X: =Parent.Width - Self.Width
      Y: =Parent.Height - Self.Height
```


