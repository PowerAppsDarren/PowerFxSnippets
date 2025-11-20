
---
title: "Office365Users Connector Snippets Overview"
description: "Overview and index of Office365Users connector snippets for Power Apps user management"
category: "integrations"
subcategory: "office365-users"
tags:
  - office365
  - users
  - connector
  - overview
difficulty: beginner
products:
  - power-apps-canvas
dependencies: []
author: "PowerFxSnippets Community"
created: 2025-11-20
updated: 2025-11-20
license: "MIT"
related: []
---

# Office365Users Snippets

This folder contains code snippets related to the Office365Users connector in Power Apps.
All snippets now include metadata for better discoverability and tooling support.

## Available Snippets

## You May be interested in the following:

- [People Picker Combobox](PeoplePIckerCombobox.md)
- [Automatically Add a User](auto-add-user.md)
- [Get Manager Rollup](get-manager-rollup.md)
- [Get Direct Reports](get-direct-reports.md)
- [Display All Profile Fields](display-all-fields.md)

# Create Database Tables

You may want to create data sources to hold the org chart data. This will keep you from having to use the Office365Users connector to make many calls each time you need data. This becomes evident in an example where you have a gallery control listing all the staff in a department or the whole organization. Can you imagine how inefficient it would be to call methods on this connector for each row?

[Sample ERD hosted in DrawSQL ⬇️](https://drawsql.app/teams/neeseus/diagrams/org-chart-profile-data)

![Screenshot: ERD](drawSQL.png)
