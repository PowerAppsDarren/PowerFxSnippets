# New Topic Template

This is a template to be used for new code snippets for this code repository.

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
                    FirstName: M365User.givenName,
                    ManagerEmail: Office365Users.ManagerV2(M365User.id).mail,
                    LastName: M365User.surname,
                    Title: M365User.displayName,
                    UserEmail: M365User.mail,
                    EntraID: M365User.id,
                    OfficeLocation: M365User.officeLocation,
                    JobTitle: M365User.jobTitle,
                    Department: M365User.department,
                    PhotoBase64: Substitute(
                        JSON(
                            M365UserPhoto,
                            JSONFormat.IncludeBinaryData
                        ),
                        """",
                        ""
                    ),
                    PhotoBase64Length: Len(
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

## Final Considerations

I hope you have found this helpful. If you need any help with the Power Platform, don't hesitate to email us at [support@superpowerlabs.co](support@superpowerlabs.co).
