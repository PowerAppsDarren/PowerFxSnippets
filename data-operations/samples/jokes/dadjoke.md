---
title: "Sample Data: Dad Jokes Collection"
description: "Collection of family-friendly dad jokes for testing and entertainment"
license: "MIT"
category: "data-management"
subcategory: "samples"
tags:
  - sample-data
  - csv
  - jokes
  - humor
  - entertainment
difficulty: beginner
products:
  - power-apps-canvas
author: "PowerAppsDarren"
created: 2024-01-01
updated: 2024-12-17
---

## Overview

A curated collection of classic dad jokes perfect for testing Power Apps features like galleries, random selection, and text display. Great for building fun applications or adding humor to demos.

## Columns

| Column | Type   | Description                            |
|--------|--------|----------------------------------------|
| ID     | Number | Unique identifier for each joke        |
| Title  | Text   | The setup or question part of the joke |
| Answer | Text   | The punchline or answer                |

## Use Cases

- Building a "Joke of the Day" app
- Testing gallery controls with text-heavy content
- Creating random selection demonstrations
- Building entertainment or team morale apps
- Educational apps for children

## File Details

- **Format**: CSV
- **Encoding**: UTF-8 with BOM
- **Rows**: ~100 jokes

## Sample Jokes

| Title                                   | Answer                    |
|-----------------------------------------|---------------------------|
| Why don't skeletons fight each other?   | They don't have the guts. |
| What do you call a fish with no eyes?   | Fsh.                      |
| Why did the coffee file a police report?| It got mugged.            |

## Sample Power Fx Usage

```powerfx
// Display random joke
With(
    {randomJoke: Last(FirstN(Shuffle(colDadJokes), 1))},
    Notify(randomJoke.Title & " - " & randomJoke.Answer, NotificationType.Information)
)

// Search jokes
Filter(colDadJokes, txtSearch.Text in Title || txtSearch.Text in Answer)

// Count total jokes
CountRows(colDadJokes)
```

## Building a Joke App

```powerfx
// OnSelect of "Next Joke" button
UpdateContext({
    locCurrentJoke: Last(FirstN(Shuffle(colDadJokes), 1))
})

// Display setup
locCurrentJoke.Title

// Display punchline (reveal button)
locCurrentJoke.Answer
```

## Notes

- All jokes are family-friendly and appropriate for all ages
- Great for icebreakers and team building applications
- Can be combined with timer controls for automated joke rotation
