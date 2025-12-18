---
title: "Nested Galleries"
description: "Implementation of nested galleries with parent-child relationships and dynamic data generation"
category: "ui-controls"
subcategory: "gallery"
tags:
  - gallery
  - nested
  - parent-child
  - dynamic
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

# Nested Galleries

This snippet demonstrates nested galleries with parent-child relationships and dynamic data generation.

[nested-galleries.msapp](https://github.com/PowerAppsDarren/PowerFxSnippets/blob/main/Controls/Gallery/ResponsiveGallery.yaml)

[Video](https://www.loom.com/share/e7d61632ead649a096a4881d96ec96f0?sid=413f2730-019c-46b3-954a-3bad50497a9b)

## Add This to Your Application

```PowerFx
- btnGenData:
    Control: Button
    Properties:
      OnSelect: |-
        =ClearCollect(
            colMasterData, 
            ForAll(
                Sequence(6) As My, 
                {
                    Title: "#" & My.Value & " - Master Data Table",
                    DetailTable: 
                        ForAll(
                            Sequence(RandBetween(1, 8)), 
                            {
                                Title: "#" & ThisRecord.Value & " - " & GUID()
                            }
                        )
                }
            )    
        )
      Text: ="Create Data"
      Height: =42
      Width: =132
      X: =24
      Y: =27
- galParent:
    Control: Gallery
    Variant: variableTemplateHeightGallery
    Properties:
      Items: =colMasterData
      BorderThickness: =4
      DelayItemLoading: =true
      Fill: =RGBA(106, 122, 127, 1)
      Height: =Parent.Height - Self.Y - 40
      Layout: =Layout.Vertical
      LoadingSpinner: =LoadingSpinner.Data
      TemplateFill: =Color.White
      TemplatePadding: =1
      TemplateSize: =300
      Width: =1314
      X: =24
      Y: =87
    Children:
    - Label1:
        Control: Label
        Properties:
          OnSelect: =Select(Parent)
          Text: =ThisItem.Title
          BorderThickness: =1
          Height: =50
          Width: =608
          X: =10
          Y: =10
    - galChild:
        Control: Gallery
        Variant: galleryVertical
        Properties:
          Items: |-
            =ThisItem.DetailTable
            //Filter(Table2, FK = ThisItem.ID)
          BorderStyle: =BorderStyle.Dotted
          BorderThickness: =4
          DelayItemLoading: =true
          Fill: =RGBA(253, 207, 180, 1)
          Height: =Self.AllItemsCount * 52 + 4
          Layout: =Layout.Vertical
          LoadingSpinner: =LoadingSpinner.Data
          TemplateFill: =Color.AliceBlue
          TemplatePadding: =2
          TemplateSize: =50
          Width: =638
          X: =80
          Y: =80
        Children:
        - TextCanvas4_1:
            Control: Text
            Properties:
              Text: =Upper(ThisItem.Title)
              Height: |
                =50
              Width: =448
              X: =40

```

---

## History

| Date       | Author | Changes                          |
|------------|--------|----------------------------------|
| 2025-12-17 | Claude | Moved to interactions/ subfolder |
