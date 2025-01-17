# Eliminate String Within String (user-defined function)

```PowerFx
    fx_CodeGen_EliminateString(SourceString:Text, ToEliminate:Text):Text = (
        With( 
            {
                myLenString: Len(ToEliminate),
                myScreenFound: Not IsBlank(
                    Find(
                        Upper(ToEliminate), 
                        Upper(SourceString)
                    )
                ), 
                myScreenPosition: Find(
                    Upper(ToEliminate), 
                    Upper(SourceString)
                )
            }, 
            If( 
                myScreenFound, 
                Concatenate(
                    Left(SourceString, myScreenPosition - 1), 
                    Mid(SourceString, myScreenPosition + myLenString)
                ), 
                SourceString
            ) // & "--" & myScreenPosition
        )
    );
```