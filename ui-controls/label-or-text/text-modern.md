---
title: "Modern Text Label Control"
description: "A modern text label control with border styling and primary color font for canvas apps"
category: "ui-controls"
subcategory: "label"
tags:
  - text
  - label
  - modern
  - ui
difficulty: beginner
products:
  - power-apps-canvas
dependencies: []
author: "PowerFxSnippets Community"
created: 2025-11-20
updated: 2025-11-20
license: "MIT"
related: []
---

# Modern Text Label Control

This snippet provides a modern text label control with border and primary color styling.

## Add This to Your Application

```PowerFx
- lblText:
    Control: Text
    Properties:
      BorderColor: =RGBA(229, 229, 229, 1)
      BorderStyle: =BorderStyle.Solid
      BorderThickness: =1
      FontColor: =App.Theme.Colors.Primary
      PaddingLeft: =5
      PaddingRight: =5
      Text: ="This is a text (or modern label) control"
      Width: =300
```


