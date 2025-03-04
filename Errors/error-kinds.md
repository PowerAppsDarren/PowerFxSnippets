# New Topic

This is a helpful canvas Power Apps code snippet.

## Add This to Your Application

```PowerFx
    //
    //
    //
    fxErrorKinds = [
        {
            KindName: "None",
            KindNumber: 0,
            OrdinalPosition: 1,
            Description: "System error. There's no error."
        },
        {
            KindName: "Sync",
            KindNumber: 1,
            OrdinalPosition: 2,
            Description: "An error was reported by the data source. Check the Message column for more information."
        },
        {
            KindName: "MissingRequired",
            KindNumber: 2,
            OrdinalPosition: 3,
            Description: "A required field of a record was missing."
        },
        {
            KindName: "CreatePermission",
            KindNumber: 3,
            OrdinalPosition: 4,
            Description: "The user doesn't have create record permission for the data source. For example, the Collect function was called."
        },
        {
            KindName: "EditPermissions",
            KindNumber: 4,
            OrdinalPosition: 5,
            Description: "The user doesn't have create record permission for the data source. For example, the Patch function was called."
        },
        {
            KindName: "DeletePermissions",
            KindNumber: 5,
            OrdinalPosition: 6,
            Description: "The user doesn't have delete record permission for the data source. For example, the Remove function was called."
        },
        {
            KindName: "Conflict",
            KindNumber: 6,
            OrdinalPosition: 7,
            Description: "The record being updated has already been changed at the source and the conflict needs to be resolved. A common solution is to save any local changes, refresh the record, and reapply the changes."
        },
        {
            KindName: "NotFound",
            KindNumber: 7,
            OrdinalPosition: 8,
            Description: "Record couldn't be found. For example, the record to be modified in the Patch function."
        },
        {
            KindName: "ConstraintViolated",
            KindNumber: 8,
            OrdinalPosition: 9,
            Description: "The record didn't pass a constraint check on the server."
        },
        {
            KindName: "GeneratedValue",
            KindNumber: 9,
            OrdinalPosition: 10,
            Description: "A value was erroneously passed to the server for a field that is automatically calculated by the server."
        },
        {
            KindName: "ReadOnlyValue",
            KindNumber: 10,
            OrdinalPosition: 11,
            Description: "Column is read only and can't be modified."
        },
        {
            KindName: "Validation",
            KindNumber: 11,
            OrdinalPosition: 12,
            Description: "The record didn't pass a validation check."
        },
        {
            KindName: "Unknown",
            KindNumber: 12,
            OrdinalPosition: 13,
            Description: "There was an error, but of an unknown kind."
        },
        {
            KindName: "Div0",
            KindNumber: 13,
            OrdinalPosition: 14,
            Description: "Division by zero."
        },
        {
            KindName: "BadLanguageCode",
            KindNumber: 14,
            OrdinalPosition: 15,
            Description: "An invalid or unrecognized language code was used."
        },
        {
            KindName: "BadRegex",
            KindNumber: 15,
            OrdinalPosition: 16,
            Description: "Invalid regular expression. Check the syntax used with the IsMatch, Match, or MatchAll functions."
        },
        {
            KindName: "InvalidFunctionUsage",
            KindNumber: 16,
            OrdinalPosition: 17,
            Description: "Invalid usage of a function. Often one or more of the arguments to the function is incorrect or used in an invalid way."
        },
        {
            KindName: "FileNotFound",
            KindNumber: 17,
            OrdinalPosition: 18,
            Description: "The SaveData storage couldn't be found."
        },
        {
            KindName: "AnalysisError",
            KindNumber: 18,
            OrdinalPosition: 19,
            Description: "System error. There was a problem with compiler analysis."
        },
        {
            KindName: "ReadPermission",
            KindNumber: 19,
            OrdinalPosition: 20,
            Description: "The user doesn't have read record permission for the data source."
        },
        {
            KindName: "NotSupported",
            KindNumber: 20,
            OrdinalPosition: 21,
            Description: "Operation not supported by this player or device."
        },
        {
            KindName: "InsufficientMemory",
            KindNumber: 21,
            OrdinalPosition: 22,
            Description: "There isn't enough memory or storage on the device for the operation."
        },
        {
            KindName: "QuoteExceeded",
            KindNumber: 22,
            OrdinalPosition: 23,
            Description: "Storage quota exceeded."
        },
        {
            KindName: "Network",
            KindNumber: 23,
            OrdinalPosition: 24,
            Description: "There was a problem with network communications."
        },
        {
            KindName: "Numeric",
            KindNumber: 24,
            OrdinalPosition: 25,
            Description: "A numeric function was used in an improper way. For example, Sqrt with -1."
        },
        {
            KindName: "InvalidArgument",
            KindNumber: 25,
            OrdinalPosition: 26,
            Description: "An invalid argument was passed to a function."
        },
        {
            KindName: "Internal",
            KindNumber: 26,
            OrdinalPosition: 27,
            Description: "System error. There was an internal problem with one of the functions."
        },
        {
            KindName: "NotApplicable",
            KindNumber: 27,
            OrdinalPosition: 28,
            Description: "No value is available. Useful to differentiate a blank value that can be treated as a zero in numerical calculations from blank values that should be flagged as a potential problem if the value is used."
        }
    ];
```

## Free Community & Course Materials
🆓 Get access to our free Power Apps crash course (and our community) here: 
- https://tinyurl.com/DarrensStuffFree 🔗

## Support

I hope you have found this helpful. If you need any help with the Power Platform, don't hesitate to email us at 
* [support@superpowerlabs.co](support@superpowerlabs.co).
* https://powerplatformlinks.com 

## Disclaimer

THIS CODE IS PROVIDED AS IS WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING ANY IMPLIED WARRANTIES OF FITNESS FOR A PARTICULAR PURPOSE, MERCHANTABILITY, OR NON-INFRINGEMENT.

