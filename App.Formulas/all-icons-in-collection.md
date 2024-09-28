# All Icons in canvas Power Apps

All the icons in canvas Power Apps are contained in an enumeration so you can easily referenced. Let's take this one step further and put them all into a collection so we can work with them much more easier. Just paste the code below in your App.Formulas.

## Add This to Your Application

```JavaScript
    fxIcons = Sort(
        [
            {
                Sequence:       1,
                Name:           "Add",
                Icon:           Icon.Add,
                Description:    "A plus sign icon indicating addition or creation of new items",
                Tags:           ["plus", "new", "create"],
                Category:       "Actions",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M11%2011v-11h1v11h11v1h-11v11h-1v-11h-11v-1h11z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       2,
                Name:           "Cancel",
                Icon:           Icon.Cancel,
                Description:    "An 'X' icon typically used to cancel actions or close dialogs",
                Tags:           ["close", "delete", "remove"],
                Category:       "Actions",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12%2011.293l10.293-10.293.707.707-10.293%2010.293%2010.293%2010.293-.707.707-10.293-10.293-10.293%2010.293-.707-.707%2010.293-10.293-10.293-10.293.707-.707%2010.293%2010.293z%22%2F%3E%3C%2Fsvg%3E"
            },
            {
                Sequence:       3,
                Name:           "CancelBadge",
                Icon:           Icon.CancelBadge,
                Description:    "An 'X' icon within a circular badge, often used to indicate cancellation or removal in a more prominent way",
                Tags:           ["close", "delete", "remove", "badge"],
                Category:       "Notifications",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12%200c6.623%200%2012%205.377%2012%2012s-5.377%2012-12%2012-12-5.377-12-12%205.377-12%2012-12zm0%201c6.071%200%2011%204.929%2011%2011s-4.929%2011-11%2011-11-4.929-11-11%204.929-11%2011-11zm0%2010.293l5.293-5.293.707.707-5.293%205.293%205.293%205.293-.707.707-5.293-5.293-5.293%205.293-.707-.707%205.293-5.293-5.293-5.293.707-.707%205.293%205.293z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       4,
                Name:           "Edit",
                Icon:           Icon.Edit,
                Description:    "A pencil icon typically used to represent editing or modifying content",
                Tags:           ["modify", "change", "update", "pencil"],
                Category:       "Actions",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12%200c6.623%200%2012%205.377%2012%2012s-5.377%2012-12%2012-12-5.377-12-12%205.377-12%2012-12zm0%201c6.071%200%2011%204.929%2011%2011s-4.929%2011-11%2011-11-4.929-11-11%204.929-11%2011-11zm0%2010.293l5.293-5.293.707.707-5.293%205.293%205.293%205.293-.707.707-5.293-5.293-5.293%205.293-.707-.707%205.293-5.293-5.293-5.293.707-.707%205.293%205.293z%22%2F%3E%3C%2Fsvg%3E"
            },
            {
                Sequence:       5,
                Name:           "Check",
                Icon:           Icon.Check,
                Description:    "A checkmark icon often used to indicate completion, confirmation, or selection",
                Tags:           ["complete", "confirm", "select", "approve"],
                Category:       "Actions",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M21%206.285l-11.16%2012.733-6.84-6.018%201.319-1.49%205.341%204.686%209.865-11.196%201.475%201.285z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       6,
                Name:           "CheckBadge",
                Icon:           Icon.CheckBadge,
                Description:    "A checkmark icon within a circular badge, typically used to indicate successful completion or approval in a more prominent way",
                Tags:           ["complete", "confirm", "approve", "badge", "success"],
                Category:       "Notifications",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12%200c6.623%200%2012%205.377%2012%2012s-5.377%2012-12%2012-12-5.377-12-12%205.377-12%2012-12zm0%201c6.071%200%2011%204.929%2011%2011s-4.929%2011-11%2011-11-4.929-11-11%204.929-11%2011-11zm7%207.457l-9.005%209.565-4.995-5.865.761-.649%204.271%205.016%208.24-8.752.728.685z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       7,
                Name:           "Search",
                Icon:           Icon.Search,
                Description:    "A magnifying glass icon typically used for search functionality or to indicate a search action",
                Tags:           ["find", "lookup", "explore", "magnifying glass"],
                Category:       "Actions",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M15.853%2016.56c-1.683%201.517-3.911%202.44-6.353%202.44-5.243%200-9.5-4.257-9.5-9.5s4.257-9.5%209.5-9.5%209.5%204.257%209.5%209.5c0%202.442-.923%204.67-2.44%206.353l7.44%207.44-.707.707-7.44-7.44zm-6.353-15.56c4.691%200%208.5%203.809%208.5%208.5s-3.809%208.5-8.5%208.5-8.5-3.809-8.5-8.5%203.809-8.5%208.5-8.5z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       8,
                Name:           "Filter",
                Icon:           Icon.Filter,
                Description:    "A funnel-like icon typically used to represent filtering or sorting options",
                Tags:           ["sort", "funnel", "refine", "narrow"],
                Category:       "Data",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M24%2024h-24v-24h24v24zm-22-22v20h20v-20h-20zm20 1h-19v3h19v-3zm-2 5h-15v3h15v-3zm-3 5h-9v3h9v-3z%22%2F%3E%3C%2Fsvg%3E"
            },
            {
                Sequence:       9,
                Name:           "FilterFlat",
                Icon:           Icon.FilterFlat,
                Description:    "A simplified filter icon, typically used to represent filtering or sorting options in a flat design style",
                Tags:           ["sort", "funnel", "refine", "narrow", "flat"],
                Category:       "Data",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M1%201h22v4h-22v-4zm3%206h16v4h-16v-4zm3%206h10v4h-10v-4z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       10,
                Name:           "FilterFlatFilled",
                Icon:           Icon.FilterFlatFilled,
                Description:    "A filled version of the simplified filter icon, representing filtering or sorting options in a flat, solid design style",
                Tags:           ["sort", "funnel", "refine", "narrow", "flat", "filled"],
                Category:       "Data",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M0%200h24v6h-24v-6zm4%208h16v6h-16v-6zm4%208h8v6h-8v-6z%22%2F%3E%3C%2Fsvg%3E"
            },
            {
                Sequence:       11,
                Name:           "Sort",
                Icon:           Icon.Sort,
                Description:    "An icon representing sorting functionality, typically shown as stacked horizontal lines of decreasing length",
                Tags:           ["order", "arrange", "organize", "sequence"],
                Category:       "Data",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M3%204h18v2H3V4zm0%207h14v2H3v-2zm0%207h8v2H3v-2z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       12,
                Name:           "Reload",
                Icon:           Icon.Reload,
                Description:    "A circular arrow icon typically used to represent reloading, refreshing, or syncing content",
                Tags:           ["refresh", "update", "sync", "circular"],
                Category:       "Actions",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M23%2012c0%206.075-4.925%2011-11%2011S1%2018.075%201%2012%205.925%201%2012%201c2.357%200%204.545.74%206.33%202h-4.33v2h7V0h-2v3.102A10.954%2010.954%200%200012%201C5.373%201%200%206.373%200%2012s5.373%2011%2012%2011%2012-5.373%2012-11h-1z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       13,
                Name:           "Trash",
                Icon:           Icon.Trash,
                Description:    "A trash can icon typically used to represent deletion or removal of items",
                Tags:           ["delete", "remove", "discard", "bin"],
                Category:       "Actions",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M19%2024h-14c-1.104%200-2-.896-2-2v-16h18v16c0%201.104-.896%202-2%202zm-7-10.414l3.293-3.293%201.414%201.414-3.293%203.293%203.293%203.293-1.414%201.414-3.293-3.293-3.293%203.293-1.414-1.414%203.293-3.293-3.293-3.293%201.414-1.414%203.293%203.293zm10-8.586h-20v-2h6v-1.5c0-.827.673-1.5%201.5-1.5h5c.825%200%201.5.671%201.5%201.5v1.5h6v2zm-8-3h-4v1h4v-1z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       14,
                Name:           "Save",
                Icon:           Icon.Save,
                Description:    "A floppy disk icon typically used to represent saving or storing data",
                Tags:           ["store", "preserve", "record", "floppy"],
                Category:       "Actions",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M22%2024h-20v-24h14l6%206v18zm-7-23h-12v22h18v-16h-6v-6zm3%2015v1h-12v-1h12zm0-3v1h-12v-1h12zm0-3v1h-12v-1h12zm-2-4h-3v-4h3v4z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       15,
                Name:           "Download",
                Icon:           Icon.Download,
                Description:    "An arrow pointing downward into a tray, typically used to represent downloading or saving files",
                Tags:           ["save", "retrieve", "get", "arrow"],
                Category:       "Actions",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M11%201v16.6l-4.3-4.3-1.4%201.4%206.7%206.7%206.7-6.7-1.4-1.4-4.3%204.3v-16.6h-2zm-9%2020v2h20v-2h-20z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       16,
                Name:           "Copy",
                Icon:           Icon.Copy,
                Description:    "Two overlapping rectangles, typically used to represent copying or duplicating content",
                Tags:           ["duplicate", "clone", "replicate", "paste"],
                Category:       "Actions",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M20%208v-8h-14v24h14v-8h4v-8h-4zm-6%204h2v4h-2v-4zm-10-12h10v20h-10v-20zm14%13v5h-2v-3h-6v3h-2v-5h10zm0-13v5h-10v-5h10z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       17,
                Name:           "LikeDislike",
                Icon:           Icon.LikeDislike,
                Description:    "A combination of thumbs up and thumbs down icons, typically used for rating or feedback",
                Tags:           ["feedback", "rating", "thumbs", "vote"],
                Category:       "Social",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12%200l5.5%205.5-1.5%201.5-2-2v6h6l-2-2%201.5-1.5%205.5%205.5-5.5%205.5-1.5-1.5%202-2h-6v6l2-2%201.5%201.5-5.5%205.5-5.5-5.5%201.5-1.5%202%202v-6h-6l2%202-1.5%201.5-5.5-5.5%205.5-5.5%201.5%201.5-2%202h6v-6l-2%202-1.5-1.5z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       18,
                Name:           "Crop",
                Icon:           Icon.Crop,
                Description:    "An icon representing the crop tool, typically used in image editing to trim or resize images",
                Tags:           ["trim", "resize", "edit", "image"],
                Category:       "Design",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M24%2020h-4v-4h-2v4h-14v-14h4v-2h-4v-4h-2v4h-2v2h2v14h14v2h2v-2h4v-2zm-8-12h-10v10h10v-10z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       19,
                Name:           "Pin",
                Icon:           Icon.Pin,
                Description:    "An icon representing a pushpin, typically used to indicate location or to 'pin' items for quick access",
                Tags:           ["location", "mark", "save", "bookmark"],
                Category:       "Navigation",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M9%2024l3-6h-6l4-18h7l-3%2012h6l-11%2012zm-2-8h6l-2%204.059v-4.059h-4z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       20,
                Name:           "ClearDrawing",
                Icon:           Icon.ClearDrawing,
                Description:    "An icon representing clearing or erasing a drawing, typically shown as an eraser or clear canvas",
                Tags:           ["erase", "clear", "delete", "reset"],
                Category:       "Design",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M5.662%2023l-5.369-5.365c-.195-.195-.293-.45-.293-.707%200-.256.098-.512.293-.707l14.929-14.928c.195-.194.451-.293.707-.293.255%200%20.512.099.707.293l7.071%207.073c.196.195.293.451.293.708%200%20.256-.097.511-.293.707l-11.216%2011.219h5.514v2h-12.343zm3.657-2l-5.486-5.486-1.419%201.414%204.076%204.072h2.829zm.456-11.429l-4.528%204.528%205.658%205.659%204.527-4.53-5.657-5.657z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       21,
                Name:           "ExpandView",
                Icon:           Icon.ExpandView,
                Description:    "An icon representing expanding or enlarging a view, typically shown as outward-pointing arrows",
                Tags:           ["enlarge", "maximize", "fullscreen", "zoom"],
                Category:       "View",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M24%200l-6%206-1.41-1.41%204.59-4.59h-5.18v-2h8v8h-2v-5.18l-4.59%204.59-1.41-1.41%206-6zm-24%2024l6-6%201.41%201.41-4.59%204.59h5.18v2h-8v-8h2v5.18l4.59-4.59%201.41%201.41-6%206z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       22,
                Name:           "CollapseAll",
                Icon:           Icon.CollapseView,
                Description:    "An icon representing the action to collapse all expanded items or sections, typically shown as inward-pointing arrows",
                Tags:           ["collapse", "minimize", "shrink", "fold"],
                Category:       "View",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12%2011.293l10.293-10.293.707.707-11%2011-11-11%20.707-.707%2010.293%2010.293zm0%205.414l-10.293-10.293-.707.707%2011%2011%2011-11-.707-.707-10.293%2010.293z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       23,
                Name:           "Draw",
                Icon:           Icon.Draw,
                Description:    "An icon representing a drawing tool, typically shown as a pencil or brush for creating or editing graphics",
                Tags:           ["pencil", "sketch", "create", "design"],
                Category:       "Design",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M19.479%202l2.521%202.521-14.864%2014.864-5.136%201.615%201.615-5.136%2014.864-14.864zm3.521%201.229l-1.886-1.886-14.511%2014.511-1.005%203.184%203.184-1.005%2014.218-14.804zm-8.911%2010.693l-2.416%202.418-.707-.707%202.418-2.418.705.707zm-3.685-6.567l2.525%202.525-.707.707-2.525-2.525.707-.707zm5.992%205.99l-2.416%202.418-.707-.707%202.418-2.418.705.707z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       24,
                Name:           "Compose",
                Icon:           Icon.Compose,
                Description:    "An icon representing the action of composing or writing, typically shown as a pen or pencil with paper",
                Tags:           ["write", "create", "edit", "document"],
                Category:       "Communication",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M22%2024h-20v-24h14l6%206v18zm-7-23h-12v22h18v-16h-6v-6zm1%205h4.586l-4.586-4.586v4.586zm-3%2013h3v-1h-3v1zm0-2h3v-1h-3v1zm0-2h8v-1h-8v1zm0-2h8v-1h-8v1zm0-2h8v-1h-8v1zm-4-2v8h1v-8h-1zm2.448%204.751l.552.449v-5.2h-1v5.2l.552-.449c.97-.791%202.294-.781%203.248.029l.552.449v-5.678h-1v2.849l.448-.366c.967-.789%202.292-.781%203.252.025l.3.245v-2.753h-1v1.589l.552-.449c.97-.791%202.294-.781%203.248.029l.552.449v-6.118h-13v12h2.448zm.552%203.249l1-1v-5.998h-2v5.998l1%201zm5%200l1-1v-5.998h-2v5.998l1%201zm5%200l1-1v-5.998h-2v5.998l1%201z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       25,
                Name:           "Erase",
                Icon:           Icon.Erase,
                Description:    "An icon representing an eraser tool, typically used for removing or deleting content in drawing or editing applications",
                Tags:           ["delete", "remove", "clear", "clean"],
                Category:       "Design",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M5.662%2023l-5.369-5.365c-.195-.195-.293-.45-.293-.707%200-.256.098-.512.293-.707l14.929-14.928c.195-.194.451-.293.707-.293.255%200%20.512.099.707.293l7.071%207.073c.196.195.293.451.293.708%200%20.256-.097.511-.293.707l-11.216%2011.219h5.514v2h-12.343zm3.657-2l-5.486-5.486-1.419%201.414%204.076%204.072h2.829zm.456-11.429l-4.528%204.528%205.658%205.659%204.527-4.53-5.657-5.657z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       26,
                Name:           "Message",
                Icon:           Icon.Message,
                Description:    "An icon representing a message or chat bubble, typically used for communication or messaging features",
                Tags:           ["chat", "communication", "text", "speech"],
                Category:       "Communication",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M24%2020h-3v4l-5.333-4h-7.667v-4h2v2h6.333l2.667%202v-2h3v-8.001h-2v-2h4v12.001zm-6-6h-9.667l-5.333%204v-4h-3v-14.001h18v14.001zm-9-4.084h9v-1.831h-9v1.831zm0-3.415h9v-1.829h-9v1.829zm-5-3.5h14v-1.001h-14v1.001z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       27,
                Name:           "Post",
                Icon:           Icon.Post,
                Description:    "An icon representing a post or publication, typically shown as a document or note being sent or published",
                Tags:           ["publish", "send", "share", "submit"],
                Category:       "Communication",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M24%2021h-24v-18h24v18zm-23-16.477v15.477h22v-15.477l-10.999%2010-11.001-10zm21.089-.523h-20.176l10.088%209.171%2010.088-9.171z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       28,
                Name:           "AddDocument",
                Icon:           Icon.AddDocument,
                Description:    "An icon representing the action of adding a new document, typically shown as a document with a plus sign",
                Tags:           ["new", "create", "file", "add"],
                Category:       "Files",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M22%2024h-20v-24h14l6%206v18zm-7-23h-12v22h18v-16h-6v-6zm3%2015v1h-12v-1h12zm0-3v1h-12v-1h12zm0-3v1h-12v-1h12zm-2-4h4.586l-4.586-4.586v4.586z%22%2F%3E%3Cpath%20d%3D%22M16%2016h-3v3h-2v-3h-3v-2h3v-3h2v3h3v2z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       29,
                Name:           "AddLibrary",
                Icon:           Icon.AddLibrary,
                Description:    "An icon representing the action of adding a new library or collection, typically shown as multiple documents or books with a plus sign",
                Tags:           ["collection", "books", "add", "create"],
                Category:       "Files",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M22%2024h-17c-1.657%200-3-1.343-3-3v-18c0-1.657%201.343-3%203-3h17v24zm-2-4h-14.505c-1.375%200-1.375%202%200%202h14.505v-2zm0-18h-15v16h15v-16zm-3%2012v1h-9v-1h9zm0-3v1h-9v-1h9zm0-3v1h-9v-1h9z%22%2F%3E%3Cpath%20d%3D%22M16%2016h-3v3h-2v-3h-3v-2h3v-3h2v3h3v2z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       30,
                Name:           "Import",
                Icon:           Icon.Import,
                Description:    "An icon representing the action of importing data or files, typically shown as an arrow pointing into a box or document",
                Tags:           ["upload", "transfer", "input", "inbound"],
                Category:       "Data",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M16%2016h-14v-12h14v12zm2-12v12h-1v2h-16v-14h17zm-7%2012v-8l-4%208h4zm7-12h-16v12h1v-11h15v-1zm-4.5%2010c-.276%200-.5.224-.5.5s.224.5.5.5.5-.224.5-.5-.224-.5-.5-.5z%22%2F%3E%3Cpath%20d%3D%22M11%207.492v4.508h2v-4.508l2.538%202.598%201.414-1.414-4.952-5.068-4.952%205.068%201.414%201.414%202.538-2.598z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       31,
                Name:           "Export",
                Icon:           Icon.Export,
                Description:    "An icon representing the action of exporting data or files, typically shown as an arrow pointing out of a box or document",
                Tags:           ["download", "transfer", "output", "outbound"],
                Category:       "Data",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M16%2016h-14v-12h14v12zm2-12v12h-1v2h-16v-14h17zm-7%2012v-8l-4%208h4zm7-12h-16v12h1v-11h15v-1zm-4.5%2010c-.276%200-.5.224-.5.5s.224.5.5.5.5-.224.5-.5-.224-.5-.5-.5z%22%2F%3E%3Cpath%20d%3D%22M11%2012v-4.508l-2.538%202.598-1.414-1.414%204.952-5.068%204.952%205.068-1.414%201.414-2.538-2.598v4.508h-2z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       32,
                Name:           "QuestionMark",
                Icon:           Icon.QuestionMark,
                Description:    "An icon representing a question or help, typically shown as a question mark symbol",
                Tags:           ["help", "inquiry", "support", "information"],
                Category:       "Information",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12%200c6.623%200%2012%205.377%2012%2012s-5.377%2012-12%2012-12-5.377-12-12%205.377-12%2012-12zm0%201c6.071%200%2011%204.929%2011%2011s-4.929%2011-11%2011-11-4.929-11-11%204.929-11%2011-11zm.053%2017c.466%200%20.844-.378.844-.845%200-.466-.378-.844-.844-.844-.466%200-.845.378-.845.844%200%20.467.379.845.845.845zm.468-2.822h-.998c-.035-1.162.182-2.054.939-2.943.491-.57%201.607-1.479%201.945-2.058.722-1.229.077-2.358-.82-2.645-.9-.287-1.926-.082-2.516.636l-.701-.701c.725-.903%201.943-1.357%203.215-1.076%201.272.282%202.028%201.542%201.747%202.742-.181.775-1.215%201.549-1.88%202.204-.665.655-.962%201.408-.931%203.841zm-.053-13.178c4.97%200%209%204.03%209%209s-4.03%209-9%209-9-4.03-9-9%204.03-9%209-9z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       33,
                Name:           "Help",
                Icon:           Icon.Help,
                Description:    "An icon representing assistance or support, typically shown as a question mark or a lifebuoy",
                Tags:           ["support", "assistance", "guidance", "information"],
                Category:       "Information",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12%200c6.623%200%2012%205.377%2012%2012s-5.377%2012-12%2012-12-5.377-12-12%205.377-12%2012-12zm0%201c6.071%200%2011%204.929%2011%2011s-4.929%2011-11%2011-11-4.929-11-11%204.929-11%2011-11zm.5%2017h-1v-2h1v2zm1.6-5.605c-.362.373-.642.619-.842.737-.201.117-.458.176-.769.176-.67%200-1.237-.198-1.7-.594-.462-.396-.694-.948-.694-1.658%200-.436.107-.817.321-1.144.214-.327.518-.602.911-.824-.154-.181-.291-.351-.411-.509-.12-.158-.214-.323-.282-.495-.068-.172-.102-.360-.102-.563%200-.468.138-.858.414-1.168.276-.311.684-.466%201.226-.466.488%200%20.883.128%201.185.384.303.256.454.611.454%201.063%200%20.262-.058.495-.174.696-.116.201-.3.405-.553.612l-.651.509c-.204.153-.356.307-.454.461-.098.154-.146.354-.146.598h-1.18c0-.361.073-.674.22-.939.146-.265.382-.518.706-.759l.648-.48c.193-.145.332-.292.419-.44.086-.15.13-.323.13-.521%200-.287-.092-.512-.275-.675-.184-.163-.445-.244-.785-.244-.382%200-.673.104-.874.312-.201.208-.301.463-.301.766%200%20.12.028.241.083.362.056.122.157.27.304.445l.44.524zm1.528%201.676c.273-.273.489-.54.648-.801.159-.261.238-.538.238-.831%200-.293-.085-.532-.255-.717-.17-.185-.406-.278-.708-.278-.327%200-.576.093-.747.28-.171.186-.257.423-.257.709%200%20.207.057.394.172.559.114.166.3.355.559.57l.35.309z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       34,
                Name:           "ThumbsDown",
                Icon:           Icon.ThumbsDown,
                Description:    "An icon representing disapproval or dislike, typically shown as a hand with the thumb pointing downward",
                Tags:           ["dislike", "negative", "feedback", "rating"],
                Category:       "Social",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12%200c6.623%200%2012%205.377%2012%2012s-5.377%2012-12%2012-12-5.377-12-12%205.377-12%2012-12zm0%201c6.071%200%2011%204.929%2011%2011s-4.929%2011-11%2011-11-4.929-11-11%204.929-11%2011-11zm0%2012.25c0%20.69.559%201.25%201.25%201.25h1.75v5h-1.75c-.69%200-1.25.56-1.25%201.25v.25h-4.5v-7.75h4.5zm1-1h-6.5v9.75h6.5v-.25c0-.69.56-1.25%201.25-1.25h1.75v-7h-1.75c-.69%200-1.25-.56-1.25-1.25zm-3.5-2.125c0-.345.28-.625.625-.625h.625v-1.25h-.625c-1.036%200-1.875.84-1.875%201.875v1.25h1.25v-1.25zm5%202.125h2c.69%200%201.25-.56%201.25-1.25v-3.5c0-.69-.56-1.25-1.25-1.25h-2v6z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       35,
                Name:           "ThumbsDownFilled",
                Icon:           Icon.ThumbsDownFilled,
                Description:    "A filled icon representing strong disapproval or dislike, typically shown as a solid hand with the thumb pointing downward",
                Tags:           ["dislike", "negative", "feedback", "rating", "filled"],
                Category:       "Social",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12%200c6.623%200%2012%205.377%2012%2012s-5.377%2012-12%2012-12-5.377-12-12%205.377-12%2012-12zm5.5%2010h-2.5v-3.5c0-.69-.56-1.25-1.25-1.25h-5.5c-1.38%200-2.5%201.12-2.5%202.5v7.75c0%20.69.56%201.25%201.25%201.25h3.25v3.75c0%20.69.56%201.25%201.25%201.25h5.5c.69%200%201.25-.56%201.25-1.25v-9.5c0-.69-.56-1.25-1.25-1.25zm-7.5%200h-1.5v-2.25c0-.414.336-.75.75-.75h.75v3z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       36,
                Name:           "ThumbsUpFilled",
                Icon:           Icon.ThumbsUpFilled,
                Description:    "A filled icon representing strong approval or like, typically shown as a solid hand with the thumb pointing upward",
                Tags:           ["like", "positive", "feedback", "rating", "filled"],
                Category:       "Social",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12%200c6.623%200%2012%205.377%2012%2012s-5.377%2012-12%2012-12-5.377-12-12%205.377-12%2012-12zm5.5%2014h-2.5v3.5c0%20.69-.56%201.25-1.25%201.25h-5.5c-1.38%200-2.5-1.12-2.5-2.5v-7.75c0-.69.56-1.25%201.25-1.25h3.25v-3.75c0-.69.56-1.25%201.25-1.25h5.5c.69%200%201.25.56%201.25%201.25v9.5c0%20.69-.56%201.25-1.25%201.25zm-7.5%200h-1.5v2.25c0%20.414.336.75.75.75h.75v-3z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       37,
                Name:           "Undo",
                Icon:           Icon.Undo,
                Description:    "An icon representing the action of undoing or reverting a previous action, typically shown as a curved arrow pointing left or counterclockwise",
                Tags:           ["revert", "reverse", "back", "previous"],
                Category:       "Actions",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M17.026%2022.957c10.957-11.421-2.326-20.865-10.384-13.309l2.464%202.352h-9.106v-8.947l2.232%202.229c14.794-13.203%2031.51%207.051%2014.794%2017.675z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       38,
                Name:           "Redo",
                Icon:           Icon.Redo,
                Description:    "An icon representing the action of redoing or reapplying a previously undone action, typically shown as a curved arrow pointing right or clockwise",
                Tags:           ["reapply", "forward", "repeat", "next"],
                Category:       "Actions",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M6.974%2022.957c-10.957-11.421%202.326-20.865%2010.384-13.309l-2.464%202.352h9.106v-8.947l-2.232%202.229c-14.794-13.203-31.51%207.051-14.794%2017.675z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       39,
                Name:           "ZoomIn",
                Icon:           Icon.ZoomIn,
                Description:    "An icon representing the action of zooming in or enlarging a view, typically shown as a magnifying glass with a plus sign",
                Tags:           ["magnify", "enlarge", "increase", "expand"],
                Category:       "View",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M15.853%2016.56c-1.683%201.517-3.911%202.44-6.353%202.44-5.243%200-9.5-4.257-9.5-9.5s4.257-9.5%209.5-9.5%209.5%204.257%209.5%209.5c0%202.442-.923%204.67-2.44%206.353l7.44%207.44-.707.707-7.44-7.44zm-6.353-15.56c4.691%200%208.5%203.809%208.5%208.5s-3.809%208.5-8.5%208.5-8.5-3.809-8.5-8.5%203.809-8.5%208.5-8.5zm-4.5%208h4v-4h1v4h4v1h-4v4h-1v-4h-4v-1z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       40,
                Name:           "ZoomOut",
                Icon:           Icon.ZoomOut,
                Description:    "An icon representing the action of zooming out or reducing a view, typically shown as a magnifying glass with a minus sign",
                Tags:           ["reduce", "decrease", "shrink", "minimize"],
                Category:       "View",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M15.853%2016.56c-1.683%201.517-3.911%202.44-6.353%202.44-5.243%200-9.5-4.257-9.5-9.5s4.257-9.5%209.5-9.5%209.5%204.257%209.5%209.5c0%202.442-.923%204.67-2.44%206.353l7.44%207.44-.707.707-7.44-7.44zm-6.353-15.56c4.691%200%208.5%203.809%208.5%208.5s-3.809%208.5-8.5%208.5-8.5-3.809-8.5-8.5%203.809-8.5%208.5-8.5zm-4.5%208h9v1h-9v-1z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       41,
                Name:           "OpenInNewWindow",
                Icon:           Icon.OpenInNewWindow,
                Description:    "An icon representing the action of opening a link or content in a new window or tab, typically shown as a square with an arrow pointing outward",
                Tags:           ["external", "link", "new tab", "launch"],
                Category:       "Navigation",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M14%204h-13v18h20v-11h1v12h-22v-20h14v1zm10%205h-1v-6.293l-11.646%2011.647-.708-.708%2011.647-11.646h-6.293v-1h8v8z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       42,
                Name:           "Share",
                Icon:           Icon.Share,
                Description:    "An icon representing the action of sharing content or information, typically shown as interconnected nodes or an arrow pointing outward from a circle",
                Tags:           ["distribute", "send", "social", "connect"],
                Category:       "Communication",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M14%204h-13v18h20v-11h1v12h-22v-20h14v1zm10%205h-1v-6.293l-11.646%2011.647-.708-.708%2011.647-11.646h-6.293v-1h8v8zm-4%208h5v1h-5v-1zm-4-3h9v1h-9v-1zm2-3h7v1h-7v-1zm-1-2h8v1h-8v-1z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       43,
                Name:           "Publish",
                Icon:           Icon.Publish,
                Description:    "An icon representing the action of publishing or making content publicly available, typically shown as an upward arrow or a document with an upward arrow",
                Tags:           ["release", "upload", "distribute", "make public"],
                Category:       "Content",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M14%200v10h2v-4.5l6%206v-3l-6-6v-2.5h-2zm-7.5%203c1.93%200%203.5%201.57%203.5%203.5s-1.57%203.5-3.5%203.5-3.5-1.57-3.5-3.5%201.57-3.5%203.5-3.5zm0-1c-2.48%200-4.5%202.02-4.5%204.5s2.02%204.5%204.5%204.5%204.5-2.02%204.5-4.5-2.02-4.5-4.5-4.5zm.5%208v2h-1v-2h1zm-1-1v-1h1v1h-1zm0-2v-1h1v1h-1zm9%2011v-2h-10v2h-6v6h22v-6h-6zm-11%205h-4v-4h4v4zm16%200h-4v-4h4v4z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       44,
                Name:           "Link",
                Icon:           Icon.Link,
                Description:    "An icon representing a hyperlink or connection between elements, typically shown as a chain link or interlocking rings",
                Tags:           ["hyperlink", "url", "connect", "attach"],
                Category:       "Web",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M14.851%2011.923c-.179-.641-.521-1.246-1.025-1.749-1.562-1.562-4.095-1.563-5.657%200l-4.998%204.998c-1.562%201.563-1.563%204.095%200%205.657%201.562%201.563%204.096%201.561%205.656%200l3.842-3.841.333.009c.404%200%20.802-.04%201.189-.117l-4.657%204.656c-.975.976-2.255%201.464-3.535%201.464-1.28%200-2.56-.488-3.535-1.464-1.952-1.951-1.952-5.12%200-7.071l4.998-4.998c.975-.976%202.256-1.464%203.536-1.464%201.279%200%202.56.488%203.535%201.464.493.493.861%201.063%201.105%201.672l-.787.784zm-5.703.147c.178.643.521%201.25%201.026%201.756%201.562%201.563%204.096%201.561%205.656%200l4.999-4.998c1.563-1.562%201.563-4.095%200-5.657-1.562-1.562-4.095-1.563-5.657%200l-3.841%203.841-.333-.009c-.404%200-.802.04-1.189.117l4.656-4.656c.975-.976%202.256-1.464%203.536-1.464%201.279%200%202.56.488%203.535%201.464%201.951%201.951%201.951%205.119%200%207.071l-4.999%204.998c-.975.976-2.255%201.464-3.535%201.464-1.28%200-2.56-.488-3.535-1.464-.494-.495-.863-1.067-1.107-1.678l.788-.785z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       45,
                Name:           "Sync",
                Icon:           Icon.Sync,
                Description:    "An icon representing synchronization or data refresh, typically shown as two circular arrows forming a loop",
                Tags:           ["refresh", "update", "reload", "synchronize"],
                Category:       "Data",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12%204V1L8%205l4%204V6c3.31%200%206%202.69%206%206%200%201.01-.25%201.97-.7%202.8l1.46%201.46C19.54%2015.03%2020%2013.57%2020%2012c0-4.42-3.58-8-8-8zm0%2014c-3.31%200-6-2.69-6-6%200-1.01.25-1.97.7-2.8L5.24%207.74C4.46%208.97%204%2010.43%204%2012c0%204.42%203.58%208%208%208v3l4-4-4-4v3z%22%2F%3E%3C%2Fsvg%3E"
            },
            {
                Sequence:       46,
                Name:           "View",
                Icon:           Icon.View,
                Description:    "An icon representing the action of viewing or previewing content, typically shown as an eye",
                Tags:           ["preview", "see", "visibility", "show"],
                Category:       "Actions",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12.01%2020c-5.065%200-9.586-4.211-12.01-8.424%202.418-4.103%206.943-7.576%2012.01-7.576%205.135%200%209.635%203.453%2011.999%207.564-2.241%204.43-6.726%208.436-11.999%208.436zm-10.842-8.416c.843%201.331%205.018%207.416%2010.842%207.416%206.305%200%2010.112-6.103%2010.851-7.405-.772-1.198-4.606-6.595-10.851-6.595-6.116%200-10.025%205.355-10.842%206.584zm10.832-4.584c2.76%200%205%202.24%205%205s-2.24%205-5%205-5-2.24-5-5%202.24-5%205-5zm0%201c2.208%200%204%201.792%204%204s-1.792%204-4%204-4-1.792-4-4%201.792-4%204-4z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       47,
                Name:           "Hide",
                Icon:           Icon.Hide,
                Description:    "An icon representing the action of hiding or concealing content, typically shown as an eye with a slash through it",
                Tags:           ["invisible", "conceal", "hidden", "private"],
                Category:       "Actions",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M8.137%2015.147c-.71-.857-1.146-1.947-1.146-3.147%200-2.76%202.241-5%205-5%201.201%200%202.291.435%203.148%201.145l1.897-1.897c-1.441-.738-3.122-1.248-5.035-1.248-6.115%200-10.025%205.355-10.842%206.584.529.834%202.379%203.527%205.113%205.428l1.865-1.865zm6.294-6.294c-.673-.53-1.515-.853-2.44-.853-2.207%200-4%201.792-4%204%200%20.923.324%201.765.854%202.439l5.586-5.586zm7.56-6.146l-19.292%2019.293-.708-.707%203.548-3.548c-2.298-1.612-4.234-3.885-5.548-6.169%202.418-4.103%206.943-7.576%2012.01-7.576%202.065%200%204.021.566%205.782%201.501l3.501-3.501.707.707zm-2.465%203.879l-.734.734c2.236%201.619%203.628%203.604%204.061%204.274-.739%201.303-4.546%207.406-10.852%207.406-1.425%200-2.749-.368-3.951-.938l-.748.748c1.475.742%203.057%201.19%204.699%201.19%205.274%200%209.758-4.006%2011.999-8.436-1.087-1.891-2.63-3.637-4.474-4.978zm-3.535%205.414c0-.554-.113-1.082-.317-1.562l.734-.734c.361.69.583%201.464.583%202.296%200%202.759-2.24%205-5%205-.832%200-1.604-.223-2.295-.583l.734-.735c.48.204%201.007.318%201.561.318%202.208%200%204-1.792%204-4z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       48,
                Name:           "Bookmark",
                Icon:           Icon.Bookmark,
                Description:    "An icon representing a bookmark or saved item, typically shown as a ribbon or tag",
                Tags:           ["save", "favorite", "mark", "flag"],
                Category:       "Actions",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M5%200v24l7-6%207%206v-24h-14zm1%201h12v20.827l-6-5.144-6%205.144v-20.827z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       49,
                Name:           "BookmarkFilled",
                Icon:           Icon.BookmarkFilled,
                Description:    "A filled icon representing a bookmark or saved item, typically shown as a solid ribbon or tag",
                Tags:           ["save", "favorite", "mark", "flag", "filled"],
                Category:       "Actions",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M5%200v24l7-6%207%206v-24h-14z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       50,
                Name:           "Reset",
                Icon:           Icon.Reset,
                Description:    "An icon representing the action of resetting or returning to an initial state, typically shown as a circular arrow",
                Tags:           ["restart", "refresh", "revert", "circular arrow"],
                Category:       "Actions",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12%200c6.623%200%2012%205.377%2012%2012s-5.377%2012-12%2012-12-5.377-12-12%205.377-12%2012-12zm0%201c6.071%200%2011%204.929%2011%2011s-4.929%2011-11%2011-11-4.929-11-11%204.929-11%2011-11zm0%2010.293l5.293-5.293.707.707-5.293%205.293%205.293%205.293-.707.707-5.293-5.293-5.293%205.293-.707-.707%205.293-5.293-5.293-5.293.707-.707%205.293%205.293z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       51,
                Name:           "Blocked",
                Icon:           Icon.Blocked,
                Description:    "An icon representing a blocked or prohibited state, typically shown as a circle with a diagonal line through it",
                Tags:           ["prohibited", "forbidden", "stop", "no"],
                Category:       "Status",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12%200c6.623%200%2012%205.377%2012%2012s-5.377%2012-12%2012-12-5.377-12-12%205.377-12%2012-12zm0%201c6.071%200%2011%204.929%2011%2011s-4.929%2011-11%2011-11-4.929-11-11%204.929-11%2011-11zm7.293%2016.707l-13-13%20.707-.707%2013%2013-.707.707z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       52,
                Name:           "DockLeft",
                Icon:           Icon.DockLeft,
                Description:    "An icon representing docking or aligning content to the left side, typically shown as a rectangle with a smaller rectangle aligned to its left edge",
                Tags:           ["align", "left", "layout", "position"],
                Category:       "Layout",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M3%203h18v18h-18v-18zm1%201v16h6v-16h-6zm8%200v16h8v-16h-8z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       53,
                Name:           "AddUser",
                Icon:           Icon.AddUser,
                Description:    "An icon representing the action of adding a new user, typically shown as a user silhouette with a plus sign",
                Tags:           ["new user", "create account", "sign up", "register"],
                Category:       "Users",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M15.5%2012c2.484%200%204.5%202.016%204.5%204.5s-2.016%204.5-4.5%204.5-4.5-2.016-4.5-4.5%202.016-4.5%204.5-4.5zm.5%202h-1v2h-2v1h2v2h1v-2h2v-1h-2v-2zm-7.18%204h-6.32v2h5.789c-.249-.566-.385-1.196-.385-1.856%200-.046.003-.091.005-.137l-5.788-.003c.111-2.777%202.255-5.004%205.011-5.004%201.156%200%202.257.391%203.14%201.104.299-.609.722-1.155%201.239-1.6-1.223-.915-2.745-1.454-4.379-1.454-4.015%200-7.288%203.273-7.288%207.288v2.712h14.325c-.406-.582-.715-1.243-.893-1.954h-4.456zm6.837-10c1.19%200%202.159-.971%202.159-2.165%200-1.195-.969-2.165-2.159-2.165s-2.158.97-2.158%202.165c0%201.194.968%202.165%202.158%202.165zm1.838%202.524v1.476h-2.667v7.714h-1.715v-7.714h-2.738v-1.476h7.12z%22%2F%3E%3C%2Fsvg%3E"
            },
            {
                Sequence:       54,
                Name:           "Cut",
                Icon:           Icon.Cut,
                Description:    "An icon representing a cutting action, typically shown as a pair of scissors",
                Tags:           ["scissors", "trim", "clip", "snip"],
                Category:       "Actions",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M11.5%200c1.93%200%203.5%201.57%203.5%203.5%200%20.592-.148%201.151-.41%201.638l-2.35%202.35-1.64-1.64c.258-.487.4-1.046.4-1.638%200-1.93-1.57-3.5-3.5-3.5s-3.5%201.57-3.5%203.5c0%20.592.148%201.151.41%201.638l-2.35%202.35-1.64-1.64c.258-.487.4-1.046.4-1.638%200-1.93-1.57-3.5-3.5-3.5s-3.5%201.57-3.5%203.5%201.57%203.5%203.5%203.5c.592%200%201.151-.148%201.638-.41l2.35%202.35-1.64%201.64c-.487-.258-1.046-.4-1.638-.4-1.93%200-3.5%201.57-3.5%203.5s1.57%203.5%203.5%203.5%203.5-1.57%203.5-3.5c0-.592-.148-1.151-.41-1.638l2.35-2.35%201.64%201.64c-.258.487-.4%201.046-.4%201.638%200%201.93%201.57%203.5%203.5%203.5s3.5-1.57%203.5-3.5-1.57-3.5-3.5-3.5c-.592%200-1.151.148-1.638.41l-2.35-2.35%201.64-1.64c.487.258%201.046.4%201.638.4%201.93%200%203.5-1.57%203.5-3.5zm-1%2017.5c-.827%200-1.5-.673-1.5-1.5s.673-1.5%201.5-1.5%201.5.673%201.5%201.5-.673%201.5-1.5%201.5zm-10-10c-.827%200-1.5-.673-1.5-1.5s.673-1.5%201.5-1.5%201.5.673%201.5%201.5-.673%201.5-1.5%201.5z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       55,
                Name:           "Paste",
                Icon:           Icon.Paste,
                Description:    "An icon representing the action of pasting content, typically shown as a clipboard or document with a downward arrow",
                Tags:           ["insert", "paste", "clipboard", "add"],
                Category:       "Actions",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M8%200v2c-2.209%200-4%201.791-4%204v12h16V6c0-2.209-1.791-4-4-4H8zm0%204h6c.552%200%201%20.448%201%201v2H7V5c0-.552.448-1%201-1zm0%204h4c.552%200%201%20.448%201%201v3H7V9c0-.552.448-1%201-1z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       56,
                Name:           "Leave",
                Icon:           Icon.Leave,
                Description:    "An icon representing the action of leaving or exiting, typically shown as a door with an arrow pointing outward",
                Tags:           ["exit", "logout", "depart", "sign out"],
                Category:       "Actions",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M11%2021h8v-2l1-1v4h-9v2l-10-3v-18l10-3v2h9v5l-1-1v-3h-8v18zm10.053-9l-3.293-3.293.707-.707%204.5%204.5-4.5%204.5-.707-.707%203.293-3.293h-9.053v-1h9.053z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       57,
                Name:           "Home",
                Icon:           Icon.Home,
                Description:    "An icon representing a home or main page, typically shown as a simple house shape",
                Tags:           ["house", "main", "start", "homepage"],
                Category:       "Navigation",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12%206.453l9%208.375v9.172h-6v-6h-6v6h-6v-9.172l9-8.375zm12%205.695l-12-11.148-12%2011.133%201.361%201.465%2010.639-9.868%2010.639%209.883%201.361-1.465z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       58,
                Name:           "Hamburger",
                Icon:           Icon.Hamburger,
                Description:    "An icon representing a menu, typically shown as three horizontal lines stacked vertically",
                Tags:           ["menu", "navigation", "options", "sidebar"],
                Category:       "Navigation",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M24%2018v1h-24v-1h24zm0-6v1h-24v-1h24zm0-6v1h-24v-1h24z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       59,
                Name:           "Settings",
                Icon:           Icon.Settings,
                Description:    "An icon representing settings or configuration options, typically shown as a gear or cog wheel",
                Tags:           ["configuration", "options", "preferences", "gear"],
                Category:       "System",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M24%2013.616v-3.232c-1.651-.587-2.694-.752-3.219-2.019v-.001c-.527-1.271.1-2.134.847-3.707l-2.285-2.285c-1.561.742-2.433%201.375-3.707.847h-.001c-1.269-.526-1.435-1.576-2.019-3.219h-3.232c-.582%201.635-.749%202.692-2.019%203.219h-.001c-1.271.528-2.132-.098-3.707-.847l-2.285%202.285c.745%201.568%201.375%202.434.847%203.707-.527%201.271-1.584%201.438-3.219%202.02v3.232c1.632.58%202.692.749%203.219%202.019.53%201.282-.114%202.166-.847%203.707l2.285%202.286c1.562-.743%202.434-1.375%203.707-.847h.001c1.27.526%201.436%201.579%202.019%203.219h3.232c.582-1.636.75-2.69%202.027-3.222h.001c1.262-.524%202.12.101%203.698.851l2.285-2.286c-.744-1.563-1.375-2.433-.848-3.706.527-1.271%201.588-1.44%203.221-2.021zm-12%202.384c-2.209%200-4-1.791-4-4s1.791-4%204-4%204%201.791%204%204-1.791%204-4%204z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       60,
                Name:           "More",
                Icon:           Icon.More,
                Description:    "An icon representing additional options or actions, typically shown as three dots (ellipsis) either horizontally or vertically aligned",
                Tags:           ["ellipsis", "options", "additional", "menu"],
                Category:       "Navigation",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12%2016c1.656%200%203%201.344%203%203s-1.344%203-3%203-3-1.344-3-3%201.344-3%203-3zm0-8c1.656%200%203%201.344%203%203s-1.344%203-3%203-3-1.344-3-3%201.344-3%203-3zm0-8c1.656%200%203%201.344%203%203s-1.344%203-3%203-3-1.344-3-3%201.344-3%203-3z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       61,
                Name:           "Waffle",
                Icon:           Icon.Waffle,
                Description:    "An icon representing a menu of multiple options, typically shown as a 3x3 grid of small squares",
                Tags:           ["menu", "grid", "options", "navigation"],
                Category:       "Navigation",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M0%200h7v7h-7zm8.5%200h7v7h-7zm8.5%200h7v7h-7zm-17%208.5h7v7h-7zm8.5%200h7v7h-7zm8.5%200h7v7h-7zm-17%208.5h7v7h-7zm8.5%200h7v7h-7zm8.5%200h7v7h-7z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       62,
                Name:           "ChevronLeft",
                Icon:           Icon.ChevronLeft,
                Description:    "An icon representing a left-pointing chevron, typically used for navigation or to indicate a collapsible menu",
                Tags:           ["left", "arrow", "back", "previous"],
                Category:       "Navigation",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M15.707%2017.293l-5.293-5.293%205.293-5.293c.391-.391.391-1.023%200-1.414s-1.023-.391-1.414%200l-6%206c-.391.391-.391%201.023%200%201.414l6%206c.391.391%201.023.391%201.414%200s.391-1.023%200-1.414z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       63,
                Name:           "ChevronRight",
                Icon:           Icon.ChevronRight,
                Description:    "An icon representing a right-pointing chevron, typically used for navigation or to indicate an expandable menu",
                Tags:           ["right", "arrow", "next", "forward"],
                Category:       "Navigation",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M8.293%2017.293l5.293-5.293-5.293-5.293c-.391-.391-.391-1.023%200-1.414s1.023-.391%201.414%200l6%206c.391.391.391%201.023%200%201.414l-6%206c-.391.391-1.023.391-1.414%200s-.391-1.023%200-1.414z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       64,
                Name:           "ChevronUp",
                Icon:           Icon.ChevronUp,
                Description:    "An icon representing an upward-pointing chevron, typically used for navigation or to indicate an expandable menu",
                Tags:           ["up", "arrow", "expand", "collapse"],
                Category:       "Navigation",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12%208.293l-5.293%205.293c-.391.391-1.023.391-1.414%200s-.391-1.023%200-1.414l6-6c.391-.391%201.023-.391%201.414%200l6%206c.391.391.391%201.023%200%201.414s-1.023.391-1.414%200l-5.293-5.293z%22%2F%3E%3C%2Fsvg%3E"
            },
            {
                Sequence:       65,
                Name:           "ChevronDown",
                Icon:           Icon.ChevronDown,
                Description:    "An icon representing a downward-pointing chevron, typically used for navigation or to indicate a collapsible menu",
                Tags:           ["down", "arrow", "expand", "collapse"],
                Category:       "Navigation",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12%2015.707l5.293-5.293c.391-.391%201.023-.391%201.414%200s.391%201.023%200%201.414l-6%206c-.391.391-1.023.391-1.414%200l-6-6c-.391-.391-.391-1.023%200-1.414s1.023-.391%201.414%200l5.293%205.293z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       66,
                Name:           "NextArrow",
                Icon:           Icon.NextArrow,
                Description:    "An icon representing a forward or next action, typically shown as an arrow pointing to the right",
                Tags:           ["forward", "next", "advance", "right"],
                Category:       "Navigation",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M4%2012l10%206v-12l-10%206zm2%200l6-3.6v7.2l-6-3.6zm12.351-3.636l-2.351%201.636%202.351%201.636v2.364l-5.351-3.636%205.351-3.636v2.636z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       67,
                Name:           "BackArrow",
                Icon:           Icon.BackArrow,
                Description:    "An icon representing a backward or previous action, typically shown as an arrow pointing to the left",
                Tags:           ["back", "previous", "return", "left"],
                Category:       "Navigation",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M20%2012l-10%206v-12l10%206zm-2%200l-6-3.6v7.2l6-3.6zm-12.351-3.636l2.351%201.636-2.351%201.636v2.364l5.351-3.636-5.351-3.636v2.636z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       68,
                Name:           "ArrowDown",
                Icon:           Icon.ArrowDown,
                Description:    "An icon representing a downward direction or action, typically shown as an arrow pointing downward",
                Tags:           ["down", "descend", "dropdown", "expand"],
                Category:       "Navigation",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M11%2021.883l-6.235-7.527-.765.644%207.521%209%207.479-9-.764-.645-6.236%207.529v-21.884h-1v21.883z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       69,
                Name:           "ArrowUp",
                Icon:           Icon.ArrowUp,
                Description:    "An icon representing an upward direction or action, typically shown as an arrow pointing upward",
                Tags:           ["up", "ascend", "upward", "rise"],
                Category:       "Navigation",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M11%202.206l-6.235%207.528-.765-.645%207.521-9%207.479%209-.764.646-6.236-7.53v21.884h-1v-21.883z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       70,
                Name:           "ArrowLeft",
                Icon:           Icon.ArrowLeft,
                Description:    "An icon representing a leftward direction or action, typically shown as an arrow pointing to the left",
                Tags:           ["left", "back", "previous", "backward"],
                Category:       "Navigation",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M2.117%2012l7.527%206.235-.644.765-9-7.521%209-7.479.645.764-7.529%206.236h21.884v1h-21.883z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       71,
                Name:           "ArrowRight",
                Icon:           Icon.ArrowRight,
                Description:    "An icon representing a rightward direction or action, typically shown as an arrow pointing to the right",
                Tags:           ["right", "forward", "next", "advance"],
                Category:       "Navigation",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M21.883%2012l-7.527%206.235.644.765%209-7.521-9-7.479-.645.764%207.529%206.236h-21.884v1h21.883z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       72,
                Name:           "Camera",
                Icon:           Icon.Camera,
                Description:    "An icon representing a camera or photo-taking action, typically shown as a simplified camera shape",
                Tags:           ["photo", "picture", "capture", "image"],
                Category:       "Media",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M24%2022h-24v-20h24v20zm-1-19h-22v18h22v-18zm-1%2016h-20v-14h20v14zm-2-12h-16v10h16v-10zm-4%204.111c0-1.157-.934-2.092-2.083-2.092s-2.083.935-2.083%202.092c0%201.157.934%202.092%202.083%202.092s2.083-.935%202.083-2.092zm4%205.889h-16l4-8%203%206%202-4%207%206z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       73,
                Name:           "Document",
                Icon:           Icon.Document,
                Description:    "An icon representing a document or file, typically shown as a rectangular shape with a folded corner",
                Tags:           ["file", "paper", "page", "document"],
                Category:       "Files",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M22%2024h-20v-24h14l6%206v18zm-7-23h-12v22h18v-16h-6v-6zm1%205h4.586l-4.586-4.586v4.586z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       74,
                Name:           "DockCheckProperties",
                Icon:           Icon.DockCheckProperties,
                Description:    "An icon representing a document with a checkmark, typically used to indicate verified or approved document properties",
                Tags:           ["document", "checkmark", "verify", "approve", "properties"],
                Category:       "Files",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M22%2024h-20v-24h14l6%206v18zm-7-23h-12v22h18v-16h-6v-6zm1%205h4.586l-4.586-4.586v4.586zm-3%2010l-4.5-4.5-1.5%201.5%206%206%209-9-1.5-1.5-7.5%207.5z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       75,
                Name:           "Folder",
                Icon:           Icon.Folder,
                Description:    "An icon representing a folder or directory, typically shown as a simplified folder shape",
                Tags:           ["directory", "file system", "storage", "organize"],
                Category:       "Files",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M0%202h8l3%203h10v4h3v13h-24v-20zm22%2018v-11h-22v11h22zm-3-17h-9.586l-3-3h-6.414v3h19v-3h-3v2h3v1z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       76,
                Name:           "Journal",
                Icon:           Icon.Journal,
                Description:    "An icon representing a journal or log, typically shown as a book or notebook",
                Tags:           ["log", "notebook", "diary", "record"],
                Category:       "Files",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M3%200h18v24h-18v-24zm2%202v20h14v-20h-14zm3.5%204h7v1h-7v-1zm0%204h7v1h-7v-1zm0%204h7v1h-7v-1z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       77,
                Name:           "ForkKnife",
                Icon:           Icon.ForkKnife,
                Description:    "An icon representing food or dining, typically shown as a fork and knife crossed or side by side",
                Tags:           ["food", "dining", "restaurant", "meal"],
                Category:       "Miscellaneous",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M11%205h-1v1h1v-1zm3-1h-1v1h1v-1zm-2-1h-1v1h1v-1zm3%203h-1v1h1v-1zm2-2h-1v1h1v-1zm-3%204h-1v1h1v-1zm3-2h-1v1h1v-1zm2%202h-1v1h1v-1zm-3%202h-1v1h1v-1zm3%200h-1v1h1v-1zm2%200h-1v1h1v-1zm-9-8h-1v1h1v-1zm3%200h-1v1h1v-1zm3%200h-1v1h1v-1zm3%200h-1v1h1v-1zm-12%2012h-1v1h1v-1zm0-2h-1v1h1v-1zm0-2h-1v1h1v-1zm0-2h-1v1h1v-1zm0-2h-1v1h1v-1zm0-2h-1v1h1v-1zm12%2010h-1v1h1v-1zm-3%200h-1v1h1v-1zm-3%200h-1v1h1v-1zm-3%200h-1v1h1v-1z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       78,
                Name:           "Transportation",
                Icon:           Icon.Transportation,
                Description:    "An icon representing transportation or travel, typically shown as a vehicle or mode of transport",
                Tags:           ["travel", "vehicle", "transport", "journey"],
                Category:       "Travel",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M3%2022v-20h18v20h-18zm1-19v18h16v-18h-16zm5.5%2015c.828%200%201.5.672%201.5%201.5s-.672%201.5-1.5%201.5-1.5-.672-1.5-1.5.672-1.5%201.5-1.5zm8%200c.828%200%201.5.672%201.5%201.5s-.672%201.5-1.5%201.5-1.5-.672-1.5-1.5.672-1.5%201.5-1.5zm-8-12h8v5h-8v-5z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       79,
                Name:           "Airplane",
                Icon:           Icon.Airplane,
                Description:    "An icon representing an airplane or air travel, typically shown as a simplified side view of an aircraft",
                Tags:           ["flight", "travel", "aviation", "transport"],
                Category:       "Travel",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M21.5%2011.5l-5.5-3.5v-4c0-1.1-.9-2-2-2s-2%20.9-2%202v4l-5.5%203.5-4.5.5v2l5.5-1.5%204.5-2v4l-2%201.5v2l3.5-1%203.5%201v-2l-2-1.5v-4l4.5%202%205.5%201.5v-2l-4.5-.5z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       80,
                Name:           "Bus",
                Icon:           Icon.Bus,
                Description:    "An icon representing a bus or public transportation, typically shown as a simplified side view of a bus",
                Tags:           ["public transport", "travel", "vehicle", "commute"],
                Category:       "Travel",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M2%2012h20v8h-2v2h-16v-2h-2v-8zm18-2h-16v8h16v-8zm-14.5%206.5c.828%200%201.5.672%201.5%201.5s-.672%201.5-1.5%201.5-1.5-.672-1.5-1.5.672-1.5%201.5-1.5zm11%200c.828%200%201.5.672%201.5%201.5s-.672%201.5-1.5%201.5-1.5-.672-1.5-1.5.672-1.5%201.5-1.5zm-12.5-13.5h14v3h-14v-3z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       81,
                Name:           "Cars",
                Icon:           Icon.Cars,
                Description:    "An icon representing multiple cars or vehicles, typically shown as simplified car silhouettes",
                Tags:           ["vehicles", "automobiles", "transport", "traffic"],
                Category:       "Transportation",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M3%2018h18v3h-18v-3zm0-7h18v4h-18v-4zm18-1h-18v-1l2-5h14l2%205v1zm-17-5l-1.5%204h17l-1.5-4h-14z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       82,
                Name:           "Money",
                Icon:           Icon.Money,
                Description:    "An icon representing money or currency, typically shown as banknotes or coins",
                Tags:           ["currency", "cash", "finance", "payment"],
                Category:       "Finance",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M22%207h-19v11h19v-11zm-3%209h-13v-7h13v7zm-3-5h-7v3h7v-3zm-9-11h15v2h-15v-2zm18 0h2v15h-2v-15zm-18 17h15v2h-15v-2zm-4-17h2v15h-2v-15z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       83,
                Name:           "Currency",
                Icon:           Icon.Currency,
                Description:    "An icon representing currency or exchange, typically shown as a dollar sign or multiple currency symbols",
                Tags:           ["money", "exchange", "finance", "forex"],
                Category:       "Finance",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12%200c6.623%200%2012%205.377%2012%2012s-5.377%2012-12%2012-12-5.377-12-12%205.377-12%2012-12zm0%201c6.071%200%2011%204.929%2011%2011s-4.929%2011-11%2011-11-4.929-11-11%204.929-11%2011-11zm0%2011h6v1h-7v-9h1v8zm-3%204h-1v-3h1v3z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       84,
                Name:           "AddToCalendar",
                Icon:           Icon.AddToCalendar,
                Description:    "An icon representing the action of adding an event to a calendar, typically shown as a calendar with a plus sign",
                Tags:           ["event", "schedule", "appointment", "date"],
                Category:       "Calendar",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M24%2022h-24v-20h24v20zm-1-19h-22v18h22v-18zm-16.5%2013.5c.69%200%201.25.56%201.25%201.25s-.56%201.25-1.25%201.25-1.25-.56-1.25-1.25.56-1.25%201.25-1.25zm6.5%200c.69%200%201.25.56%201.25%201.25s-.56%201.25-1.25%201.25-1.25-.56-1.25-1.25.56-1.25%201.25-1.25zm5%200c.69%200%201.25.56%201.25%201.25s-.56%201.25-1.25%201.25-1.25-.56-1.25-1.25.56-1.25%201.25-1.25zm-11.5-6.5c.69%200%201.25.56%201.25%201.25s-.56%201.25-1.25%201.25-1.25-.56-1.25-1.25.56-1.25%201.25-1.25zm6.5%200c.69%200%201.25.56%201.25%201.25s-.56%201.25-1.25%201.25-1.25-.56-1.25-1.25.56-1.25%201.25-1.25zm5%200c.69%200%201.25.56%201.25%201.25s-.56%201.25-1.25%201.25-1.25-.56-1.25-1.25.56-1.25%201.25-1.25zm-11.5-6.5c.69%200%201.25.56%201.25%201.25s-.56%201.25-1.25%201.25-1.25-.56-1.25-1.25.56-1.25%201.25-1.25zm6.5%200c.69%200%201.25.56%201.25%201.25s-.56%201.25-1.25%201.25-1.25-.56-1.25-1.25.56-1.25%201.25-1.25zm5%200c.69%200%201.25.56%201.25%201.25s-.56%201.25-1.25%201.25-1.25-.56-1.25-1.25.56-1.25%201.25-1.25zm4.5%201h1v2h-1v-2z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       85,
                Name:           "CalendarBlank",
                Icon:           Icon.CalendarBlank,
                Description:    "An icon representing a blank calendar or date selection, typically shown as an empty calendar grid",
                Tags:           ["date", "schedule", "month", "empty"],
                Category:       "Calendar",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M24%2022h-24v-20h24v20zm-1-19h-22v18h22v-18zm-16.5%2013.5h3v3h-3v-3zm6.5%200h3v3h-3v-3zm6.5%200h3v3h-3v-3zm-13-6.5h3v3h-3v-3zm6.5%200h3v3h-3v-3zm6.5%200h3v3h-3v-3zm-13-6.5h3v3h-3v-3zm6.5%200h3v3h-3v-3zm6.5%200h3v3h-3v-3z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       86,
                Name:           "OfficeBuilding",
                Icon:           Icon.OfficeBuilding,
                Description:    "An icon representing an office building or corporate structure, typically shown as a multi-story building",
                Tags:           ["building", "corporate", "company", "workplace"],
                Category:       "Business",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M24%2024h-24v-24h24v24zm-1-23h-22v22h22v-22zm-4%208h-14v1h14v-1zm0%204h-14v1h14v-1zm0%204h-14v1h14v-1zm-16-12h18v18h-18v-18zm1%201h16v16h-16v-16z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       87,
                Name:           "PaperClip",
                Icon:           Icon.PaperClip,
                Description:    "An icon representing an attachment or linked file, typically shown as a paper clip",
                Tags:           ["attachment", "file", "link", "document"],
                Category:       "Files",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M14%200c5.523%200%2010%204.477%2010%2010%200%205.522-4.477%2010-10%2010-5.522%200-10-4.478-10-10%200-5.523%204.478-10%2010-10zm-1.707%206.293c.391-.391%201.023-.391%201.414%200l3%203c.391.391.391%201.023%200%201.414l-5%205c-.391.391-1.023.391-1.414%200l-3-3c-.391-.391-.391-1.023%200-1.414l5-5zm-2.293%202.293l-2%202%201.293%201.293%202-2-1.293-1.293zm4%204l-2%202%201.293%201.293%202-2-1.293-1.293z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       88,
                Name:           "Newspaper",
                Icon:           Icon.Newspaper,
                Description:    "An icon representing a newspaper or news article, typically shown as a folded newspaper",
                Tags:           ["news", "article", "press", "media"],
                Category:       "Media",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M24%2024h-24v-24h24v24zm-1-23h-22v22h22v-22zm-3%2013h-16v1h16v-1zm0%202h-16v1h16v-1zm0%202h-16v1h16v-1zm-8-9h8v5h-8v-5zm1%201h6v3h-6v-3zm-9%200h7v1h-7v-1zm0%202h7v1h-7v-1zm0%202h7v1h-7v-1z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       89,
                Name:           "Lock",
                Icon:           Icon.Lock,
                Description:    "An icon representing security or a locked state, typically shown as a padlock",
                Tags:           ["security", "locked", "private", "protected"],
                Category:       "Security",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M18%2010v-4c0-3.313-2.687-6-6-6s-6%202.687-6%206v4h-3v14h18v-14h-3zm-5%207.723v2.277h-2v-2.277c-.595-.347-1-.984-1-1.723%200-1.104.896-2%202-2s2%20.896%202%202c0%20.738-.404%201.376-1%201.723zm-5-7.723v-4c0-2.206%201.794-4%204-4%202.205%200%204%201.794%204%204v4h-8z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       90,
                Name:           "Waypoint",
                Icon:           Icon.Waypoint,
                Description:    "An icon representing a location or destination point, typically shown as a map pin or marker",
                Tags:           ["location", "pin", "marker", "destination"],
                Category:       "Maps",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12%200c-4.198%200-8%203.403-8%207.602%200%204.198%203.469%209.21%208%2016.398%204.531-7.188%208-12.2%208-16.398%200-4.199-3.801-7.602-8-7.602zm0%2011c-1.657%200-3-1.343-3-3s1.343-3%203-3%203%201.343%203%203-1.343%203-3%203z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       91,
                Name:           "Location",
                Icon:           Icon.Location,
                Description:    "An icon representing a geographical location or position, typically shown as a crosshair or target",
                Tags:           ["position", "coordinates", "gps", "pinpoint"],
                Category:       "Maps",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12%200c-4.198%200-8%203.403-8%207.602%200%206.243%206.377%206.903%208%2016.398%201.623-9.495%208-10.155%208-16.398%200-4.199-3.801-7.602-8-7.602zm0%2011c-1.657%200-3-1.343-3-3s1.343-3%203-3%203%201.343%203%203-1.343%203-3%203z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       92,
                Name:           "DocumentPDF",
                Icon:           Icon.DocumentPDF,
                Description:    "An icon representing a PDF document, typically shown as a file with PDF text",
                Tags:           ["pdf", "file", "document", "adobe"],
                Category:       "Files",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M22%2024h-20v-24h14l6%206v18zm-7-23h-12v22h18v-16h-6v-6zm3%2015v1h-8v-1h8zm0-3v1h-8v-1h8zm0-3v1h-8v-1h8zm-1-4h4.586l-4.586-4.586v4.586z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       93,
                Name:           "Bell",
                Icon:           Icon.Bell,
                Description:    "An icon representing a notification or alert, typically shown as a bell shape",
                Tags:           ["notification", "alert", "reminder", "alarm"],
                Category:       "Notifications",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M15%2021c0%201.598-1.392%203-2.971%203s-3.029-1.402-3.029-3h6zm.137-17.055c-.644-.374-1.042-1.07-1.041-1.82v-.003c.001-1.172-.938-2.122-2.096-2.122s-2.097.95-2.097%202.122v.003c.001.751-.396%201.446-1.041%201.82-4.668%202.709-1.985%2011.715-6.862%2013.306v1.749h20v-1.749c-4.877-1.591-2.193-10.598-6.863-13.306zm-3.137-2.945c.552%200%201%20.449%201%201%200%20.552-.448%201-1%201s-1-.448-1-1c0-.551.448-1%201-1zm-6.451%2016c1.189-1.667%201.605-3.891%201.964-5.815.447-2.39.869-4.648%202.354-5.509%201.38-.801%202.956-.76%204.267%200%201.485.861%201.907%203.119%202.354%205.509.359%201.924.775%204.148%201.964%205.815h-12.903z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       94,
                Name:           "ShoppingCart",
                Icon:           Icon.ShoppingCart,
                Description:    "An icon representing a shopping cart or basket, typically used for e-commerce",
                Tags:           ["cart", "basket", "shopping", "ecommerce"],
                Category:       "Commerce",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M13.5%2021c-.276%200-.5-.224-.5-.5s.224-.5.5-.5.5.224.5.5-.224.5-.5.5m0-2c-.828%200-1.5.672-1.5%201.5s.672%201.5%201.5%201.5%201.5-.672%201.5-1.5-.672-1.5-1.5-1.5m-6%202c-.276%200-.5-.224-.5-.5s.224-.5.5-.5.5.224.5.5-.224.5-.5.5m0-2c-.828%200-1.5.672-1.5%201.5s.672%201.5%201.5%201.5%201.5-.672%201.5-1.5-.672-1.5-1.5-1.5m16.5-16h-2.964l-3.642%2015h-13.321l-4.073-13.003h19.522l.728-2.997h3.75v1zm-22.581%202.997l3.393%2011.003h11.794l2.674-11.003h-17.861z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       95,
                Name:           "Phone",
                Icon:           Icon.Phone,
                Description:    "An icon representing a telephone or mobile device, typically shown as a handset or smartphone shape",
                Tags:           ["telephone", "call", "mobile", "contact"],
                Category:       "Communication",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M16%2022.621l-3.521-6.795c-.007.004-1.974.97-2.064%201.011-2.24%201.086-6.799-7.82-4.609-8.994l2.082-1.026-3.492-6.817-2.106%201.039c-7.202%203.755%204.233%2025.982%2011.6%2022.615.121-.055%202.102-1.029%202.11-1.033z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       96,
                Name:           "PhoneHangUp",
                Icon:           Icon.PhoneHangUp,
                Description:    "An icon representing ending a phone call, typically shown as a phone handset facing down",
                Tags:           ["end call", "hang up", "telephone", "disconnect"],
                Category:       "Communication",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12%201c-6.627%200-12%204.373-12%2011v1h24v-1c0-6.627-5.373-11-12-11zm7.997%2014h-15.994c-.398%200-.721-.323-.721-.721%200-2.369%201.739-4.279%204.218-4.279h8c2.479%200%204.218%201.91%204.218%204.279%200%20.398-.323.721-.721.721z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       97,
                Name:           "Mobile",
                Icon:           Icon.Mobile,
                Description:    "An icon representing a mobile phone or smartphone, typically shown as a rectangular device with a screen",
                Tags:           ["smartphone", "cellphone", "device", "handheld"],
                Category:       "Devices",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M16%200h-8c-1.104%200-2%20.896-2%202v20c0%201.104.896%202%202%202h8c1.104%200%202-.896%202-2v-20c0-1.104-.896-2-2-2zm-3%2022h-2v-1h2v1zm3-3h-8v-15h8v15z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       98,
                Name:           "Laptop",
                Icon:           Icon.Laptop,
                Description:    "An icon representing a laptop computer, typically shown as a portable computer with a screen and keyboard",
                Tags:           ["computer", "notebook", "portable", "device"],
                Category:       "Devices",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M20%2021h-16c-1.104%200-2-.896-2-2v-12c0-1.104.896-2%202-2h16c1.104%200%202%20.896%202%202v12c0%201.104-.896%202-2%202zm-16-14v12h16v-12h-16zm14%2010h-12v1h12v-1zm-6-7c1.656%200%203%201.344%203%203s-1.344%203-3%203-3-1.344-3-3%201.344-3%203-3z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       99,
                Name:           "ComputerDesktop",
                Icon:           Icon.ComputerDesktop,
                Description:    "An icon representing a desktop computer, typically shown as a monitor with a keyboard",
                Tags:           ["computer", "PC", "workstation", "desktop"],
                Category:       "Devices",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M22%2018v-12h-20v12h20zm2-12v14h-24v-14h24zm-15%2015v1h-3v-1h3zm8%200v1h-3v-1h3zm-4%200v1h-3v-1h3z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       100,
                Name:           "Devices",
                Icon:           Icon.Devices,
                Description:    "An icon representing multiple electronic devices, typically shown as a combination of smartphone, tablet, and laptop or desktop computer",
                Tags:           ["electronics", "gadgets", "technology", "multi-device"],
                Category:       "Devices",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M24%2020v1h-24v-1h24zm-13-5h2v4h-2v-4zm-8%204h6v-3h-1v2h-4v-14h3v-1h-4v16zm20-6h-1v5h-6v-5h-1v6h8v-6zm-11-11v17h12v-17h-12zm11%2016h-10v-15h10v15zm-14-13v4h2v-4h-2zm1%2014h1v-3h-2v4h1v-1z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       101,
                Name:           "Controller",
                Icon:           Icon.Controller,
                Description:    "An icon representing a game controller or gamepad, typically shown as a simplified gaming device with buttons",
                Tags:           ["gamepad", "gaming", "joystick", "console"],
                Category:       "Entertainment",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M19%2010h-14c-2.762%200-5%202.239-5%205s2.238%205%205%205h14c2.762%200%205-2.239%205-5s-2.238-5-5-5zm-15%208c-1.654%200-3-1.346-3-3s1.346-3%203-3%203%201.346%203%203-1.346%203-3%203zm3-5v4h2v-4h-2zm3%200v4h2v-4h-2zm3%200v4h2v-4h-2zm3%201h2v2h-2v-2zm3-1v4h2v-4h-2z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       102,
                Name:           "Tools",
                Icon:           Icon.Tools,
                Description:    "An icon representing tools or settings, typically shown as a wrench and screwdriver crossed",
                Tags:           ["settings", "repair", "maintenance", "configure"],
                Category:       "Utilities",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M5.662%2023.91c1.186-1.186%201.186-3.11%200-4.296l-1.038-1.038c-1.186-1.186-3.11-1.186-4.296%200-1.186%201.186-1.186%203.11%200%204.296l1.038%201.038c1.186%201.186%203.11%201.186%204.296%200zm15.241-15.241c1.186-1.186%201.186-3.11%200-4.296l-1.038-1.038c-1.186-1.186-3.11-1.186-4.296%200-1.186%201.186-1.186%203.11%200%204.296l1.038%201.038c1.186%201.186%203.11%201.186%204.296%200zm-8.37%208.37c-.585.585-.585%201.536%200%202.121l3.535%203.536c.586.585%201.536.585%202.121%200%20.586-.585.586-1.536%200-2.121l-3.535-3.536c-.585-.585-1.536-.585-2.121%200zm4.413-11.084c.586-.586.586-1.535%200-2.121l-3.536-3.535c-.585-.586-1.535-.586-2.121%200-.586.585-.586%201.535%200%202.121l3.536%203.535c.585.586%201.535.586%202.121%200z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       103,
                Name:           "ToolsWrench",
                Icon:           Icon.ToolsWrench,
                Description:    "An icon representing a wrench tool, typically shown as a single adjustable wrench",
                Tags:           ["wrench", "repair", "maintenance", "adjust"],
                Category:       "Utilities",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M22.526%2012.832l-4.588-4.588c-.089-.089-.234-.089-.323%200l-1.647%201.647c-.089.089-.089.234%200%20.323l4.588%204.588c.089.089.234.089.323%200l1.647-1.647c.089-.089.089-.234%200-.323zm-5.085%201.647l-1.647-1.647c-.089-.089-.234-.089-.323%200l-9.647%209.647c-.089.089-.089.234%200%20.323l1.647%201.647c.089.089.234.089.323%200l9.647-9.647c.089-.089.089-.234%200-.323zm-11.97%2011.97l-1.647-1.647c-.089-.089-.234-.089-.323%200l-2.47%202.47c-.089.089-.089.234%200%20.323l1.647%201.647c.089.089.234.089.323%200l2.47-2.47c.089-.089.089-.234%200-.323zm-3.441-3.441l-1.647-1.647c-.089-.089-.234-.089-.323%200l-2.47%202.47c-.089.089-.089.234%200%20.323l1.647%201.647c.089.089.234.089.323%200l2.47-2.47c.089-.089.089-.234%200-.323z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       104,
                Name:           "Mail",
                Icon:           Icon.Mail,
                Description:    "An icon representing an envelope or email, typically shown as a simplified envelope shape",
                Tags:           ["email", "message", "envelope", "communication"],
                Category:       "Communication",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M24%2021h-24v-18h24v18zm-23-16.477v15.477h22v-15.477l-10.999%2010-11.001-10zm21.089-.523h-20.176l10.088%209.171%2010.088-9.171z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       105,
                Name:           "Send",
                Icon:           Icon.Send,
                Description:    "An icon representing the action of sending a message, typically shown as a paper airplane",
                Tags:           ["send", "message", "paper airplane", "submit"],
                Category:       "Communication",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M24%200l-6%2022-8.129-8.129%207.239-7.239-13.11%206.871%201.17%201.17-5.17%2012.17%2022-18.87zm-13%207.739l-1.261%201.261%204.222%204.222%201.261-1.261-4.222-4.222z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       106,
                Name:           "Clock",
                Icon:           Icon.Clock,
                Description:    "An icon representing a clock or time, typically shown as a circular clock face with hands",
                Tags:           ["time", "watch", "schedule", "hour"],
                Category:       "Time",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12%200c6.623%200%2012%205.377%2012%2012s-5.377%2012-12%2012-12-5.377-12-12%205.377-12%2012-12zm0%201c6.071%200%2011%204.929%2011%2011s-4.929%2011-11%2011-11-4.929-11-11%204.929-11%2011-11zm0%2011h6v1h-7v-9h1v8z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       107,
                Name:           "ListWatchlistRemind",
                Icon:           Icon.ListWatchlistRemind,
                Description:    "An icon representing a watchlist or reminder list, typically shown as a checklist with a clock or bell",
                Tags:           ["watchlist", "reminder", "checklist", "alert"],
                Category:       "Productivity",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M24%2023h-24v-19h4v-3h4v3h8v-3h4v3h4v19zm-1-15h-22v14h22v-14zm-16.501%208.794l1.032-.128c.201.93.693%201.538%201.644%201.538.957%200%201.731-.686%201.731-1.634%200-.989-.849-1.789-2.073-1.789h-.635v-1.092h.576c1.096%200%201.872-.744%201.872-1.673%200-.775-.597-1.357-1.444-1.357-.789%200-1.404.507-1.541%201.322l-1.031-.229c.238-1.199%201.137-2.041%202.556-2.041%201.492%200%202.518.969%202.518%202.34%200%201.028-.624%201.774-1.509%201.981.994.104%201.739.992%201.739%202.079%200%201.462-1.262%202.486-2.892%202.486-1.617%200-2.563-.916-2.798-2.064l1.255-.739zm8.896-3.068h-2.395v2.395h-1v-2.395h-2.395v-1h2.395v-2.395h1v2.395h2.395v1z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       108,
                Name:           "LogJournal",
                Icon:           Icon.LogJournal,
                Description:    "An icon representing a log or journal, typically shown as a book or notepad with writing",
                Tags:           ["log", "journal", "record", "diary"],
                Category:       "Productivity",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M24%2023h-24v-19h4v-3h4v3h8v-3h4v3h4v19zm-1-15h-22v14h22v-14zm-16.5%208h3v3h-3v-3zm6.5%200h3v3h-3v-3zm6.5%200h3v3h-3v-3zm-13-4h3v3h-3v-3zm6.5%200h3v3h-3v-3zm6.5%200h3v3h-3v-3zm-13-4h3v3h-3v-3zm6.5%200h3v3h-3v-3zm6.5%200h3v3h-3v-3z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       109,
                Name:           "Note",
                Icon:           Icon.Note,
                Description:    "An icon representing a note or memo, typically shown as a piece of paper with writing or a folded corner",
                Tags:           ["memo", "paper", "write", "document"],
                Category:       "Productivity",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M22%2024h-20v-24h14l6%206v18zm-7-23h-12v22h18v-16h-6v-6zm1%205h4.586l-4.586-4.586v4.586zm-3%2013h-8v-1h8v1zm0-3h-8v-1h8v1zm0-3h-8v-1h8v1z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       110,
                Name:           "PhotosPictures",
                Icon:           Icon.PhotosPictures,
                Description:    "An icon representing photos or pictures, typically shown as multiple overlapping image frames",
                Tags:           ["photos", "pictures", "images", "gallery"],
                Category:       "Media",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M24%2022h-24v-20h24v20zm-1-19h-22v18h22v-18zm-1%2016h-19l4-7.492%203%203.048%205.013-7.556%206.987%2012zm-11.848-2.865l-2.91-2.956-2.574%204.821h15.593l-5.303-9.108-4.806%207.243zm-4.652-11.135c1.38%200%202.5%201.12%202.5%202.5s-1.12%202.5-2.5%202.5-2.5-1.12-2.5-2.5%201.12-2.5%202.5-2.5zm0%201c.828%200%201.5.672%201.5%201.5s-.672%201.5-1.5%201.5-1.5-.672-1.5-1.5.672-1.5%201.5-1.5z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       111,
                Name:           "RadarActivityMonitor",
                Icon:           Icon.RadarActivityMonitor,
                Description:    "An icon representing a radar or activity monitor, typically shown as a circular display with scanning lines or activity indicators",
                Tags:           ["radar", "monitor", "activity", "scan"],
                Category:       "Analytics",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12%200c6.623%200%2012%205.377%2012%2012s-5.377%2012-12%2012-12-5.377-12-12%205.377-12%2012-12zm0%201c6.071%200%2011%204.929%2011%2011s-4.929%2011-11%2011-11-4.929-11-11%204.929-11%2011-11zm0%2011h6v1h-7v-9h1v8z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       112,
                Name:           "Tablet",
                Icon:           Icon.Tablet,
                Description:    "An icon representing a tablet device, typically shown as a rectangular device with a large screen",
                Tags:           ["device", "iPad", "touchscreen", "portable"],
                Category:       "Devices",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M22%200h-20v24h20v-24zm-1%2023h-18v-22h18v22zm-3-20h-12v18h12v-18zm-6%2017c.552%200%201-.448%201-1s-.448-1-1-1-1%20.448-1%201%20.448%201%201%201z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       113,
                Name:           "Tag",
                Icon:           Icon.Tag,
                Description:    "An icon representing a tag or label, typically shown as a simplified tag shape with a hole for attachment",
                Tags:           ["label", "category", "price", "identifier"],
                Category:       "Commerce",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12.503%200c6.683%200%2011.941%205.421%2011.497%2012.253-.444%206.831-6.159%2011.747-12.841%2011.747-6.683%200-11.941-5.421-11.497-12.253.444-6.831%206.159-11.747%2012.841-11.747zm4.647%207.705c-.707%200-1.28.573-1.28%201.28%200%20.707.573%201.28%201.28%201.28.707%200%201.28-.573%201.28-1.28%200-.707-.573-1.28-1.28-1.28z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       114,
                Name:           "CameraAperture",
                Icon:           Icon.CameraAperture,
                Description:    "An icon representing a camera aperture, typically shown as a circular shape with blades forming an opening",
                Tags:           ["camera", "lens", "photography", "focus"],
                Category:       "Media",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12%200c-6.627%200-12%205.373-12%2012s5.373%2012%2012%2012%2012-5.373%2012-12-5.373-12-12-12zm0%2022c-5.514%200-10-4.486-10-10s4.486-10%2010-10%2010%204.486%2010%2010-4.486%2010-10%2010zm-1.834-15.444l4.244%207.352-7.352%204.244%204.244-7.352-1.136-4.244zm1.834%202.444c-1.104%200-2%20.896-2%202s.896%202%202%202%202-.896%202-2-.896-2-2-2z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       115,
                Name:           "ColorPicker",
                Icon:           Icon.ColorPicker,
                Description:    "An icon representing a color picker tool, typically shown as an eyedropper or color selection tool",
                Tags:           ["eyedropper", "color", "palette", "design"],
                Category:       "Design",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M21.192%2013.918l-8.941-8.941-1.414%201.414%208.941%208.941%201.414-1.414zm-9.61-6.11l-2.83-2.83-7.778%207.778%202.83%202.83%207.778-7.778zm-7.06%207.06l1.415%201.415-2.242%202.242-1.414-1.414%202.241-2.243zm-1.415%205.657l2.243-2.242%201.414%201.414-2.242%202.243-1.415-1.415zm3.535%201.414l-1.414-1.414%202.242-2.243%201.414%201.415-2.242%202.242zm.708-9.192l2.121%202.121-2.121%202.121-2.121-2.121%202.121-2.121zm.707-2.121l1.414%201.414-2.121%202.121-1.414-1.414%202.121-2.121zm8.49-5.193l2.121%202.121-1.414%201.414-2.121-2.121%201.414-1.414zm-1.414%202.828l2.121%202.121-2.121%202.121-2.121-2.121%202.121-2.121zm-2.121%204.243l2.121%202.121-2.121%202.121-2.121-2.121%202.121-2.121zm4.243%202.121l2.121%202.121-1.415%201.415-2.121-2.122%201.415-1.414zm2.121-2.121l1.414%201.414-2.121%202.121-1.414-1.414%202.121-2.121zm2.121-6.364l-2.121%202.121-1.414-1.414%202.121-2.121%201.414%201.414z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       116,
                Name:           "DetailList",
                Icon:           Icon.DetailList,
                Description:    "An icon representing a detailed list view, typically shown as multiple horizontal lines representing list items with additional details",
                Tags:           ["list", "details", "view", "items"],
                Category:       "Interface",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M24%203h-16v2h16v-2zm0%204h-16v2h16v-2zm0%204h-16v2h16v-2zm0%204h-16v2h16v-2zm0%204h-16v2h16v-2zm-18-16h-6v2h6v-2zm0%204h-6v2h6v-2zm0%204h-6v2h6v-2zm0%204h-6v2h6v-2zm0%204h-6v2h6v-2z%22%2F%3E%3C%2Fsvg%3E"
            },
            {
                Sequence:       117,
                Name:           "DocumentWithContent",
                Icon:           Icon.DocumentWithContent,
                Description:    "An icon representing a document with content, typically shown as a paper sheet with lines or text",
                Tags:           ["file", "content", "text", "paper"],
                Category:       "Files",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M22%2024h-20v-24h14l6%206v18zm-7-23h-12v22h18v-16h-6v-6zm1%205h4.586l-4.586-4.586v4.586zm-3%2013h-8v-1h8v1zm0-3h-8v-1h8v1zm0-3h-8v-1h8v1zm0-3h-4v-1h4v1z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       118,
                Name:           "ListScrollEmpty",
                Icon:           Icon.ListScrollEmpty,
                Description:    "An icon representing an empty scrollable list, typically shown as a rectangle with horizontal lines and a scroll bar",
                Tags:           ["list", "empty", "scroll", "view"],
                Category:       "Interface",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M24%2021h-24v-18h24v18zm-1-17h-22v16h22v-16zm-3%204h-16v1h16v-1zm0%203h-16v1h16v-1zm0%203h-16v1h16v-1zm-18-8h1v12h-1v-12z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       119,
                Name:           "ListScrollWatchlist",
                Icon:           Icon.ListScrollWatchlist,
                Description:    "An icon representing a scrollable watchlist, typically shown as a list with a scroll bar and a star or eye symbol",
                Tags:           ["watchlist", "scroll", "favorites", "monitor"],
                Category:       "Interface",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M24%2021h-24v-18h24v18zm-1-17h-22v16h22v-16zm-3%204h-16v1h16v-1zm0%203h-16v1h16v-1zm0%203h-16v1h16v-1zm-18-8h1v12h-1v-12zm4%2010l2-2%202%202%204-4%202%202%204-4v6h-14v-6z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       120,
                Name:           "OptionsList",
                Icon:           Icon.OptionsList,
                Description:    "An icon representing a list of options or settings, typically shown as a series of horizontal lines with toggles or checkboxes",
                Tags:           ["options", "settings", "menu", "preferences"],
                Category:       "Interface",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M24%2014v-4h-4v4h4zm-8%200v-4h-4v4h4zm-8%200v-4h-4v4h4zm16%206v-4h-4v4h4zm-8%200v-4h-4v4h4zm-8%200v-4h-4v4h4zm16-12v-4h-4v4h4zm-8%200v-4h-4v4h4zm-8%200v-4h-4v4h4z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       121,
                Name:           "LightningBolt",
                Icon:           Icon.LightningBolt,
                Description:    "An icon representing a lightning bolt, typically shown as a jagged line symbolizing electricity or fast action",
                Tags:           ["electricity", "power", "energy", "fast"],
                Category:       "Weather",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M13%200l-13%2016h8l-8%208%2024-14h-8l8-10z%22%2F%3E%3C%2Fsvg%3E"
            },
            {
                Sequence:       122,
                Name:           "HorizontalLine",
                Icon:           Icon.HorizontalLine,
                Description:    "An icon representing a horizontal line, typically shown as a straight horizontal line used for separation or division",
                Tags:           ["line", "separator", "divider", "horizontal"],
                Category:       "Interface",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M24%2011v2h-24v-2h24z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       123,
                Name:           "VerticalLine",
                Icon:           Icon.VerticalLine,
                Description:    "An icon representing a vertical line, typically shown as a straight vertical line used for separation or division",
                Tags:           ["line", "separator", "divider", "vertical"],
                Category:       "Interface",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M11%200h2v24h-2v-24z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       124,
                Name:           "Ribbon",
                Icon:           Icon.Ribbon,
                Description:    "An icon representing a ribbon, typically shown as a decorative ribbon shape often used for awards or special designations",
                Tags:           ["award", "prize", "recognition", "decoration"],
                Category:       "Miscellaneous",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M13.5%2018.972h-3l-2.5%205.028%204-2%204%202-2.5-5.028zm9.5-10.972c0%205.523-4.477%2010-10%2010s-10-4.477-10-10%204.477-10%2010-10%2010%204.477%2010%2010zm-10%208c4.411%200%208-3.589%208-8s-3.589-8-8-8-8%203.589-8%208%203.589%208%208%208z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       125,
                Name:           "Diamond",
                Icon:           Icon.Diamond,
                Description:    "An icon representing a diamond, typically shown as a stylized diamond shape often used to symbolize luxury or value",
                Tags:           ["gem", "jewel", "luxury", "value"],
                Category:       "Miscellaneous",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12%200l-12%2012%2012%2012%2012-12-12-12zm-1.047%2013.423l-5.584-5.584%205.584-5.584%205.584%205.584-5.584%205.584z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       126,
                Name:           "Alarm",
                Icon:           Icon.Alarm,
                Description:    "An icon representing an alarm, typically shown as a ringing bell or clock face with alarm indicators",
                Tags:           ["alert", "notification", "reminder", "clock"],
                Category:       "Time",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12%200c6.623%200%2012%205.377%2012%2012s-5.377%2012-12%2012-12-5.377-12-12%205.377-12%2012-12zm0%201c6.071%200%2011%204.929%2011%2011s-4.929%2011-11%2011-11-4.929-11-11%204.929-11%2011-11zm0%2011h6v1h-7v-9h1v8zm-5.268-4.732l-2.146-2.146.707-.707%202.146%202.146-.707.707zm10.536%200l-.707-.707%202.146-2.146.707.707-2.146%202.146z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       127,
                Name:           "History",
                Icon:           Icon.History,
                Description:    "An icon representing history or past events, typically shown as a clock face with an arrow pointing counterclockwise",
                Tags:           ["past", "time", "record", "chronology"],
                Category:       "Time",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12%200c6.623%200%2012%205.377%2012%2012s-5.377%2012-12%2012-12-5.377-12-12%205.377-12%2012-12zm0%201c6.071%200%2011%204.929%2011%2011s-4.929%2011-11%2011-11-4.929-11-11%204.929-11%2011-11zm1%205h-2v7h6v-2h-4v-5z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       128,
                Name:           "Heart",
                Icon:           Icon.Heart,
                Description:    "An icon representing a heart, typically shown as a stylized heart shape often used to symbolize love, affection, or favorites",
                Tags:           ["love", "like", "favorite", "affection"],
                Category:       "Miscellaneous",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12%2021.593c-5.63-5.539-11-10.297-11-14.402%200-3.791%203.068-5.191%205.281-5.191%201.312%200%204.151.501%205.719%204.457%201.59-3.968%204.464-4.447%205.726-4.447%202.54%200%205.274%201.621%205.274%205.181%200%204.069-5.136%208.625-11%2014.402m5.726-20.583c-2.203%200-4.446%201.042-5.726%203.238-1.285-2.206-3.522-3.248-5.719-3.248-3.183%200-6.281%202.187-6.281%206.191%200%204.661%205.571%209.429%2012%2015.809%206.43-6.38%2012-11.148%2012-15.809%200-4.011-3.095-6.181-6.274-6.181%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       129,
                Name:           "Print",
                Icon:           Icon.Print,
                Description:    "An icon representing a printer or the action of printing, typically shown as a simplified printer device",
                Tags:           ["printer", "document", "paper", "output"],
                Category:       "Office",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M19%2020h-14v-8h-2v10h18v-10h-2v8zm-10-15v-5h6v5h2v-5c0-1.104-.896-2-2-2h-6c-1.104%200-2%20.896-2%202v5h2zm11%203h-20c-1.104%200-2%20.896-2%202v5c0%201.104.896%202%202%202h1v-3h18v3h1c1.104%200%202-.896%202-2v-5c0-1.104-.896-2-2-2zm-1%202c.552%200%201%20.448%201%201s-.448%201-1%201-1-.448-1-1%20.448-1%201-1z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       130,
                Name:           "Error",
                Icon:           Icon.Error,
                Description:    "An icon representing an error or warning, typically shown as an exclamation mark in a triangle or circle",
                Tags:           ["warning", "alert", "danger", "caution"],
                Category:       "Interface",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12%200c6.623%200%2012%205.377%2012%2012s-5.377%2012-12%2012-12-5.377-12-12%205.377-12%2012-12zm0%201c6.071%200%2011%204.929%2011%2011s-4.929%2011-11%2011-11-4.929-11-11%204.929-11%2011-11zm.5%2017h-1v-2h1v2zm-1-3.464v-8.536h1v8.536h-1z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       131,
                Name:           "Flag",
                Icon:           Icon.Flag,
                Description:    "An icon representing a flag, typically shown as a rectangular or triangular shape on a pole",
                Tags:           ["banner", "marker", "signal", "country"],
                Category:       "Miscellaneous",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M4%200v24h-2v-24h2zm18%201h-16v10h16l-4-5 4-5zm-3.435%2015h-12.565v1h12.585l-.02-.999v-.001zm0%203h-12.565v1h12.585l-.02-.999v-.001z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       132,
                Name:           "Notebook",
                Icon:           Icon.Notebook,
                Description:    "An icon representing a notebook or journal, typically shown as a bound book with lines or a spiral binding",
                Tags:           ["journal", "diary", "notes", "writing"],
                Category:       "Office",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M22%200h-20v24h20v-24zm-1%2023h-18v-22h18v22zm-3-3h-12v-1h12v1zm0-3h-12v-1h12v1zm0-3h-12v-1h12v1zm-7.348-3.863l.948.3c-.145.529-.387.922-.725%201.178-.338.257-.767.385-1.287.385-.643%200-1.171-.22-1.585-.659-.414-.439-.621-1.04-.621-1.802%200-.806.208-1.432.624-1.878.416-.446.963-.669%201.642-.669.592%200%201.073.175%201.443.525.221.207.386.505.496.892l-.968.231c-.057-.251-.177-.449-.358-.594-.182-.146-.403-.218-.663-.218-.359%200-.65.129-.874.386-.223.258-.335.675-.335%201.252%200%20.613.11%201.049.331%201.308.22.26.506.39.858.39.26%200%20.484-.082.671-.248.187-.165.322-.425.403-.779zm3.023%201.78l-1.731-4.842h1.06l1.226%203.584%201.186-3.584h1.037l-1.734%204.842h-1.044z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       133,
                Name:           "Bug",
                Icon:           Icon.Bug,
                Description:    "An icon representing a bug or software error, typically shown as a stylized insect or a symbol indicating a programming issue",
                Tags:           ["error", "glitch", "insect", "debugging"],
                Category:       "Development",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M19%2024h-14c-1.104%200-2-.896-2-2v-16c0-1.104.896-2%202-2h14c1.104%200%202%20.896%202%202v16c0%201.104-.896%202-2%202zm-9-9h-2v2h2v-2zm4%200h-2v2h2v-2zm4%200h-2v2h2v-2zm-12%200h-2v2h2v-2zm8-4h-2v2h2v-2zm4%200h-2v2h2v-2zm-8%200h-2v2h2v-2zm-4%200h-2v2h2v-2zm12-4h-2v2h2v-2zm-4%200h-2v2h2v-2zm-4%200h-2v2h2v-2zm-4%200h-2v2h2v-2z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       134,
                Name:           "Microphone",
                Icon:           Icon.Microphone,
                Description:    "An icon representing a microphone, typically shown as a simplified handheld or stand microphone used for audio input",
                Tags:           ["audio", "voice", "record", "sound"],
                Category:       "Media",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12%201c-2.209%200-4%201.791-4%204v6c0%202.209%201.791%204%204%204s4-1.791%204-4v-6c0-2.209-1.791-4-4-4zm0%202c1.103%200%202%20.897%202%202v6c0%201.103-.897%202-2%202s-2-.897-2-2v-6c0-1.103.897-2%202-2zm-6%2010v1c0%203.313%202.687%206%206%206s6-2.687%206-6v-1h-2v1c0%202.206-1.794%204-4%204s-4-1.794-4-4v-1h-2zm-2%204v2h16v-2h-16z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       135,
                Name:           "Video",
                Icon:           Icon.Video,
                Description:    "An icon representing video or a video camera, typically shown as a simplified camera or a play button within a frame",
                Tags:           ["movie", "film", "camera", "recording"],
                Category:       "Media",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M0%201v22h24v-22h-24zm4%2018v-14h16v14h-16zm2-12v10h12v-10h-12zm15%2010l3%202v-12l-3%202v8z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       136,
                Name:           "Shop",
                Icon:           Icon.Shop,
                Description:    "An icon representing a shop or store, typically shown as a simplified storefront or shopping bag",
                Tags:           ["store", "retail", "market", "commerce"],
                Category:       "Commerce",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M24%2022h-24v-14h24v14zm-2-12h-20v10h20v-10zm-10-2v-6h-2v6h-6v2h14v-2h-6zm-4%2011h-3v-3h3v3zm4%200h-3v-3h3v3zm4%200h-3v-3h3v3zm4%200h-3v-3h3v3z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       137,
                Name:           "Phonebook",
                Icon:           Icon.Phonebook,
                Description:    "An icon representing a phonebook or contact list, typically shown as a book with a telephone symbol or a list of contacts",
                Tags:           ["contacts", "directory", "address book", "phone list"],
                Category:       "Communication",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M24%2022h-24v-20h24v20zm-1-19h-22v18h22v-18zm-4%204h-14v1h14v-1zm0%203h-14v1h14v-1zm0%203h-14v1h14v-1zm-3%203h-11v1h11v-1zm-11-12h10v2h-10v-2z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       138,
                Name:           "Enhance",
                Icon:           Icon.Enhance,
                Description:    "An icon representing enhancement or improvement, typically shown as a magic wand or a sparkle symbol",
                Tags:           ["improve", "upgrade", "optimize", "magic"],
                Category:       "Editing",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12%200l-11%206v12.131l11%205.869%2011-5.869v-12.066l-11-6.065zm7.91%206.646l-7.905%204.218-7.872-4.294%207.862-4.289%207.915%204.365zm-6.91%2014.554v-8.6l8-4.269v8.6l-8%204.269z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       139,
                Name:           "Unlock",
                Icon:           Icon.Unlock,
                Description:    "An icon representing an unlocked state, typically shown as an open padlock or a lock with an open shackle",
                Tags:           ["open", "access", "security", "permission"],
                Category:       "Security",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M23.5%2018h-23v-12h23v12zm-1-11h-21v10h21v-10zm-14.5%207h-3v-2.414l3-3.086v5.5zm7%200h-3v-2.414l3-3.086v5.5zm7%200h-3v-2.414l3-3.086v5.5zm-14-7h-3v-2h3v2zm7%200h-3v-2h3v2zm7%200h-3v-2h3v2z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       140,
                Name:           "Calculator",
                Icon:           Icon.Calculator,
                Description:    "An icon representing a calculator, typically shown as a simplified device with number buttons and a display screen",
                Tags:           ["math", "computation", "arithmetic", "calculate"],
                Category:       "Office",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M20%200h-16v24h16v-24zm-2%2022h-12v-20h12v20zm-2-18h-8v4h8v-4zm0%206h-2v2h2v-2zm0%204h-2v2h2v-2zm0%204h-2v2h2v-2zm-4-8h-2v2h2v-2zm0%204h-2v2h2v-2zm0%204h-2v2h2v-2zm-4-8h-2v2h2v-2zm0%204h-2v2h2v-2zm0%204h-2v2h2v-2z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       141,
                Name:           "Support",
                Icon:           Icon.Support,
                Description:    "An icon representing support or customer service, typically shown as a headset, speech bubble, or a person offering assistance",
                Tags:           ["help", "customer service", "assistance", "technical support"],
                Category:       "Communication",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12%200c6.627%200%2012%205.373%2012%2012s-5.373%2012-12%2012-12-5.373-12-12%205.373-12%2012-12zm0%202c5.514%200%2010%204.486%2010%2010s-4.486%2010-10%2010-10-4.486-10-10%204.486-10%2010-10zm0%2013.5c-1.38%200-2.5-1.12-2.5-2.5s1.12-2.5%202.5-2.5%202.5%201.12%202.5%202.5-1.12%202.5-2.5%202.5zm1.5-9.5h-3v2h3v-2z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       142,
                Name:           "Lightbulb",
                Icon:           Icon.Lightbulb,
                Description:    "An icon representing a lightbulb, typically shown as a simplified incandescent bulb shape, often used to symbolize ideas or inspiration",
                Tags:           ["idea", "inspiration", "innovation", "creativity"],
                Category:       "Miscellaneous",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12%200c-4.087%200-7.5%203.413-7.5%207.5%200%203.053%201.878%205.671%204.5%206.75v4.75h6v-4.75c2.622-1.079%204.5-3.697%204.5-6.75%200-4.087-3.413-7.5-7.5-7.5zm0%2021c-.553%200-1%20.448-1%201s.447%201%201%201%201-.448%201-1-.447-1-1-1zm0-18c3.308%200%206%202.692%206%206s-2.692%206-6%206-6-2.692-6-6%202.692-6%206-6z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       143,
                Name:           "Key",
                Icon:           Icon.Key,
                Description:    "An icon representing a key, typically shown as a simplified key shape with a distinctive head and shaft, often used to symbolize access or security",
                Tags:           ["access", "security", "unlock", "password"],
                Category:       "Security",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M16%201c-4.418%200-8%203.582-8%208%200%20.585.063%201.155.182%201.704l-8.182%208.296v5h6v-2h2v-2h2l3.066-3.111c.909.359%201.898.557%202.934.557%204.418%200%208-3.582%208-8s-3.582-8-8-8zm0%2013c-2.761%200-5-2.239-5-5s2.239-5%205-5%205%202.239%205%205-2.239%205-5%205z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       144,
                Name:           "Scan",
                Icon:           Icon.Scan,
                Description:    "An icon representing scanning or barcode reading, typically shown as a simplified scanner or barcode with scanning lines",
                Tags:           ["barcode", "QR code", "reader", "scanning"],
                Category:       "Technology",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M24%2021v1h-24v-1h24zm0-20h-24v1h24v-1zm-24%2019h24v-16h-24v16zm23-15v14h-22v-14h22z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       145,
                Name:           "Hospital",
                Icon:           Icon.Hospital,
                Description:    "An icon representing a hospital or medical facility, typically shown as a building with a cross symbol or a simplified medical emblem",
                Tags:           ["medical", "healthcare", "emergency", "clinic"],
                Category:       "Health",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M24%2024h-24v-24h24v24zm-1-23h-22v22h22v-22zm-11%201h1v8h8v1h-8v8h-1v-8h-8v-1h8v-8z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       146,
                Name:           "Health",
                Icon:           Icon.Health,
                Description:    "An icon representing health or wellness, typically shown as a heart symbol, medical cross, or a simplified human figure",
                Tags:           ["wellness", "medical", "healthcare", "healthy"],
                Category:       "Health",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12%200c6.627%200%2012%205.373%2012%2012s-5.373%2012-12%2012-12-5.373-12-12%205.373-12%2012-12zm0%201c6.071%200%2011%204.929%2011%2011s-4.929%2011-11%2011-11-4.929-11-11%204.929-11%2011-11zm0%2011h6v1h-6v6h-1v-6h-6v-1h6v-6h1v6z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       147,
                Name:           "Medical",
                Icon:           Icon.Medical,
                Description:    "An icon representing medical or healthcare services, typically shown as a medical cross, caduceus symbol, or a simplified medical instrument",
                Tags:           ["healthcare", "doctor", "medicine", "hospital"],
                Category:       "Health",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M15.999%2012.998v-2h-4v-4h-2v4h-4v2h4v4h2v-4h4zm-15.999-12.998v24h24v-24h-24zm22%2022h-20v-20h20v20z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       148,
                Name:           "Manufacture",
                Icon:           Icon.Manufacture,
                Description:    "An icon representing manufacturing or industrial production, typically shown as a factory building, assembly line, or gear symbols",
                Tags:           ["factory", "industry", "production", "assembly"],
                Category:       "Industry",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M20%209.352v-3.352h-16v14h16v-3.352l4%202.352v-12l-4%202.352zm-2%208.648h-12v-10h12v10zm-7-6h-3v4h3v-4zm5%200h-3v4h3v-4z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       149,
                Name:           "Train",
                Icon:           Icon.Train,
                Description:    "An icon representing a train or railway transportation, typically shown as a simplified side view of a train or locomotive",
                Tags:           ["railway", "transportation", "locomotive", "subway"],
                Category:       "Transportation",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M18%209h-12v8h12v-8zm-10 7c-.552%200-1-.448-1-1s.448-1%201-1%201%20.448%201%201-.448%201-1%201zm8%200c-.552%200-1-.448-1-1s.448-1%201-1%201%20.448%201%201-.448%201-1%201zm2-12h-12l-2-5h16l-2%205zm-12%2013h12v5h-12v-5z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       150,
                Name:           "Globe",
                Icon:           Icon.Globe,
                Description:    "An icon representing a globe or world map, typically shown as a circular shape with simplified continents or latitude and longitude lines",
                Tags:           ["world", "earth", "international", "global"],
                Category:       "Geography",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12%200c6.623%200%2012%205.377%2012%2012s-5.377%2012-12%2012-12-5.377-12-12%205.377-12%2012-12zm1%2016.057v-3.057h2.994c-.059%201.143-.212%202.24-.456%203.279-.823-.12-1.674-.188-2.538-.222zm1.957%202.162c-.499%201.33-1.159%202.497-1.957%203.456v-3.62c.666.028%201.319.081%201.957.164zm-1.957-7.219v-3.015c.868-.034%201.721-.103%202.548-.224.238%201.027.389%202.111.446%203.239h-2.994zm0-5.014v-3.661c.806.969%201.471%202.15%201.971%203.496-.642.084-1.3.137-1.971.165zm2.703-3.267c1.237.496%202.354%201.228%203.29%202.146-.642.234-1.311.442-2.019.607-.344-.992-.775-1.91-1.271-2.753zm-7.241%2013.56c-.244-1.039-.398-2.136-.456-3.279h2.994v3.057c-.865.034-1.714.102-2.538.222zm2.538%202.162v3.62c-.798-.959-1.458-2.126-1.957-3.456.638-.083%201.291-.136%201.957-.164zm-2.994-7.055c.057-1.128.207-2.212.446-3.239.827.121%201.68.19%202.548.224v3.015h-2.994zm1.024-5.179c.5-1.346%201.165-2.527%201.97-3.496v3.661c-.671-.028-1.329-.081-1.97-.165zm-2.005-.35c-.708-.165-1.377-.373-2.018-.607.937-.918%202.053-1.65%203.29-2.146-.496.844-.927%201.762-1.272%202.753zm-.549%201.918c-.264%201.151-.434%202.36-.492%203.611h-3.933c.165-1.658.739-3.197%201.617-4.518.88.361%201.816.67%202.808.907zm.009%209.262c-.988.236-1.92.542-2.797.9-.89-1.328-1.471-2.879-1.637-4.551h3.934c.058%201.265.231%202.488.5%203.651zm.553%201.917c.342.976.768%201.881%201.257%202.712-1.223-.49-2.326-1.211-3.256-2.115.636-.229%201.299-.435%201.999-.597zm9.924%200c.7.163%201.362.367%201.999.597-.931.903-2.034%201.625-3.257%202.116.489-.832.915-1.737%201.258-2.713zm.553-1.917c.27-1.163.442-2.386.501-3.651h3.934c-.167%201.672-.748%203.223-1.638%204.551-.877-.358-1.81-.664-2.797-.9zm.501-5.651c-.058-1.251-.229-2.46-.492-3.611.992-.237%201.929-.546%202.809-.907.877%201.321%201.451%202.86%201.616%204.518h-3.933z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       151,
                Name:           "GlobeNotConnected",
                Icon:           Icon.GlobeNotConnected,
                Description:    "An icon representing a globe with no internet connection, typically shown as a globe symbol with a disconnection indicator",
                Tags:           ["no internet", "offline", "disconnected", "network error"],
                Category:       "Network",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12%200c6.623%200%2012%205.377%2012%2012s-5.377%2012-12%2012-12-5.377-12-12%205.377-12%2012-12zm0%202c5.519%200%2010%204.481%2010%2010s-4.481%2010-10%2010-10-4.481-10-10%204.481-10%2010-10zm-2%208l-4-4-4%204%201.41%201.41%202.59-2.58v11.17h2v-11.17l2.59%202.58%201.41-1.41zm8%204l-4%204%204%204%201.41-1.41-2.58-2.59h11.17v-2h-11.17l2.58-2.59-1.41-1.41z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       152,
                Name:           "GlobeRefresh",
                Icon:           Icon.GlobeRefresh,
                Description:    "An icon representing a globe with a refresh or reload action, typically shown as a globe symbol with circular arrows indicating refresh",
                Tags:           ["reload", "update", "sync", "global refresh"],
                Category:       "Network",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12%200c6.623%200%2012%205.377%2012%2012s-5.377%2012-12%2012-12-5.377-12-12%205.377-12%2012-12zm0%202c5.519%200%2010%204.481%2010%2010s-4.481%2010-10%2010-10-4.481-10-10%204.481-10%2010-10zm5.707%207.293l-1.414%201.414c.667.667%201.085%201.588%201.085%202.607%200%202.033-1.654%203.686-3.686%203.686-1.019%200-1.94-.418-2.607-1.085l-1.414%201.414c.945.944%202.246%201.529%203.686%201.529%202.871%200%205.2-2.329%205.2-5.2%200-1.44-.585-2.741-1.529-3.686zm-9.414%201.414l1.414-1.414c-.945-.944-2.246-1.529-3.686-1.529-2.871%200-5.2%202.329-5.2%205.2%200%201.44.585%202.741%201.529%203.686l1.414-1.414c-.667-.667-1.085-1.588-1.085-2.607%200-2.033%201.654-3.686%203.686-3.686%201.019%200%201.94.418%202.607%201.085z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       153,
                Name:           "GlobeChangesPending",
                Icon:           Icon.GlobeChangesPending,
                Description:    "An icon representing a globe with pending changes, typically shown as a globe symbol with a clock or hourglass indicator",
                Tags:           ["global updates", "pending changes", "world sync", "update in progress"],
                Category:       "Network",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12%200c6.623%200%2012%205.377%2012%2012s-5.377%2012-12%2012-12-5.377-12-12%205.377-12%2012-12zm0%202c5.519%200%2010%204.481%2010%2010s-4.481%2010-10%2010-10-4.481-10-10%204.481-10%2010-10zm1%2010v-6h-2v8h7v-2h-5z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       154,
                Name:           "GlobeWarning",
                Icon:           Icon.GlobeWarning,
                Description:    "An icon representing a globe with a warning or alert, typically shown as a globe symbol with an exclamation mark or warning triangle",
                Tags:           ["global alert", "world warning", "international caution", "earth hazard"],
                Category:       "Network",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12%200c6.623%200%2012%205.377%2012%2012s-5.377%2012-12%2012-12-5.377-12-12%205.377-12%2012-12zm0%202c5.519%200%2010%204.481%2010%2010s-4.481%2010-10%2010-10-4.481-10-10%204.481-10%2010-10zm-1.086%2013.914h2.172v-2.172h-2.172v2.172zm0-8.914h2.172v-2h-2.172v2zm0%206.742h2.172v-4.828h-2.172v4.828z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       155,
                Name:           "GlobeError",
                Icon:           Icon.GlobeError,
                Description:    "An icon representing a globe with an error or critical issue, typically shown as a globe symbol with an 'X' mark or error symbol",
                Tags:           ["global error", "world problem", "international issue", "earth malfunction"],
                Category:       "Network",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12%200c6.623%200%2012%205.377%2012%2012s-5.377%2012-12%2012-12-5.377-12-12%205.377-12%2012-12zm0%202c5.519%200%2010%204.481%2010%2010s-4.481%2010-10%2010-10-4.481-10-10%204.481-10%2010-10zm0%208.75l3.536%203.536-1.414%201.414-2.122-2.122-2.122%202.122-1.414-1.414%203.536-3.536zm0-4.75c-2.209%200-4%201.791-4%204s1.791%204%204%204%204-1.791%204-4-1.791-4-4-4z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       156,
                Name:           "HalfFilledCircle",
                Icon:           Icon.HalfFilledCircle,
                Description:    "An icon representing a circle that is half filled, typically shown as a circular shape with one half solid and the other half empty or outlined",
                Tags:           ["half", "semicircle", "partial", "50 percent"],
                Category:       "Shapes",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12%200c6.623%200%2012%205.377%2012%2012s-5.377%2012-12%2012-12-5.377-12-12%205.377-12%2012-12zm0%202c5.519%200%2010%204.481%2010%2010s-4.481%2010-10%2010v-20z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       157,
                Name:           "Tray",
                Icon:           Icon.Tray,
                Description:    "An icon representing a tray or platform, typically shown as a flat, rectangular shape with raised edges, often used to symbolize a container or serving surface",
                Tags:           ["container", "platform", "serving", "inbox"],
                Category:       "Office",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M24%2023h-24v-13h24v13zm-1-12h-22v11h22v-11zm-15%206h-5v1h5v-1zm6-1h-5v1h5v-1zm6%200h-5v1h5v-1zm-12-2h-5v1h5v-1zm6%200h-5v1h5v-1zm6%200h-5v1h5v-1zm-13-8l4-4h9v1h4l-4%204v1h-13v-2zm1-1h11v1h-11v-1z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       158,
                Name:           "Text",
                Icon:           Icon.Text,
                Description:    "An icon representing text or typography, typically shown as a letter 'T' or a few lines symbolizing written content",
                Tags:           ["typography", "font", "writing", "content"],
                Category:       "Editing",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M24%2020h-24v-1h24v1zm0-19v2h-24v-2h24zm-8%205h8v2h-8v-2zm0%205h8v2h-8v-2zm-16-5h14v10h-14v-10z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       159,
                Name:           "Shirt",
                Icon:           Icon.Shirt,
                Description:    "An icon representing a shirt or clothing item, typically shown as a simplified outline of a collared shirt or t-shirt",
                Tags:           ["clothing", "apparel", "fashion", "garment"],
                Category:       "Fashion",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M16%2022h-8v-2h8v2zm4-4h-16v-12h3.562l2.438-2.438v2.438h4v-2.438l2.438%202.438h3.562v12zm-2-10h-12v8h12v-8z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       160,
                Name:           "Signal",
                Icon:           Icon.Signal,
                Description:    "An icon representing the Signal messaging app, typically shown as a speech bubble with a padlock inside",
                Tags:           ["messaging", "secure communication", "privacy", "encryption"],
                Category:       "Communication",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12%200c6.623%200%2012%205.377%2012%2012s-5.377%2012-12%2012-12-5.377-12-12%205.377-12%2012-12zm0%202c5.519%200%2010%204.481%2010%2010s-4.481%2010-10%2010-10-4.481-10-10%204.481-10%2010-10zm-3.5%2014.5l9-9-1.41-1.41-7.59%207.59-3.59-3.59-1.41%201.41%205%205z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       161,
                Name:           "People",
                Icon:           Icon.People,
                Description:    "An icon representing a group of people or users, typically shown as multiple simplified human figures",
                Tags:           ["users", "group", "community", "team"],
                Category:       "Social",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M17.997%2018h-11.995l-.002-.623c0-1.259.1-1.986%201.588-2.33%201.684-.389%203.344-.736%202.545-2.209-2.366-4.363-.674-6.838%201.866-6.838%202.491%200%204.226%202.383%201.866%206.839-.775%201.464.826%201.812%202.545%202.209%201.49.344%201.589%201.072%201.589%202.333l-.002.619zm4.811-2.214c-1.29-.298-2.49-.559-1.909-1.657%201.769-3.342.469-5.129-1.4-5.129-1.265%200-2.248.817-2.248%202.324%200%203.903%202.268%201.77%202.246%206.676h4.501l.002-.463c0-.946-.074-1.493-1.192-1.751zm-22.806%202.214h4.501c-.021-4.906%202.246-2.772%202.246-6.676%200-1.507-.983-2.324-2.248-2.324-1.869%200-3.169%201.787-1.399%205.129.581%201.099-.619%201.359-1.909%201.657-1.119.258-1.193.805-1.193%201.751l.002.463z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       162,
                Name:           "Person",
                Icon:           Icon.Person,
                Description:    "An icon representing a single person or user, typically shown as a simplified human figure or head and shoulders silhouette",
                Tags:           ["user", "individual", "profile", "avatar"],
                Category:       "Social",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12%200c6.623%200%2012%205.377%2012%2012s-5.377%2012-12%2012-12-5.377-12-12%205.377-12%2012-12zm8.127%2019.41c-.282-.401-.772-.654-1.624-.85-3.848-.906-4.097-1.501-4.352-2.059-.259-.565-.19-1.23.205-1.977%201.726-3.257%202.09-6.024%201.027-7.79-.674-1.119-1.875-1.734-3.383-1.734-1.521%200-2.732.626-3.409%201.763-1.066%201.789-.693%204.544%201.049%207.757.402.742.476%201.406.22%201.974-.265.586-.611%201.19-4.365%202.066-.852.196-1.342.449-1.623.848%202.012%202.207%204.91%203.592%208.128%203.592s6.115-1.385%208.127-3.59zm.65-.782c1.395-1.844%202.223-4.14%202.223-6.628%200-6.071-4.929-11-11-11s-11%204.929-11%2011c0%202.487.827%204.783%202.222%206.626.409-.452%201.049-.81%202.049-1.041%202.025-.462%203.376-.836%203.678-1.502.122-.272.061-.628-.188-1.087-1.917-3.535-2.282-6.641-1.03-8.745.853-1.431%202.408-2.251%204.269-2.251%201.845%200%203.391.808%204.24%202.218%201.251%202.079.896%205.195-1%208.774-.245.463-.304.821-.179%201.094.305.668%201.644%201.038%203.667%201.499%201%20.23%201.64.59%202.049%201.043z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       163,
                Name:           "EmojiFrown",
                Icon:           Icon.EmojiFrown,
                Description:    "An icon representing a frowning face emoji, typically shown as a circular face with downturned eyes and mouth",
                Tags:           ["sad", "unhappy", "disappointed", "negative"],
                Category:       "Emoji",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12%200c6.623%200%2012%205.377%2012%2012s-5.377%2012-12%2012-12-5.377-12-12%205.377-12%2012-12zm0%201c6.071%200%2011%204.929%2011%2011s-4.929%2011-11%2011-11-4.929-11-11%204.929-11%2011-11zm0%2012.25c2.781%200%205.181%201.458%206.51%203.635l-.868.54c-1.152-1.857-3.228-3.075-5.642-3.075-2.414%200-4.49%201.218-5.642%203.075l-.868-.54c1.329-2.177%203.729-3.635%206.51-3.635zm-3.53-5.75c.552%200%201%20.448%201%201s-.448%201-1%201-1-.448-1-1%20.448-1%201-1zm7.06%200c.552%200%201%20.448%201%201s-.448%201-1%201-1-.448-1-1%20.448-1%201-1z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       164,
                Name:           "EmojiSmile",
                Icon:           Icon.EmojiSmile,
                Description:    "An icon representing a smiling face emoji, typically shown as a circular face with upturned eyes and mouth",
                Tags:           ["happy", "joy", "positive", "cheerful"],
                Category:       "Emoji",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12%200c6.623%200%2012%205.377%2012%2012s-5.377%2012-12%2012-12-5.377-12-12%205.377-12%2012-12zm0%201c6.071%200%2011%204.929%2011%2011s-4.929%2011-11%2011-11-4.929-11-11%204.929-11%2011-11zm0%2012.25c2.781%200%205.181%201.458%206.51%203.635l-.868.54c-1.152-1.857-3.228-3.075-5.642-3.075-2.414%200-4.49%201.218-5.642%203.075l-.868-.54c1.329-2.177%203.729-3.635%206.51-3.635zm-3.53-5.75c.552%200%201%20.448%201%201s-.448%201-1%201-1-.448-1-1%20.448-1%201-1zm7.06%200c.552%200%201%20.448%201%201s-.448%201-1%201-1-.448-1-1%20.448-1%201-1z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       165,
                Name:           "EmojiSad",
                Icon:           Icon.EmojiSad,
                Description:    "An icon representing a sad face emoji, typically shown as a circular face with downturned eyes and mouth, often with a tear",
                Tags:           ["unhappy", "crying", "upset", "depressed"],
                Category:       "Emoji",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12%200c6.623%200%2012%205.377%2012%2012s-5.377%2012-12%2012-12-5.377-12-12%205.377-12%2012-12zm0%201c6.071%200%2011%204.929%2011%2011s-4.929%2011-11%2011-11-4.929-11-11%204.929-11%2011-11zm0%2012.25c2.781%200%205.181%201.458%206.51%203.635l-.868.54c-1.152-1.857-3.228-3.075-5.642-3.075-2.414%200-4.49%201.218-5.642%203.075l-.868-.54c1.329-2.177%203.729-3.635%206.51-3.635zm-3.53-5.75c.552%200%201%20.448%201%201s-.448%201-1%201-1-.448-1-1%20.448-1%201-1zm7.06%200c.552%200%201%20.448%201%201s-.448%201-1%201-1-.448-1-1%20.448-1%201-1zm-3.53%206.75l1.414%201.414-1.414%201.414-1.414-1.414%201.414-1.414z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       166,
                Name:           "EmojiNeutral",
                Icon:           Icon.EmojiNeutral,
                Description:    "An icon representing a neutral face emoji, typically shown as a circular face with straight line for a mouth and neutral eyes",
                Tags:           ["indifferent", "expressionless", "poker face", "impartial"],
                Category:       "Emoji",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12%200c6.623%200%2012%205.377%2012%2012s-5.377%2012-12%2012-12-5.377-12-12%205.377-12%2012-12zm0%201c6.071%200%2011%204.929%2011%2011s-4.929%2011-11%2011-11-4.929-11-11%204.929-11%2011-11zm-3.5%207.5c.828%200%201.5.672%201.5%201.5s-.672%201.5-1.5%201.5-1.5-.672-1.5-1.5.672-1.5%201.5-1.5zm7%200c.828%200%201.5.672%201.5%201.5s-.672%201.5-1.5%201.5-1.5-.672-1.5-1.5.672-1.5%201.5-1.5zm-7.5%207h8v1h-8v-1z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       167,
                Name:           "EmojiHappy",
                Icon:           Icon.EmojiHappy,
                Description:    "An icon representing a happy face emoji, typically shown as a circular face with wide smile and upturned eyes",
                Tags:           ["joyful", "ecstatic", "grinning", "elated"],
                Category:       "Emoji",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12%200c6.623%200%2012%205.377%2012%2012s-5.377%2012-12%2012-12-5.377-12-12%205.377-12%2012-12zm0%201c6.071%200%2011%204.929%2011%2011s-4.929%2011-11%2011-11-4.929-11-11%204.929-11%2011-11zm0%2012.25c2.781%200%205.181%201.458%206.51%203.635l-.868.54c-1.152-1.857-3.228-3.075-5.642-3.075-2.414%200-4.49%201.218-5.642%203.075l-.868-.54c1.329-2.177%203.729-3.635%206.51-3.635zm-3.53-5.75c.552%200%201%20.448%201%201s-.448%201-1%201-1-.448-1-1%20.448-1%201-1zm7.06%200c.552%200%201%20.448%201%201s-.448%201-1%201-1-.448-1-1%20.448-1%201-1z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       168,
                Name:           "Warning",
                Icon:           Icon.Warning,
                Description:    "An icon representing a warning or caution, typically shown as a triangle with an exclamation mark inside",
                Tags:           ["alert", "caution", "danger", "attention"],
                Category:       "Interface",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12%205.177l8.631%2015.823h-17.262l8.631-15.823zm0-4.177l-12%2022h24l-12-22zm-1%2014h2v2h-2v-2zm0-6h2v4h-2v-4z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       169,
                Name:           "Information",
                Icon:           Icon.Information,
                Description:    "An icon representing information or details, typically shown as a lowercase 'i' in a circle",
                Tags:           ["info", "details", "help", "about"],
                Category:       "Interface",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12%200c6.623%200%2012%205.377%2012%2012s-5.377%2012-12%2012-12-5.377-12-12%205.377-12%2012-12zm0%201c6.071%200%2011%204.929%2011%2011s-4.929%2011-11%2011-11-4.929-11-11%204.929-11%2011-11zm.5%2017h-1v-9h1v9zm-.5-12c.466%200%20.845.378.845.845%200%20.466-.379.844-.845.844-.466%200-.845-.378-.845-.844%200-.467.379-.845.845-.845z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       170,
                Name:           "Database",
                Icon:           Icon.Database,
                Description:    "An icon representing a database or data storage, typically shown as a cylindrical shape or stacked disks",
                Tags:           ["storage", "data", "server", "repository"],
                Category:       "Technology",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12%200c-6.627%200-12%201.791-12%204v4c0%202.209%205.373%204%2012%204s12-1.791%2012-4v-4c0-2.209-5.373-4-12-4zm-1%202.062c3.299%200%205.973.55%205.973%201.225%200%20.675-2.674%201.225-5.973%201.225-3.299%200-5.973-.55-5.973-1.225%200-.675%202.674-1.225%205.973-1.225zm1%2015.938c-6.627%200-12-1.791-12-4v4c0%202.209%205.373%204%2012%204s12-1.791%2012-4v-4c0%202.209-5.373%204-12%204zm0-5c-6.627%200-12-1.791-12-4v4c0%202.209%205.373%204%2012%204s12-1.791%2012-4v-4c0%202.209-5.373%204-12%204z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       171,
                Name:           "Weather",
                Icon:           Icon.Weather,
                Description:    "An icon representing weather conditions, typically shown as a sun, cloud, or combination of weather symbols",
                Tags:           ["forecast", "climate", "meteorology", "temperature"],
                Category:       "Nature",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12%200c6.623%200%2012%205.377%2012%2012s-5.377%2012-12%2012-12-5.377-12-12%205.377-12%2012-12zm0%202c5.519%200%2010%204.481%2010%2010s-4.481%2010-10%2010-10-4.481-10-10%204.481-10%2010-10zm0%202c-4.418%200-8%203.582-8%208s3.582%208%208%208%208-3.582%208-8-3.582-8-8-8zm0%202c3.314%200%206%202.686%206%206s-2.686%206-6%206-6-2.686-6-6%202.686-6%206-6zm0%202c-2.21%200-4%201.79-4%204s1.79%204%204%204%204-1.79%204-4-1.79-4-4-4z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       172,
                Name:           "TrendingHashtag",
                Icon:           Icon.TrendingHashtag,
                Description:    "An icon representing a trending hashtag, typically shown as a hashtag symbol (#) with an upward arrow or graph",
                Tags:           ["popular", "viral", "social media", "trend"],
                Category:       "Social Media",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M22%207h-7v-2h7v2zm1.726%2010c-1.06%202.67-3.341%205-6.51%206h-7.433c-3.169-1-5.45-3.33-6.51-6h20.453zm-18.726-3c1.23-2.019%203.285-3.814%206.704-4.814l1.296-.186v-6h2v12h-10zm16.226-7c1.23%202.019%201.774%204.481%201.774%207%200%20.686-.051%201.36-.147%202h-19.706c-.097-.64-.147-1.314-.147-2%200-2.519.544-4.981%201.774-7h16.452z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       173,
                Name:           "TrendingUpwards",
                Icon:           Icon.TrendingUpwards,
                Description:    "An icon representing an upward trend, typically shown as a line graph or arrow pointing upwards",
                Tags:           ["increase", "growth", "rising", "improvement"],
                Category:       "Business",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M23%206.373l-9.357%209.357-3.637-3.637-9.006%209.006-.894-.894%209.9-9.9%203.637%203.637%208.463-8.463.894.894z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       174,
                Name:           "Items",
                Icon:           Icon.Items,
                Description:    "An icon representing multiple items or a list, typically shown as stacked rectangles or a bulleted list",
                Tags:           ["list", "inventory", "collection", "elements"],
                Category:       "Interface",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M24%203h-16v2h16v-2zm0%204h-16v2h16v-2zm0%204h-16v2h16v-2zm0%204h-16v2h16v-2zm0%204h-16v2h16v-2zm-20-16h2v2h-2v-2zm0%204h2v2h-2v-2zm0%204h2v2h-2v-2zm0%204h2v2h-2v-2zm0%204h2v2h-2v-2z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       175,
                Name:           "LevelsLayersItems",
                Icon:           Icon.LevelsLayersItems,
                Description:    "An icon representing multiple levels, layers, or stacked items, typically shown as overlapping shapes or stacked planes",
                Tags:           ["layers", "stack", "hierarchy", "organization"],
                Category:       "Interface",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M11.954%2011c3.33%200%207.057%206.123%207.632%208.716.575%202.594-2.327%204.113-4.042%204.284-1.714.172-3.403-1.268-3.59-3.005-.187-1.738%201.595-3.06%203.238-3.625%201.642-.565%203.438.12%203.799%201.88-.361-1.76-2.157-2.445-3.799-1.88-1.643.565-3.425%201.887-3.238%203.625.187%201.737%201.876%203.177%203.59%203.005%201.715-.171%204.617-1.69%204.042-4.284-.575-2.593-4.302-8.716-7.632-8.716z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       176,
                Name:           "Trending",
                Icon:           Icon.Trending,
                Description:    "An icon representing trending or popular topics, typically shown as a graph with an upward trend or a flame symbol",
                Tags:           ["popular", "viral", "hot topic", "trending now"],
                Category:       "Social Media",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M16.001%2024h-12c-2.209%200-4-1.791-4-4v-12c0-2.209%201.791-4%204-4h12c2.209%200%204%201.791%204%204v12c0%202.209-1.791%204-4%204zm0-2c1.103%200%202-.897%202-2v-12c0-1.103-.897-2-2-2h-12c-1.103%200-2%20.897-2%202v12c0%201.103.897%202%202%202h12zm-5-6.411l-3.294-3.294-4.706%204.706v-9.705h16v6.706l-5%205-3-3zm-1.705-10.589c-1.933%200-3.5%201.567-3.5%203.5s1.567%203.5%203.5%203.5%203.5-1.567%203.5-3.5-1.567-3.5-3.5-3.5zm0%205c-.828%200-1.5-.672-1.5-1.5s.672-1.5%201.5-1.5%201.5.672%201.5%201.5-.672%201.5-1.5%201.5z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       177,
                Name:           "LineWeight",
                Icon:           Icon.LineWeight,
                Description:    "An icon representing line weight or thickness, typically shown as multiple horizontal lines of varying thicknesses",
                Tags:           ["thickness", "stroke", "width", "border"],
                Category:       "Design",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M24%2020h-24v-1h24v1zm0-3h-24v-1h24v1zm0-4h-24v-2h24v2zm0-5h-24v-3h24v3z%22%2F%3E%3C%2Fsvg%3E"
            }, 
            {
                Sequence:       178,
                Name:           "Printing3D",
                Icon:           Icon.Printing3D,
                Description:    "An icon representing 3D printing, typically shown as a simplified 3D printer or a cube being constructed layer by layer",
                Tags:           ["additive manufacturing", "rapid prototyping", "3D modeling", "fabrication"],
                Category:       "Technology",
                SVG:            "data:image/svg+xml, %3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M24%2021h-3l1-1.447v-5.553h-1v-2h-1v2h-3v-2h-1v2h-1v5.553l1%201.447h-3v-8l-2.243-2.243-1.757%201.757v-.514h-4v4h.514l-1.757%201.757%202.243%202.243h8v3h-24v-24h24v21zm-10-1h-3v-1h3v1zm-5-15h-3v-3h3v3zm13-3h-8v8h8v-8z%22%2F%3E%3C%2Fsvg%3E"
            }
        ], 
        Sequence, 
        SortOrder.Ascending
    );
```

## Final Considerations

I hope you have found this helpful. If you need any help with the Power Platform, don't hesitate to email us at [support@superpowerlabs.co](support@superpowerlabs.co).
