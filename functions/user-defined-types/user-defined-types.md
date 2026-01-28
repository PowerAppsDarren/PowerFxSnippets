---
title: "User Defined Types Overview"
description: "Introduction to creating and using user-defined types (UDTs) in Power Apps to define custom data structures and improve type safety"
category: "business-logic"
subcategory: "user-defined-types"
tags:
  - user-defined-types
  - udt
  - type-system
  - data-structures
  - type-safety
difficulty: advanced
products:
  - power-apps-canvas
author: "Unknown"
created: 2026-01-26
updated: 2026-01-26
license: "MIT"
---
# User Defined Types

Here are some examples of User Defined Types:

```PowerFx

fxMyPerson := Type({FirstName: Text, LastName: Text});

fxPeople := Type([fxMyPerson]);

```
---

## History

| Date | Author | Changes |
|------|--------|---------|
| 2026-01-27 | Migration | Initial TOC and history section added |
