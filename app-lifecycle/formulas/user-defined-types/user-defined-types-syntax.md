---
title: "User Defined Types Syntax"
description: "Examples of defining custom types (records and collections) in Power Fx."
category: "app-architecture"
subcategory: "formulas"
tags:
  - types
  - udt
  - syntax
  - data-structure
difficulty: intermediate
products:
  - power-apps-canvas
author: "Darren Neese"
created: 2025-11-19
updated: 2025-11-19
license: "MIT"
---

# User Defined Types

## Table of Contents

- [Add This to Your App.Formulas!](#add-this-to-your-appformulas)

This is a helpful canvas Power Apps code snippet.

## Add This to Your App.Formulas!

```PowerFx

    //
    // Here is an example of a user defined type in PowerFx
    // with basic information about a person.
    //
    fxMyPerson := Type(
        {
            FirstName:          Text,
            LastName:           Text,
            DateOfBirth:        Date,
            Email:              Text,
            Phone:              Text,
            Notes:              Text
        }
    );

    //
    // Here is an example of a user defined type in PowerFx
    // We simply define a type that is a collection of the fxMyPerson type.
    //
    fxPeople := Type(
        [
            fxMyPerson
        ]
    );

```
---

## History

| Date | Author | Changes |
|------|--------|---------|
| 2026-01-27 | Migration | Initial TOC and history section added |
