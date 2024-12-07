


```
//
// Replace this GUID with the EntraID of the manager
// you'd like to use as the default, like the CEO. 
//
fxCEOEntraID = "7dafdcff-a8c2-4a85-a104-44264b223476";

fxGetEntraUser(Identifier:Text):fxEntraUser = ( 
    Office365Users.SearchUserV2({searchTerm: Identifier, top: 1})    
);

fxEntraUser := Type({
    aboutMe:Text,
    accountEnabled:Boolean,
    birthday:DateTime,
    businessPhones: [
        {
            Value:Text
        }
    ],
    city:Text,
    companyName:Text,
    country:Text,
    department:Text,
    displayName:Text,
    givenName:Text,
    hireDate:DateTime,
    id:Text,
    interests: [{Value:Text}],
    jobTitle:Text,
    mail:Text,
    mailNickname:Text,
    mobilePhone:Text,
    mySite:Text,
    officeLocation:Text,
    pastProjects: [{Value:Text}],
    postalCode:Text,
    preferredLanguage:Text,
    preferredName:Text,
    responsibilities: [{Value:Text}],
    schools: [{Value:Text}],
    skills: [{Value:Text}],
    state:Text,
    streetAddress:Text,
    surname:Text,
    userPrincipalName:Text,
    userType:Text
});

fxManagerDefault = (
    IfError(
        Office365Users.ManagerV2(User().EntraObjectId), 
        fxGetEntraUser(fxCEOEntraID), 
        Office365Users.ManagerV2(User().EntraObjectId)
    )
);
```