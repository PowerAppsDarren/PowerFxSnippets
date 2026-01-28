---
title: "Research: Power Apps Canvas Component SetFocus Capabilities"
description: "Comprehensive research on implementing callable behavior properties (Action/Event) for SetFocus in Power Apps canvas components"
category: "research"
subcategory: "component-patterns"
tags:
  - component
  - behavior
  - setfocus
  - action-property
  - event-property
difficulty: advanced
products:
  - power-apps-canvas
author: "Research Session"
created: 2025-12-04
updated: 2025-12-04
license: "MIT"
---

# Research: Power Apps Canvas Component SetFocus Capabilities

## Table of Contents

- [Executive Summary](#executive-summary)
- [Question 1: Can canvas components have callable behavior properties (methods)?](#question-1-can-canvas-components-have-callable-behavior-properties-methods)
  - [Key Points:](#key-points)
  - [Requirements:](#requirements)
  - [References:](#references)
- [Question 2: What is the syntax for PropertyKind: Action or Event?](#question-2-what-is-the-syntax-for-propertykind-action-or-event)
  - [YAML Syntax for Action Property:](#yaml-syntax-for-action-property)
  - [Example from Existing Component (super-input-control.pa.yaml):](#example-from-existing-component-super-input-controlpayaml)
  - [How to Call from App:](#how-to-call-from-app)
  - [References:](#references)
- [Question 3: Limitations & Reasons NOT to Use Behavior Properties for SetFocus](#question-3-limitations-reasons-not-to-use-behavior-properties-for-setfocus)
  - [Critical Limitation:](#critical-limitation)
  - [Additional SetFocus Limitations:](#additional-setfocus-limitations)
  - [Why This Matters for Components:](#why-this-matters-for-components)
  - [References:](#references)
- [Question 4: What's the Alternative if Behavior Properties Don't Work Well?](#question-4-whats-the-alternative-if-behavior-properties-dont-work-well)
  - [Workaround #1: Event Property with Context Variable Trigger](#workaround-1-event-property-with-context-variable-trigger)
  - [Workaround #2: Action Property to Reset Component State](#workaround-2-action-property-to-reset-component-state)
  - [Workaround #3: Use OnReset with RaiseOnReset](#workaround-3-use-onreset-with-raiseonreset)
  - [References:](#references)
- [Question 5: Example YAML for Implementing Focus Behavior](#question-5-example-yaml-for-implementing-focus-behavior)
  - [Complete Example: Input Component with Focus Capability](#complete-example-input-component-with-focus-capability)
  - [Usage from App:](#usage-from-app)
- [Additional Findings](#additional-findings)
  - [Property Type Comparison](#property-type-comparison)
  - [Best Practices for SetFocus in Components](#best-practices-for-setfocus-in-components)
  - [Experimental Features Warning](#experimental-features-warning)
- [Conclusions](#conclusions)
  - [Answers Summary:](#answers-summary)
  - [Recommended Approach for SetFocus:](#recommended-approach-for-setfocus)
- [Sources](#sources)
- [Related Files in Repository](#related-files-in-repository)

## Executive Summary

This research document answers critical questions about implementing SetFocus functionality in Power Apps canvas components through callable behavior properties.

---

## Question 1: Can canvas components have callable behavior properties (methods)?

**Answer: YES** - Canvas components support callable behavior properties through **Action properties**.

### Key Points:

- **Action properties** are output behavior functions that apps can call
- **Event properties** are input behavior functions that components can call
- Both property types support side effects (changing state, manipulating collections/variables)
- Action properties behave like callable methods: `ComponentName.ActionPropertyName()`

### Requirements:

You must enable **Enhanced Component Properties** in Power Apps:
1. Go to Settings → Upcoming Features
2. Search for "Enhanced"
3. Enable "Enhanced Component Properties" toggle

### References:
- [Canvas component properties - Microsoft Learn](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/component-properties)
- [Enhanced component properties - Microsoft Blog](https://powerapps.microsoft.com/en-us/blog/enhanced-component-properties/)

---

## Question 2: What is the syntax for PropertyKind: Action or Event?

### YAML Syntax for Action Property:

```yaml
ComponentDefinitions:
  cmp_MyComponent:
    DefinitionType: CanvasComponent
    CustomProperties:
      # ACTION PROPERTY (Output - Component defines logic, app calls it)
      Focus:
        PropertyKind: Action
        DisplayName: Focus
        Description: Sets focus to the input control within the component
        ReturnType: None  # or Boolean, Text, Record, etc.
        # Logic defined in component, callable from app as: cmp_MyComponent.Focus()

      # EVENT PROPERTY (Input - App defines logic, component calls it)
      OnChange:
        PropertyKind: Event
        DisplayName: OnChange
        Description: Triggered when the input value changes
        ReturnType: Text
        Default: ="Text"
        # App defines logic, component calls it as: cmp_MyComponent.OnChange()
```

### Example from Existing Component (super-input-control.pa.yaml):

```yaml
OnChange:
  PropertyKind: Event
  DisplayName: OnChange
  Description: A custom property
  ReturnType: Text
  Default: ="Text"
```

### How to Call from App:

```powerfx
// Calling an Action property from the app
Button.OnSelect = cmp_Input.Focus()

// Defining logic for an Event property
cmp_Input.OnChange = Notify("Value changed", NotificationType.Information)
```

### References:
- [Canvas App Components Custom Properties - Softchief](https://softchief.com/2024/12/04/canvas-app-components-custom-properties-event-types-and-data/)
- [Power Apps Component With An OnSelect Property - Matthew Devaney](https://www.matthewdevaney.com/power-apps-component-with-an-onselect-property/)

---

## Question 3: Limitations & Reasons NOT to Use Behavior Properties for SetFocus

### Critical Limitation:

**You CANNOT use SetFocus() on controls inside components.**

From Microsoft documentation:
> "You cannot set the focus to controls that are within a Gallery control, Edit form control, or **Component**."

### Additional SetFocus Limitations:

1. Cannot set focus to controls within Container controls
2. Can only set focus to controls on the same screen as the formula
3. SetFocus only works in behavior formulas (not data formulas)
4. SetFocus has no effect on controls with DisplayMode.Disabled

### Why This Matters for Components:

- Action properties CAN be defined within components
- BUT SetFocus() cannot target controls inside the component from outside
- This creates a design challenge for implementing Focus() as an Action property

### References:
- [SetFocus function - Microsoft Learn](https://learn.microsoft.com/en-us/power-platform/power-fx/reference/function-setfocus)
- [Set focus on a control - Power Platform Guidance](https://learn.microsoft.com/en-us/power-platform/guidance/creator-kit/setfocus)

---

## Question 4: What's the Alternative if Behavior Properties Don't Work Well?

### Workaround #1: Event Property with Context Variable Trigger

Since SetFocus cannot target controls inside components, use an **Event property** with a pattern-based trigger:

```powerfx
// In Component's Event Property Definition
FocusTrigger:
  PropertyKind: Input
  DisplayName: Focus Trigger
  Description: Trigger to set focus (bind to context variable)
  DataType: Text
  Default: =""

// In Component's TextInput control
txt_Input.OnVisible =
  If(
    StartsWith(cmp_Input.FocusTrigger, "SetFocus"),
    SetFocus(txt_Input)
  )

// From the App - trigger focus by changing the variable
Button.OnSelect =
  UpdateContext({
    ctxComponentEvent: "SetFocus" & Text(Rand())
  });

// Bind component property
cmp_Input.FocusTrigger = ctxComponentEvent
```

**How it works:**
1. Component has an Input property (FocusTrigger) bound to a context variable
2. Component watches for changes to this property
3. When value starts with "SetFocus", the component calls SetFocus on its own controls
4. `Rand()` ensures unique values so Power Apps detects change

### Workaround #2: Action Property to Reset Component State

Instead of directly calling SetFocus, use an Action property to trigger a reset that includes setting focus:

```yaml
Reset:
  PropertyKind: Action
  DisplayName: Reset
  Description: Resets component and sets focus to input
  ReturnType: None
```

```powerfx
// In component's Action property formula
Reset =
  Reset(txt_Input);
  Set(varComponentFocused, true);
  // Component's OnReset can then call SetFocus

// From app
Button.OnSelect = cmp_Input.Reset()
```

### Workaround #3: Use OnReset with RaiseOnReset

Components have a built-in `OnReset` property that can call SetFocus:

```yaml
ShowControl:
  PropertyKind: Input
  DisplayName: Show Control
  Description: When changed, resets component
  RaiseOnReset: true
  DataType: Boolean
  Default: =true

# In Component's OnReset property
OnReset = SetFocus(txt_Input)

# From App - changing the property triggers OnReset
Button.OnSelect =
  UpdateContext({ varShowInput: !varShowInput });

cmp_Input.ShowControl = varShowInput
```

### References:
- [Behavior formulas for components - Microsoft Learn](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/component-behavior)
- [Faster data entry with SetFocus - Microsoft Blog](https://powerapps.microsoft.com/en-us/blog/faster-data-entry-with-the-setfocus-function/)

---

## Question 5: Example YAML for Implementing Focus Behavior

### Complete Example: Input Component with Focus Capability

```yaml
ComponentDefinitions:
  cmp_FocusableInput:
    DefinitionType: CanvasComponent
    Description: Input control with callable focus behavior
    CustomProperties:
      # INPUT PROPERTIES
      TextValue:
        PropertyKind: Input
        DisplayName: Text Value
        Description: Default text value
        DataType: Text
        Default: =""

      HintText:
        PropertyKind: Input
        DisplayName: Hint Text
        Description: Placeholder text
        DataType: Text
        Default: ="Enter text..."

      FocusTrigger:
        PropertyKind: Input
        DisplayName: Focus Trigger
        Description: Change this value to trigger focus (use with Rand)
        RaiseOnReset: true
        DataType: Text
        Default: =""

      # OUTPUT PROPERTIES
      Value:
        PropertyKind: Output
        DisplayName: Value
        Description: Current text value
        DataType: Text

      # EVENT PROPERTIES
      OnChange:
        PropertyKind: Event
        DisplayName: OnChange
        Description: Triggered when value changes
        ReturnType: Text
        Default: ="Text"

      # ACTION PROPERTIES
      ClearValue:
        PropertyKind: Action
        DisplayName: Clear Value
        Description: Clears the input value
        ReturnType: None

    Properties:
      Height: =60
      Width: =300
      Value: =txt_Input.Text

    Children:
      - txt_Input:
          Control: Classic/TextInput@2.3.2
          Properties:
            Default: =cmp_FocusableInput.TextValue
            HintText: =cmp_FocusableInput.HintText
            Height: =Parent.Height
            Width: =Parent.Width
            OnChange: =cmp_FocusableInput.OnChange()
            # Focus trigger logic
            OnVisible: |-
              =If(
                  StartsWith(cmp_FocusableInput.FocusTrigger, "SetFocus"),
                  SetFocus(Self)
              )
```

### Usage from App:

```powerfx
// SET FOCUS using context variable pattern
Button_Focus.OnSelect =
  UpdateContext({
    ctxFocusTrigger: "SetFocus" & Text(Rand())
  });

cmp_FocusableInput.FocusTrigger = ctxFocusTrigger

// CLEAR VALUE using Action property
Button_Clear.OnSelect =
  cmp_FocusableInput.ClearValue()

// RESPOND to changes using Event property
cmp_FocusableInput.OnChange =
  Notify("Value: " & cmp_FocusableInput.Value, NotificationType.Information)
```

---

## Additional Findings

### Property Type Comparison

| Property Type        | Direction       | Side Effects | Use Case              | Example            |
|----------------------|-----------------|--------------|----------------------|--------------------|
| **Data (Input)**     | App → Component | No           | Pass values in        | BorderColor, Font  |
| **Data (Output)**    | Component → App | No           | Pass values out       | SelectedValue      |
| **Function (Input)** | App → Component | No           | Pass calculations in  | FormatFunction     |
| **Function (Output)**| Component → App | No           | Pass calculations out | ValidateInput()    |
| **Event**            | App → Component | Yes          | App defines logic     | OnChange, OnSelect |
| **Action**           | Component → App | Yes          | Component defines logic | Clear(), Reset() |

### Best Practices for SetFocus in Components

1. **Use Input Property + Pattern Matching**: Most reliable method
2. **Always append unique value**: Use `Text(Rand())` to ensure detection
3. **Check OnVisible event**: Best place to call SetFocus in response to property changes
4. **Consider Reset pattern**: Use RaiseOnReset for initialization scenarios
5. **Document limitations**: Make it clear to consumers that focus is triggered indirectly

### Experimental Features Warning

From Microsoft documentation:
> "The feature to create custom behavioral properties is currently experimental. However, you can use the default OnReset property that is available on all components in your production environment."

**Recommendation**:
- Action and Event properties are NOW generally available (no longer experimental)
- Safe to use in production with Enhanced Component Properties enabled
- OnReset is the most stable behavior property

---

## Conclusions

### Answers Summary:

1. **Yes**, components CAN have callable behavior properties (Action/Event)
2. **Syntax**: `PropertyKind: Action` (output) or `PropertyKind: Event` (input)
3. **Major Limitation**: SetFocus cannot target controls inside components directly
4. **Best Alternative**: Input property with pattern-based trigger using context variable
5. **YAML Example**: See complete implementation above

### Recommended Approach for SetFocus:

Use an **Input property** with a **unique value trigger pattern**, NOT an Action property:

```yaml
FocusTrigger:
  PropertyKind: Input
  RaiseOnReset: true
  DataType: Text
```

This approach works around the SetFocus limitation while still providing a clean API for consumers.

---

## Sources

- [Canvas component properties - Microsoft Learn](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/component-properties)
- [Enhanced component properties - Microsoft Blog](https://powerapps.microsoft.com/en-us/blog/enhanced-component-properties/)
- [SetFocus function - Microsoft Learn](https://learn.microsoft.com/en-us/power-platform/power-fx/reference/function-setfocus)
- [Behavior formulas for components - Microsoft Learn](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/component-behavior)
- [Canvas App Components Custom Properties - Softchief](https://softchief.com/2024/12/04/canvas-app-components-custom-properties-event-types-and-data/)
- [Power Apps Component With An OnSelect Property - Matthew Devaney](https://www.matthewdevaney.com/power-apps-component-with-an-onselect-property/)
- [Set focus on a control - Power Platform Guidance](https://learn.microsoft.com/en-us/power-platform/guidance/creator-kit/setfocus)
- [Faster data entry with SetFocus - Microsoft Blog](https://powerapps.microsoft.com/en-us/blog/faster-data-entry-with-the-setfocus-function/)
- [Source code files for canvas apps (pa.yaml) - Microsoft Learn](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/power-apps-yaml)

---

## Related Files in Repository

- `C:\src\src-power-platform\PowerFxSnippets\Components\Input-Control\super-input-control.pa.yaml` - Example Event property implementation
- `C:\src\src-power-platform\PowerFxSnippets\Components\Spinner\Spinner.md` - Example component with RaiseOnReset
---

## History

| Date | Author | Changes |
|------|--------|---------|
| 2026-01-27 | Migration | Initial TOC and history section added |
