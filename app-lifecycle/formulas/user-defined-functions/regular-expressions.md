---
title: "Regular Expressions Collection"
description: "A collection of common regular expressions for validation (email, phone, SSN, etc.) with a UDF lookup function."
category: "app-lifecycle"
subcategory: "formulas"
tags:
  - regex
  - validation
  - patterns
  - input
  - udf
difficulty: intermediate
products:
  - power-apps-canvas
author: "Darren Neese"
created: 2025-11-19
updated: 2025-11-19
license: "MIT"
---

# Regular Expressions

Here's an easy way to implement a set of pre-defined regular expressions in your Power Apps application. This can be useful for validating user input, such as email addresses, phone numbers, and more. You can add more regular expressions to the `fxRegExStrings` table as needed.

## Add This to Your Application

```PowerFx
    fxGetRegEx(RegExName:Text):Text = LookUp(
        fxRegExStrings, 
        Name = RegExName, 
        Expression
    );

    fxRegExStrings = [
        {
            Name: "Numeric",
            Expression: "^\d+(.\d+)?$"
        }, 
        {
            Name: "Email",
            Expression: "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}$"
        },
        {
            Name: "Phone Number (USA)",
            Expression: "^?([0−9]3)?([0−9]3)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$"
        },
        {
            Name: "Phone Number (International)",
            Expression: "^\+(?:[0-9] ?){6,14}[0-9]$"
        }, 
        {
            Name: "SSN (USA)",
            Expression: "^(?!000|666|9\d{2})\d{3}-(?!00)\d{2}-(?!0000)\d{4}$"
        }, 
        {
            Name: "URL",
            Expression: "^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$"
        }, 
        /*
            At least one lowercase letter
            At least one uppercase letter
            At least one digit
            At least one special character
            Minimum length of 8 characters
            Maximum length of 32 characters
        */
        {
            Name: "Password",
            Expression: "^(?=.[a-z])(?=.[A-Z])(?=.\d)(?=.[*.!@#$%^&(){}[:;<>,.?/~_+-=|\).{8,32}$"
        },
        {
            Name: "Postal Code (USA)",
            Expression: "^($$d{5}(-\d{4})?|[A-CEGHJ-NPRSTVXY]\d[A-CEGHJ-NPRSTV-Z] ?\d[A-CEGHJ-NPRSTV-Z]\d)$"
        }, 
        {
            Name: "Date",
            Expression: "^(0[1-9]|1[0-2])/(0[1-9]|\d|31)/\d{4}$"
        }, 
        {
            Name: "Time (12 Hour)",
            Expression: "^(0?[1-9]|1[0-2]):[0-5]0-9$"
        }, 
        {
            Name: "Time (24 Hour)",
            Expression: "^([01]\d|2[0-3]):[0-5]\d$"
        }
    ];
```

