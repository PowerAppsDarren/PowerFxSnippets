---
title: "User Defined Types Syntax"
description: "Examples of defining custom types (records and collections) in Power Fx."
category: "App.Formulas"
tags: ["types", "udt", "syntax", "data-structure"]
difficulty: intermediate
author: "Darren Neese"
created: 2025-11-19
updated: 2025-11-19
license: "MIT"
---

# User Defined Types

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

# Parting Thoughts

### Free Community & Course Materials

🆓 Get access to our [free community and resources](https://tinyurl.com/DarrensStuffFree) ⬅️

### Support

I hope you have found this helpful. If you need any help with the Power Platform, don't hesitate to message us from [Our Website](https://superpowerlabs.co)

### Disclaimer

THIS CODE IS PROVIDED **AS IS WITHOUT WARRANTY OF ANY KIND**, EITHER EXPRESS OR IMPLIED, INCLUDING ANY IMPLIED WARRANTIES OF FITNESS FOR A PARTICULAR PURPOSE, MERCHANTABILITY, OR NON-INFRINGEMENT.
