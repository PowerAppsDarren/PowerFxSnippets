---
title: "Power Automate Integration"
description: "Patterns for integrating Power Apps with Power Automate flows"
category: "integrations"
subcategory: "power-automate"
tags:
  - power-automate
  - flows
  - automation
  - triggers
  - actions
difficulty: intermediate
products:
  - power-apps-canvas
  - power-automate
author: "PowerAppsDarren"
created: 2026-01-27
updated: 2026-01-27
---

# Power Automate Integration

Patterns for integrating Power Apps with Power Automate flows.

## Overview

This folder contains patterns for calling Power Automate flows from Power Apps, handling responses, and implementing common automation scenarios.

## Directory Structure

```
power-automate/
├── sharepoint/           # SharePoint-specific flow patterns
└── README.md
```

## Flow Integration Types

### Instant Flows (Triggered from Power Apps)

Flows that run when explicitly called from Power Apps.

```powerfx
// Call a flow with parameters
'FlowName'.Run(
    param1,
    param2,
    param3
)
```

### Scheduled Flows

Background automation that runs on a schedule.

### Automated Flows

Flows triggered by events (new item created, modified, etc.).

## Calling Flows from Power Apps

### Basic Flow Call

```powerfx
// Simple flow call
'Send Approval Email'.Run(
    txtRecipient.Text,
    txtSubject.Text,
    txtBody.Text
)
```

### With Response Handling

```powerfx
// Store flow response
Set(
    varFlowResponse,
    'Process Data'.Run(
        galSelected.Selected.ID,
        User().Email
    )
);

// Use response data
If(
    varFlowResponse.success,
    Notify("Success: " & varFlowResponse.message, NotificationType.Success),
    Notify("Error: " & varFlowResponse.error, NotificationType.Error)
)
```

### With Loading State

```powerfx
// Show loading indicator
UpdateContext({isProcessing: true});

// Call flow
Set(
    varResult,
    'Long Running Process'.Run(txtInput.Text)
);

// Hide loading indicator
UpdateContext({isProcessing: false});

// Handle result
If(
    varResult.success,
    Navigate('Success Screen', ScreenTransition.Fade)
)
```

## Common Patterns

### SharePoint Document Generation

See [sharepoint/](./sharepoint/) for patterns including:

- Document creation from templates
- PDF generation
- File management

### Approval Workflows

```powerfx
// Start approval
'Start Approval'.Run(
    galRequests.Selected.ID,
    galRequests.Selected.Title,
    txtApproverEmail.Text
)
```

### Data Processing

For operations too complex for Power Fx:

```powerfx
// Complex calculations in flow
Set(
    varCalculationResult,
    'Complex Calculation Flow'.Run(
        JSON(colInputData, JSONFormat.IndentFour)
    )
)
```

### Email with Attachments

```powerfx
// Send email with attachment via flow
'Send Email With Attachment'.Run(
    txtTo.Text,
    txtSubject.Text,
    txtBody.Text,
    galAttachments.Selected.Url
)
```

## Best Practices

### 1. Error Handling

Always handle flow errors gracefully:

```powerfx
// Wrap in IfError
IfError(
    'MyFlow'.Run(param1),
    Notify("Flow failed: " & FirstError.Message, NotificationType.Error);
    false,
    true
)
```

### 2. Response Schema

Design flows to return consistent response schemas:

```json
{
    "success": true,
    "message": "Operation completed",
    "data": { },
    "error": null
}
```

### 3. Performance

- Use flows for complex operations, not simple data reads
- Consider async patterns for long-running flows
- Minimize flow calls inside loops

### 4. Security

- Use connection references for deployment
- Implement proper error messages (don't expose internal errors)
- Validate inputs before calling flows

## Related Resources

- [Power Automate Documentation](https://learn.microsoft.com/en-us/power-automate/)
- [Connector Patterns](../connectors/)
- [Integrations Overview](../README.md)

---

## History

| Date       | Author      | Changes                          |
|------------|-------------|----------------------------------|
| 2026-01-27 | Claude      | Created initial README           |
