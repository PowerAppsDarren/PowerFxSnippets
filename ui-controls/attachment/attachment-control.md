---
title: "Attachment Control"
description: "Examples of basic and advanced Attachment controls with accessibility and styling."
category: "ui-controls"
subcategory: "attachment"
tags: ["attachments", "files", "upload", "accessibility"]
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

# Attachment Control

This control is used to manage file attachments in Power Apps.
It allows users to upload, view, and delete files as needed.

## Simple Attachment Control

Here is the most simple and basic YAML code for an attachment control:

```yaml
- attAttachFiles:
    Control: Attachments
```

## Much More Useful Attachment Control

This example includes properties for accessibility, language, maximum attachment size, and more:
- You will never get a an App Checker accessibility error about not having an accessible label.
- The control is centered in the parent container vertically and horizontally.

```yaml
- attAttachFiles:
    Control: Attachments
    Properties:
      AccessibleLabel: ="Upload files here"
      ContentLanguage: =Language()
      MaxAttachmentSize: =50
      MaxAttachments: =10
      Tooltip: ="Upload files here"
      BorderColor: =App.Theme.Colors.Lighter60
      BorderThickness: =3
      Color: =App.Theme.Colors.Darker30
      Fill: =ColorFade(App.Theme.Colors.Lighter80, 70%)
      FocusedBorderThickness: =2
      HoverColor: =Self.Color
      ItemErrorColor: =Color.Red
      PaddingBottom: =10
      PaddingLeft: =10
      PaddingRight: =10
      PaddingTop: =10
      Width: =400
      X: =(Parent.Width - Self.Width) / 2
      Y: =(Parent.Height - Self.Height) / 2
```
