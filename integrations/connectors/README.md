---
title: "Connector Patterns"
description: "Power Platform connector usage patterns and best practices"
category: "integrations"
subcategory: "connectors"
tags:
  - connectors
  - office365
  - sharepoint
  - dataverse
  - api
difficulty: intermediate
products:
  - power-apps-canvas
  - power-automate
author: "PowerAppsDarren"
created: 2026-01-27
updated: 2026-01-27
---

# Connector Patterns

## Table of Contents

- [Overview](#overview)
- [Directory Structure](#directory-structure)
- [Available Connectors](#available-connectors)
  - [[Office 365 Outlook](./office365-outlook/)](#office-365-outlookoffice365-outlook)
  - [[Office 365 Users](./office365-users/)](#office-365-usersoffice365-users)
- [Connector Best Practices](#connector-best-practices)
  - [1. Delegation Awareness](#1-delegation-awareness)
  - [2. Error Handling](#2-error-handling)
  - [3. Performance Optimization](#3-performance-optimization)
  - [4. Connection References (ALM)](#4-connection-references-alm)
- [Common Patterns](#common-patterns)
  - [People Picker](#people-picker)
  - [Send Email](#send-email)
  - [Get Manager](#get-manager)
- [Related Resources](#related-resources)

Patterns for working with Power Platform connectors in Power Apps.

## Overview

This folder contains patterns and examples for using various Power Platform connectors. Connectors are pre-built integrations that allow Power Apps to interact with external services and data sources.

## Directory Structure

```
connectors/
├── office365-outlook/    # Email and calendar operations
├── office365-users/      # User profile and directory lookups
└── README.md
```

## Available Connectors

### [Office 365 Outlook](./office365-outlook/)

Email, calendar, and contact operations.

**Common uses:**

- Send emails with attachments
- Read inbox messages
- Manage calendar events
- Access contacts

### [Office 365 Users](./office365-users/)

User profile and organizational data.

**Common uses:**

- People picker implementations
- User profile lookups
- Org chart navigation
- Manager/direct reports queries

## Connector Best Practices

### 1. Delegation Awareness

Understand which operations are delegable:

```powerfx
// Delegable - runs on server
Filter(SharePointList, Status = "Active")

// Non-delegable - limited to 500/2000 records
Filter(SharePointList, Text(ID) = "123")
```

### 2. Error Handling

Always handle potential connector errors:

```powerfx
// Check for errors after connector calls
If(
    !IsBlank(Errors(DataSource)),
    Notify("Error connecting to data source", NotificationType.Error),
    // Success logic
)
```

### 3. Performance Optimization

- Cache frequently-used data in collections
- Use `Concurrent()` for parallel connector calls
- Minimize connector calls in galleries

```powerfx
// Cache user data on app start
ClearCollect(
    colCurrentUser,
    Office365Users.MyProfile()
);

// Then reference the cached data
colCurrentUser.DisplayName
```

### 4. Connection References (ALM)

For solutions deployed across environments:

```powerfx
// Use environment variables for connection-specific values
LookUp(
    'Environment Variable Values',
    'Environment Variable Definition'.'Schema Name' = "prefix_SharePointSiteUrl"
).Value
```

## Common Patterns

### People Picker

```powerfx
// Search for users
Office365Users.SearchUser({searchTerm: txtSearch.Text, top: 15})
```

### Send Email

```powerfx
// Send email with Office365Outlook
Office365Outlook.SendEmailV2(
    txtTo.Text,
    txtSubject.Text,
    txtBody.Text
)
```

### Get Manager

```powerfx
// Get current user's manager
Office365Users.Manager(User().Email)
```

## Related Resources

- [Power Apps Connectors List](https://learn.microsoft.com/en-us/connectors/connector-reference/connector-reference-powerapps-connectors)
- [Custom Connectors](../../custom-connectors-apis/)
- [Power Automate Integration](../power-automate/)
- [Integrations Overview](../README.md)

---

## History

| Date       | Author      | Changes                          |
|------------|-------------|----------------------------------|
| 2026-01-27 | Claude      | Created initial README           |
