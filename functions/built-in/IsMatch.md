# IsMatch

This is some YAML you can paste into your canvas Power Apps applciation that will 

## Add This to Your Application

```PowerFx
IsMatch(
    txtTime.Value, 
    "^(0?[1-9]|1[0-2]):[0-5][0-9](\s)?(AM|PM)$",
    MatchOptions.Complete
)
```

