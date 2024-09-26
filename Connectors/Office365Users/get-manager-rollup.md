# Get Manager Rollup

The user and their manager and their manager and their manager, and so on.

## Add this code to your screen

```JavaScript
Clear(colManagers);
ForAll(
    Sequence(10) As My,
        If(
            My.Value = 1, 
            Collect(colManagers, gblCurrentUser), 
            If(
                Not IsBlank(Last(colManagers).ManagerEmail),
                Collect(
                    colManagers, 
                    With(
                        {
                            M365User:       Office365Users.ManagerV2(Last(colManagers).EntraID),
                            M365UserEmail:  Office365Users.ManagerV2(Last(colManagers).EntraID).mail,
                            M365UserPhoto:  Office365Users.UserPhotoV2(
                                                Office365Users.ManagerV2(Last(colManagers).EntraID).id
                                            )
                        }, 
                        If(
                            CountRows(
                                Filter(
                                    AppUser,
                                    UserEmail = M365UserEmail
                                )
                            ) = 0,
                            Patch(
                                AppUser,
                                Defaults(AppUser),
                                {
                                    FirstName:      M365User.givenName,
                                    ManagerEmail:   IfError(
                                        Office365Users.ManagerV2(M365User.id).mail, "", Office365Users.ManagerV2(M365User.id).mail),
                                    LastName:       M365User.surname,
                                    Title:          M365User.displayName,
                                    UserEmail:      M365User.mail,
                                    EntraID:        M365User.id,
                                    OfficeLocation: M365User.officeLocation,
                                    JobTitle:       M365User.jobTitle,
                                    Department:     M365User.department,
                                    PhotoBase64:    Substitute(
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
                            ),      
                            LookUp(
                                AppUser,
                                UserEmail = Office365Users.ManagerV2(Last(colManagers).EntraID).mail
                            )
                        );
                    )
                )
        )
    )
)
```

## Final Considerations

I hope you have found this helpful. If you need any help with the Power Platform, don't hesitate to email us at [support@superpowerlabs.co](support@superpowerlabs.co).
