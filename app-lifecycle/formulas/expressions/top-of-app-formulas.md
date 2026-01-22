---
title: "Top of App Formulas"
description: "Table of contents and naming guidelines for App.Formulas."
category: "app-architecture"
subcategory: "formulas"
tags:
  - formulas
  - naming
  - guidelines
  - toc
  - expression
difficulty: beginner
products:
  - power-apps-canvas
author: "Darren Neese"
created: 2025-11-19
updated: 2025-11-19
license: "MIT"
---

```PowerFx
    /*
        ==========================================
        🚨 APP.FORMULAS - TABLE OF CONTENTS 🚨

        Author: Darren Neese

        ==========================================

        Naming Guidlines (all the ideas):

            Notes (our guidline is based on these, in order of priority):
                - Adhere to any current standards (practiced in the industry)
                - To be extremely handy while coding (IntelliSense)
                    - Having to wrap names with single quotes is NOT
                - All while retaining a meaningful name
                - Pretty (examples of ugly)
                    - Underscores could be considered ugly
                    - But!!! they are the only special chacter to use
                    -       that won't require 'var MyVar'
                - Personal preference

            All the types of thigs that can be in App.Formulas

                1 - Named Expressions (named formulas)
                    - fx...
                    - fxExp_    ** favorite

                2 - UDF (be sure to them on in settings)
                    - fxUDF_
                    - fxFun_     ** favorite
                    - fxFu

                3 - UDT (be sure to them on in settings)
                    - fxUDT_
                    - fxTyp_     ** favorite

                    Example of primitive types:
                    - (you don't need to do so - already defined)

                    Example of record:
                    - fxTyp_Customer
                    - fxTyp_Customer_Record **maybe too much?

                    Example of table of ...
                    - fxTyp_Customer_Table
                    - fxTyp_Customer_Collection

            I love ProperCasing (personal preference - Darren Neese)

        ==========================================
    */
    fxEnableErrorEmailNotifications = false; // Set to true to enable email notifications for errors (requires Office365Outlook connector)
