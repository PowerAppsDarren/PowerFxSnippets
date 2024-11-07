# Find Proportional Value

Calculates a proportional value based on two related fractions where one value is unknown.

Given two equivalent fractions (Known/KnownDenominator = UnknownNumerator/UnknownDenominator),
Solves for either UnknownNumerator or UnknownDenominator, but not both.

## Add This to Your Application

```PowerFx    
/* ===========================================================================================

    Calculates a proportional value based on two related fractions where one value is unknown.

    Given two equivalent fractions (Known/KnownDenominator = UnknownNumerator/UnknownDenominator),
    solves for either UnknownNumerator or UnknownDenominator, but not both.

    Parameters:
        Known (Number): The known value in the first fraction
        KnownDenominator (Number): The denominator of the first fraction
        UnknownNumerator (Number): The numerator of the second fraction (provide Blank() if this is what you're solving for)
        UnknownDenominator (Number): The denominator of the second fraction (provide Blank() if this is what you're solving for)

    Returns:
        Number: The calculated unknown value

    Throws:
        Error if both UnknownNumerator and UnknownDenominator are provided

    Example 1 - Finding numerator:
        If Known/KnownDenominator = x/10, and Known = 5, KnownDenominator = 2
        fxFindProportionalValue(5, 2, Blank(), 10) returns 25

    Example 2 - Finding denominator:
        If Known/KnownDenominator = 25/x, and Known = 5, KnownDenominator = 2
        fxFindProportionalValue(5, 2, 25, Blank()) returns 10

    ===========================================================================*/
    fxFindProportionalValue(Known:Number, KnownDenominator:Number, UnknownNumerator:Number, UnknownDenominator:Number):Number = 
        With(
            {
                KnownFraction: Known / KnownDenominator,
                UnknownFraction: UnknownNumerator / UnknownDenominator
            },
            If(
                IsBlank(UnknownNumerator),
                KnownFractionUnknownDenominator,
                If(
                    IsBlank(UnknownDenominator),
                    UnknownNumerator / KnownFraction,
                    Error("Both numerator and denominator of the unknown fraction are provided.")
                )
            )
        );
```

Here is some YAML code you can paste onto a screen to use or test:

```YAML    
- Container2:
    Control: GroupContainer
    Variant: manualLayoutContainer
    Properties:
      BorderThickness: =2
      DropShadow: =DropShadow.Semibold
      Fill: =RGBA(245, 245, 245, 1)
      Height: =185
      Width: =547
      X: =84
      Y: =68
    Children:
    - txtDenominator:
        Control: Classic/TextInput
        Properties:
          Default: ="16"
          Format: =TextFormat.Number
          Width: =100
          X: =40
          Y: =104
    - txtNumerator:
        Control: Classic/TextInput
        Properties:
          Default: ="9"
          Format: =TextFormat.Number
          Width: =100
          X: =40
          Y: =40
    - txtUnknownDenominator:
        Control: Classic/TextInput
        Properties:
          Default: ="804"
          Format: =TextFormat.Number
          Width: =100
          X: =243
          Y: =104
    - txtUnknownNumberator:
        Control: Classic/TextInput
        Properties:
          Default: =
          Format: =TextFormat.Number
          Width: =100
          X: =243
          Y: =40
    - Label3:
        Control: Label
        Properties:
          Text: |-
            =If(
                Len(txtUnknownDenominator.Text) = 0, 
                fxSolveFraction(
                    Value(txtNumerator.Text), 
                    Value(txtDenominator.Text), 
                    Value(txtUnknownNumberator.Text),
                    Blank()
                )
            )
          BorderStyle: =BorderStyle.Dashed
          BorderThickness: =1
          X: =356
          Y: =104
    - Label3_1:
        Control: Label
        Properties:
          Text: |-
            =If(
                Len(txtUnknownNumberator.Text) = 0, 
                fxSolveFraction(
                    Value(txtNumerator.Text), 
                    Value(txtDenominator.Text),
                    Blank(),
                    Value(txtUnknownDenominator.Text)
                )
            )
          BorderStyle: =BorderStyle.Dashed
          BorderThickness: =1
          X: =356
          Y: =40
```

## Final Considerations

I hope you have found this helpful. If you need any help with the Power Platform, don't hesitate to email us at 
* [support@superpowerlabs.co](support@superpowerlabs.co).
* https://powerplatformlinks.com
