---
title: "Status Board Gallery (Kanban Style)"
description: "A task/status board style gallery with status color stripes, priority badges, and filter tabs"
category: "ui-controls"
subcategory: "gallery"
tags:
  - gallery
  - kanban
  - status
  - tasks
  - priority
  - layout
difficulty: intermediate
products:
  - power-apps-canvas
author: "PowerAppsDarren"
created: 2024-01-01
updated: 2024-01-01
---

# Status Board Gallery (Kanban Style)

A task/status board style gallery (Kanban-inspired but vertical) with status indicators, priority badges, and filter tabs.

## Features

- Vertical responsive container layout
- Bold drop shadow on main content container
- Heading "Task Board" outside the gallery
- Summary row with task count and status filter tabs (To Do, In Progress, Done)
- Card-style items with:
  - Status color indicator stripe on left edge
  - Task title (bold)
  - Assignee name with person icon
  - Due date with calendar icon
  - Priority badge (High/Medium/Low with colors)
- Selection state elevates the card with bold shadow

## Sample Data Structure

```powerfx
Items: =[
    {Title: "Design Homepage", Assignee: "Alice", DueDate: "Dec 5", Priority: "High", Status: "In Progress"},
    {Title: "Write Documentation", Assignee: "Bob", DueDate: "Dec 7", Priority: "Medium", Status: "To Do"}
]
```

## Add This to Your Application

