---
title: "Custom Calendar Control"
description: "A custom calendar implementation using galleries for month and day views."
category: "ui-controls"
subcategory: "calendar"
tags: ["calendar", "date", "gallery", "ui"]
difficulty: advanced
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

# Custom Calendar Control

```PowerFx
- MonthDayGallery1:
    Control: Gallery
    Variant: MonthDayGallery
    Properties:
      AccessibleLabel: ="Days of selected month"
      Items: =[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19, 20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41]
      WrapCount: =7
      Height: =425
      Layout: =Layout.Vertical
      ShowScrollbar: =false
      TemplatePadding: =0
      TemplateSize: =60
      Visible: =_calendarVisible
      Width: =420
      Y: =WeekdayGallery1.Y + WeekdayGallery1.Height
    Children:
    - Title2:
        Control: Label
        Properties:
          OnSelect: =Set(_dateSelected, DateAdd(_firstDayInView, ThisItem.Value, TimeUnit.Days))
          Text: =Day(DateAdd(_firstDayInView,ThisItem.Value, TimeUnit.Days))
          Align: =Align.Center
          BorderColor: =RGBA(0, 0, 0, 0)
          Color: =If(DateAdd(_firstDayInView, ThisItem.Value) = _dateSelected, RGBA(255, 255, 255, 1), DateAdd(_firstDayInView, ThisItem.Value) = Today(), RGBA(47, 41, 43, 1), LblMonthSelected1.Color)
          Fill: |-
            =/*Fill value changes if the gallery item day = today, or if it lies outside of the current month*/
            If(
                /*Date selected is today*/
                DateAdd(_firstDayInView, ThisItem.Value) = Today() && DateAdd(_firstDayInView, ThisItem.Value) = _dateSelected, RGBA(0,0,0,0),
                /*Today when it is not selected*/
                DateAdd(_firstDayInView, ThisItem.Value) = Today(), ColorFade(Subcircle1.Fill, 0.67),
                /*The day is outside the range of the currently selected month*/
                Abs(Self.Text - ThisItem.Value) > 10,RGBA(200, 200, 200, 0.3), RGBA(0, 0, 0, 0))
          FocusedBorderColor: =Self.Color
          FocusedBorderThickness: =2
          Height: =MonthDayGallery1.TemplateHeight
          Size: =17 * MonthDayGallery1.TemplateWidth / 91
          TabIndex: =0
          Visible: |-
            =/*This item is in a row containing no days of the visible month. It is in the row after the row where the last day of the month occurs*/
             !(DateAdd(_firstDayInView,ThisItem.Value, TimeUnit.Days) - Weekday(DateAdd(_firstDayInView,ThisItem.Value, TimeUnit.Days)) + 1 > _lastDayOfMonth)
          Width: =MonthDayGallery1.TemplateWidth
          Wrap: =false
    - Subcircle1:
        Control: Circle
        Properties:
          OnSelect: =Select(Parent)
          Height: =3 * Title2.Size
          Visible: =And(DateAdd(_firstDayInView, ThisItem.Value) = _dateSelected, Title2.Visible)
          Width: =Self.Height
          X: =MonthDayGallery1.TemplateWidth/2 - Self.Width/2
          Y: =MonthDayGallery1.TemplateHeight / 2 - Self.Height / 2
    - Circle1:
        Control: Circle
        Properties:
          OnSelect: =Select(Parent)
          Height: =Self.Width
          Visible: |-
            =/*Visible if calendar events are found on this day*/
            CountRows(Filter(MyCalendarEvents, DateValue(Text(Start)) = DateAdd(_firstDayInView,ThisItem.Value, TimeUnit.Days))) > 0 && !Subcircle1.Visible && Title2.Visible
          Width: =6.5
          X: =MonthDayGallery1.TemplateWidth / 2 - Self.Width / 2
          Y: =MonthDayGallery1.TemplateHeight * (0.75)
- WeekdayGallery1:
    Control: Gallery
    Variant: WeekdayGallery
    Properties:
      AccessibleLabel: ="Days of the week"
      Items: =Calendar.WeekdaysShort()
      Height: =45
      ShowScrollbar: =false
      TemplatePadding: =0
      TemplateSize: =60
      Visible: =_calendarVisible
      Width: =420
      Y: =LblMonthSelected1.Y + LblMonthSelected1.Height + 10
    Children:
    - Title1:
        Control: Label
        Properties:
          OnSelect: =Select(Parent)
          Text: =ThisItem.Value
          Align: =Align.Center
          Height: =WeekdayGallery1.TemplateHeight
          Size: =17 * WeekdayGallery1.TemplateWidth / 77
          Width: =WeekdayGallery1.TemplateWidth
          Wrap: =false
          X: =WeekdayGallery1.TemplateWidth / 2 - Self.Width / 2
          Y: =WeekdayGallery1.TemplateHeight / 2 - Self.Height / 2
- iconNextMonth1:
    Control: Classic/Icon
    Variant: ChevronRight
    Properties:
      OnSelect: |-
        =/*changes month view to next month*/
        Set(_firstDayOfMonth, DateAdd(_firstDayOfMonth, 1, TimeUnit.Months));
        Set(_firstDayInView, DateAdd(_firstDayOfMonth, -(Weekday(_firstDayOfMonth) - 2 + 1), TimeUnit.Days));
        /*collects calendar events for all days in current month view. Updates _maxDate to prevent duplicate data collection if user returns to this month view*/
        Set(_lastDayOfMonth, DateAdd(DateAdd(_firstDayOfMonth, 1, TimeUnit.Months), -1, TimeUnit.Days));
        If(_lastDayOfMonth > _maxDate, Set(_maxDate, _lastDayOfMonth); Collect(MyCalendarEvents, Office365Outlook.GetEventsCalendarViewV2(_myCalendar.Name, Text(_firstDayOfMonth, DateTimeFormat.UTC), Text(_maxDate, DateTimeFormat.UTC)).value))
      Tooltip: ="View next month"
      Height: =50
      Icon: =Icon.ChevronRight
      PaddingBottom: =7
      PaddingLeft: =7
      PaddingRight: =7
      PaddingTop: =7
      TabIndex: =0
      Visible: =_calendarVisible
      Width: =59
      X: =419 - Self.Width
      Y: =LblMonthSelected1.Y
- iconPrevMonth1:
    Control: Classic/Icon
    Variant: ChevronLeft
    Properties:
      OnSelect: |-
        =/*changes month view to previous month*/
        Set(_firstDayOfMonth, DateAdd(_firstDayOfMonth, -1, TimeUnit.Months));
        Set(_firstDayInView, DateAdd(_firstDayOfMonth, -(Weekday(_firstDayOfMonth) - 2 + 1), TimeUnit.Days));
        Set(_lastDayOfMonth, DateAdd(DateAdd(_firstDayOfMonth, 1, TimeUnit.Months), -1, TimeUnit.Days));
        /*collects calendar events for all days in current month view. Updates _minDate to prevent duplicate data collection if user returns to this month view*/
        If(_minDate > _firstDayOfMonth, Set(_minDate, _firstDayOfMonth); Collect(MyCalendarEvents, Office365Outlook.GetEventsCalendarViewV2(_myCalendar.Name, Text(_minDate, DateTimeFormat.UTC), Text(_lastDayOfMonth, DateTimeFormat.UTC)).value))
      Tooltip: ="View previous month"
      Height: =50
      Icon: =Icon.ChevronLeft
      PaddingBottom: =7
      PaddingLeft: =7
      PaddingRight: =7
      PaddingTop: =7
      TabIndex: =0
      Visible: =_calendarVisible
      Width: =59
      Y: =LblMonthSelected1.Y
- LblMonthSelected1:
    Control: Label
    Properties:
      Text: =Text(_firstDayOfMonth, "mmmm yyyy")
      Align: =Align.Center
      Height: =50
      Size: =18
      Visible: =_calendarVisible
      Width: =419
      Wrap: =false
      Y: =dropdownCalendarSelection1.Y + dropdownCalendarSelection1.Height + 40
---

## History

| Date | Author | Changes |
|------|--------|---------|
| 2026-01-27 | Migration | Initial TOC and history section added |
