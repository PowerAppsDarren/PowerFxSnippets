---
title: "Timeline Style Gallery"
description: "A vertical timeline gallery for displaying chronological events with connecting lines and color-coded markers"
category: "ui-controls"
subcategory: "gallery"
tags:
  - gallery
  - timeline
  - chronological
  - events
  - layout
difficulty: intermediate
products:
  - power-apps-canvas
author: "PowerAppsDarren"
created: 2024-01-01
updated: 2024-01-01
---

# Timeline Style Gallery

A vertical timeline-style gallery component for displaying chronological events with visual connecting lines and color-coded markers.

## Features

- Vertical timeline with connecting line
- Circle markers for each event
- Date/time displayed on left side
- Event title and description on right side
- Color-coded by event type (Meeting=blue, Review=green, Development=yellow)
- Bold drop shadow on content container
- Heading and summary row outside the gallery
- Fully responsive vertical auto-layout

## Sample Data Structure

```powerfx
Items: =[
    {Date: "Dec 1", Time: "9:00 AM", Title: "Project Kickoff", Description: "Initial meeting with stakeholders", Type: "Meeting"},
    {Date: "Dec 2", Time: "2:00 PM", Title: "Design Review", Description: "Review wireframes and mockups", Type: "Review"}
]
```

## Add This to Your Application

