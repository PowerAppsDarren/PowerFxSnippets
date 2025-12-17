---
title: "User-Defined Types Examples"
description: "Comprehensive examples of User-Defined Types (UDT), Named Formulas, and User-Defined Functions (UDF)."
category: "app-lifecycle"
subcategory: "formulas"
tags:
  - udt
  - udf
  - named-formulas
  - advanced
difficulty: advanced
products:
  - power-apps-canvas
author: "Darren Neese"
created: 2025-11-19
updated: 2025-11-19
license: "MIT"
---

# User-Defined Types

The following code is based on this article here: https://powerplatformlinks.com/CanvasUserDefined

## Named Formulas

Here are some examples of named formulas, below. These are called "named expressions" because they are expressions that are given a name. They are used to define constants that can be used in other formulas. They are defined in the App.Formulas property of the App object.

```PowerFx
    fxLightGray = ColorValue("#e5e5e5");
    fxDefaultBorderRadius = 20;
    fxGetFirstName = First(Split(User().FullName, " " )).Value;
    fxGetLastName = Last(Split(User().FullName, " " )).Value;
```

# User-Defined Functions

```PowerFx
    fxMyDateFormat(DateTimeValue:DateTime):Text = Upper(
        Text(
            DateTimeValue, "dd -- mmm -- yyyy"
        )
    );
```

# User-Defined Types

```PowerFx
    fxPerson := Type(
        {
            FirstName: Text, 
            LastName: Text,
            DateOfBirth: Date,
            Address: fxAddress  // Here is a type defined within a type!
        }
    );

    fxAddress := Type(
        {
            AddressLine1: Text, 
            AddressLine2: Text, 
            City: Text, 
            State: Text,
            Zip: Text
        }
    );
```

And now, putting it all together: 

```PowerFx
    fxGetUsersFromState(FilterState:Text):fxPeople = 
        AddColumns(
            ShowColumns(
                Filter(
                    AppUser, 
                    IsActive = true
                    And State = FilterState
                ), 
                FirstName, 
                LastName
            ), 
            Address,
            LookUp(Address, UserID = ThisRecord.ID)
        );
```

