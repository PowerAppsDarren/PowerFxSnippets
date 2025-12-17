# Image to Base 64 String

This is some YAML you can paste into your canvas Power Apps applciation that will 

## Add This to Your Application

```PowerFx
Substitute(
    JSON(
        imgUpdatedImage.Image,
        JSONFormat.IncludeBinaryData
    ),
    """",
    ""
)
```

