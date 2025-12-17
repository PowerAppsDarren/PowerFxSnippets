---
title: "Auto-Add User from Office 365"
description: "Automatically add the current user to the app's user table if they don't exist, retrieving profile information from Office 365 Users connector"
category: "integrations"
subcategory: "office365-users"
tags:
  - office365
  - users
  - auto-add
  - profile
  - authentication
difficulty: intermediate
products:
  - power-apps-canvas
dependencies:
  - Office365Users
author: "PowerFxSnippets Community"
created: 2025-11-20
updated: 2025-11-20
license: "MIT"
related: []
---

# Auto-Add User from Office 365

This pattern automatically adds the current user to the app's user table if they don't exist, retrieving profile information from the Office 365 Users connector.

## Security and Privacy Considerations

This pattern requires the **Office365Users** connector, which must be authorized by the user. The snippet reads and persists personal attributes including name, email, job title, department, manager, and photo.

**Important:**
- **Permissions:** Ensure users have granted necessary permissions to the Office365Users connector.
- **Data Minimization:** In production, review which fields are truly needed. Only collect data that is required for your application's functionality.
- **Photo Storage:** Storing user photos (PhotoBase64) can consume significant storage space and may have privacy implications. Consider avoiding storage of photos or moving them to a dedicated, access-controlled store where appropriate.
- **Compliance:** This snippet is a pattern and must be validated against your local organizational compliance rules and data privacy regulations (e.g., GDPR) before use.

## Step 01 - Add this code to your screen

```JavaScript
// ===========================================================
// AUTOMATICALLY ADD THIS USER, IF NEEDED
// ===========================================================
With(
    {
        M365User: Office365Users.MyProfileV2(),
        M365UserPhoto: Office365Users.UserPhotoV2(User().EntraObjectId)
    },
    If(
        CountRows(
            Filter(
                AppUser,
                UserEmail = User().Email
            )
        ) = 0,
        Set(
            gblCurrentUser,
            Patch(
                AppUser,
                Defaults(AppUser),
                {
                    FirstName: M365User.givenName,          // Optional: Remove if not needed
                    ManagerEmail: Office365Users.ManagerV2(M365User.id).mail, // Optional: Remove if not needed
                    LastName: M365User.surname,             // Optional: Remove if not needed
                    Title: M365User.displayName,            // Optional: Remove if not needed
                    UserEmail: M365User.mail,               // Required for identification
                    EntraID: M365User.id,                   // Required for identification
                    OfficeLocation: M365User.officeLocation,// Optional: Remove if not needed
                    JobTitle: M365User.jobTitle,            // Optional: Remove if not needed
                    Department: M365User.department,        // Optional: Remove if not needed
                    // Note: Storing photos should be avoided or moved to a dedicated, access-controlled store where appropriate.
                    PhotoBase64: Substitute(                // Optional: Remove if not needed
                        JSON(
                            M365UserPhoto,
                            JSONFormat.IncludeBinaryData
                        ),
                        """",
                        ""
                    ),
                    PhotoBase64Length: Len(                 // Optional: Remove if not needed
                        Substitute(
                            JSON(
                                M365UserPhoto,
                                JSONFormat.IncludeBinaryData
                            ),
                            """",
                            ""
                        )
                    )
                }
            )
        );,
        Set(
            gblCurrentUser,
            LookUp(
                AppUser,
                UserEmail = User().Email
            )
        );
    );
);
```
