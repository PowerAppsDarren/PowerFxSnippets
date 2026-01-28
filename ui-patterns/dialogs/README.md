---
title: "Dialog Patterns"
description: "Modal dialogs, confirmation prompts, and popup patterns for Power Apps"
category: "ui-patterns"
subcategory: "dialogs"
tags:
  - dialogs
  - modals
  - popups
  - confirmations
  - overlays
difficulty: intermediate
products:
  - power-apps-canvas
author: "PowerAppsDarren"
created: 2026-01-27
updated: 2026-01-27
---

# Dialog Patterns

Reusable dialog and modal patterns for Power Apps canvas applications.

## Overview

This folder contains patterns for implementing dialogs, modals, and popup interfaces in Power Apps. Dialogs are essential for user confirmations, data entry forms, alerts, and contextual information display.

## Contents

| File | Description |
|------|-------------|
| [Dialogs.md](./Dialogs.md) | Introduction to dialog patterns |

## Common Dialog Types

### Confirmation Dialogs

Used when actions require user confirmation (delete, submit, cancel changes).

```powerfx
// Show confirmation dialog
UpdateContext({showConfirmDialog: true, pendingAction: "delete"});

// In dialog's Confirm button:
If(
    pendingAction = "delete",
    Remove(DataSource, ThisItem);
    UpdateContext({showConfirmDialog: false})
)
```

### Information Dialogs

Display important information or alerts to users.

### Input Dialogs

Collect user input in a focused, modal context.

## Implementation Pattern

A typical dialog implementation includes:

1. **Overlay Container** - Semi-transparent background that blocks interaction
2. **Dialog Container** - Centered content area with the dialog UI
3. **Close Mechanism** - Button or background click to dismiss
4. **Focus Management** - Proper tab order within the dialog

### Basic Dialog Structure

```yaml
# Overlay (semi-transparent background)
Container_Overlay:
  Control: GroupContainer
  Properties:
    Visible: =varShowDialog
    Fill: =RGBA(0, 0, 0, 0.5)
    X: =0
    Y: =0
    Width: =App.Width
    Height: =App.Height

# Dialog Content
Container_Dialog:
  Control: GroupContainer
  Properties:
    Visible: =varShowDialog
    X: =(App.Width - Self.Width) / 2
    Y: =(App.Height - Self.Height) / 2
    Width: =400
    Height: =300
    Fill: =Color.White
```

## Best Practices

- Always provide a way to close the dialog (X button, Cancel, or click outside)
- Use consistent styling across all dialogs in your app
- Keep dialog content focused and minimal
- Consider mobile responsiveness
- Use appropriate transitions for better UX

## Related Resources

- [UI Patterns Overview](../README.md)
- [Theming Patterns](../theming/README.md)
- [Menu Patterns](../menus/README.md)

---

## History

| Date       | Author      | Changes                          |
|------------|-------------|----------------------------------|
| 2026-01-27 | Claude      | Created initial README           |
