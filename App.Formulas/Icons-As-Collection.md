# Icons

This code works great, doesn't it?

```text
IconControl1.Icon = Icon.Home 
```

Icon is an **enumeration**, just like Color, Font, and Alignment. You type these enumeration names, then use a "." to see all the possible values. Very nice. However, it can be a bit tedious to remember all the icons and their names. 

That's why I've created a collection of all the icons in canvas Power Apps. This way, you can easily list, filter, sort, lookup and search for an icon by name or description, and use the "Icon" property in the collection just like you would do with the enumeration. Look at all the other fields contained in the colletion: 

1. **Sequence**: A number that indicates the order of the icon in the collection. This can be useful for sorting or filtering the icons.
2. **Name**: The name of the icon, which is the same as the name you would use in the enumeration. For example, "Home" is the name of the home icon.
3. **Icon**: The actual icon, which you can use in your app. For example, Icon.Home is the home icon.
4. **Description**: A brief description of the icon, which can be useful for understanding its purpose and usage.
5. **Tags**: A list of keywords or tags associated with the icon, which can be used for searching or filtering the icons based on their functionality or appearance.
6. **Category**: The category of the icon, which can be used for grouping or organizing the icons based on their purpose or usage. For example, "Actions" is a category that includes icons such as "Add", "Cancel", "Edit", "Check", "Search", "Filter", "Sort", "Reload", "Trash", "Save", "Download", "Copy", "LikeDislike", "Crop", and "Pin".

## Add This to Your Application

All the icons in canvas Power Apps are contained in an enumeration so you can easily referenced. Let's take this one step further and put them all into a collection so we can work with them much more easier. Just paste the code below in your App.Formulas.

