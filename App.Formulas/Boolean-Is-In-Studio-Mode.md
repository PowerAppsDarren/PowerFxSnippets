---
title: "Are We in Studio Mode?"
description: "Determine if the app is running in Studio Mode (editing mode) to show/hide elements."
category: "App.Formulas"
tags: ["studio-mode", "environment", "debug"]
difficulty: beginner
author: "Matthew Devaney"
created: 2025-11-19
updated: 2025-11-19
license: "MIT"
---

# Are We in Studio Mode?

This is a helpful canvas Power Apps code snippet that will help you determine if you are in Studio Mode. What is Studio Mode? Studio Mode is the mode where you are editing the Power App. This is helpful when you want to show or hide certain elements when you are in Studio Mode.

Credit: [Matthew Devaney](https://www.linkedin.com/feed/update/urn:li:activity:7244677047485136896/)


```PowerFx
fxIsInStudioMode = StartsWith(Host.Version, "PowerApps-Studio");
```
