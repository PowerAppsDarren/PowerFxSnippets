---
title: "Menu Patterns"
description: "Navigation menus, hamburger menus, and menu item patterns for Power Apps"
category: "ui-patterns"
subcategory: "menus"
tags:
  - menus
  - navigation
  - hamburger
  - sidebar
  - tabs
difficulty: intermediate
products:
  - power-apps-canvas
author: "PowerAppsDarren"
created: 2026-01-27
updated: 2026-01-27
---

# Menu Patterns

Navigation and menu patterns for Power Apps canvas applications.

## Overview

This folder contains patterns for implementing various menu and navigation systems in Power Apps. Good navigation is essential for user experience, especially in apps with multiple screens.

## Contents

| File | Description |
|------|-------------|
| [Menu-Items-Schema.md](./Menu-Items-Schema.md) | Schema for menu item data structures |

## Menu Types

### Side Navigation (Sidebar)

Vertical menu typically on the left side of the screen.

```powerfx
// Menu items collection
ClearCollect(
    colMenuItems,
    {
        ID: 1,
        Title: "Home",
        Icon: Icon.Home,
        Screen: 'Home Screen',
        Order: 1
    },
    {
        ID: 2,
        Title: "Dashboard",
        Icon: Icon.LineChart,
        Screen: 'Dashboard Screen',
        Order: 2
    },
    {
        ID: 3,
        Title: "Settings",
        Icon: Icon.Settings,
        Screen: 'Settings Screen',
        Order: 3
    }
)
```

### Top Navigation (Navbar)

Horizontal menu at the top of the screen.

### Tab Navigation

Tab-style navigation for switching between views on a single screen.

### Hamburger Menu

Collapsible menu that expands/collapses on demand.

```powerfx
// Toggle menu visibility
UpdateContext({showMenu: !showMenu})

// Menu container width (animated effect)
Width: =If(showMenu, 250, 50)
```

## Menu Item Structure

A well-designed menu item typically includes:

| Property | Type | Description |
|----------|------|-------------|
| ID | Number | Unique identifier |
| Title | Text | Display text |
| Icon | Icon/Text | Visual icon |
| Screen | Screen | Target screen |
| Order | Number | Sort order |
| Visible | Boolean | Show/hide condition |
| Badge | Text | Notification count |
| Children | Table | Sub-menu items |

## Navigation Patterns

### Basic Navigation

```powerfx
// In menu item OnSelect
Navigate(ThisItem.Screen, ScreenTransition.Fade)
```

### With Parameters

```powerfx
// Pass context to target screen
Navigate(
    ThisItem.Screen,
    ScreenTransition.Fade,
    {selectedCategory: ThisItem.ID}
)
```

### Highlight Active Item

```powerfx
// Menu item Fill property
Fill: =If(
    App.ActiveScreen = ThisItem.Screen,
    fxTheme.PrimaryLight,
    Transparent
)
```

## Best Practices

1. **Consistency** - Use the same menu across all screens
2. **Clear labels** - Use descriptive, action-oriented text
3. **Visual hierarchy** - Group related items together
4. **Active state** - Clearly indicate the current location
5. **Accessibility** - Ensure keyboard navigation works
6. **Mobile-friendly** - Consider touch targets and responsive design

## Related Resources

- [UI Patterns Overview](../README.md)
- [Dialog Patterns](../dialogs/README.md)
- [App Navigation](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/add-screen-context-variables)

---

## History

| Date       | Author      | Changes                          |
|------------|-------------|----------------------------------|
| 2026-01-27 | Claude      | Enhanced README with patterns    |
