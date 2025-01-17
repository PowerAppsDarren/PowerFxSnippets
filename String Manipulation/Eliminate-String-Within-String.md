# Eliminate String Within String (user-defined function)

This user-defined function will eliminate a string within another string. The function will return the source string with the string to eliminate removed. If the string to eliminate is not found, the source string is returned as is.

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