```yaml
- cStatusBoardWrapper:
    Control: GroupContainer
    Variant: verticalAutoLayoutContainer
    Properties:
      Fill: =RGBA(248, 249, 250, 1)
      Height: =Parent.Height
      Width: =Parent.Width
      LayoutDirection: =LayoutDirection.Vertical
      LayoutMode: =LayoutMode.Auto
      LayoutGap: =16
      PaddingTop: =24
      PaddingBottom: =24
      PaddingLeft: =24
      PaddingRight: =24
    Children:

    # Heading - Outside the gallery
    - lblTaskBoardHeading:
        Control: Label
        Properties:
          Text: ="Task Board"
          FontWeight: =FontWeight.Bold
          Size: =24
          Color: =RGBA(32, 33, 36, 1)
          Height: =40
          Width: =Parent.Width - 48
          PaddingLeft: =0
          Align: =Align.Left

    # Summary/Filter Row - Outside the gallery
    - cFilterRow:
        Control: GroupContainer
        Variant: horizontalAutoLayoutContainer
        Properties:
          Height: =48
          Width: =Parent.Width - 48
          Fill: =RGBA(0, 0, 0, 0)
          LayoutMode: =LayoutMode.Auto
          LayoutGap: =12
          LayoutAlignItems: =LayoutAlignItems.Center
        Children:
        # Total Tasks Count
        - lblTotalTasks:
            Control: Label
            Properties:
              Text: =CountRows(galTaskBoard.AllItems) & " tasks"
              Size: =14
              Color: =RGBA(96, 98, 102, 1)
              Height: =36
              Width: =80
              VerticalAlign: =VerticalAlign.Middle

        # To Do Badge
        - lblFilterToDo:
            Control: Label
            Properties:
              Text: ="To Do (" & CountIf(galTaskBoard.AllItems, Status = "To Do") & ")"
              Size: =12
              FontWeight: =FontWeight.Semibold
              Color: =RGBA(0, 120, 212, 1)
              Fill: =RGBA(222, 236, 249, 1)
              Height: =32
              Width: =80
              Align: =Align.Center
              VerticalAlign: =VerticalAlign.Middle
              RadiusTopLeft: =16
              RadiusTopRight: =16
              RadiusBottomLeft: =16
              RadiusBottomRight: =16

        # In Progress Badge
        - lblFilterInProgress:
            Control: Label
            Properties:
              Text: ="In Progress (" & CountIf(galTaskBoard.AllItems, Status = "In Progress") & ")"
              Size: =12
              FontWeight: =FontWeight.Semibold
              Color: =RGBA(255, 140, 0, 1)
              Fill: =RGBA(255, 244, 206, 1)
              Height: =32
              Width: =110
              Align: =Align.Center
              VerticalAlign: =VerticalAlign.Middle
              RadiusTopLeft: =16
              RadiusTopRight: =16
              RadiusBottomLeft: =16
              RadiusBottomRight: =16

        # Done Badge
        - lblFilterDone:
            Control: Label
            Properties:
              Text: ="Done (" & CountIf(galTaskBoard.AllItems, Status = "Done") & ")"
              Size: =12
              FontWeight: =FontWeight.Semibold
              Color: =RGBA(16, 124, 16, 1)
              Fill: =RGBA(223, 246, 221, 1)
              Height: =32
              Width: =75
              Align: =Align.Center
              VerticalAlign: =VerticalAlign.Middle
              RadiusTopLeft: =16
              RadiusTopRight: =16
              RadiusBottomLeft: =16
              RadiusBottomRight: =16

    # Main Content Container with Bold Drop Shadow
    - cTaskBoardContent:
        Control: GroupContainer
        Variant: verticalAutoLayoutContainer
        Properties:
          DropShadow: =DropShadow.Bold
          Fill: =RGBA(255, 255, 255, 1)
          Height: =Parent.Height - 180
          Width: =Parent.Width - 48
          RadiusTopLeft: =12
          RadiusTopRight: =12
          RadiusBottomLeft: =12
          RadiusBottomRight: =12
          LayoutMode: =LayoutMode.Auto
          PaddingTop: =16
          PaddingBottom: =16
          PaddingLeft: =16
          PaddingRight: =16
        Children:

        # Gallery
        - galTaskBoard:
            Control: Gallery
            Variant: galleryVertical
            Properties:
              Items: |
                =[
                    {Title: "Design Homepage", Assignee: "Alice", DueDate: "Dec 5", Priority: "High", Status: "In Progress"},
                    {Title: "Write Documentation", Assignee: "Bob", DueDate: "Dec 7", Priority: "Medium", Status: "To Do"},
                    {Title: "Code Review", Assignee: "Charlie", DueDate: "Dec 4", Priority: "Low", Status: "Done"},
                    {Title: "API Integration", Assignee: "Diana", DueDate: "Dec 6", Priority: "High", Status: "In Progress"},
                    {Title: "Unit Tests", Assignee: "Eve", DueDate: "Dec 8", Priority: "Medium", Status: "To Do"},
                    {Title: "Bug Fixes", Assignee: "Frank", DueDate: "Dec 3", Priority: "High", Status: "Done"}
                ]
              Height: =Parent.Height - 32
              Width: =Parent.Width - 32
              TemplatePadding: =8
              TemplateSize: =100
              ShowScrollbar: =true
            Children:

            # Task Card
            - cTaskCard:
                Control: GroupContainer
                Variant: manualLayoutContainer
                Properties:
                  Height: =92
                  Width: =Parent.TemplateWidth - 16
                  Fill: =If(ThisItem.IsSelected, RGBA(248, 250, 252, 1), RGBA(255, 255, 255, 1))
                  DropShadow: =If(ThisItem.IsSelected, DropShadow.Bold, DropShadow.Regular)
                  RadiusTopLeft: =8
                  RadiusTopRight: =8
                  RadiusBottomLeft: =8
                  RadiusBottomRight: =8
                  BorderColor: =RGBA(230, 230, 230, 1)
                  BorderThickness: =1
                Children:

                # Status Color Stripe (Left Edge)
                - rectStatusStripe:
                    Control: Rectangle
                    Properties:
                      Fill: |
                        =Switch(
                            ThisItem.Status,
                            "To Do", RGBA(0, 120, 212, 1),
                            "In Progress", RGBA(255, 140, 0, 1),
                            "Done", RGBA(16, 124, 16, 1),
                            RGBA(158, 158, 158, 1)
                        )
                      Height: =Parent.Height
                      Width: =6
                      X: =0
                      Y: =0
                      RadiusTopLeft: =8
                      RadiusBottomLeft: =8

                # Task Title
                - lblTaskTitle:
                    Control: Label
                    Properties:
                      Text: =ThisItem.Title
                      FontWeight: =FontWeight.Semibold
                      Size: =15
                      Color: =RGBA(32, 33, 36, 1)
                      Height: =28
                      Width: =Parent.Width - 130
                      X: =20
                      Y: =12
                      VerticalAlign: =VerticalAlign.Middle

                # Priority Badge
                - lblPriorityBadge:
                    Control: Label
                    Properties:
                      Text: =ThisItem.Priority
                      Size: =10
                      FontWeight: =FontWeight.Semibold
                      Color: |
                        =Switch(
                            ThisItem.Priority,
                            "High", RGBA(164, 38, 44, 1),
                            "Medium", RGBA(255, 140, 0, 1),
                            "Low", RGBA(16, 124, 16, 1),
                            RGBA(96, 98, 102, 1)
                        )
                      Fill: |
                        =Switch(
                            ThisItem.Priority,
                            "High", RGBA(253, 231, 233, 1),
                            "Medium", RGBA(255, 244, 206, 1),
                            "Low", RGBA(223, 246, 221, 1),
                            RGBA(243, 243, 243, 1)
                        )
                      Height: =24
                      Width: =60
                      X: =Parent.Width - 80
                      Y: =14
                      Align: =Align.Center
                      VerticalAlign: =VerticalAlign.Middle
                      RadiusTopLeft: =12
                      RadiusTopRight: =12
                      RadiusBottomLeft: =12
                      RadiusBottomRight: =12

                # Assignee Row
                - cAssigneeRow:
                    Control: GroupContainer
                    Variant: horizontalAutoLayoutContainer
                    Properties:
                      Height: =24
                      Width: =200
                      X: =20
                      Y: =44
                      Fill: =RGBA(0, 0, 0, 0)
                      LayoutMode: =LayoutMode.Auto
                      LayoutGap: =8
                      LayoutAlignItems: =LayoutAlignItems.Center
                    Children:
                    - icoUser:
                        Control: Classic/Icon
                        Properties:
                          Icon: =Icon.Person
                          Color: =RGBA(96, 98, 102, 1)
                          Height: =18
                          Width: =18
                    - lblAssignee:
                        Control: Label
                        Properties:
                          Text: =ThisItem.Assignee
                          Size: =12
                          Color: =RGBA(96, 98, 102, 1)
                          Height: =24
                          Width: =120
                          VerticalAlign: =VerticalAlign.Middle

                # Due Date Row
                - cDueDateRow:
                    Control: GroupContainer
                    Variant: horizontalAutoLayoutContainer
                    Properties:
                      Height: =24
                      Width: =150
                      X: =20
                      Y: =66
                      Fill: =RGBA(0, 0, 0, 0)
                      LayoutMode: =LayoutMode.Auto
                      LayoutGap: =8
                      LayoutAlignItems: =LayoutAlignItems.Center
                    Children:
                    - icoCalendar:
                        Control: Classic/Icon
                        Properties:
                          Icon: =Icon.CalendarBlank
                          Color: =RGBA(96, 98, 102, 1)
                          Height: =18
                          Width: =18
                    - lblDueDate:
                        Control: Label
                        Properties:
                          Text: ="Due: " & ThisItem.DueDate
                          Size: =12
                          Color: =RGBA(96, 98, 102, 1)
                          Height: =24
                          Width: =100
                          VerticalAlign: =VerticalAlign.Middle
```

## Free Community & Course Materials

Get access to our free Power Apps crash course (and our community) here:
- https://tinyurl.com/DarrensStuffFree

## Support

If you need any help with the Power Platform, don't hesitate to email us at:
- support@superpowerlabs.co
- https://powerplatformlinks.com

## Disclaimer

THIS CODE IS PROVIDED AS IS WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING ANY IMPLIED WARRANTIES OF FITNESS FOR A PARTICULAR PURPOSE, MERCHANTABILITY, OR NON-INFRINGEMENT.

---

## History

| Date | Author | Changes |
|------|--------|---------|
| 2025-12-17 | Claude | Converted from YAML to markdown, added to layouts/ |