```yaml
- cTimelineWrapper:
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
    - lblTimelineHeading:
        Control: Label
        Properties:
          Text: ="Activity Timeline"
          FontWeight: =FontWeight.Bold
          Size: =24
          Color: =RGBA(32, 33, 36, 1)
          Height: =40
          Width: =Parent.Width - 48
          PaddingLeft: =8
          Align: =Align.Left

    # Summary Row - Outside the gallery
    - cTimelineSummary:
        Control: GroupContainer
        Variant: horizontalAutoLayoutContainer
        Properties:
          Height: =36
          Width: =Parent.Width - 48
          Fill: =RGBA(0, 0, 0, 0)
          LayoutMode: =LayoutMode.Auto
          LayoutGap: =24
          LayoutAlignItems: =LayoutAlignItems.Center
          PaddingLeft: =8
        Children:
        - lblEventCount:
            Control: Label
            Properties:
              Text: =CountRows(galTimeline.AllItems) & " events"
              Size: =14
              Color: =RGBA(95, 99, 104, 1)
              Height: =30
              Width: =100
        - lblDateRange:
            Control: Label
            Properties:
              Text: ="Dec 1 - Dec 5, 2024"
              Size: =14
              Color: =RGBA(95, 99, 104, 1)
              Height: =30
              Width: =160

    # Main Content Container with Bold Drop Shadow
    - cTimelineContent:
        Control: GroupContainer
        Variant: verticalAutoLayoutContainer
        Properties:
          DropShadow: =DropShadow.Bold
          Fill: =RGBA(255, 255, 255, 1)
          Height: =Parent.Height - 160
          Width: =Parent.Width - 48
          RadiusTopLeft: =12
          RadiusTopRight: =12
          RadiusBottomLeft: =12
          RadiusBottomRight: =12
          LayoutMode: =LayoutMode.Auto
          PaddingTop: =24
          PaddingBottom: =24
          PaddingLeft: =24
          PaddingRight: =24
        Children:

        # Gallery
        - galTimeline:
            Control: Gallery
            Variant: galleryVertical
            Properties:
              Items: |
                =[
                    {Date: "Dec 1", Time: "9:00 AM", Title: "Project Kickoff", Description: "Initial meeting with stakeholders", Type: "Meeting"},
                    {Date: "Dec 2", Time: "2:00 PM", Title: "Design Review", Description: "Review wireframes and mockups", Type: "Review"},
                    {Date: "Dec 3", Time: "10:00 AM", Title: "Development Start", Description: "Begin sprint 1 development", Type: "Development"},
                    {Date: "Dec 4", Time: "11:30 AM", Title: "Code Review", Description: "Review initial implementation", Type: "Review"},
                    {Date: "Dec 5", Time: "3:00 PM", Title: "Sprint Planning", Description: "Plan sprint 2 activities", Type: "Meeting"}
                ]
              Height: =Parent.Height - 48
              Width: =Parent.Width - 48
              TemplatePadding: =0
              TemplateSize: =100
              ShowScrollbar: =true
            Children:

            # Timeline Item Container
            - cTimelineItem:
                Control: GroupContainer
                Variant: horizontalAutoLayoutContainer
                Properties:
                  Height: =90
                  Width: =Parent.TemplateWidth
                  Fill: =RGBA(0, 0, 0, 0)
                  LayoutMode: =LayoutMode.Auto
                  LayoutGap: =0
                  LayoutAlignItems: =LayoutAlignItems.Start
                Children:

                # Left Side: Date and Time
                - cDateSection:
                    Control: GroupContainer
                    Variant: verticalAutoLayoutContainer
                    Properties:
                      Height: =Parent.Height
                      Width: =100
                      Fill: =RGBA(0, 0, 0, 0)
                      LayoutMode: =LayoutMode.Auto
                      LayoutGap: =2
                      LayoutAlignItems: =LayoutAlignItems.End
                      PaddingRight: =16
                      PaddingTop: =8
                    Children:
                    - lblDate:
                        Control: Label
                        Properties:
                          Text: =ThisItem.Date
                          FontWeight: =FontWeight.Semibold
                          Size: =13
                          Color: =RGBA(32, 33, 36, 1)
                          Height: =22
                          Width: =80
                          Align: =Align.Right
                    - lblTime:
                        Control: Label
                        Properties:
                          Text: =ThisItem.Time
                          Size: =11
                          Color: =RGBA(95, 99, 104, 1)
                          Height: =18
                          Width: =80
                          Align: =Align.Right

                # Timeline Connector
                - cTimelineConnector:
                    Control: GroupContainer
                    Variant: manualLayoutContainer
                    Properties:
                      Height: =Parent.Height
                      Width: =32
                      Fill: =RGBA(0, 0, 0, 0)
                    Children:
                    # Top line segment
                    - rectLineTop:
                        Control: Rectangle
                        Properties:
                          Fill: =RGBA(218, 220, 224, 1)
                          Height: =12
                          Width: =2
                          X: =15
                          Y: =0
                    # Circle marker
                    - circleMarker:
                        Control: Circle
                        Properties:
                          Fill: |
                            =Switch(
                                ThisItem.Type,
                                "Meeting", RGBA(66, 133, 244, 1),
                                "Review", RGBA(52, 168, 83, 1),
                                "Development", RGBA(251, 188, 4, 1),
                                RGBA(158, 158, 158, 1)
                            )
                          Height: =16
                          Width: =16
                          X: =8
                          Y: =12
                    # Bottom line segment
                    - rectLineBottom:
                        Control: Rectangle
                        Properties:
                          Fill: =RGBA(218, 220, 224, 1)
                          Height: =Parent.Height - 28
                          Width: =2
                          X: =15
                          Y: =28

                # Right Side: Event Details
                - cEventDetails:
                    Control: GroupContainer
                    Variant: verticalAutoLayoutContainer
                    Properties:
                      Height: =80
                      Width: =Parent.Width - 148
                      Fill: =If(ThisItem.IsSelected, RGBA(232, 245, 255, 1), RGBA(248, 249, 250, 1))
                      LayoutMode: =LayoutMode.Auto
                      LayoutGap: =6
                      LayoutAlignItems: =LayoutAlignItems.Stretch
                      PaddingTop: =12
                      PaddingBottom: =12
                      PaddingLeft: =16
                      PaddingRight: =16
                      RadiusTopLeft: =8
                      RadiusTopRight: =8
                      RadiusBottomLeft: =8
                      RadiusBottomRight: =8
                    Children:
                    - lblEventTitle:
                        Control: Label
                        Properties:
                          Text: =ThisItem.Title
                          FontWeight: =FontWeight.Semibold
                          Size: =14
                          Color: =RGBA(32, 33, 36, 1)
                          Height: =24
                          Width: =Parent.Width - 32
                          VerticalAlign: =VerticalAlign.Middle
                    - lblEventDescription:
                        Control: Label
                        Properties:
                          Text: =ThisItem.Description
                          Size: =12
                          Color: =RGBA(95, 99, 104, 1)
                          Height: =20
                          Width: =Parent.Width - 32
                          VerticalAlign: =VerticalAlign.Top
                    - lblEventType:
                        Control: Label
                        Properties:
                          Text: =ThisItem.Type
                          Size: =10
                          FontWeight: =FontWeight.Semibold
                          Color: |
                            =Switch(
                                ThisItem.Type,
                                "Meeting", RGBA(66, 133, 244, 1),
                                "Review", RGBA(52, 168, 83, 1),
                                "Development", RGBA(251, 188, 4, 1),
                                RGBA(158, 158, 158, 1)
                            )
                          Height: =18
                          Width: =100
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
