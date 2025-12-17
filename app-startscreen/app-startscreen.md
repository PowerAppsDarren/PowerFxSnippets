# App.StartScreen

This is a helpful canvas Power Apps code snippet.

## Add This to Your Application

```PowerFx
// ===================================================================================
// The following code is an example of how to implement "deep linking"
//      -Replace "QUERY_STRING_PARAMETER" with the parameter of your chioce
//      -Replace the string on the right side with what you want to match it with
//      -Pass the screen into the navigate function
// ===================================================================================
If(
    Param("QUERY_STRING_PARAMETER") = "QUERY_STRING_PARAMETER",
    'Loading Screen',
    'Loading Screen'
)
```


