# Jokes Sample Data

## Table of Contents

- [Contents](#contents)
- [Dataset Details](#dataset-details)
  - [Dad Jokes](#dad-jokes)
- [Usage Ideas](#usage-ideas)
- [Quick Start](#quick-start)
- [Contributing](#contributing)

A collection of family-friendly joke datasets for testing and entertainment applications.

## Contents

| File          | Description                      |
|---------------|----------------------------------|
| `dadjoke.csv` | Collection of classic dad jokes  |
| `dadjoke.md`  | Dataset documentation            |

## Dataset Details

### Dad Jokes
- **Rows**: ~100 jokes
- **Format**: ID, Title (setup), Answer (punchline)
- **Audience**: Family-friendly, all ages

## Usage Ideas

- Joke of the Day apps
- Team morale boosters
- Kids' entertainment apps
- Demo applications
- Gallery control examples

## Quick Start

```powerfx
// Load jokes
ClearCollect(colJokes, 'dadjoke')

// Random joke
With(
    {joke: Last(FirstN(Shuffle(colJokes), 1))},
    "Q: " & joke.Title & Char(10) & "A: " & joke.Answer
)
```

## Contributing

Have more clean jokes to add? Feel free to extend the dataset!
---

## History

| Date | Author | Changes |
|------|--------|---------|
| 2026-01-27 | Migration | Initial TOC and history section added |
