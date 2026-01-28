---
title: "Email Attachments"
description: "Send email with multiple attachments using Office365Outlook connector."
category: "integrations"
subcategory: "office365-outlook"
tags: ["email", "attachments", "outlook", "office365"]
difficulty: intermediate
products:
  - power-apps-canvas
dependencies:
  - Office365Outlook
author: "Darren Neese"
created: 2025-11-19
updated: 2025-11-19
license: "MIT"
related: []
---

# Email Attachments

```PowerFx
- Gallery2:
    Control: Gallery
    Variant: galleryVertical
    Properties:
      Items: =attFiles.Attachments
      WrapCount: =2
      BorderThickness: =2
      DelayItemLoading: =true
      Fill: =RGBA(202, 202, 202, 1)
      Height: =482
      Layout: =Layout.Vertical
      LoadingSpinner: =LoadingSpinner.Data
      TemplateFill: =Color.White
      TemplateSize: =200
      Width: =673
      X: =636
      Y: =36
    Children:
    - Image1:
        Control: Image
        Properties:
          OnSelect: =Select(Parent)
          Image: =ThisItem.Value
          Height: =200
          ImagePosition: =ImagePosition.Fill
          Width: =329
- attFiles:
    Control: Attachments
    Properties:
      MaxAttachmentSize: =50
      MaxAttachments: =10
      Tooltip: ="Upload Files Here"
      BorderColor: =App.Theme.Colors.Primary
      Height: =482
      PaddingBottom: =5
      PaddingLeft: =If(Self.DisplayMode = DisplayMode.Edit, 5, 0)
      PaddingRight: =5
      PaddingTop: =5
      Width: =579
      X: =35
      Y: =36
- btnSendAttachments:
    Control: Button
    Properties:
      OnSelect: |
        =Office365Outlook.SendEmailV2(
            User().Email,
            "Send Multiple Attachements From PowerApps",
            "Please find attached report FYU",
            {
                Attachments: ForAll(
                    attFiles.Attachments,
                    {
                        Name: ThisRecord.Name,
                        ContentBytes: ThisRecord.Value
                    }
                )
            }
        );
      Text: ="Send These Files"
      Width: =220
      X: =1089
      Y: =555
---

## History

| Date | Author | Changes |
|------|--------|---------|
| 2026-01-27 | Migration | Initial TOC and history section added |
