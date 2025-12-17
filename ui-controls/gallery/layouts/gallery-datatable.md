---
title: "Data Table Style Gallery"
description: "A professional data table gallery with column headers, alternating rows, and search toolbar"
category: "ui-controls"
subcategory: "gallery"
tags:
  - gallery
  - datatable
  - table
  - zebra-striping
  - columns
  - layout
difficulty: intermediate
products:
  - power-apps-canvas
author: "PowerAppsDarren"
created: 2024-01-01
updated: 2024-01-01
---

# Data Table Style Gallery

A professional data table style gallery component featuring column headers, alternating row colors (zebra striping), and a toolbar with record count.

## Features

- Responsive vertical container layout
- Bold drop shadow for depth
- Static header row with column labels
- Toolbar with record count and search icon
- Alternating row colors (zebra striping)
- Selection indicator with chevron
- Four columns: Employee Name, Department, Email, Status
- Status color coding (Active = green, On Leave = red)

## Sample Data Structure

```powerfx
Items: =[
    {Name: "John Smith", Department: "Engineering", Email: "jsmith@company.com", Status: "Active"},
    {Name: "Jane Doe", Department: "Marketing", Email: "jdoe@company.com", Status: "Active"}
]
```

## Add This to Your Application

```yaml
- cDataTableWrapper:
    Control: GroupContainer
    Variant: verticalAutoLayoutContainer
    Properties:
      Fill: =RGBA(248, 249, 250, 1)
      Height: =Parent.Height
      Width: =Parent.Width
      LayoutDirection: =LayoutDirection.Vertical
      LayoutMode: =LayoutMode.Auto
      PaddingTop: =24
      PaddingBottom: =24
      PaddingLeft: =24
      PaddingRight: =24
    Children:

    # Heading Label - Outside the gallery
    - lblDataTableHeading:
        Control: Label
        Properties:
          Text: ="Employee Directory"
          FontWeight: =FontWeight.Bold
          Size: =24
          Color: =RGBA(32, 31, 30, 1)
          Height: =50
          Width: =Parent.Width - 48
          PaddingLeft: =0
          Align: =Align.Left
          VerticalAlign: =VerticalAlign.Middle

    # Summary/Toolbar Row - Outside the gallery
    - cToolbarRow:
        Control: GroupContainer
        Variant: horizontalAutoLayoutContainer
        Properties:
          Height: =50
          Width: =Parent.Width - 48
          Fill: =RGBA(243, 242, 241, 1)
          LayoutMode: =LayoutMode.Auto
          LayoutAlignItems: =LayoutAlignItems.Center
          PaddingLeft: =20
          PaddingRight: =20
          RadiusTopLeft: =8
          RadiusTopRight: =8
          RadiusBottomLeft: =0
          RadiusBottomRight: =0
        Children:
        - lblRecordCount:
            Control: Label
            Properties:
              Text: =CountRows(galEmployeeTable.AllItems) & " records"
              Size: =13
              Color: =RGBA(96, 94, 92, 1)
              Height: =Parent.Height
              Width: =150
              VerticalAlign: =VerticalAlign.Middle
        - icoSearch:
            Control: Classic/Icon
            Properties:
              Icon: =Icon.Search
              Color: =RGBA(96, 94, 92, 1)
              Height: =32
              Width: =32
              PaddingTop: =4
              PaddingBottom: =4

    # Main Content Container with Bold Drop Shadow
    - cTableContent:
        Control: GroupContainer
        Variant: verticalAutoLayoutContainer
        Properties:
          DropShadow: =DropShadow.Bold
          Fill: =RGBA(255, 255, 255, 1)
          Height: =Parent.Height - 160
          Width: =Parent.Width - 48
          RadiusTopLeft: =0
          RadiusTopRight: =0
          RadiusBottomLeft: =8
          RadiusBottomRight: =8
          LayoutMode: =LayoutMode.Auto
        Children:

        # Column Header Row - Outside the gallery
        - cHeaderRow:
            Control: GroupContainer
            Variant: horizontalAutoLayoutContainer
            Properties:
              Height: =50
              Width: =Parent.Width
              Fill: =RGBA(0, 120, 212, 1)
              LayoutMode: =LayoutMode.Auto
              LayoutAlignItems: =LayoutAlignItems.Center
              PaddingLeft: =20
              PaddingRight: =20
            Children:
            - lblHeaderName:
                Control: Label
                Properties:
                  Text: ="Employee Name"
                  FontWeight: =FontWeight.Semibold
                  Size: =14
                  Color: =RGBA(255, 255, 255, 1)
                  Height: =Parent.Height
                  Width: =200
                  VerticalAlign: =VerticalAlign.Middle
                  PaddingLeft: =30
            - lblHeaderDept:
                Control: Label
                Properties:
                  Text: ="Department"
                  FontWeight: =FontWeight.Semibold
                  Size: =14
                  Color: =RGBA(255, 255, 255, 1)
                  Height: =Parent.Height
                  Width: =180
                  VerticalAlign: =VerticalAlign.Middle
            - lblHeaderEmail:
                Control: Label
                Properties:
                  Text: ="Email"
                  FontWeight: =FontWeight.Semibold
                  Size: =14
                  Color: =RGBA(255, 255, 255, 1)
                  Height: =Parent.Height
                  Width: =280
                  VerticalAlign: =VerticalAlign.Middle
            - lblHeaderStatus:
                Control: Label
                Properties:
                  Text: ="Status"
                  FontWeight: =FontWeight.Semibold
                  Size: =14
                  Color: =RGBA(255, 255, 255, 1)
                  Height: =Parent.Height
                  Width: =120
                  VerticalAlign: =VerticalAlign.Middle

        # Gallery
        - galEmployeeTable:
            Control: Gallery
            Variant: galleryVertical
            Properties:
              Items: |
                =AddColumns(
                    [
                        {Name: "John Smith", Department: "Engineering", Email: "jsmith@company.com", Status: "Active"},
                        {Name: "Jane Doe", Department: "Marketing", Email: "jdoe@company.com", Status: "Active"},
                        {Name: "Bob Wilson", Department: "Sales", Email: "bwilson@company.com", Status: "On Leave"},
                        {Name: "Sarah Johnson", Department: "Engineering", Email: "sjohnson@company.com", Status: "Active"},
                        {Name: "Mike Brown", Department: "HR", Email: "mbrown@company.com", Status: "Active"},
                        {Name: "Emily Davis", Department: "Finance", Email: "edavis@company.com", Status: "Active"},
                        {Name: "Chris Lee", Department: "Engineering", Email: "clee@company.com", Status: "On Leave"}
                    ] As Record,
                    RowIndex, CountRows(Filter([{Name: "John Smith"}, {Name: "Jane Doe"}, {Name: "Bob Wilson"}, {Name: "Sarah Johnson"}, {Name: "Mike Brown"}, {Name: "Emily Davis"}, {Name: "Chris Lee"}], Name <= Record.Name))
                )
              Height: =Parent.Height - 50
              Width: =Parent.Width
              TemplatePadding: =0
              TemplateSize: =55
              TemplateFill: |
                =If(
                    ThisItem.IsSelected,
                    RGBA(232, 245, 255, 1),
                    If(
                        Mod(Value(ThisItem.RowIndex), 2) = 0,
                        RGBA(255, 255, 255, 1),
                        RGBA(250, 249, 248, 1)
                    )
                )
              ShowScrollbar: =true
            Children:

            # Row Container
            - cRowTemplate:
                Control: GroupContainer
                Variant: horizontalAutoLayoutContainer
                Properties:
                  Height: =Parent.TemplateHeight
                  Width: =Parent.TemplateWidth
                  Fill: =RGBA(0, 0, 0, 0)
                  LayoutMode: =LayoutMode.Auto
                  LayoutAlignItems: =LayoutAlignItems.Center
                  PaddingLeft: =20
                  PaddingRight: =20
                Children:

                # Selection Indicator
                - icoSelection:
                    Control: Classic/Icon
                    Properties:
                      Icon: =Icon.ChevronRight
                      Color: =RGBA(0, 120, 212, 1)
                      Visible: =ThisItem.IsSelected
                      Height: =24
                      Width: =24

                # Employee Name
                - lblEmployeeName:
                    Control: Label
                    Properties:
                      Text: =ThisItem.Name
                      Size: =13
                      Color: =RGBA(32, 31, 30, 1)
                      Height: =Parent.Height
                      Width: =If(icoSelection.Visible, 176, 200)
                      VerticalAlign: =VerticalAlign.Middle
                      PaddingLeft: =If(icoSelection.Visible, 6, 30)

                # Department
                - lblDepartment:
                    Control: Label
                    Properties:
                      Text: =ThisItem.Department
                      Size: =13
                      Color: =RGBA(50, 49, 48, 1)
                      Height: =Parent.Height
                      Width: =180
                      VerticalAlign: =VerticalAlign.Middle

                # Email
                - lblEmail:
                    Control: Label
                    Properties:
                      Text: =ThisItem.Email
                      Size: =13
                      Color: =RGBA(50, 49, 48, 1)
                      Height: =Parent.Height
                      Width: =280
                      VerticalAlign: =VerticalAlign.Middle

                # Status
                - lblStatusValue:
                    Control: Label
                    Properties:
                      Text: =ThisItem.Status
                      Size: =13
                      FontWeight: =FontWeight.Semibold
                      Color: |
                        =If(
                            ThisItem.Status = "Active",
                            RGBA(16, 124, 16, 1),
                            RGBA(164, 38, 44, 1)
                        )
                      Height: =Parent.Height
                      Width: =120
                      VerticalAlign: =VerticalAlign.Middle
```


---

## History

| Date | Author | Changes |
|------|--------|---------|
| 2025-12-17 | Claude | Converted from YAML to markdown, added to layouts/ |
