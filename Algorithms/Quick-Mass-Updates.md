# Performing Mass Updates Quickly

There will always be a time where you need to fix data, sanitize it, or make it different for some reason. Even when you fix a bug that wrote data to a database; it doesn't mean the data was all fixed and made right when you fixed the bug! Find out to do mass updates or adding of records that are literally 10 times as fast as doing individual patches for each record in a loop. 

<iframe width="560" height="315" src="https://www.youtube.com/embed/0aonIcYUOsE?si=FD2ppmbzE13YUUa_" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

```PowerFx
// ================================================================
// Best way to do bulk updating to a persistent data source
//
//  - Go get the data by filtering out to get at precisely you 
//    intend to update. 
// 
//  - If you need to do bulk inserts (new records), it is still 
//    a good idea to do a filter to at least get the database
//    schema for that table. 
//
//          Example: Filter(DATASOURCE, fase)
//          // this will get you zero records, but the collection
//          // you put it into will have all the fields and types
//
// ================================================================
ClearCollect(
    colChevys,
    Filter(
        VehicleSample,
        Make = "Chevrolet"
    )
);

// ================================================================
// In memory collection updates are super fast
// Even if there are tons of records to update, performing the 
// insert or update in memory proves itself to almost seems to 
// happen instantaneously. 
// ================================================================
UpdateIf(
    colChevys, 
    // true here means all the records we have will be affected
    true,    
    {
        Make: "Chevy"
    }
);

// ================================================================
// Update them all in one shot
// If you're updating hundreds or even thousands of records, 
// it will still take some time, but it typically speeds up the 
// process 10 fold. 
// ================================================================
Patch(
    VehicleSample, 
    colChevys
);
```