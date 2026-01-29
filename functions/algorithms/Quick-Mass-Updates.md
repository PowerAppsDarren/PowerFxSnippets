---
title: "Performing Mass Updates Quickly"
description: "Learn how to efficiently perform mass updates or add records in a data source, speeding up the process significantly compared to making individual updates for each record."
category: "business-logic"
subcategory: "algorithms"
tags:
  - mass-updates
  - performance
  - data-operations
  - bulk-operations
difficulty: intermediate
products:
  - power-apps-canvas
author: "Unknown"
created: 2026-01-22
updated: 2026-01-22
license: "MIT"
---
# Performing Mass Updates Quickly

## Table of Contents

There will always be a time where you need to fix data, sanitize it, or make it different for some reason. Even when you fix a bug that wrote data to a database; it doesn't mean the data was all fixed and made right when you fixed the bug. Find out to do mass updates or adding of records that are literally 10 times as fast as doing individual patches for each record in a loop.

- [Associated YouTube Video Walkthrough](https://youtu.be/0aonIcYUOsE)

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
---

## History

| Date | Author | Changes |
|------|--------|---------|
| 2026-01-27 | Migration | Initial TOC and history section added |
