# Find Proportional Value

Calculates a proportional value based on two related fractions where one value is unknown.

 * Given two equivalent fractions (Known/KnownDenominator = UnknownNumerator/UnknownDenominator),
 * Solves for either UnknownNumerator or UnknownDenominator, but not both.

## Add This to Your Application

```PowerFx    
/**
 * Calculates a proportional value based on two related fractions where one value is unknown.
 * 
 * Given two equivalent fractions (Known/KnownDenominator = UnknownNumerator/UnknownDenominator),
 * solves for either UnknownNumerator or UnknownDenominator, but not both.
 * 
 * Parameters:
 *     Known (Number): The known value in the first fraction
 *     KnownDenominator (Number): The denominator of the first fraction
 *     UnknownNumerator (Number): The numerator of the second fraction (provide Blank() if this is what you're solving for)
 *     UnknownDenominator (Number): The denominator of the second fraction (provide Blank() if this is what you're solving for)
 * 
 * Returns:
 *     Number: The calculated unknown value
 * 
 * Throws:
 *     Error if both UnknownNumerator and UnknownDenominator are provided
 * 
 * Example 1 - Finding numerator:
 *     If Known/KnownDenominator = x/10, and Known = 5, KnownDenominator = 2
 *     fxFindProportionalValue(5, 2, Blank(), 10) returns 25
 * 
 * Example 2 - Finding denominator:
 *     If Known/KnownDenominator = 25/x, and Known = 5, KnownDenominator = 2
 *     fxFindProportionalValue(5, 2, 25, Blank()) returns 10
 */
fxFindProportionalValue(Known:Number, KnownDenominator:Number, UnknownNumerator:Number, UnknownDenominator:Number):Number = 
    With(
        {
            KnownFraction: Known / KnownDenominator,
            UnknownFraction: UnknownNumerator / UnknownDenominator
        },
        If(
            IsBlank(UnknownNumerator),
            KnownFraction * UnknownDenominator,
            If(
                IsBlank(UnknownDenominator),
                UnknownNumerator / KnownFraction,
                Error("Both numerator and denominator of the unknown fraction are provided.")
            )
        )
    );
```

## Final Considerations

I hope you have found this helpful. If you need any help with the Power Platform, don't hesitate to email us at [support@superpowerlabs.co](support@superpowerlabs.co).
