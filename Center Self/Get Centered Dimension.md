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
```

---

## Free Community & Course Materials

🆓 Get access to our [free community and resources](https://tinyurl.com/DarrensStuffFree) ⬅️

## Support

I hope you have found this helpful. If you need any help with the Power Platform, don't hesitate to message us from [Our Website](https://superpowerlabs.co)

## Disclaimer

THIS CODE IS PROVIDED **AS IS WITHOUT WARRANTY OF ANY KIND**, EITHER EXPRESS OR IMPLIED, INCLUDING ANY IMPLIED WARRANTIES OF FITNESS FOR A PARTICULAR PURPOSE, MERCHANTABILITY, OR NON-INFRINGEMENT.
