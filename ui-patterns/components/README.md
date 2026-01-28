---
title: "Component Patterns"
description: "Reusable canvas components and PCF code components for Power Apps"
category: "ui-patterns"
subcategory: "components"
tags:
  - components
  - custom-components
  - pcf
  - code-components
  - reusable
difficulty: intermediate
products:
  - power-apps-canvas
  - power-apps-model-driven
author: "PowerAppsDarren"
created: 2026-01-27
updated: 2026-01-27
---

# Component Patterns

Reusable component patterns for Power Apps development.

## Overview

This folder contains patterns for creating and using reusable components in Power Apps. Components allow you to build once and reuse across multiple screens and apps, improving consistency and reducing maintenance.

## Directory Structure

```
components/
├── custom-components/    # Canvas app components (Power Fx)
└── code-components/      # PCF components (TypeScript/React)
```

## Component Types

### Custom Components (Canvas)

Built entirely with Power Fx within Power Apps Studio. Best for:

- UI patterns that need to be reused across screens
- Input controls with custom validation
- Display components with specific layouts
- Components that non-developers should be able to modify

### Code Components (PCF)

Built with TypeScript and optionally React. Best for:

- Complex visualizations
- Integration with external libraries
- Performance-critical components
- Features not possible with standard controls

## Creating Canvas Components

### Basic Component Structure

1. **Properties** - Define input/output properties
2. **UI Layout** - Design the component interface
3. **Behavior** - Implement component logic

### Component Property Types

| Type | Use Case |
|------|----------|
| Input | Pass data into the component |
| Output | Return data from the component |
| Event | Trigger actions in the parent |
| Data | Pass tables/records |

### Example: Button with Loading State

```powerfx
// Component Properties:
// - Text (Input, Text)
// - IsLoading (Input, Boolean)
// - OnSelect (Event)
// - Disabled (Input, Boolean)

// Button OnSelect:
If(
    !IsLoading && !Disabled,
    Select(Parent)  // Triggers the component's OnSelect
)

// Button Text:
If(IsLoading, "Loading...", Text)

// Button DisplayMode:
If(IsLoading || Disabled, DisplayMode.Disabled, DisplayMode.Edit)
```

## Best Practices

### Component Design

- Keep components focused on a single purpose
- Use clear, descriptive property names
- Provide sensible default values
- Document all properties and their expected values

### Performance

- Minimize the number of controls inside components
- Avoid complex calculations in frequently-updated properties
- Use `With()` for repeated calculations

### Reusability

- Design for flexibility with input properties
- Don't hardcode data sources or colors
- Make styling customizable through properties

## Folder Contents

### [custom-components/](./custom-components/)

Canvas app component implementations including:

- Input controls with validation
- Navigation components
- Display patterns
- Form components

### [code-components/](./code-components/)

PCF component patterns and implementations (advanced).

## Related Resources

- [Power Apps Component Framework](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/overview)
- [Create Canvas App Components](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/create-component)
- [UI Patterns Overview](../README.md)

---

## History

| Date       | Author      | Changes                          |
|------------|-------------|----------------------------------|
| 2026-01-27 | Claude      | Created initial README           |