```JavaScript
    fxIcons = Sort(
        [
            {
                Sequence:       1,
                Name:           "Add",
                Icon:           Icon.Add,
                Description:    "A plus sign icon indicating addition or creation of new items",
                Tags:           ["plus", "new", "create"],
                Category:       "Actions"
            }, 
            {
                Sequence:       2,
                Name:           "Cancel",
                Icon:           Icon.Cancel,
                Description:    "An 'X' icon typically used to cancel actions or close dialogs",
                Tags:           ["close", "delete", "remove"],
                Category:       "Actions"
            },
            {
                Sequence:       3,
                Name:           "CancelBadge",
                Icon:           Icon.CancelBadge,
                Description:    "An 'X' icon within a circular badge, often used to indicate cancellation or removal in a more prominent way",
                Tags:           ["close", "delete", "remove", "badge"],
                Category:       "Notifications"
            }, 
            {
                Sequence:       4,
                Name:           "Edit",
                Icon:           Icon.Edit,
                Description:    "A pencil icon typically used to represent editing or modifying content",
                Tags:           ["modify", "change", "update", "pencil"],
                Category:       "Actions"
            },
            {
                Sequence:       5,
                Name:           "Check",
                Icon:           Icon.Check,
                Description:    "A checkmark icon often used to indicate completion, confirmation, or selection",
                Tags:           ["complete", "confirm", "select", "approve"],
                Category:       "Actions"
            }, 
            {
                Sequence:       6,
                Name:           "CheckBadge",
                Icon:           Icon.CheckBadge,
                Description:    "A checkmark icon within a circular badge, typically used to indicate successful completion or approval in a more prominent way",
                Tags:           ["complete", "confirm", "approve", "badge", "success"],
                Category:       "Notifications"
            }, 
            {
                Sequence:       7,
                Name:           "Search",
                Icon:           Icon.Search,
                Description:    "A magnifying glass icon typically used for search functionality or to indicate a search action",
                Tags:           ["find", "lookup", "explore", "magnifying glass"],
                Category:       "Actions"
            }, 
            {
                Sequence:       8,
                Name:           "Filter",
                Icon:           Icon.Filter,
                Description:    "A funnel-like icon typically used to represent filtering or sorting options",
                Tags:           ["sort", "funnel", "refine", "narrow"],
                Category:       "Data"
            },
            {
                Sequence:       9,
                Name:           "FilterFlat",
                Icon:           Icon.FilterFlat,
                Description:    "A simplified filter icon, typically used to represent filtering or sorting options in a flat design style",
                Tags:           ["sort", "funnel", "refine", "narrow", "flat"],
                Category:       "Data"
            }, 
            {
                Sequence:       10,
                Name:           "FilterFlatFilled",
                Icon:           Icon.FilterFlatFilled,
                Description:    "A filled version of the simplified filter icon, representing filtering or sorting options in a flat, solid design style",
                Tags:           ["sort", "funnel", "refine", "narrow", "flat", "filled"],
                Category:       "Data"
            },
            {
                Sequence:       11,
                Name:           "Sort",
                Icon:           Icon.Sort,
                Description:    "An icon representing sorting functionality, typically shown as stacked horizontal lines of decreasing length",
                Tags:           ["order", "arrange", "organize", "sequence"],
                Category:       "Data"
            }, 
            {
                Sequence:       12,
                Name:           "Reload",
                Icon:           Icon.Reload,
                Description:    "A circular arrow icon typically used to represent reloading, refreshing, or syncing content",
                Tags:           ["refresh", "update", "sync", "circular"],
                Category:       "Actions"
            }, 
            {
                Sequence:       13,
                Name:           "Trash",
                Icon:           Icon.Trash,
                Description:    "A trash can icon typically used to represent deletion or removal of items",
                Tags:           ["delete", "remove", "discard", "bin"],
                Category:       "Actions"
            }, 
            {
                Sequence:       14,
                Name:           "Save",
                Icon:           Icon.Save,
                Description:    "A floppy disk icon typically used to represent saving or storing data",
                Tags:           ["store", "preserve", "record", "floppy"],
                Category:       "Actions"
            }, 
            {
                Sequence:       15,
                Name:           "Download",
                Icon:           Icon.Download,
                Description:    "An arrow pointing downward into a tray, typically used to represent downloading or saving files",
                Tags:           ["save", "retrieve", "get", "arrow"],
                Category:       "Actions"
            }, 
            {
                Sequence:       16,
                Name:           "Copy",
                Icon:           Icon.Copy,
                Description:    "Two overlapping rectangles, typically used to represent copying or duplicating content",
                Tags:           ["duplicate", "clone", "replicate", "paste"],
                Category:       "Actions"
            }, 
            {
                Sequence:       17,
                Name:           "LikeDislike",
                Icon:           Icon.LikeDislike,
                Description:    "A combination of thumbs up and thumbs down icons, typically used for rating or feedback",
                Tags:           ["feedback", "rating", "thumbs", "vote"],
                Category:       "Social"
            }, 
            {
                Sequence:       18,
                Name:           "Crop",
                Icon:           Icon.Crop,
                Description:    "An icon representing the crop tool, typically used in image editing to trim or resize images",
                Tags:           ["trim", "resize", "edit", "image"],
                Category:       "Design"
            }, 
            {
                Sequence:       19,
                Name:           "Pin",
                Icon:           Icon.Pin,
                Description:    "An icon representing a pushpin, typically used to indicate location or to 'pin' items for quick access",
                Tags:           ["location", "mark", "save", "bookmark"],
                Category:       "Navigation"
            }, 
            {
                Sequence:       20,
                Name:           "ClearDrawing",
                Icon:           Icon.ClearDrawing,
                Description:    "An icon representing clearing or erasing a drawing, typically shown as an eraser or clear canvas",
                Tags:           ["erase", "clear", "delete", "reset"],
                Category:       "Design"
            }, 
            {
                Sequence:       21,
                Name:           "ExpandView",
                Icon:           Icon.ExpandView,
                Description:    "An icon representing expanding or enlarging a view, typically shown as outward-pointing arrows",
                Tags:           ["enlarge", "maximize", "fullscreen", "zoom"],
                Category:       "View"
            }, 
            {
                Sequence:       22,
                Name:           "CollapseAll",
                Icon:           Icon.CollapseView,
                Description:    "An icon representing the action to collapse all expanded items or sections, typically shown as inward-pointing arrows",
                Tags:           ["collapse", "minimize", "shrink", "fold"],
                Category:       "View"
            }, 
            {
                Sequence:       23,
                Name:           "Draw",
                Icon:           Icon.Draw,
                Description:    "An icon representing a drawing tool, typically shown as a pencil or brush for creating or editing graphics",
                Tags:           ["pencil", "sketch", "create", "design"],
                Category:       "Design"
            }, 
            {
                Sequence:       24,
                Name:           "Compose",
                Icon:           Icon.Compose,
                Description:    "An icon representing the action of composing or writing, typically shown as a pen or pencil with paper",
                Tags:           ["write", "create", "edit", "document"],
                Category:       "Communication"
            }, 
            {
                Sequence:       25,
                Name:           "Erase",
                Icon:           Icon.Erase,
                Description:    "An icon representing an eraser tool, typically used for removing or deleting content in drawing or editing applications",
                Tags:           ["delete", "remove", "clear", "clean"],
                Category:       "Design"
            }, 
            {
                Sequence:       26,
                Name:           "Message",
                Icon:           Icon.Message,
                Description:    "An icon representing a message or chat bubble, typically used for communication or messaging features",
                Tags:           ["chat", "communication", "text", "speech"],
                Category:       "Communication"
            }, 
            {
                Sequence:       27,
                Name:           "Post",
                Icon:           Icon.Post,
                Description:    "An icon representing a post or publication, typically shown as a document or note being sent or published",
                Tags:           ["publish", "send", "share", "submit"],
                Category:       "Communication"
            }, 
            {
                Sequence:       28,
                Name:           "AddDocument",
                Icon:           Icon.AddDocument,
                Description:    "An icon representing the action of adding a new document, typically shown as a document with a plus sign",
                Tags:           ["new", "create", "file", "add"],
                Category:       "Files"
            }, 
            {
                Sequence:       29,
                Name:           "AddLibrary",
                Icon:           Icon.AddLibrary,
                Description:    "An icon representing the action of adding a new library or collection, typically shown as multiple documents or books with a plus sign",
                Tags:           ["collection", "books", "add", "create"],
                Category:       "Files"
            }, 
            {
                Sequence:       30,
                Name:           "Import",
                Icon:           Icon.Import,
                Description:    "An icon representing the action of importing data or files, typically shown as an arrow pointing into a box or document",
                Tags:           ["upload", "transfer", "input", "inbound"],
                Category:       "Data"
            }, 
            {
                Sequence:       31,
                Name:           "Export",
                Icon:           Icon.Export,
                Description:    "An icon representing the action of exporting data or files, typically shown as an arrow pointing out of a box or document",
                Tags:           ["download", "transfer", "output", "outbound"],
                Category:       "Data"
            }, 
            {
                Sequence:       32,
                Name:           "QuestionMark",
                Icon:           Icon.QuestionMark,
                Description:    "An icon representing a question or help, typically shown as a question mark symbol",
                Tags:           ["help", "inquiry", "support", "information"],
                Category:       "Information"
            }, 
            {
                Sequence:       33,
                Name:           "Help",
                Icon:           Icon.Help,
                Description:    "An icon representing assistance or support, typically shown as a question mark or a lifebuoy",
                Tags:           ["support", "assistance", "guidance", "information"],
                Category:       "Information"
            }, 
            {
                Sequence:       34,
                Name:           "ThumbsDown",
                Icon:           Icon.ThumbsDown,
                Description:    "An icon representing disapproval or dislike, typically shown as a hand with the thumb pointing downward",
                Tags:           ["dislike", "negative", "feedback", "rating"],
                Category:       "Social"
            }, 
            {
                Sequence:       35,
                Name:           "ThumbsDownFilled",
                Icon:           Icon.ThumbsDownFilled,
                Description:    "A filled icon representing strong disapproval or dislike, typically shown as a solid hand with the thumb pointing downward",
                Tags:           ["dislike", "negative", "feedback", "rating", "filled"],
                Category:       "Social"
            }, 
            {
                Sequence:       36,
                Name:           "ThumbsUpFilled",
                Icon:           Icon.ThumbsUpFilled,
                Description:    "A filled icon representing strong approval or like, typically shown as a solid hand with the thumb pointing upward",
                Tags:           ["like", "positive", "feedback", "rating", "filled"],
                Category:       "Social"
            }, 
            {
                Sequence:       37,
                Name:           "Undo",
                Icon:           Icon.Undo,
                Description:    "An icon representing the action of undoing or reverting a previous action, typically shown as a curved arrow pointing left or counterclockwise",
                Tags:           ["revert", "reverse", "back", "previous"],
                Category:       "Actions"
            }, 
            {
                Sequence:       38,
                Name:           "Redo",
                Icon:           Icon.Redo,
                Description:    "An icon representing the action of redoing or reapplying a previously undone action, typically shown as a curved arrow pointing right or clockwise",
                Tags:           ["reapply", "forward", "repeat", "next"],
                Category:       "Actions"
            }, 
            {
                Sequence:       39,
                Name:           "ZoomIn",
                Icon:           Icon.ZoomIn,
                Description:    "An icon representing the action of zooming in or enlarging a view, typically shown as a magnifying glass with a plus sign",
                Tags:           ["magnify", "enlarge", "increase", "expand"],
                Category:       "View"
            }, 
            {
                Sequence:       40,
                Name:           "ZoomOut",
                Icon:           Icon.ZoomOut,
                Description:    "An icon representing the action of zooming out or reducing a view, typically shown as a magnifying glass with a minus sign",
                Tags:           ["reduce", "decrease", "shrink", "minimize"],
                Category:       "View"
            }, 
            {
                Sequence:       41,
                Name:           "OpenInNewWindow",
                Icon:           Icon.OpenInNewWindow,
                Description:    "An icon representing the action of opening a link or content in a new window or tab, typically shown as a square with an arrow pointing outward",
                Tags:           ["external", "link", "new tab", "launch"],
                Category:       "Navigation"
            }, 
            {
                Sequence:       42,
                Name:           "Share",
                Icon:           Icon.Share,
                Description:    "An icon representing the action of sharing content or information, typically shown as interconnected nodes or an arrow pointing outward from a circle",
                Tags:           ["distribute", "send", "social", "connect"],
                Category:       "Communication"
            }, 
            {
                Sequence:       43,
                Name:           "Publish",
                Icon:           Icon.Publish,
                Description:    "An icon representing the action of publishing or making content publicly available, typically shown as an upward arrow or a document with an upward arrow",
                Tags:           ["release", "upload", "distribute", "make public"],
                Category:       "Content"
            }, 
            {
                Sequence:       44,
                Name:           "Link",
                Icon:           Icon.Link,
                Description:    "An icon representing a hyperlink or connection between elements, typically shown as a chain link or interlocking rings",
                Tags:           ["hyperlink", "url", "connect", "attach"],
                Category:       "Web"
            }, 
            {
                Sequence:       45,
                Name:           "Sync",
                Icon:           Icon.Sync,
                Description:    "An icon representing synchronization or data refresh, typically shown as two circular arrows forming a loop",
                Tags:           ["refresh", "update", "reload", "synchronize"],
                Category:       "Data"
            },
            {
                Sequence:       46,
                Name:           "View",
                Icon:           Icon.View,
                Description:    "An icon representing the action of viewing or previewing content, typically shown as an eye",
                Tags:           ["preview", "see", "visibility", "show"],
                Category:       "Actions"
            }, 
            {
                Sequence:       47,
                Name:           "Hide",
                Icon:           Icon.Hide,
                Description:    "An icon representing the action of hiding or concealing content, typically shown as an eye with a slash through it",
                Tags:           ["invisible", "conceal", "hidden", "private"],
                Category:       "Actions"
            }, 
            {
                Sequence:       48,
                Name:           "Bookmark",
                Icon:           Icon.Bookmark,
                Description:    "An icon representing a bookmark or saved item, typically shown as a ribbon or tag",
                Tags:           ["save", "favorite", "mark", "flag"],
                Category:       "Actions"
            }, 
            {
                Sequence:       49,
                Name:           "BookmarkFilled",
                Icon:           Icon.BookmarkFilled,
                Description:    "A filled icon representing a bookmark or saved item, typically shown as a solid ribbon or tag",
                Tags:           ["save", "favorite", "mark", "flag", "filled"],
                Category:       "Actions"
            }, 
            {
                Sequence:       50,
                Name:           "Reset",
                Icon:           Icon.Reset,
                Description:    "An icon representing the action of resetting or returning to an initial state, typically shown as a circular arrow",
                Tags:           ["restart", "refresh", "revert", "circular arrow"],
                Category:       "Actions"
            }, 
            {
                Sequence:       51,
                Name:           "Blocked",
                Icon:           Icon.Blocked,
                Description:    "An icon representing a blocked or prohibited state, typically shown as a circle with a diagonal line through it",
                Tags:           ["prohibited", "forbidden", "stop", "no"],
                Category:       "Status"
            }, 
            {
                Sequence:       52,
                Name:           "DockLeft",
                Icon:           Icon.DockLeft,
                Description:    "An icon representing docking or aligning content to the left side, typically shown as a rectangle with a smaller rectangle aligned to its left edge",
                Tags:           ["align", "left", "layout", "position"],
                Category:       "Layout"
            }, 
            {
                Sequence:       53,
                Name:           "AddUser",
                Icon:           Icon.AddUser,
                Description:    "An icon representing the action of adding a new user, typically shown as a user silhouette with a plus sign",
                Tags:           ["new user", "create account", "sign up", "register"],
                Category:       "Users"
            },
            {
                Sequence:       54,
                Name:           "Cut",
                Icon:           Icon.Cut,
                Description:    "An icon representing a cutting action, typically shown as a pair of scissors",
                Tags:           ["scissors", "trim", "clip", "snip"],
                Category:       "Actions"
            }, 
            {
                Sequence:       55,
                Name:           "Paste",
                Icon:           Icon.Paste,
                Description:    "An icon representing the action of pasting content, typically shown as a clipboard or document with a downward arrow",
                Tags:           ["insert", "paste", "clipboard", "add"],
                Category:       "Actions"
            }, 
            {
                Sequence:       56,
                Name:           "Leave",
                Icon:           Icon.Leave,
                Description:    "An icon representing the action of leaving or exiting, typically shown as a door with an arrow pointing outward",
                Tags:           ["exit", "logout", "depart", "sign out"],
                Category:       "Actions"
            }, 
            {
                Sequence:       57,
                Name:           "Home",
                Icon:           Icon.Home,
                Description:    "An icon representing a home or main page, typically shown as a simple house shape",
                Tags:           ["house", "main", "start", "homepage"],
                Category:       "Navigation"
            }, 
            {
                Sequence:       58,
                Name:           "Hamburger",
                Icon:           Icon.Hamburger,
                Description:    "An icon representing a menu, typically shown as three horizontal lines stacked vertically",
                Tags:           ["menu", "navigation", "options", "sidebar"],
                Category:       "Navigation"
            }, 
            {
                Sequence:       59,
                Name:           "Settings",
                Icon:           Icon.Settings,
                Description:    "An icon representing settings or configuration options, typically shown as a gear or cog wheel",
                Tags:           ["configuration", "options", "preferences", "gear"],
                Category:       "System"
            }, 
            {
                Sequence:       60,
                Name:           "More",
                Icon:           Icon.More,
                Description:    "An icon representing additional options or actions, typically shown as three dots (ellipsis) either horizontally or vertically aligned",
                Tags:           ["ellipsis", "options", "additional", "menu"],
                Category:       "Navigation"
            }, 
            {
                Sequence:       61,
                Name:           "Waffle",
                Icon:           Icon.Waffle,
                Description:    "An icon representing a menu of multiple options, typically shown as a 3x3 grid of small squares",
                Tags:           ["menu", "grid", "options", "navigation"],
                Category:       "Navigation"
            }, 
            {
                Sequence:       62,
                Name:           "ChevronLeft",
                Icon:           Icon.ChevronLeft,
                Description:    "An icon representing a left-pointing chevron, typically used for navigation or to indicate a collapsible menu",
                Tags:           ["left", "arrow", "back", "previous"],
                Category:       "Navigation"
            }, 
            {
                Sequence:       63,
                Name:           "ChevronRight",
                Icon:           Icon.ChevronRight,
                Description:    "An icon representing a right-pointing chevron, typically used for navigation or to indicate an expandable menu",
                Tags:           ["right", "arrow", "next", "forward"],
                Category:       "Navigation"
            }, 
            {
                Sequence:       64,
                Name:           "ChevronUp",
                Icon:           Icon.ChevronUp,
                Description:    "An icon representing an upward-pointing chevron, typically used for navigation or to indicate an expandable menu",
                Tags:           ["up", "arrow", "expand", "collapse"],
                Category:       "Navigation"
            },
            {
                Sequence:       65,
                Name:           "ChevronDown",
                Icon:           Icon.ChevronDown,
                Description:    "An icon representing a downward-pointing chevron, typically used for navigation or to indicate a collapsible menu",
                Tags:           ["down", "arrow", "expand", "collapse"],
                Category:       "Navigation"
            }, 
            {
                Sequence:       66,
                Name:           "NextArrow",
                Icon:           Icon.NextArrow,
                Description:    "An icon representing a forward or next action, typically shown as an arrow pointing to the right",
                Tags:           ["forward", "next", "advance", "right"],
                Category:       "Navigation"
            }, 
            {
                Sequence:       67,
                Name:           "BackArrow",
                Icon:           Icon.BackArrow,
                Description:    "An icon representing a backward or previous action, typically shown as an arrow pointing to the left",
                Tags:           ["back", "previous", "return", "left"],
                Category:       "Navigation"
            }, 
            {
                Sequence:       68,
                Name:           "ArrowDown",
                Icon:           Icon.ArrowDown,
                Description:    "An icon representing a downward direction or action, typically shown as an arrow pointing downward",
                Tags:           ["down", "descend", "dropdown", "expand"],
                Category:       "Navigation"
            }, 
            {
                Sequence:       69,
                Name:           "ArrowUp",
                Icon:           Icon.ArrowUp,
                Description:    "An icon representing an upward direction or action, typically shown as an arrow pointing upward",
                Tags:           ["up", "ascend", "upward", "rise"],
                Category:       "Navigation"
            }, 
            {
                Sequence:       70,
                Name:           "ArrowLeft",
                Icon:           Icon.ArrowLeft,
                Description:    "An icon representing a leftward direction or action, typically shown as an arrow pointing to the left",
                Tags:           ["left", "back", "previous", "backward"],
                Category:       "Navigation"
            }, 
            {
                Sequence:       71,
                Name:           "ArrowRight",
                Icon:           Icon.ArrowRight,
                Description:    "An icon representing a rightward direction or action, typically shown as an arrow pointing to the right",
                Tags:           ["right", "forward", "next", "advance"],
                Category:       "Navigation"
            }, 
            {
                Sequence:       72,
                Name:           "Camera",
                Icon:           Icon.Camera,
                Description:    "An icon representing a camera or photo-taking action, typically shown as a simplified camera shape",
                Tags:           ["photo", "picture", "capture", "image"],
                Category:       "Media"
            }, 
            {
                Sequence:       73,
                Name:           "Document",
                Icon:           Icon.Document,
                Description:    "An icon representing a document or file, typically shown as a rectangular shape with a folded corner",
                Tags:           ["file", "paper", "page", "document"],
                Category:       "Files"
            }, 
            {
                Sequence:       74,
                Name:           "DockCheckProperties",
                Icon:           Icon.DockCheckProperties,
                Description:    "An icon representing a document with a checkmark, typically used to indicate verified or approved document properties",
                Tags:           ["document", "checkmark", "verify", "approve", "properties"],
                Category:       "Files"
            }, 
            {
                Sequence:       75,
                Name:           "Folder",
                Icon:           Icon.Folder,
                Description:    "An icon representing a folder or directory, typically shown as a simplified folder shape",
                Tags:           ["directory", "file system", "storage", "organize"],
                Category:       "Files"
            }, 
            {
                Sequence:       76,
                Name:           "Journal",
                Icon:           Icon.Journal,
                Description:    "An icon representing a journal or log, typically shown as a book or notebook",
                Tags:           ["log", "notebook", "diary", "record"],
                Category:       "Files"
            }, 
            {
                Sequence:       77,
                Name:           "ForkKnife",
                Icon:           Icon.ForkKnife,
                Description:    "An icon representing food or dining, typically shown as a fork and knife crossed or side by side",
                Tags:           ["food", "dining", "restaurant", "meal"],
                Category:       "Miscellaneous"
            }, 
            {
                Sequence:       78,
                Name:           "Transportation",
                Icon:           Icon.Transportation,
                Description:    "An icon representing transportation or travel, typically shown as a vehicle or mode of transport",
                Tags:           ["travel", "vehicle", "transport", "journey"],
                Category:       "Travel"
            }, 
            {
                Sequence:       79,
                Name:           "Airplane",
                Icon:           Icon.Airplane,
                Description:    "An icon representing an airplane or air travel, typically shown as a simplified side view of an aircraft",
                Tags:           ["flight", "travel", "aviation", "transport"],
                Category:       "Travel"
            }, 
            {
                Sequence:       80,
                Name:           "Bus",
                Icon:           Icon.Bus,
                Description:    "An icon representing a bus or public transportation, typically shown as a simplified side view of a bus",
                Tags:           ["public transport", "travel", "vehicle", "commute"],
                Category:       "Travel"
            }, 
            {
                Sequence:       81,
                Name:           "Cars",
                Icon:           Icon.Cars,
                Description:    "An icon representing multiple cars or vehicles, typically shown as simplified car silhouettes",
                Tags:           ["vehicles", "automobiles", "transport", "traffic"],
                Category:       "Transportation"
            }, 
            {
                Sequence:       82,
                Name:           "Money",
                Icon:           Icon.Money,
                Description:    "An icon representing money or currency, typically shown as banknotes or coins",
                Tags:           ["currency", "cash", "finance", "payment"],
                Category:       "Finance"
            }, 
            {
                Sequence:       83,
                Name:           "Currency",
                Icon:           Icon.Currency,
                Description:    "An icon representing currency or exchange, typically shown as a dollar sign or multiple currency symbols",
                Tags:           ["money", "exchange", "finance", "forex"],
                Category:       "Finance"
            }, 
            {
                Sequence:       84,
                Name:           "AddToCalendar",
                Icon:           Icon.AddToCalendar,
                Description:    "An icon representing the action of adding an event to a calendar, typically shown as a calendar with a plus sign",
                Tags:           ["event", "schedule", "appointment", "date"],
                Category:       "Calendar"
            }, 
            {
                Sequence:       85,
                Name:           "CalendarBlank",
                Icon:           Icon.CalendarBlank,
                Description:    "An icon representing a blank calendar or date selection, typically shown as an empty calendar grid",
                Tags:           ["date", "schedule", "month", "empty"],
                Category:       "Calendar"
            }, 
            {
                Sequence:       86,
                Name:           "OfficeBuilding",
                Icon:           Icon.OfficeBuilding,
                Description:    "An icon representing an office building or corporate structure, typically shown as a multi-story building",
                Tags:           ["building", "corporate", "company", "workplace"],
                Category:       "Business"
            }, 
            {
                Sequence:       87,
                Name:           "PaperClip",
                Icon:           Icon.PaperClip,
                Description:    "An icon representing an attachment or linked file, typically shown as a paper clip",
                Tags:           ["attachment", "file", "link", "document"],
                Category:       "Files"
            }, 
            {
                Sequence:       88,
                Name:           "Newspaper",
                Icon:           Icon.Newspaper,
                Description:    "An icon representing a newspaper or news article, typically shown as a folded newspaper",
                Tags:           ["news", "article", "press", "media"],
                Category:       "Media"
            }, 
            {
                Sequence:       89,
                Name:           "Lock",
                Icon:           Icon.Lock,
                Description:    "An icon representing security or a locked state, typically shown as a padlock",
                Tags:           ["security", "locked", "private", "protected"],
                Category:       "Security"
            }, 
            {
                Sequence:       90,
                Name:           "Waypoint",
                Icon:           Icon.Waypoint,
                Description:    "An icon representing a location or destination point, typically shown as a map pin or marker",
                Tags:           ["location", "pin", "marker", "destination"],
                Category:       "Maps"
            }, 
            {
                Sequence:       91,
                Name:           "Location",
                Icon:           Icon.Location,
                Description:    "An icon representing a geographical location or position, typically shown as a crosshair or target",
                Tags:           ["position", "coordinates", "gps", "pinpoint"],
                Category:       "Maps"
            }, 
            {
                Sequence:       92,
                Name:           "DocumentPDF",
                Icon:           Icon.DocumentPDF,
                Description:    "An icon representing a PDF document, typically shown as a file with PDF text",
                Tags:           ["pdf", "file", "document", "adobe"],
                Category:       "Files"
            }, 
            {
                Sequence:       93,
                Name:           "Bell",
                Icon:           Icon.Bell,
                Description:    "An icon representing a notification or alert, typically shown as a bell shape",
                Tags:           ["notification", "alert", "reminder", "alarm"],
                Category:       "Notifications"
            }, 
            {
                Sequence:       94,
                Name:           "ShoppingCart",
                Icon:           Icon.ShoppingCart,
                Description:    "An icon representing a shopping cart or basket, typically used for e-commerce",
                Tags:           ["cart", "basket", "shopping", "ecommerce"],
                Category:       "Commerce"
            }, 
            {
                Sequence:       95,
                Name:           "Phone",
                Icon:           Icon.Phone,
                Description:    "An icon representing a telephone or mobile device, typically shown as a handset or smartphone shape",
                Tags:           ["telephone", "call", "mobile", "contact"],
                Category:       "Communication"
            }, 
            {
                Sequence:       96,
                Name:           "PhoneHangUp",
                Icon:           Icon.PhoneHangUp,
                Description:    "An icon representing ending a phone call, typically shown as a phone handset facing down",
                Tags:           ["end call", "hang up", "telephone", "disconnect"],
                Category:       "Communication"
            }, 
            {
                Sequence:       97,
                Name:           "Mobile",
                Icon:           Icon.Mobile,
                Description:    "An icon representing a mobile phone or smartphone, typically shown as a rectangular device with a screen",
                Tags:           ["smartphone", "cellphone", "device", "handheld"],
                Category:       "Devices"
            }, 
            {
                Sequence:       98,
                Name:           "Laptop",
                Icon:           Icon.Laptop,
                Description:    "An icon representing a laptop computer, typically shown as a portable computer with a screen and keyboard",
                Tags:           ["computer", "notebook", "portable", "device"],
                Category:       "Devices"
            }, 
            {
                Sequence:       99,
                Name:           "ComputerDesktop",
                Icon:           Icon.ComputerDesktop,
                Description:    "An icon representing a desktop computer, typically shown as a monitor with a keyboard",
                Tags:           ["computer", "PC", "workstation", "desktop"],
                Category:       "Devices"
            }, 
            {
                Sequence:       100,
                Name:           "Devices",
                Icon:           Icon.Devices,
                Description:    "An icon representing multiple electronic devices, typically shown as a combination of smartphone, tablet, and laptop or desktop computer",
                Tags:           ["electronics", "gadgets", "technology", "multi-device"],
                Category:       "Devices"
            }, 
            {
                Sequence:       101,
                Name:           "Controller",
                Icon:           Icon.Controller,
                Description:    "An icon representing a game controller or gamepad, typically shown as a simplified gaming device with buttons",
                Tags:           ["gamepad", "gaming", "joystick", "console"],
                Category:       "Entertainment"
            }, 
            {
                Sequence:       102,
                Name:           "Tools",
                Icon:           Icon.Tools,
                Description:    "An icon representing tools or settings, typically shown as a wrench and screwdriver crossed",
                Tags:           ["settings", "repair", "maintenance", "configure"],
                Category:       "Utilities"
            }, 
            {
                Sequence:       103,
                Name:           "ToolsWrench",
                Icon:           Icon.ToolsWrench,
                Description:    "An icon representing a wrench tool, typically shown as a single adjustable wrench",
                Tags:           ["wrench", "repair", "maintenance", "adjust"],
                Category:       "Utilities"
            }, 
            {
                Sequence:       104,
                Name:           "Mail",
                Icon:           Icon.Mail,
                Description:    "An icon representing an envelope or email, typically shown as a simplified envelope shape",
                Tags:           ["email", "message", "envelope", "communication"],
                Category:       "Communication"
            }, 
            {
                Sequence:       105,
                Name:           "Send",
                Icon:           Icon.Send,
                Description:    "An icon representing the action of sending a message, typically shown as a paper airplane",
                Tags:           ["send", "message", "paper airplane", "submit"],
                Category:       "Communication"
            }, 
            {
                Sequence:       106,
                Name:           "Clock",
                Icon:           Icon.Clock,
                Description:    "An icon representing a clock or time, typically shown as a circular clock face with hands",
                Tags:           ["time", "watch", "schedule", "hour"],
                Category:       "Time"
            }, 
            {
                Sequence:       107,
                Name:           "ListWatchlistRemind",
                Icon:           Icon.ListWatchlistRemind,
                Description:    "An icon representing a watchlist or reminder list, typically shown as a checklist with a clock or bell",
                Tags:           ["watchlist", "reminder", "checklist", "alert"],
                Category:       "Productivity"
            }, 
            {
                Sequence:       108,
                Name:           "LogJournal",
                Icon:           Icon.LogJournal,
                Description:    "An icon representing a log or journal, typically shown as a book or notepad with writing",
                Tags:           ["log", "journal", "record", "diary"],
                Category:       "Productivity"
            }, 
            {
                Sequence:       109,
                Name:           "Note",
                Icon:           Icon.Note,
                Description:    "An icon representing a note or memo, typically shown as a piece of paper with writing or a folded corner",
                Tags:           ["memo", "paper", "write", "document"],
                Category:       "Productivity"
            }, 
            {
                Sequence:       110,
                Name:           "PhotosPictures",
                Icon:           Icon.PhotosPictures,
                Description:    "An icon representing photos or pictures, typically shown as multiple overlapping image frames",
                Tags:           ["photos", "pictures", "images", "gallery"],
                Category:       "Media"
            }, 
            {
                Sequence:       111,
                Name:           "RadarActivityMonitor",
                Icon:           Icon.RadarActivityMonitor,
                Description:    "An icon representing a radar or activity monitor, typically shown as a circular display with scanning lines or activity indicators",
                Tags:           ["radar", "monitor", "activity", "scan"],
                Category:       "Analytics"
            }, 
            {
                Sequence:       112,
                Name:           "Tablet",
                Icon:           Icon.Tablet,
                Description:    "An icon representing a tablet device, typically shown as a rectangular device with a large screen",
                Tags:           ["device", "iPad", "touchscreen", "portable"],
                Category:       "Devices"
            }, 
            {
                Sequence:       113,
                Name:           "Tag",
                Icon:           Icon.Tag,
                Description:    "An icon representing a tag or label, typically shown as a simplified tag shape with a hole for attachment",
                Tags:           ["label", "category", "price", "identifier"],
                Category:       "Commerce"
            }, 
            {
                Sequence:       114,
                Name:           "CameraAperture",
                Icon:           Icon.CameraAperture,
                Description:    "An icon representing a camera aperture, typically shown as a circular shape with blades forming an opening",
                Tags:           ["camera", "lens", "photography", "focus"],
                Category:       "Media"
            }, 
            {
                Sequence:       115,
                Name:           "ColorPicker",
                Icon:           Icon.ColorPicker,
                Description:    "An icon representing a color picker tool, typically shown as an eyedropper or color selection tool",
                Tags:           ["eyedropper", "color", "palette", "design"],
                Category:       "Design"
            }, 
            {
                Sequence:       116,
                Name:           "DetailList",
                Icon:           Icon.DetailList,
                Description:    "An icon representing a detailed list view, typically shown as multiple horizontal lines representing list items with additional details",
                Tags:           ["list", "details", "view", "items"],
                Category:       "Interface"
            },
            {
                Sequence:       117,
                Name:           "DocumentWithContent",
                Icon:           Icon.DocumentWithContent,
                Description:    "An icon representing a document with content, typically shown as a paper sheet with lines or text",
                Tags:           ["file", "content", "text", "paper"],
                Category:       "Files"
            }, 
            {
                Sequence:       118,
                Name:           "ListScrollEmpty",
                Icon:           Icon.ListScrollEmpty,
                Description:    "An icon representing an empty scrollable list, typically shown as a rectangle with horizontal lines and a scroll bar",
                Tags:           ["list", "empty", "scroll", "view"],
                Category:       "Interface"
            }, 
            {
                Sequence:       119,
                Name:           "ListScrollWatchlist",
                Icon:           Icon.ListScrollWatchlist,
                Description:    "An icon representing a scrollable watchlist, typically shown as a list with a scroll bar and a star or eye symbol",
                Tags:           ["watchlist", "scroll", "favorites", "monitor"],
                Category:       "Interface"
            }, 
            {
                Sequence:       120,
                Name:           "OptionsList",
                Icon:           Icon.OptionsList,
                Description:    "An icon representing a list of options or settings, typically shown as a series of horizontal lines with toggles or checkboxes",
                Tags:           ["options", "settings", "menu", "preferences"],
                Category:       "Interface"
            }, 
            {
                Sequence:       121,
                Name:           "LightningBolt",
                Icon:           Icon.LightningBolt,
                Description:    "An icon representing a lightning bolt, typically shown as a jagged line symbolizing electricity or fast action",
                Tags:           ["electricity", "power", "energy", "fast"],
                Category:       "Weather"
            },
            {
                Sequence:       122,
                Name:           "HorizontalLine",
                Icon:           Icon.HorizontalLine,
                Description:    "An icon representing a horizontal line, typically shown as a straight horizontal line used for separation or division",
                Tags:           ["line", "separator", "divider", "horizontal"],
                Category:       "Interface"
            }, 
            {
                Sequence:       123,
                Name:           "VerticalLine",
                Icon:           Icon.VerticalLine,
                Description:    "An icon representing a vertical line, typically shown as a straight vertical line used for separation or division",
                Tags:           ["line", "separator", "divider", "vertical"],
                Category:       "Interface"
            }, 
            {
                Sequence:       124,
                Name:           "Ribbon",
                Icon:           Icon.Ribbon,
                Description:    "An icon representing a ribbon, typically shown as a decorative ribbon shape often used for awards or special designations",
                Tags:           ["award", "prize", "recognition", "decoration"],
                Category:       "Miscellaneous"
            }, 
            {
                Sequence:       125,
                Name:           "Diamond",
                Icon:           Icon.Diamond,
                Description:    "An icon representing a diamond, typically shown as a stylized diamond shape often used to symbolize luxury or value",
                Tags:           ["gem", "jewel", "luxury", "value"],
                Category:       "Miscellaneous"
            }, 
            {
                Sequence:       126,
                Name:           "Alarm",
                Icon:           Icon.Alarm,
                Description:    "An icon representing an alarm, typically shown as a ringing bell or clock face with alarm indicators",
                Tags:           ["alert", "notification", "reminder", "clock"],
                Category:       "Time"
            }, 
            {
                Sequence:       127,
                Name:           "History",
                Icon:           Icon.History,
                Description:    "An icon representing history or past events, typically shown as a clock face with an arrow pointing counterclockwise",
                Tags:           ["past", "time", "record", "chronology"],
                Category:       "Time"
            }, 
            {
                Sequence:       128,
                Name:           "Heart",
                Icon:           Icon.Heart,
                Description:    "An icon representing a heart, typically shown as a stylized heart shape often used to symbolize love, affection, or favorites",
                Tags:           ["love", "like", "favorite", "affection"],
                Category:       "Miscellaneous"
            }, 
            {
                Sequence:       129,
                Name:           "Print",
                Icon:           Icon.Print,
                Description:    "An icon representing a printer or the action of printing, typically shown as a simplified printer device",
                Tags:           ["printer", "document", "paper", "output"],
                Category:       "Office"
            }, 
            {
                Sequence:       130,
                Name:           "Error",
                Icon:           Icon.Error,
                Description:    "An icon representing an error or warning, typically shown as an exclamation mark in a triangle or circle",
                Tags:           ["warning", "alert", "danger", "caution"],
                Category:       "Interface"
            }, 
            {
                Sequence:       131,
                Name:           "Flag",
                Icon:           Icon.Flag,
                Description:    "An icon representing a flag, typically shown as a rectangular or triangular shape on a pole",
                Tags:           ["banner", "marker", "signal", "country"],
                Category:       "Miscellaneous"
            }, 
            {
                Sequence:       132,
                Name:           "Notebook",
                Icon:           Icon.Notebook,
                Description:    "An icon representing a notebook or journal, typically shown as a bound book with lines or a spiral binding",
                Tags:           ["journal", "diary", "notes", "writing"],
                Category:       "Office"
            }, 
            {
                Sequence:       133,
                Name:           "Bug",
                Icon:           Icon.Bug,
                Description:    "An icon representing a bug or software error, typically shown as a stylized insect or a symbol indicating a programming issue",
                Tags:           ["error", "glitch", "insect", "debugging"],
                Category:       "Development"
            }, 
            {
                Sequence:       134,
                Name:           "Microphone",
                Icon:           Icon.Microphone,
                Description:    "An icon representing a microphone, typically shown as a simplified handheld or stand microphone used for audio input",
                Tags:           ["audio", "voice", "record", "sound"],
                Category:       "Media"
            }, 
            {
                Sequence:       135,
                Name:           "Video",
                Icon:           Icon.Video,
                Description:    "An icon representing video or a video camera, typically shown as a simplified camera or a play button within a frame",
                Tags:           ["movie", "film", "camera", "recording"],
                Category:       "Media"
            }, 
            {
                Sequence:       136,
                Name:           "Shop",
                Icon:           Icon.Shop,
                Description:    "An icon representing a shop or store, typically shown as a simplified storefront or shopping bag",
                Tags:           ["store", "retail", "market", "commerce"],
                Category:       "Commerce"
            }, 
            {
                Sequence:       137,
                Name:           "Phonebook",
                Icon:           Icon.Phonebook,
                Description:    "An icon representing a phonebook or contact list, typically shown as a book with a telephone symbol or a list of contacts",
                Tags:           ["contacts", "directory", "address book", "phone list"],
                Category:       "Communication"
            }, 
            {
                Sequence:       138,
                Name:           "Enhance",
                Icon:           Icon.Enhance,
                Description:    "An icon representing enhancement or improvement, typically shown as a magic wand or a sparkle symbol",
                Tags:           ["improve", "upgrade", "optimize", "magic"],
                Category:       "Editing"
            }, 
            {
                Sequence:       139,
                Name:           "Unlock",
                Icon:           Icon.Unlock,
                Description:    "An icon representing an unlocked state, typically shown as an open padlock or a lock with an open shackle",
                Tags:           ["open", "access", "security", "permission"],
                Category:       "Security"
            }, 
            {
                Sequence:       140,
                Name:           "Calculator",
                Icon:           Icon.Calculator,
                Description:    "An icon representing a calculator, typically shown as a simplified device with number buttons and a display screen",
                Tags:           ["math", "computation", "arithmetic", "calculate"],
                Category:       "Office"
            }, 
            {
                Sequence:       141,
                Name:           "Support",
                Icon:           Icon.Support,
                Description:    "An icon representing support or customer service, typically shown as a headset, speech bubble, or a person offering assistance",
                Tags:           ["help", "customer service", "assistance", "technical support"],
                Category:       "Communication"
            }, 
            {
                Sequence:       142,
                Name:           "Lightbulb",
                Icon:           Icon.Lightbulb,
                Description:    "An icon representing a lightbulb, typically shown as a simplified incandescent bulb shape, often used to symbolize ideas or inspiration",
                Tags:           ["idea", "inspiration", "innovation", "creativity"],
                Category:       "Miscellaneous"
            }, 
            {
                Sequence:       143,
                Name:           "Key",
                Icon:           Icon.Key,
                Description:    "An icon representing a key, typically shown as a simplified key shape with a distinctive head and shaft, often used to symbolize access or security",
                Tags:           ["access", "security", "unlock", "password"],
                Category:       "Security"
            }, 
            {
                Sequence:       144,
                Name:           "Scan",
                Icon:           Icon.Scan,
                Description:    "An icon representing scanning or barcode reading, typically shown as a simplified scanner or barcode with scanning lines",
                Tags:           ["barcode", "QR code", "reader", "scanning"],
                Category:       "Technology"
            }, 
            {
                Sequence:       145,
                Name:           "Hospital",
                Icon:           Icon.Hospital,
                Description:    "An icon representing a hospital or medical facility, typically shown as a building with a cross symbol or a simplified medical emblem",
                Tags:           ["medical", "healthcare", "emergency", "clinic"],
                Category:       "Health"
            }, 
            {
                Sequence:       146,
                Name:           "Health",
                Icon:           Icon.Health,
                Description:    "An icon representing health or wellness, typically shown as a heart symbol, medical cross, or a simplified human figure",
                Tags:           ["wellness", "medical", "healthcare", "healthy"],
                Category:       "Health"
            }, 
            {
                Sequence:       147,
                Name:           "Medical",
                Icon:           Icon.Medical,
                Description:    "An icon representing medical or healthcare services, typically shown as a medical cross, caduceus symbol, or a simplified medical instrument",
                Tags:           ["healthcare", "doctor", "medicine", "hospital"],
                Category:       "Health"
            }, 
            {
                Sequence:       148,
                Name:           "Manufacture",
                Icon:           Icon.Manufacture,
                Description:    "An icon representing manufacturing or industrial production, typically shown as a factory building, assembly line, or gear symbols",
                Tags:           ["factory", "industry", "production", "assembly"],
                Category:       "Industry"
            }, 
            {
                Sequence:       149,
                Name:           "Train",
                Icon:           Icon.Train,
                Description:    "An icon representing a train or railway transportation, typically shown as a simplified side view of a train or locomotive",
                Tags:           ["railway", "transportation", "locomotive", "subway"],
                Category:       "Transportation"
            }, 
            {
                Sequence:       150,
                Name:           "Globe",
                Icon:           Icon.Globe,
                Description:    "An icon representing a globe or world map, typically shown as a circular shape with simplified continents or latitude and longitude lines",
                Tags:           ["world", "earth", "international", "global"],
                Category:       "Geography"
            }, 
            {
                Sequence:       151,
                Name:           "GlobeNotConnected",
                Icon:           Icon.GlobeNotConnected,
                Description:    "An icon representing a globe with no internet connection, typically shown as a globe symbol with a disconnection indicator",
                Tags:           ["no internet", "offline", "disconnected", "network error"],
                Category:       "Network"
            }, 
            {
                Sequence:       152,
                Name:           "GlobeRefresh",
                Icon:           Icon.GlobeRefresh,
                Description:    "An icon representing a globe with a refresh or reload action, typically shown as a globe symbol with circular arrows indicating refresh",
                Tags:           ["reload", "update", "sync", "global refresh"],
                Category:       "Network"
            }, 
            {
                Sequence:       153,
                Name:           "GlobeChangesPending",
                Icon:           Icon.GlobeChangesPending,
                Description:    "An icon representing a globe with pending changes, typically shown as a globe symbol with a clock or hourglass indicator",
                Tags:           ["global updates", "pending changes", "world sync", "update in progress"],
                Category:       "Network"
            }, 
            {
                Sequence:       154,
                Name:           "GlobeWarning",
                Icon:           Icon.GlobeWarning,
                Description:    "An icon representing a globe with a warning or alert, typically shown as a globe symbol with an exclamation mark or warning triangle",
                Tags:           ["global alert", "world warning", "international caution", "earth hazard"],
                Category:       "Network"
            }, 
            {
                Sequence:       155,
                Name:           "GlobeError",
                Icon:           Icon.GlobeError,
                Description:    "An icon representing a globe with an error or critical issue, typically shown as a globe symbol with an 'X' mark or error symbol",
                Tags:           ["global error", "world problem", "international issue", "earth malfunction"],
                Category:       "Network"
            }, 
            {
                Sequence:       156,
                Name:           "HalfFilledCircle",
                Icon:           Icon.HalfFilledCircle,
                Description:    "An icon representing a circle that is half filled, typically shown as a circular shape with one half solid and the other half empty or outlined",
                Tags:           ["half", "semicircle", "partial", "50 percent"],
                Category:       "Shapes"
            }, 
            {
                Sequence:       157,
                Name:           "Tray",
                Icon:           Icon.Tray,
                Description:    "An icon representing a tray or platform, typically shown as a flat, rectangular shape with raised edges, often used to symbolize a container or serving surface",
                Tags:           ["container", "platform", "serving", "inbox"],
                Category:       "Office"
            }, 
            {
                Sequence:       158,
                Name:           "Text",
                Icon:           Icon.Text,
                Description:    "An icon representing text or typography, typically shown as a letter 'T' or a few lines symbolizing written content",
                Tags:           ["typography", "font", "writing", "content"],
                Category:       "Editing"
            }, 
            {
                Sequence:       159,
                Name:           "Shirt",
                Icon:           Icon.Shirt,
                Description:    "An icon representing a shirt or clothing item, typically shown as a simplified outline of a collared shirt or t-shirt",
                Tags:           ["clothing", "apparel", "fashion", "garment"],
                Category:       "Fashion"
            }, 
            {
                Sequence:       160,
                Name:           "Signal",
                Icon:           Icon.Signal,
                Description:    "An icon representing the Signal messaging app, typically shown as a speech bubble with a padlock inside",
                Tags:           ["messaging", "secure communication", "privacy", "encryption"],
                Category:       "Communication"
            }, 
            {
                Sequence:       161,
                Name:           "People",
                Icon:           Icon.People,
                Description:    "An icon representing a group of people or users, typically shown as multiple simplified human figures",
                Tags:           ["users", "group", "community", "team"],
                Category:       "Social"
            }, 
            {
                Sequence:       162,
                Name:           "Person",
                Icon:           Icon.Person,
                Description:    "An icon representing a single person or user, typically shown as a simplified human figure or head and shoulders silhouette",
                Tags:           ["user", "individual", "profile", "avatar"],
                Category:       "Social"
            }, 
            {
                Sequence:       163,
                Name:           "EmojiFrown",
                Icon:           Icon.EmojiFrown,
                Description:    "An icon representing a frowning face emoji, typically shown as a circular face with downturned eyes and mouth",
                Tags:           ["sad", "unhappy", "disappointed", "negative"],
                Category:       "Emoji"
            }, 
            {
                Sequence:       164,
                Name:           "EmojiSmile",
                Icon:           Icon.EmojiSmile,
                Description:    "An icon representing a smiling face emoji, typically shown as a circular face with upturned eyes and mouth",
                Tags:           ["happy", "joy", "positive", "cheerful"],
                Category:       "Emoji"
            }, 
            {
                Sequence:       165,
                Name:           "EmojiSad",
                Icon:           Icon.EmojiSad,
                Description:    "An icon representing a sad face emoji, typically shown as a circular face with downturned eyes and mouth, often with a tear",
                Tags:           ["unhappy", "crying", "upset", "depressed"],
                Category:       "Emoji"
            }, 
            {
                Sequence:       166,
                Name:           "EmojiNeutral",
                Icon:           Icon.EmojiNeutral,
                Description:    "An icon representing a neutral face emoji, typically shown as a circular face with straight line for a mouth and neutral eyes",
                Tags:           ["indifferent", "expressionless", "poker face", "impartial"],
                Category:       "Emoji"
            }, 
            {
                Sequence:       167,
                Name:           "EmojiHappy",
                Icon:           Icon.EmojiHappy,
                Description:    "An icon representing a happy face emoji, typically shown as a circular face with wide smile and upturned eyes",
                Tags:           ["joyful", "ecstatic", "grinning", "elated"],
                Category:       "Emoji"
            }, 
            {
                Sequence:       168,
                Name:           "Warning",
                Icon:           Icon.Warning,
                Description:    "An icon representing a warning or caution, typically shown as a triangle with an exclamation mark inside",
                Tags:           ["alert", "caution", "danger", "attention"],
                Category:       "Interface"
            }, 
            {
                Sequence:       169,
                Name:           "Information",
                Icon:           Icon.Information,
                Description:    "An icon representing information or details, typically shown as a lowercase 'i' in a circle",
                Tags:           ["info", "details", "help", "about"],
                Category:       "Interface"
            }, 
            {
                Sequence:       170,
                Name:           "Database",
                Icon:           Icon.Database,
                Description:    "An icon representing a database or data storage, typically shown as a cylindrical shape or stacked disks",
                Tags:           ["storage", "data", "server", "repository"],
                Category:       "Technology"
            }, 
            {
                Sequence:       171,
                Name:           "Weather",
                Icon:           Icon.Weather,
                Description:    "An icon representing weather conditions, typically shown as a sun, cloud, or combination of weather symbols",
                Tags:           ["forecast", "climate", "meteorology", "temperature"],
                Category:       "Nature"
            }, 
            {
                Sequence:       172,
                Name:           "TrendingHashtag",
                Icon:           Icon.TrendingHashtag,
                Description:    "An icon representing a trending hashtag, typically shown as a hashtag symbol (#) with an upward arrow or graph",
                Tags:           ["popular", "viral", "social media", "trend"],
                Category:       "Social Media"
            }, 
            {
                Sequence:       173,
                Name:           "TrendingUpwards",
                Icon:           Icon.TrendingUpwards,
                Description:    "An icon representing an upward trend, typically shown as a line graph or arrow pointing upwards",
                Tags:           ["increase", "growth", "rising", "improvement"],
                Category:       "Business"
            }, 
            {
                Sequence:       174,
                Name:           "Items",
                Icon:           Icon.Items,
                Description:    "An icon representing multiple items or a list, typically shown as stacked rectangles or a bulleted list",
                Tags:           ["list", "inventory", "collection", "elements"],
                Category:       "Interface"
            }, 
            {
                Sequence:       175,
                Name:           "LevelsLayersItems",
                Icon:           Icon.LevelsLayersItems,
                Description:    "An icon representing multiple levels, layers, or stacked items, typically shown as overlapping shapes or stacked planes",
                Tags:           ["layers", "stack", "hierarchy", "organization"],
                Category:       "Interface"
            }, 
            {
                Sequence:       176,
                Name:           "Trending",
                Icon:           Icon.Trending,
                Description:    "An icon representing trending or popular topics, typically shown as a graph with an upward trend or a flame symbol",
                Tags:           ["popular", "viral", "hot topic", "trending now"],
                Category:       "Social Media"
            }, 
            {
                Sequence:       177,
                Name:           "LineWeight",
                Icon:           Icon.LineWeight,
                Description:    "An icon representing line weight or thickness, typically shown as multiple horizontal lines of varying thicknesses",
                Tags:           ["thickness", "stroke", "width", "border"],
                Category:       "Design"
            }, 
            {
                Sequence:       178,
                Name:           "Printing3D",
                Icon:           Icon.Printing3D,
                Description:    "An icon representing 3D printing, typically shown as a simplified 3D printer or a cube being constructed layer by layer",
                Tags:           ["additive manufacturing", "rapid prototyping", "3D modeling", "fabrication"],
                Category:       "Technology"
            }
        ], 
        Sequence, 
        SortOrder.Ascending
    );
```

## Final Considerations

I hope you have found this helpful. If you need any help with the Power Platform, don't hesitate to email us at [support@superpowerlabs.co](support@superpowerlabs.co).
