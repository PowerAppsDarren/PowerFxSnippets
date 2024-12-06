# HEX to RGB

Credit: https://github.com/matthewdevaney/powerapps-custom-functions/tree/main/custom_functions_hiro

## Add This to Your Application

```PowerFx
With(
    {
        tblColdec: AddColumns(
            ForAll(Split(
                Lower(
                    Right(
                        HEX,
                        6
                    )
                ),
                ""
            ), {Result: ThisRecord.Value}),
            decimal,
            If(
                ThisRecord.Result in Sequence(
                    10,
                    0
                ),
                ThisRecord.Result,
                LookUp(
                    Table(
                        {
                            key: "a",
                            val: 10
                        },
                        {
                            key: "b",
                            val: 11
                        },
                        {
                            key: "c",
                            val: 12
                        },
                        {
                            key: "d",
                            val: 13
                        },
                        {
                            key: "e",
                            val: 14
                        },
                        {
                            key: "f",
                            val: 15
                        }
                    ),
                    key = Result
                ).val
            )
        )
    },
    With(
        {
            R: 16 * First(tblColdec).decimal + Last(
                FirstN(
                    tblColdec,
                    2
                )
            ).decimal,
            G: 16 * Last(
                FirstN(
                    tblColdec,
                    3
                )
            ).decimal + Last(
                FirstN(
                    tblColdec,
                    4
                )
            ).decimal,
            B: 16 * Last(
                FirstN(
                    tblColdec,
                    5
                )
            ).decimal + Last(
                FirstN(
                    tblColdec,
                    6
                )
            ).decimal
        },
        {
            Color: RGBA(
                R,
                G,
                B,
                1
            ),
            R: R,
            G: G,
            B: B
        }
    )
)
```

## Free Community & Course Materials 

🆓 Get access to our free Power Apps crash course (and our community) here: 
- https://tinyurl.com/DarrensStuffFree 🔗

## Support

I hope you have found this helpful. If you need any help with the Power Platform, don't hesitate to email us at 
* [support@superpowerlabs.co](support@superpowerlabs.co)
* https://superpowerlabs.co 

---

## Disclaimer

**THIS CODE IS PROVIDED AS IS WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING ANY IMPLIED WARRANTIES OF FITNESS FOR A PARTICULAR PURPOSE, MERCHANTABILITY, OR NON-INFRINGEMENT.**
