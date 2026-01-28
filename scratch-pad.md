

meta-llama/llama-4-maverick:free

```PowerFx
fxExp_DBSchemas = {
    ID: 1,
    Name: "Ticketing System",
    Key: "TICKET-SYSTEM-V2",
    DisplayName: "Track-a-Ticket",
    DataSources: "SharePoint",
    Tables: [
        // ================ DEPARTMENTS TABLE ================
        {
            SortOrder: 1,
            Name: "Departments",
            Key: "DEPARTMENTS-TABLE",
            DisplayName: "Departments",
            Fields: [
                {
                    SortOrder: 1,
                    Name: "Title",
                    Key: "DEPT-TITLE",
                    DisplayName: "Department Name",
                    FieldValueType: {
                        SortOrder: 1,
                        FieldType: "Single Line of Text",
                        SharePointCode: "Text",
                        ValueType: "String",
                        DisplayName: "Department Name",
                        MetaData: {
                            MinValue: "",
                            MaxValue: "255",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "The name of the department"
                        }
                    }
                },
                {
                    SortOrder: 2,
                    Name: "CostCenter",
                    Key: "DEPT-COST-CENTER",
                    DisplayName: "Cost Center",
                    FieldValueType: {
                        SortOrder: 2,
                        FieldType: "Numeric",
                        SharePointCode: "Number",
                        ValueType: "Number",
                        DisplayName: "Cost Center Code",
                        MetaData: {
                            MinValue: "0",
                            MaxValue: "999999",
                            DecimalPlaces: 0,
                            Formatting: "######",
                            Description: "The cost center code for this department"
                        }
                    }
                },
                {
                    SortOrder: 3,
                    Name: "ManagerID",
                    Key: "DEPT-MANAGER-ID",
                    DisplayName: "Manager ID",
                    FieldValueType: {
                        SortOrder: 2,
                        FieldType: "Numeric",
                        SharePointCode: "Number",
                        ValueType: "Number",
                        DisplayName: "Manager Reference",
                        MetaData: {
                            MinValue: "0",
                            MaxValue: "999999",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Reference to the manager's user ID"
                        }
                    }
                },
                {
                    SortOrder: 4,
                    Name: "ColorCode",
                    Key: "DEPT-COLOR-CODE",
                    DisplayName: "Color Code",
                    FieldValueType: {
                        SortOrder: 1,
                        FieldType: "Single Line of Text",
                        SharePointCode: "Text",
                        ValueType: "String",
                        DisplayName: "Department Color",
                        MetaData: {
                            MinValue: "",
                            MaxValue: "7",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Hex color code for department visualization"
                        }
                    }
                },
                {
                    SortOrder: 5,
                    Name: "SortOrder",
                    Key: "DEPT-SORT-ORDER",
                    DisplayName: "Sort Order",
                    FieldValueType: {
                        SortOrder: 2,
                        FieldType: "Numeric",
                        SharePointCode: "Number",
                        ValueType: "Number",
                        DisplayName: "Display Order",
                        MetaData: {
                            MinValue: "0",
                            MaxValue: "999",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Order in which department appears in lists"
                        }
                    }
                },
                {
                    SortOrder: 6,
                    Name: "IsActive",
                    Key: "DEPT-IS-ACTIVE",
                    DisplayName: "Is Active",
                    FieldValueType: {
                        SortOrder: 3,
                        FieldType: "Yes/No",
                        SharePointCode: "Boolean",
                        ValueType: "Boolean",
                        DisplayName: "Active Status",
                        MetaData: {
                            MinValue: "",
                            MaxValue: "",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Whether this department is currently active"
                        }
                    }
                }
            ]
        },
        
        // ================ SHOW LEVELS TABLE ================
        {
            SortOrder: 2,
            Name: "ShowLevels",
            Key: "SHOW-LEVELS-TABLE",
            DisplayName: "Visibility Levels",
            Fields: [
                {
                    SortOrder: 1,
                    Name: "Title",
                    Key: "SHOW-LEVEL-TITLE",
                    DisplayName: "Level Name",
                    FieldValueType: {
                        SortOrder: 1,
                        FieldType: "Single Line of Text",
                        SharePointCode: "Text",
                        ValueType: "String",
                        DisplayName: "Visibility Level",
                        MetaData: {
                            MinValue: "",
                            MaxValue: "255",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Name of the visibility level"
                        }
                    }
                },
                {
                    SortOrder: 2,
                    Name: "SortOrder",
                    Key: "SHOW-LEVEL-SORT-ORDER",
                    DisplayName: "Sort Order",
                    FieldValueType: {
                        SortOrder: 2,
                        FieldType: "Numeric",
                        SharePointCode: "Number",
                        ValueType: "Number",
                        DisplayName: "Display Order",
                        MetaData: {
                            MinValue: "0",
                            MaxValue: "999",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Order in which level appears in lists"
                        }
                    }
                },
                {
                    SortOrder: 3,
                    Name: "IsActive",
                    Key: "SHOW-LEVEL-IS-ACTIVE",
                    DisplayName: "Is Active",
                    FieldValueType: {
                        SortOrder: 3,
                        FieldType: "Yes/No",
                        SharePointCode: "Boolean",
                        ValueType: "Boolean",
                        DisplayName: "Active Status",
                        MetaData: {
                            MinValue: "",
                            MaxValue: "",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Whether this visibility level is currently active"
                        }
                    }
                }
            ]
        },
        
        // ================ ASSIGNMENT TYPES TABLE ================
        {
            SortOrder: 3,
            Name: "AssignmentTypes",
            Key: "ASSIGNMENT-TYPES-TABLE",
            DisplayName: "Assignment Types",
            Fields: [
                {
                    SortOrder: 1,
                    Name: "Title",
                    Key: "ASSIGNMENT-TYPE-TITLE",
                    DisplayName: "Type Name",
                    FieldValueType: {
                        SortOrder: 1,
                        FieldType: "Single Line of Text",
                        SharePointCode: "Text",
                        ValueType: "String",
                        DisplayName: "Assignment Type",
                        MetaData: {
                            MinValue: "",
                            MaxValue: "255",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Name of the assignment type"
                        }
                    }
                },
                {
                    SortOrder: 2,
                    Name: "SortOrder",
                    Key: "ASSIGNMENT-TYPE-SORT-ORDER",
                    DisplayName: "Sort Order",
                    FieldValueType: {
                        SortOrder: 2,
                        FieldType: "Numeric",
                        SharePointCode: "Number",
                        ValueType: "Number",
                        DisplayName: "Display Order",
                        MetaData: {
                            MinValue: "0",
                            MaxValue: "999",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Order in which type appears in lists"
                        }
                    }
                },
                {
                    SortOrder: 3,
                    Name: "IsActive",
                    Key: "ASSIGNMENT-TYPE-IS-ACTIVE",
                    DisplayName: "Is Active",
                    FieldValueType: {
                        SortOrder: 3,
                        FieldType: "Yes/No",
                        SharePointCode: "Boolean",
                        ValueType: "Boolean",
                        DisplayName: "Active Status",
                        MetaData: {
                            MinValue: "",
                            MaxValue: "",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Whether this assignment type is currently active"
                        }
                    }
                }
            ]
        },
        
        // ================ USERS TABLE ================
        {
            SortOrder: 4,
            Name: "Users",
            Key: "USERS-TABLE",
            DisplayName: "System Users",
            Fields: [
                {
                    SortOrder: 1,
                    Name: "Title",
                    Key: "USER-TITLE",
                    DisplayName: "Display Name",
                    FieldValueType: {
                        SortOrder: 1,
                        FieldType: "Single Line of Text",
                        SharePointCode: "Text",
                        ValueType: "String",
                        DisplayName: "Full Name",
                        MetaData: {
                            MinValue: "",
                            MaxValue: "255",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "User's display name"
                        }
                    }
                },
                {
                    SortOrder: 2,
                    Name: "FirstName",
                    Key: "USER-FIRST-NAME",
                    DisplayName: "First Name",
                    FieldValueType: {
                        SortOrder: 1,
                        FieldType: "Single Line of Text",
                        SharePointCode: "Text",
                        ValueType: "String",
                        DisplayName: "First Name",
                        MetaData: {
                            MinValue: "",
                            MaxValue: "255",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "User's first name"
                        }
                    }
                },
                {
                    SortOrder: 3,
                    Name: "LastName",
                    Key: "USER-LAST-NAME",
                    DisplayName: "Last Name",
                    FieldValueType: {
                        SortOrder: 1,
                        FieldType: "Single Line of Text",
                        SharePointCode: "Text",
                        ValueType: "String",
                        DisplayName: "Last Name",
                        MetaData: {
                            MinValue: "",
                            MaxValue: "255",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "User's last name"
                        }
                    }
                },
                {
                    SortOrder: 4,
                    Name: "Email",
                    Key: "USER-EMAIL",
                    DisplayName: "Email Address",
                    FieldValueType: {
                        SortOrder: 1,
                        FieldType: "Single Line of Text",
                        SharePointCode: "Text",
                        ValueType: "String",
                        DisplayName: "Email",
                        MetaData: {
                            MinValue: "",
                            MaxValue: "255",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "User's email address"
                        }
                    }
                },
                {
                    SortOrder: 5,
                    Name: "Photo",
                    Key: "USER-PHOTO",
                    DisplayName: "Profile Photo",
                    FieldValueType: {
                        SortOrder: 6,
                        FieldType: "Image",
                        SharePointCode: "Image",
                        ValueType: "Image",
                        DisplayName: "Photo",
                        MetaData: {
                            MinValue: "",
                            MaxValue: "",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "User's profile photo"
                        }
                    }
                },
                {
                    SortOrder: 6,
                    Name: "Phone",
                    Key: "USER-PHONE",
                    DisplayName: "Phone Number",
                    FieldValueType: {
                        SortOrder: 1,
                        FieldType: "Single Line of Text",
                        SharePointCode: "Text",
                        ValueType: "String",
                        DisplayName: "Phone",
                        MetaData: {
                            MinValue: "",
                            MaxValue: "20",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "User's phone number"
                        }
                    }
                },
                {
                    SortOrder: 7,
                    Name: "Notes",
                    Key: "USER-NOTES",
                    DisplayName: "Notes",
                    FieldValueType: {
                        SortOrder: 5,
                        FieldType: "Multi-Line Text",
                        SharePointCode: "Note",
                        ValueType: "Text Area",
                        DisplayName: "Additional Notes",
                        MetaData: {
                            MinValue: "",
                            MaxValue: "",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Additional notes about the user"
                        }
                    }
                },
                {
                    SortOrder: 8,
                    Name: "DepartmentID",
                    Key: "USER-DEPARTMENT-ID",
                    DisplayName: "Department",
                    FieldValueType: {
                        SortOrder: 2,
                        FieldType: "Numeric",
                        SharePointCode: "Number",
                        ValueType: "Number",
                        DisplayName: "Department Reference",
                        MetaData: {
                            MinValue: "0",
                            MaxValue: "999999",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Reference to user's department"
                        }
                    }
                },
                {
                    SortOrder: 9,
                    Name: "IsActive",
                    Key: "USER-IS-ACTIVE",
                    DisplayName: "Is Active",
                    FieldValueType: {
                        SortOrder: 3,
                        FieldType: "Yes/No",
                        SharePointCode: "Boolean",
                        ValueType: "Boolean",
                        DisplayName: "Active Status",
                        MetaData: {
                            MinValue: "",
                            MaxValue: "",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Whether this user is currently active"
                        }
                    }
                },
                {
                    SortOrder: 10,
                    Name: "PhotoLength",
                    Key: "USER-PHOTO-LENGTH",
                    DisplayName: "Photo Size",
                    FieldValueType: {
                        SortOrder: 2,
                        FieldType: "Numeric",
                        SharePointCode: "Number",
                        ValueType: "Number",
                        DisplayName: "Photo File Size",
                        MetaData: {
                            MinValue: "0",
                            MaxValue: "9999999",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Size of the photo file in bytes"
                        }
                    }
                }
            ]
        },
        
        // ================ REQUEST STATUSES TABLE ================
        {
            SortOrder: 5,
            Name: "RequestStatuses",
            Key: "REQUEST-STATUSES-TABLE",
            DisplayName: "Request Statuses",
            Fields: [
                {
                    SortOrder: 1,
                    Name: "Title",
                    Key: "REQUEST-STATUS-TITLE",
                    DisplayName: "Status Name",
                    FieldValueType: {
                        SortOrder: 1,
                        FieldType: "Single Line of Text",
                        SharePointCode: "Text",
                        ValueType: "String",
                        DisplayName: "Status",
                        MetaData: {
                            MinValue: "",
                            MaxValue: "255",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Name of the request status"
                        }
                    }
                },
                {
                    SortOrder: 2,
                    Name: "SortOrder",
                    Key: "REQUEST-STATUS-SORT-ORDER",
                    DisplayName: "Sort Order",
                    FieldValueType: {
                        SortOrder: 2,
                        FieldType: "Numeric",
                        SharePointCode: "Number",
                        ValueType: "Number",
                        DisplayName: "Display Order",
                        MetaData: {
                            MinValue: "0",
                            MaxValue: "999",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Order in which status appears in lists"
                        }
                    }
                },
                {
                    SortOrder: 3,
                    Name: "IsActive",
                    Key: "REQUEST-STATUS-IS-ACTIVE",
                    DisplayName: "Is Active",
                    FieldValueType: {
                        SortOrder: 3,
                        FieldType: "Yes/No",
                        SharePointCode: "Boolean",
                        ValueType: "Boolean",
                        DisplayName: "Active Status",
                        MetaData: {
                            MinValue: "",
                            MaxValue: "",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Whether this request status is currently active"
                        }
                    }
                }
            ]
        },
        
        // ================ REQUEST PRIORITIES TABLE ================
        {
            SortOrder: 6,
            Name: "RequestPriorities",
            Key: "REQUEST-PRIORITIES-TABLE",
            DisplayName: "Request Priorities",
            Fields: [
                {
                    SortOrder: 1,
                    Name: "Title",
                    Key: "REQUEST-PRIORITY-TITLE",
                    DisplayName: "Priority Name",
                    FieldValueType: {
                        SortOrder: 1,
                        FieldType: "Single Line of Text",
                        SharePointCode: "Text",
                        ValueType: "String",
                        DisplayName: "Priority Level",
                        MetaData: {
                            MinValue: "",
                            MaxValue: "255",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Name of the priority level"
                        }
                    }
                },
                {
                    SortOrder: 2,
                    Name: "SortOrder",
                    Key: "REQUEST-PRIORITY-SORT-ORDER",
                    DisplayName: "Sort Order",
                    FieldValueType: {
                        SortOrder: 2,
                        FieldType: "Numeric",
                        SharePointCode: "Number",
                        ValueType: "Number",
                        DisplayName: "Display Order",
                        MetaData: {
                            MinValue: "0",
                            MaxValue: "999",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Order in which priority appears in lists"
                        }
                    }
                },
                {
                    SortOrder: 3,
                    Name: "IsActive",
                    Key: "REQUEST-PRIORITY-IS-ACTIVE",
                    DisplayName: "Is Active",
                    FieldValueType: {
                        SortOrder: 3,
                        FieldType: "Yes/No",
                        SharePointCode: "Boolean",
                        ValueType: "Boolean",
                        DisplayName: "Active Status",
                        MetaData: {
                            MinValue: "",
                            MaxValue: "",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Whether this priority level is currently active"
                        }
                    }
                }
            ]
        },
        
        // ================ REQUEST CATEGORIES TABLE ================
        {
            SortOrder: 7,
            Name: "RequestCategories",
            Key: "REQUEST-CATEGORIES-TABLE",
            DisplayName: "Request Categories",
            Fields: [
                {
                    SortOrder: 1,
                    Name: "Title",
                    Key: "REQUEST-CATEGORY-TITLE",
                    DisplayName: "Category Name",
                    FieldValueType: {
                        SortOrder: 1,
                        FieldType: "Single Line of Text",
                        SharePointCode: "Text",
                        ValueType: "String",
                        DisplayName: "Category",
                        MetaData: {
                            MinValue: "",
                            MaxValue: "255",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Name of the request category"
                        }
                    }
                },
                {
                    SortOrder: 2,
                    Name: "SortOrder",
                    Key: "REQUEST-CATEGORY-SORT-ORDER",
                    DisplayName: "Sort Order",
                    FieldValueType: {
                        SortOrder: 2,
                        FieldType: "Numeric",
                        SharePointCode: "Number",
                        ValueType: "Number",
                        DisplayName: "Display Order",
                        MetaData: {
                            MinValue: "0",
                            MaxValue: "999",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Order in which category appears in lists"
                        }
                    }
                },
                {
                    SortOrder: 3,
                    Name: "IsActive",
                    Key: "REQUEST-CATEGORY-IS-ACTIVE",
                    DisplayName: "Is Active",
                    FieldValueType: {
                        SortOrder: 3,
                        FieldType: "Yes/No",
                        SharePointCode: "Boolean",
                        ValueType: "Boolean",
                        DisplayName: "Active Status",
                        MetaData: {
                            MinValue: "",
                            MaxValue: "",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Whether this category is currently active"
                        }
                    }
                }
            ]
        },
        
        // ================ REQUESTS TABLE (MAIN) ================
        {
            SortOrder: 8,
            Name: "Requests",
            Key: "REQUESTS-TABLE",
            DisplayName: "Support Requests",
            Fields: [
                {
                    SortOrder: 1,
                    Name: "Title",
                    Key: "REQUEST-TITLE",
                    DisplayName: "Request Number",
                    FieldValueType: {
                        SortOrder: 1,
                        FieldType: "Single Line of Text",
                        SharePointCode: "Text",
                        ValueType: "String",
                        DisplayName: "Request #",
                        MetaData: {
                            MinValue: "",
                            MaxValue: "255",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Unique request identifier"
                        }
                    }
                },
                {
                    SortOrder: 2,
                    Name: "RequestDateTime",
                    Key: "REQUEST-DATE-TIME",
                    DisplayName: "Request Date/Time",
                    FieldValueType: {
                        SortOrder: 4,
                        FieldType: "Date Time",
                        SharePointCode: "DateTime",
                        ValueType: "DateTime",
                        DisplayName: "Submitted On",
                        MetaData: {
                            MinValue: "",
                            MaxValue: "",
                            DecimalPlaces: 0,
                            Formatting: "MM/DD/YYYY HH:MM",
                            Description: "When the request was submitted"
                        }
                    }
                },
                {
                    SortOrder: 3,
                    Name: "Subject",
                    Key: "REQUEST-SUBJECT",
                    DisplayName: "Subject",
                    FieldValueType: {
                        SortOrder: 1,
                        FieldType: "Single Line of Text",
                        SharePointCode: "Text",
                        ValueType: "String",
                        DisplayName: "Brief Description",
                        MetaData: {
                            MinValue: "",
                            MaxValue: "255",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Brief description of the request"
                        }
                    }
                },
                {
                    SortOrder: 4,
                    Name: "Body",
                    Key: "REQUEST-BODY",
                    DisplayName: "Description",
                    FieldValueType: {
                        SortOrder: 5,
                        FieldType: "Multi-Line Text",
                        SharePointCode: "Note",
                        ValueType: "Text Area",
                        DisplayName: "Full Description",
                        MetaData: {
                            MinValue: "",
                            MaxValue: "",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Detailed description of the request"
                        }
                    }
                },
                {
                    SortOrder: 5,
                    Name: "RequestorID",
                    Key: "REQUEST-REQUESTOR-ID",
                    DisplayName: "Requestor",
                    FieldValueType: {
                        SortOrder: 2,
                        FieldType: "Numeric",
                        SharePointCode: "Number",
                        ValueType: "Number",
                        DisplayName: "Requestor Reference",
                        MetaData: {
                            MinValue: "0",
                            MaxValue: "999999",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "ID of the person making the request"
                        }
                    }
                },
                {
                    SortOrder: 6,
                    Name: "RequestorName",
                    Key: "REQUEST-REQUESTOR-NAME",
                    DisplayName: "Requestor Name",
                    FieldValueType: {
                        SortOrder: 1,
                        FieldType: "Single Line of Text",
                        SharePointCode: "Text",
                        ValueType: "String",
                        DisplayName: "Requestor",
                        MetaData: {
                            MinValue: "",
                            MaxValue: "255",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Name of the person making the request"
                        }
                    }
                },
                {
                    SortOrder: 7,
                    Name: "PersonAffectedID",
                    Key: "REQUEST-PERSON-AFFECTED-ID",
                    DisplayName: "Person Affected",
                    FieldValueType: {
                        SortOrder: 2,
                        FieldType: "Numeric",
                        SharePointCode: "Number",
                        ValueType: "Number",
                        DisplayName: "Affected Person Reference",
                        MetaData: {
                            MinValue: "0",
                            MaxValue: "999999",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "ID of the person affected by the issue"
                        }
                    }
                },
                {
                    SortOrder: 8,
                    Name: "PersonAffectedName",
                    Key: "REQUEST-PERSON-AFFECTED-NAME",
                    DisplayName: "Person Affected Name",
                    FieldValueType: {
                        SortOrder: 1,
                        FieldType: "Single Line of Text",
                        SharePointCode: "Text",
                        ValueType: "String",
                        DisplayName: "Affected Person",
                        MetaData: {
                            MinValue: "",
                            MaxValue: "255",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Name of the person affected by the issue"
                        }
                    }
                },
                {
                    SortOrder: 9,
                    Name: "AssociatedDept",
                    Key: "REQUEST-ASSOCIATED-DEPT",
                    DisplayName: "Associated Department",
                    FieldValueType: {
                        SortOrder: 2,
                        FieldType: "Numeric",
                        SharePointCode: "Number",
                        ValueType: "Number",
                        DisplayName: "Department Reference",
                        MetaData: {
                            MinValue: "0",
                            MaxValue: "999999",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Department associated with this request"
                        }
                    }
                },
                {
                    SortOrder: 10,
                    Name: "RequestStatusID",
                    Key: "REQUEST-STATUS-ID",
                    DisplayName: "Status",
                    FieldValueType: {
                        SortOrder: 2,
                        FieldType: "Numeric",
                        SharePointCode: "Number",
                        ValueType: "Number",
                        DisplayName: "Status Reference",
                        MetaData: {
                            MinValue: "0",
                            MaxValue: "999999",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Current status of the request"
                        }
                    }
                },
                {
                    SortOrder: 11,
                    Name: "AssignedToID",
                    Key: "REQUEST-ASSIGNED-TO-ID",
                    DisplayName: "Assigned To",
                    FieldValueType: {
                        SortOrder: 2,
                        FieldType: "Numeric",
                        SharePointCode: "Number",
                        ValueType: "Number",
                        DisplayName: "Assignee Reference",
                        MetaData: {
                            MinValue: "0",
                            MaxValue: "999999",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "ID of the person assigned to this request"
                        }
                    }
                },
                {
                    SortOrder: 12,
                    Name: "AssignedToName",
                    Key: "REQUEST-ASSIGNED-TO-NAME",
                    DisplayName: "Assigned To Name",
                    FieldValueType: {
                        SortOrder: 1,
                        FieldType: "Single Line of Text",
                        SharePointCode: "Text",
                        ValueType: "String",
                        DisplayName: "Assignee",
                        MetaData: {
                            MinValue: "",
                            MaxValue: "255",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Name of the person assigned to this request"
                        }
                    }
                },
                {
                    SortOrder: 13,
                    Name: "PriorityID",
                    Key: "REQUEST-PRIORITY-ID",
                    DisplayName: "Priority",
                    FieldValueType: {
                        SortOrder: 2,
                        FieldType: "Numeric",
                        SharePointCode: "Number",
                        ValueType: "Number",
                        DisplayName: "Priority Reference",
                        MetaData: {
                            MinValue: "0",
                            MaxValue: "999999",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Priority level of the request"
                        }
                    }
                },
                {
                    SortOrder: 14,
                    Name: "RequireApproval",
                    Key: "REQUEST-REQUIRE-APPROVAL",
                    DisplayName: "Requires Approval",
                    FieldValueType: {
                        SortOrder: 3,
                        FieldType: "Yes/No",
                        SharePointCode: "Boolean",
                        ValueType: "Boolean",
                        DisplayName: "Approval Required",
                        MetaData: {
                            MinValue: "",
                            MaxValue: "",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Whether this request requires approval"
                        }
                    }
                },
                {
                    SortOrder: 15,
                    Name: "CategoryID",
                    Key: "REQUEST-CATEGORY-ID",
                    DisplayName: "Category",
                    FieldValueType: {
                        SortOrder: 2,
                        FieldType: "Numeric",
                        SharePointCode: "Number",
                        ValueType: "Number",
                        DisplayName: "Category Reference",
                        MetaData: {
                            MinValue: "0",
                            MaxValue: "999999",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Category of the request"
                        }
                    }
                },
                {
                    SortOrder: 16,
                    Name: "SuggestedTechnicianID",
                    Key: "REQUEST-SUGGESTED-TECH-ID",
                    DisplayName: "Suggested Technician",
                    FieldValueType: {
                        SortOrder: 2,
                        FieldType: "Numeric",
                        SharePointCode: "Number",
                        ValueType: "Number",
                        DisplayName: "Suggested Tech Reference",
                        MetaData: {
                            MinValue: "0",
                            MaxValue: "999999",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "ID of suggested technician"
                        }
                    }
                },
                {
                    SortOrder: 17,
                    Name: "SuggestedTechnicianName",
                    Key: "REQUEST-SUGGESTED-TECH-NAME",
                    DisplayName: "Suggested Technician Name",
                    FieldValueType: {
                        SortOrder: 1,
                        FieldType: "Single Line of Text",
                        SharePointCode: "Text",
                        ValueType: "String",
                        DisplayName: "Suggested Tech",
                        MetaData: {
                            MinValue: "",
                            MaxValue: "255",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Name of suggested technician"
                        }
                    }
                }
            ]
        },
        
        // ================ REQUEST ASSIGNMENTS TABLE ================
        {
            SortOrder: 9,
            Name: "RequestAssignments",
            Key: "REQUEST-ASSIGNMENTS-TABLE",
            DisplayName: "Request Assignments",
            Fields: [
                {
                    SortOrder: 1,
                    Name: "Title",
                    Key: "ASSIGNMENT-TITLE",
                    DisplayName: "Assignment ID",
                    FieldValueType: {
                        SortOrder: 1,
                        FieldType: "Single Line of Text",
                        SharePointCode: "Text",
                        ValueType: "String",
                        DisplayName: "Assignment Reference",
                        MetaData: {
                            MinValue: "",
                            MaxValue: "255",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Unique assignment identifier"
                        }
                    }
                },
                {
                    SortOrder: 2,
                    Name: "RequestID",
                    Key: "ASSIGNMENT-REQUEST-ID",
                    DisplayName: "Request",
                    FieldValueType: {
                        SortOrder: 2,
                        FieldType: "Numeric",
                        SharePointCode: "Number",
                        ValueType: "Number",
                        DisplayName: "Request Reference",
                        MetaData: {
                            MinValue: "0",
                            MaxValue: "999999",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "ID of the related request"
                        }
                    }
                },
                {
                    SortOrder: 3,
                    Name: "RequestSubject",
                    Key: "ASSIGNMENT-REQUEST-SUBJECT",
                    DisplayName: "Request Subject",
                    FieldValueType: {
                        SortOrder: 1,
                        FieldType: "Single Line of Text",
                        SharePointCode: "Text",
                        ValueType: "String",
                        DisplayName: "Request Description",
                        MetaData: {
                            MinValue: "",
                            MaxValue: "255",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Subject of the related request"
                        }
                    }
                },
                {
                    SortOrder: 4,
                    Name: "AssignedToID",
                    Key: "ASSIGNMENT-ASSIGNED-TO-ID",
                    DisplayName: "Assigned To",
                    FieldValueType: {
                        SortOrder: 2,
                        FieldType: "Numeric",
                        SharePointCode: "Number",
                        ValueType: "Number",
                        DisplayName: "Assignee Reference",
                        MetaData: {
                            MinValue: "0",
                            MaxValue: "999999",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "ID of the person assigned"
                        }
                    }
                },
                {
                    SortOrder: 5,
                    Name: "AssignedToName",
                    Key: "ASSIGNMENT-ASSIGNED-TO-NAME",
                    DisplayName: "Assigned To Name",
                    FieldValueType: {
                        SortOrder: 1,
                        FieldType: "Single Line of Text",
                        SharePointCode: "Text",
                        ValueType: "String",
                        DisplayName: "Assignee",
                        MetaData: {
                            MinValue: "",
                            MaxValue: "255",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Name of the person assigned"
                        }
                    }
                },
                {
                    SortOrder: 6,
                    Name: "DepartmentID",
                    Key: "ASSIGNMENT-DEPARTMENT-ID",
                    DisplayName: "Department",
                    FieldValueType: {
                        SortOrder: 2,
                        FieldType: "Numeric",
                        SharePointCode: "Number",
                        ValueType: "Number",
                        DisplayName: "Department Reference",
                        MetaData: {
                            MinValue: "0",
                            MaxValue: "999999",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Department handling this assignment"
                        }
                    }
                },
                {
                    SortOrder: 7,
                    Name: "AssignmentTypeID",
                    Key: "ASSIGNMENT-TYPE-ID",
                    DisplayName: "Assignment Type",
                    FieldValueType: {
                        SortOrder: 2,
                        FieldType: "Numeric",
                        SharePointCode: "Number",
                        ValueType: "Number",
                        DisplayName: "Type Reference",
                        MetaData: {
                            MinValue: "0",
                            MaxValue: "999999",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Type of assignment"
                        }
                    }
                },
                {
                    SortOrder: 8,
                    Name: "Notes",
                    Key: "ASSIGNMENT-NOTES",
                    DisplayName: "Notes",
                    FieldValueType: {
                        SortOrder: 5,
                        FieldType: "Multi-Line Text",
                        SharePointCode: "Note",
                        ValueType: "Text Area",
                        DisplayName: "Assignment Notes",
                        MetaData: {
                            MinValue: "",
                            MaxValue: "",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Notes about this assignment"
                        }
                    }
                },
                {
                    SortOrder: 9,
                    Name: "NeedsApproval",
                    Key: "ASSIGNMENT-NEEDS-APPROVAL",
                    DisplayName: "Needs Approval",
                    FieldValueType: {
                        SortOrder: 3,
                        FieldType: "Yes/No",
                        SharePointCode: "Boolean",
                        ValueType: "Boolean",
                        DisplayName: "Approval Required",
                        MetaData: {
                            MinValue: "",
                            MaxValue: "",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Whether this assignment needs approval"
                        }
                    }
                },
                {
                    SortOrder: 10,
                    Name: "KeepNotified",
                    Key: "ASSIGNMENT-KEEP-NOTIFIED",
                    DisplayName: "Keep Notified",
                    FieldValueType: {
                        SortOrder: 3,
                        FieldType: "Yes/No",
                        SharePointCode: "Boolean",
                        ValueType: "Boolean",
                        DisplayName: "Send Notifications",
                        MetaData: {
                            MinValue: "",
                            MaxValue: "",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Whether to keep assignee notified of changes"
                        }
                    }
                },
                {
                    SortOrder: 11,
                    Name: "CurrentlyAssigned",
                    Key: "ASSIGNMENT-CURRENTLY-ASSIGNED",
                    DisplayName: "Currently Assigned",
                    FieldValueType: {
                        SortOrder: 3,
                        FieldType: "Yes/No",
                        SharePointCode: "Boolean",
                        ValueType: "Boolean",
                        DisplayName: "Active Assignment",
                        MetaData: {
                            MinValue: "",
                            MaxValue: "",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Whether this is the current active assignment"
                        }
                    }
                }
            ]
        },
        
        // ================ REQUEST NOTES TABLE ================
        {
            SortOrder: 10,
            Name: "RequestNotes",
            Key: "REQUEST-NOTES-TABLE",
            DisplayName: "Request Notes",
            Fields: [
                {
                    SortOrder: 1,
                    Name: "Title",
                    Key: "NOTE-TITLE",
                    DisplayName: "Note ID",
                    FieldValueType: {
                        SortOrder: 1,
                        FieldType: "Single Line of Text",
                        SharePointCode: "Text",
                        ValueType: "String",
                        DisplayName: "Note Reference",
                        MetaData: {
                            MinValue: "",
                            MaxValue: "255",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Unique note identifier"
                        }
                    }
                },
                {
                    SortOrder: 2,
                    Name: "ShowLevelID",
                    Key: "NOTE-SHOW-LEVEL-ID",
                    DisplayName: "Visibility Level",
                    FieldValueType: {
                        SortOrder: 2,
                        FieldType: "Numeric",
                        SharePointCode: "Number",
                        ValueType: "Number",
                        DisplayName: "Visibility Reference",
                        MetaData: {
                            MinValue: "0",
                            MaxValue: "999999",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Visibility level of this note"
                        }
                    }
                },
                {
                    SortOrder: 3,
                    Name: "RequestID",
                    Key: "NOTE-REQUEST-ID",
                    DisplayName: "Request",
                    FieldValueType: {
                        SortOrder: 2,
                        FieldType: "Numeric",
                        SharePointCode: "Number",
                        ValueType: "Number",
                        DisplayName: "Request Reference",
                        MetaData: {
                            MinValue: "0",
                            MaxValue: "999999",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "ID of the related request"
                        }
                    }
                },
                {
                    SortOrder: 4,
                    Name: "Notes",
                    Key: "NOTE-CONTENT",
                    DisplayName: "Note Content",
                    FieldValueType: {
                        SortOrder: 5,
                        FieldType: "Multi-Line Text",
                        SharePointCode: "Note",
                        ValueType: "Text Area",
                        DisplayName: "Note Text",
                        MetaData: {
                            MinValue: "",
                            MaxValue: "",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Content of the note"
                        }
                    }
                },
                {
                    SortOrder: 5,
                    Name: "StatusChange",
                    Key: "NOTE-STATUS-CHANGE",
                    DisplayName: "Status Changed",
                    FieldValueType: {
                        SortOrder: 3,
                        FieldType: "Yes/No",
                        SharePointCode: "Boolean",
                        ValueType: "Boolean",
                        DisplayName: "Status Change Flag",
                        MetaData: {
                            MinValue: "",
                            MaxValue: "",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Whether this note represents a status change"
                        }
                    }
                },
                {
                    SortOrder: 6,
                    Name: "RequestStatusID",
                    Key: "NOTE-REQUEST-STATUS-ID",
                    DisplayName: "New Status",
                    FieldValueType: {
                        SortOrder: 2,
                        FieldType: "Numeric",
                        SharePointCode: "Number",
                        ValueType: "Number",
                        DisplayName: "Status Reference",
                        MetaData: {
                            MinValue: "0",
                            MaxValue: "999999",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "New status if this is a status change"
                        }
                    }
                },
                {
                    SortOrder: 7,
                    Name: "PercentageComplete",
                    Key: "NOTE-PERCENTAGE-COMPLETE",
                    DisplayName: "% Complete",
                    FieldValueType: {
                        SortOrder: 2,
                        FieldType: "Numeric",
                        SharePointCode: "Number",
                        ValueType: "Number",
                        DisplayName: "Completion Percentage",
                        MetaData: {
                            MinValue: "0",
                            MaxValue: "100",
                            DecimalPlaces: 0,
                            Formatting: "##%",
                            Description: "Percentage of request completion"
                        }
                    }
                },
                {
                    SortOrder: 8,
                    Name: "UserID",
                    Key: "NOTE-USER-ID",
                    DisplayName: "Created By",
                    FieldValueType: {
                        SortOrder: 2,
                        FieldType: "Numeric",
                        SharePointCode: "Number",
                        ValueType: "Number",
                        DisplayName: "User Reference",
                        MetaData: {
                            MinValue: "0",
                            MaxValue: "999999",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "ID of user who created this note"
                        }
                    }
                },
                {
                    SortOrder: 9,
                    Name: "UserName",
                    Key: "NOTE-USER-NAME",
                    DisplayName: "Created By Name",
                    FieldValueType: {
                        SortOrder: 1,
                        FieldType: "Single Line of Text",
                        SharePointCode: "Text",
                        ValueType: "String",
                        DisplayName: "Author",
                        MetaData: {
                            MinValue: "",
                            MaxValue: "255",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Name of user who created this note"
                        }
                    }
                },
                {
                    SortOrder: 10,
                    Name: "ParentNoteID",
                    Key: "NOTE-PARENT-NOTE-ID",
                    DisplayName: "Parent Note",
                    FieldValueType: {
                        SortOrder: 2,
                        FieldType: "Numeric",
                        SharePointCode: "Number",
                        ValueType: "Number",
                        DisplayName: "Parent Note Reference",
                        MetaData: {
                            MinValue: "0",
                            MaxValue: "999999",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "ID of parent note if this is a reply"
                        }
                    }
                },
                {
                    SortOrder: 11,
                    Name: "AssignmentID",
                    Key: "NOTE-ASSIGNMENT-ID",
                    DisplayName: "Assignment",
                    FieldValueType: {
                        SortOrder: 2,
                        FieldType: "Numeric",
                        SharePointCode: "Number",
                        ValueType: "Number",
                        DisplayName: "Assignment Reference",
                        MetaData: {
                            MinValue: "0",
                            MaxValue: "999999",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Related assignment ID"
                        }
                    }
                },
                {
                    SortOrder: 12,
                    Name: "ParentID",
                    Key: "NOTE-PARENT-ID",
                    DisplayName: "Parent ID",
                    FieldValueType: {
                        SortOrder: 2,
                        FieldType: "Numeric",
                        SharePointCode: "Number",
                        ValueType: "Number",
                        DisplayName: "Parent Reference",
                        MetaData: {
                            MinValue: "0",
                            MaxValue: "999999",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Generic parent reference ID"
                        }
                    }
                }
            ]
        },
        
        // ================ REQUEST IMAGES TABLE ================
        {
            SortOrder: 11,
            Name: "RequestImages",
            Key: "REQUEST-IMAGES-TABLE",
            DisplayName: "Request Images",
            Fields: [
                {
                    SortOrder: 1,
                    Name: "Title",
                    Key: "IMAGE-TITLE",
                    DisplayName: "Image Title",
                    FieldValueType: {
                        SortOrder: 1,
                        FieldType: "Single Line of Text",
                        SharePointCode: "Text",
                        ValueType: "String",
                        DisplayName: "Image Name",
                        MetaData: {
                            MinValue: "",
                            MaxValue: "255",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Title or name of the image"
                        }
                    }
                },
                {
                    SortOrder: 2,
                    Name: "RequestID",
                    Key: "IMAGE-REQUEST-ID",
                    DisplayName: "Request",
                    FieldValueType: {
                        SortOrder: 2,
                        FieldType: "Numeric",
                        SharePointCode: "Number",
                        ValueType: "Number",
                        DisplayName: "Request Reference",
                        MetaData: {
                            MinValue: "0",
                            MaxValue: "999999",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "ID of the related request"
                        }
                    }
                },
                {
                    SortOrder: 3,
                    Name: "Image",
                    Key: "IMAGE-FILE",
                    DisplayName: "Image File",
                    FieldValueType: {
                        SortOrder: 6,
                        FieldType: "Image",
                        SharePointCode: "Image",
                        ValueType: "Image",
                        DisplayName: "Uploaded Image",
                        MetaData: {
                            MinValue: "",
                            MaxValue: "",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "The uploaded image file"
                        }
                    }
                },
                {
                    SortOrder: 4,
                    Name: "LongDescription",
                    Key: "IMAGE-LONG-DESCRIPTION",
                    DisplayName: "Description",
                    FieldValueType: {
                        SortOrder: 5,
                        FieldType: "Multi-Line Text",
                        SharePointCode: "Note",
                        ValueType: "Text Area",
                        DisplayName: "Image Description",
                        MetaData: {
                            MinValue: "",
                            MaxValue: "",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Detailed description of the image"
                        }
                    }
                }
            ]
        },
        
        // ================ USER TICKET NOTIFICATIONS TABLE ================
        {
            SortOrder: 12,
            Name: "UserTicketNotifications",
            Key: "USER-TICKET-NOTIFICATIONS-TABLE",
            DisplayName: "Notification Subscriptions",
            Fields: [
                {
                    SortOrder: 1,
                    Name: "Title",
                    Key: "NOTIFICATION-TITLE",
                    DisplayName: "Notification ID",
                    FieldValueType: {
                        SortOrder: 1,
                        FieldType: "Single Line of Text",
                        SharePointCode: "Text",
                        ValueType: "String",
                        DisplayName: "Notification Reference",
                        MetaData: {
                            MinValue: "",
                            MaxValue: "255",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Unique notification identifier"
                        }
                    }
                },
                {
                    SortOrder: 2,
                    Name: "RequestID",
                    Key: "NOTIFICATION-REQUEST-ID",
                    DisplayName: "Request",
                    FieldValueType: {
                        SortOrder: 2,
                        FieldType: "Numeric",
                        SharePointCode: "Number",
                        ValueType: "Number",
                        DisplayName: "Request Reference",
                        MetaData: {
                            MinValue: "0",
                            MaxValue: "999999",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "ID of the request to monitor"
                        }
                    }
                },
                {
                    SortOrder: 3,
                    Name: "UserID",
                    Key: "NOTIFICATION-USER-ID",
                    DisplayName: "User",
                    FieldValueType: {
                        SortOrder: 2,
                        FieldType: "Numeric",
                        SharePointCode: "Number",
                        ValueType: "Number",
                        DisplayName: "User Reference",
                        MetaData: {
                            MinValue: "0",
                            MaxValue: "999999",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "ID of user to notify"
                        }
                    }
                },
                {
                    SortOrder: 4,
                    Name: "IsActive",
                    Key: "NOTIFICATION-IS-ACTIVE",
                    DisplayName: "Is Active",
                    FieldValueType: {
                        SortOrder: 3,
                        FieldType: "Yes/No",
                        SharePointCode: "Boolean",
                        ValueType: "Boolean",
                        DisplayName: "Active Status",
                        MetaData: {
                            MinValue: "",
                            MaxValue: "",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Whether this notification subscription is active"
                        }
                    }
                }
            ]
        },
        
        // ================ SLA VIOLATIONS TABLE ================
        {
            SortOrder: 13,
            Name: "SLAViolations",
            Key: "SLA-VIOLATIONS-TABLE",
            DisplayName: "SLA Violations",
            Fields: [
                {
                    SortOrder: 1,
                    Name: "Title",
                    Key: "SLA-VIOLATION-TITLE",
                    DisplayName: "Violation Name",
                    FieldValueType: {
                        SortOrder: 1,
                        FieldType: "Single Line of Text",
                        SharePointCode: "Text",
                        ValueType: "String",
                        DisplayName: "SLA Violation Type",
                        MetaData: {
                            MinValue: "",
                            MaxValue: "255",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Name of the SLA violation type"
                        }
                    }
                },
                {
                    SortOrder: 2,
                    Name: "Description",
                    Key: "SLA-VIOLATION-DESCRIPTION",
                    DisplayName: "Description",
                    FieldValueType: {
                        SortOrder: 5,
                        FieldType: "Multi-Line Text",
                        SharePointCode: "Note",
                        ValueType: "Text Area",
                        DisplayName: "Violation Description",
                        MetaData: {
                            MinValue: "",
                            MaxValue: "",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Detailed description of the SLA violation"
                        }
                    }
                },
                {
                    SortOrder: 3,
                    Name: "TimeSpan",
                    Key: "SLA-VIOLATION-TIMESPAN",
                    DisplayName: "Time Span",
                    FieldValueType: {
                        SortOrder: 2,
                        FieldType: "Numeric",
                        SharePointCode: "Number",
                        ValueType: "Number",
                        DisplayName: "Time Value",
                        MetaData: {
                            MinValue: "0",
                            MaxValue: "999999",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Time span value for the SLA"
                        }
                    }
                },
                {
                    SortOrder: 4,
                    Name: "TimeSpanInterval",
                    Key: "SLA-VIOLATION-TIMESPAN-INTERVAL",
                    DisplayName: "Time Unit",
                    FieldValueType: {
                        SortOrder: 1,
                        FieldType: "Single Line of Text",
                        SharePointCode: "Text",
                        ValueType: "String",
                        DisplayName: "Time Interval",
                        MetaData: {
                            MinValue: "",
                            MaxValue: "50",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Unit of time (hours, days, etc.)"
                        }
                    }
                },
                {
                    SortOrder: 5,
                    Name: "IsActive",
                    Key: "SLA-VIOLATION-IS-ACTIVE",
                    DisplayName: "Is Active",
                    FieldValueType: {
                        SortOrder: 3,
                        FieldType: "Yes/No",
                        SharePointCode: "Boolean",
                        ValueType: "Boolean",
                        DisplayName: "Active Status",
                        MetaData: {
                            MinValue: "",
                            MaxValue: "",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Whether this SLA violation type is active"
                        }
                    }
                }
            ]
        },
        
        // ================ REQUEST SLA VIOLATIONS TABLE ================
        {
            SortOrder: 14,
            Name: "RequestSLAViolations",
            Key: "REQUEST-SLA-VIOLATIONS-TABLE",
            DisplayName: "Request SLA Violations",
            Fields: [
                {
                    SortOrder: 1,
                    Name: "Title",
                    Key: "REQUEST-SLA-TITLE",
                    DisplayName: "Violation ID",
                    FieldValueType: {
                        SortOrder: 1,
                        FieldType: "Single Line of Text",
                        SharePointCode: "Text",
                        ValueType: "String",
                        DisplayName: "Violation Reference",
                        MetaData: {
                            MinValue: "",
                            MaxValue: "255",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "Unique violation identifier"
                        }
                    }
                },
                {
                    SortOrder: 2,
                    Name: "RequestID",
                    Key: "REQUEST-SLA-REQUEST-ID",
                    DisplayName: "Request",
                    FieldValueType: {
                        SortOrder: 2,
                        FieldType: "Numeric",
                        SharePointCode: "Number",
                        ValueType: "Number",
                        DisplayName: "Request Reference",
                        MetaData: {
                            MinValue: "0",
                            MaxValue: "999999",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "ID of the request with SLA violation"
                        }
                    }
                },
                {
                    SortOrder: 3,
                    Name: "SLAViolationID",
                    Key: "REQUEST-SLA-VIOLATION-ID",
                    DisplayName: "SLA Violation Type",
                    FieldValueType: {
                        SortOrder: 2,
                        FieldType: "Numeric",
                        SharePointCode: "Number",
                        ValueType: "Number",
                        DisplayName: "Violation Type Reference",
                        MetaData: {
                            MinValue: "0",
                            MaxValue: "999999",
                            DecimalPlaces: 0,
                            Formatting: "",
                            Description: "ID of the SLA violation type"
                        }
                    }
                }
            ]
        }
    ]
};
```
---

## History

| Date | Author | Changes |
|------|--------|---------|
| 2026-01-27 | Migration | Initial TOC and history section added |
