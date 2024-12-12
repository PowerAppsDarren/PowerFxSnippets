# ForAll Function

Even though ForAll is a [declarative function](Canvas Function List), you can use imperative code inside of it (as long as the code block is imperative, like an OnSelect) like a Patch function. 

In a declarative property of a control, you can use it to construct data to be used as a data source, like the Gallery.Items property. Because Gallery.Items doesn't start with "On___", we know it is declarative, and you cannot use imperative functions in it, like the Patch. 

The Sequence function goes well with ForAll like peanut and jelly! The following code gives you something you can use as a table/collection value...

```PowerFx
ForAll(
    Sequence(100), 
    {
        Value: "Item #" & ThisItem.Value
    }
)
```