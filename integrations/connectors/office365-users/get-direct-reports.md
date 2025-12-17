---
title: "Get Direct Reports"
description: "Retrieve direct reports for the current user using Office365Users connector."
category: "integrations"
subcategory: "office365-users"
tags: ["office365", "users", "direct-reports", "hierarchy"]
difficulty: beginner
products:
  - power-apps-canvas
dependencies:
  - Office365Users
author: "Darren Neese"
created: 2025-11-19
updated: 2025-11-21
license: "MIT"
related: []
---

# Get Direct Reports

Yes, this is a one-line simple method call. 🤔👍

## Step 01 - Add this code to your screen

```JavaScript
Office365Users.DirectReportsV2(User().EntraObjectId).value
```

## Final Considerations

I hope you have found this helpful. If you need any help with the Power Platform, don't hesitate to email us at [support@superpowerlabs.co](support@superpowerlabs.co).
