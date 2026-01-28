---
title: "Encode Decode"
description: "Comprehensive URL encoding and decoding functions to handle special characters and ensure proper data transmission in web contexts."
category: "business-logic"
subcategory: "encoding-decoding"
tags:
  - encoding
  - decoding
  - url-encoding
  - text-processing
difficulty: intermediate
products:
  - power-apps-canvas
author: "Unknown"
created: 2026-01-22
updated: 2026-01-22
license: "MIT"
---
# Encode Decode

```
Substitute(
    Substitute(
        Substitute(
            Substitute(
                Substitute(
                    Substitute(
                        Substitute(
                            Substitute(
                                Substitute(
                                    Substitute(
                                        Substitute(
                                            Substitute(
                                                Substitute(
                                                    Substitute(
                                                        Substitute(
                                                            Substitute(
                                                                Substitute(
                                                                    Substitute(
                                                                        Substitute(
                                                                            Substitute(
                                                                                Substitute(
                                                                                    Substitute(
                                                                                        Substitute(
                                                                                            Substitute(
                                                                                                Substitute(
                                                                                                    Substitute(
                                                                                                        Substitute(
                                                                                                            Substitute(
                                                                                                                Substitute(
                                                                                                                    Substitute(
                                                                                                                        Substitute(
                                                                                                                            Substitute(
                                                                                                                                Substitute(
                                                                                                                                    Substitute(
                                                                                                                                        Last(
                                                                                                                                            ForAll(
                                                                                                                                                Split(
                                                                                                                                                    DecodeURL.UrlToDecode,
                                                                                                                                                    ","
                                                                                                                                                ),
                                                                                                                                                {Result: ThisRecord.Value}
                                                                                                                                            )
                                                                                                                                        ).Result,
                                                                                                                                        "%21",
                                                                                                                                        "!"
                                                                                                                                    ),
                                                                                                                                    "%22",
                                                                                                                                    "'"
                                                                                                                                ),
                                                                                                                                "%23",
                                                                                                                                "#"
                                                                                                                            ),
                                                                                                                            "%24",
                                                                                                                            "$"
                                                                                                                        ),
                                                                                                                        "%25",
                                                                                                                        "%"
                                                                                                                    ),
                                                                                                                    "%26",
                                                                                                                    "&"
                                                                                                                ),
                                                                                                                "%27",
                                                                                                                "'"
                                                                                                            ),
                                                                                                            "%28",
                                                                                                            "("
                                                                                                        ),
                                                                                                        "%29",
                                                                                                        ")"
                                                                                                    ),
                                                                                                    "%2A",
                                                                                                    "*"
                                                                                                ),
                                                                                                "%2B",
                                                                                                "+"
                                                                                            ),
                                                                                            "%2C",
                                                                                            ","
                                                                                        ),
                                                                                        "%3C",
                                                                                        "<"
                                                                                    ),
                                                                                    "%3E",
                                                                                    ">"
                                                                                ),
                                                                                "%2D",
                                                                                "-"
                                                                            ),
                                                                            "%2F",
                                                                            "/"
                                                                        ),
                                                                        "%2E",
                                                                        "."
                                                                    ),
                                                                    "%7B",
                                                                    "{"
                                                                ),
                                                                "%7D",
                                                                "}"
                                                            ),
                                                            "%7C",
                                                            "|"
                                                        ),
                                                        "%5C",
                                                        ""
                                                    ),
                                                    "%5E",
                                                    "^"
                                                ),
                                                "%7E",
                                                "~"
                                            ),
                                            "%5B",
                                            "["
                                        ),
                                        "%5D",
                                        "]"
                                    ),
                                    "%60",
                                    "`"
                                ),
                                "%80",
                                "`"
                            ),
                            "%2F",
                            "/"
                        ),
                        "%3A",
                        ":"
                    ),
                    "%3B",
                    ";"
                ),
                "%3D",
                "="
            ),
            "%3F",
            "?"
        ),
        "%40",
        "@"
    ),
    "%27",
    "'"
)
---

## History

| Date | Author | Changes |
|------|--------|---------|
| 2026-01-27 | Migration | Initial TOC and history section added |
