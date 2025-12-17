# Get Centered Dimension (X or Y for Self)

Need to center a control in relation to its parent dimension? Use this formula to get the X or Y value for the control.

```PowerFx
    //
    // Get the X or the Y of a control in relation to
    // its parent dimension.
    //
    // Understanding the parameters:
    //   - Pass in width values to get the X value for 'Self'
    //   - Pass in height values to get the Y value for 'Self'
    //
    fxGetCenteredDimension( ParentDimension:Number,
                            SelfDimension:Number):Number = (
        (ParentDimension - SelfDimension) / 2
    );

    // You could simply copy/paste this for X value for centered self
    // #️⃣ fxGetCenteredDimension(Parent.Width, Self.Width)
    // You could simply copy/paste this for Y value for centered self
    // #️⃣ fxGetCenteredDimension(Parent.Height, Self.Height)
```
