---
title: "Code Editor Input"
description: "A multi-line text input styled as a code editor with monospaced font."
category: "ui-controls"
subcategory: "text-input"
tags: ["text-input", "code", "editor", "ui"]
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

# Code Editor

This is some YAML you can paste into your canvas Power Apps applciation that will serve well as a code editor. It's a multi-line text input that has a Courier New font and a grey background. It's also got some padding so it looks nice. You can use it to edit your Power Apps code, or to edit any other kind of code. It's a great way to get started with Power Apps development, or to learn about Power Apps development.

## Add This to Your Application

```PowerFx
- txtCodeEditor:
    Control: Classic/TextInput
    Properties:
      Default: |-)
        ="- CONTROL_NAME_GOES_HERE:
            Control: Button"
      Clear: =true
      DisabledBorderColor: =Self.Fill
      Font: =Font.'Courier New'
      Height: =Parent.Height - Self.Y * 2
      HoverFill: =Self.Fill
      LineHeight: =1.4
      Mode: =TextMode.MultiLine
      PaddingBottom: =10
      PaddingLeft: =10
      PaddingRight: =10
      PaddingTop: =10
      Size: =18
      Width: =Parent.Width - Self.X * 2
      X: =20
      Y: =20
```
