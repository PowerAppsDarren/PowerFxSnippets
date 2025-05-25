# Parsing JSON Returned by Flows

This is something you may not need to do often, but it is useful to know how to parse JSON returned by flows.

## Example

Suppose you have a flow that returns the following JSON:

```json
[
  {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
  },
  {
    "name": "Jane Smith",
    "age": 25,
    "city": "Los Angeles"
  }
]
```

Use Power Fx code like this to use the JSON:

```powerfx
UpdateContext(
    {
        locGetListListings: ParseJSON(pa_sp_list_list.Run(ThisItem.URL).response).value
    }
);
ClearCollect(
    colListListing, 
    ForAll(
        locGetListListings As My, 
        {
            Name:               Text(My.Name),
            DisplayName:        Text(My.DisplayName),
            Type:               Text(My.Type)
        }
    )    
);
```