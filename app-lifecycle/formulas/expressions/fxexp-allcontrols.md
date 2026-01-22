---
title: "All Controls Expression"
description: "A comprehensive table of all Power Apps controls with metadata like purpose, category, and tags."
category: "app-architecture"
subcategory: "formulas"
tags:
  - controls
  - reference
  - metadata
  - documentation
  - expression
difficulty: intermediate
products:
  - power-apps-canvas
author: "Darren Neese"
created: 2025-11-19
updated: 2025-11-19
license: "MIT"
---

# All Controls Expression

If you ever need a listing of all the controls available in Power Apps, here is a snippet you can paste in App.Formulas. It is an expression that will return a table of all the controls available in Power Apps.

```PowerFx
    fxExp_AllControls = [
        // Recommended Controls
        {
            MenuName: "Text",
            CommonName: "Label",
            AlternateName: "Display label",
            YAMLName: "Text",
            Purpose: "Displays text",
            ModernClassification: "Modern",
            StandardPrefix: "lbl",
            Categories: "Recommended|Display",
            Tags: ["Paragraph", "Field Label"],
            WhyUse: "The classic version does not have rounded corners (border radius)",
            YAMLTemplate:
"- @@ControlName:
    Control: @@ControlClassName
    Properties:
      Text: =""Label's Sample Text""
      VerticalAlign: =VerticalAlign.Middle
      Width: =200"
        },
        {
            MenuName: "Button",
            CommonName: "Button",
            AlternateName: "Command Button",
            YAMLName: "Button",
            Purpose: "Executes actions when clicked",
            ModernClassification: "Modern",
            StandardPrefix: "btn",
            Categories: "Recommended|Input",
            Tags: ["Action", "OnSelect", "Modern"],
            WhyUse: "Allows a user to interact by triggering specific actions within an application"
        },
        {
            MenuName: "Container",
            CommonName: "Container",
            AlternateName: "Group Box",
            YAMLName: "Container",
            Purpose: "Groups and organizes related controls",
            ModernClassification: "Modern",
            StandardPrefix: "con",
            Categories: "Recommended|Layout",
            Tags: ["Grouping", "Organization", "Layout"],
            WhyUse: "Helps organize related controls and apply styling consistently to a group"
        },
        {
            MenuName: "Vertical gallery",
            CommonName: "Gallery",
            AlternateName: "List View",
            YAMLName: "Gallery",
            Purpose: "Displays a scrollable list of records",
            ModernClassification: "Modern",
            StandardPrefix: "gal",
            Categories: "Recommended",
            Tags: ["Data", "List", "Collection", "Repeating"],
            WhyUse: "Efficiently displays multiple records in a scrollable, repeating layout"
        },
        {
            MenuName: "Form",
            CommonName: "Form",
            AlternateName: "Data Form",
            YAMLName: "Form",
            Purpose: "Displays and captures data from a data source",
            ModernClassification: "Modern",
            StandardPrefix: "frm",
            Categories: "Recommended",
            Tags: ["Data Entry", "Edit", "Display", "CRUD"],
            WhyUse: "Simplifies creating, viewing, and editing records from a data source"
        },
        {
            MenuName: "Table",
            CommonName: "Table",
            AlternateName: "Data Grid",
            YAMLName: "Table",
            Purpose: "Displays data in rows and columns",
            ModernClassification: "Modern",
            StandardPrefix: "tbl",
            Categories: "Recommended",
            Tags: ["Grid", "Data", "Tabular"],
            WhyUse: "Displays structured data in a familiar spreadsheet-like format"
        },
        {
            MenuName: "Export",
            CommonName: "Export",
            AlternateName: "Export Button",
            YAMLName: "Export",
            Purpose: "Exports data to external formats",
            ModernClassification: "Modern",
            StandardPrefix: "exp",
            Categories: "Recommended",
            Tags: ["Data", "Export", "Download"],
            WhyUse: "Enables users to export data to formats like Excel or PDF"
        },

        // Layout Controls
        {
            MenuName: "Container",
            CommonName: "Container",
            AlternateName: "Group Box",
            YAMLName: "Container",
            Purpose: "Groups and organizes related controls",
            ModernClassification: "Modern",
            StandardPrefix: "con",
            Categories: "Layout",
            Tags: ["Grouping", "Organization", "Layout"],
            WhyUse: "Helps organize related controls and apply styling consistently to a group"
        },
        {
            MenuName: "Horizontal container",
            CommonName: "Horizontal Container",
            AlternateName: "Row Container",
            YAMLName: "horizontalContainer",
            Purpose: "Arranges controls horizontally in a row",
            ModernClassification: "Modern",
            StandardPrefix: "hcon",
            Categories: "Layout",
            Tags: ["Horizontal", "Row", "Layout"],
            WhyUse: "Automatically arranges controls in a horizontal row with consistent spacing"
        },
        {
            MenuName: "Vertical container",
            CommonName: "Vertical Container",
            AlternateName: "Column Container",
            YAMLName: "verticalContainer",
            Purpose: "Arranges controls vertically in a column",
            ModernClassification: "Modern",
            StandardPrefix: "vcon",
            Categories: "Layout",
            Tags: ["Vertical", "Column", "Layout"],
            WhyUse: "Automatically arranges controls in a vertical column with consistent spacing"
        },
        {
            MenuName: "Blank",
            CommonName: "Blank",
            AlternateName: "Empty Container",
            YAMLName: "Rectangle",
            Purpose: "Creates empty space or rectangular areas",
            ModernClassification: "Modern",
            StandardPrefix: "rect",
            Categories: "Layout",
            Tags: ["Space", "Rectangle", "Background"],
            WhyUse: "Creates spacing or decorative elements in the layout"
        },
        {
            MenuName: "Flexible height gallery",
            CommonName: "Flexible Gallery",
            AlternateName: "Dynamic Height Gallery",
            YAMLName: "FlexibleHeightGallery",
            Purpose: "Displays a gallery with items of varying heights",
            ModernClassification: "Modern",
            StandardPrefix: "flxgal",
            Categories: "Layout",
            Tags: ["Gallery", "Flexible", "Dynamic"],
            WhyUse: "Accommodates varying content lengths with dynamic item heights"
        },
        {
            MenuName: "Group",
            CommonName: "Group",
            AlternateName: "Control Group",
            YAMLName: "Group",
            Purpose: "Groups controls for organization and manipulation",
            ModernClassification: "Modern",
            StandardPrefix: "grp",
            Categories: "Layout",
            Tags: ["Grouping", "Organization"],
            WhyUse: "Allows treating multiple controls as a single unit for positioning and visibility"
        },
        {
            MenuName: "Tab list",
            CommonName: "Tab Control",
            AlternateName: "Tabbed Pages",
            YAMLName: "TabList",
            Purpose: "Creates a tabbed interface for organizing content",
            ModernClassification: "Modern",
            StandardPrefix: "tab",
            Categories: "Layout",
            Tags: ["Tabs", "Navigation", "Pages"],
            WhyUse: "Organizes related content into separate tabbed pages"
        },
        {
            MenuName: "Table",
            CommonName: "Table",
            AlternateName: "Data Grid",
            YAMLName: "Table",
            Purpose: "Displays data in rows and columns",
            ModernClassification: "Modern",
            StandardPrefix: "tbl",
            Categories: "Layout",
            Tags: ["Grid", "Data", "Tabular"],
            WhyUse: "Displays structured data in a familiar spreadsheet-like format"
        },
        {
            MenuName: "Form",
            CommonName: "Form",
            AlternateName: "Data Form",
            YAMLName: "Form",
            Purpose: "Displays and captures data from a data source",
            ModernClassification: "Modern",
            StandardPrefix: "frm",
            Categories: "Layout",
            Tags: ["Data Entry", "Edit", "Display", "CRUD"],
            WhyUse: "Simplifies creating, viewing, and editing records from a data source"
        },

        // Input Controls
        {
            MenuName: "Button",
            CommonName: "Button",
            AlternateName: "Command Button",
            YAMLName: "Button",
            Purpose: "Executes actions when clicked",
            ModernClassification: "Modern",
            StandardPrefix: "btn",
            Categories: "Input",
            Tags: ["Action", "OnSelect", "Command"],
            WhyUse: "Allows users to trigger specific actions within an application"
        },
        {
            MenuName: "Text input",
            CommonName: "Text Input",
            AlternateName: "Text Field",
            YAMLName: "TextInput",
            Purpose: "Captures text input from users",
            ModernClassification: "Modern",
            StandardPrefix: "txt",
            Categories: "Input",
            Tags: ["Text", "Input", "Field", "Entry"],
            WhyUse: "Collects text data from users with built-in validation options"
        },
        {
            MenuName: "Number input",
            CommonName: "Number Input",
            AlternateName: "Numeric Field",
            YAMLName: "NumberInput",
            Purpose: "Captures numeric input from users",
            ModernClassification: "Modern",
            StandardPrefix: "num",
            Categories: "Input",
            Tags: ["Number", "Input", "Numeric", "Entry"],
            WhyUse: "Collects numeric data with built-in validation and formatting"
        },
        {
            MenuName: "Dropdown",
            CommonName: "Dropdown",
            AlternateName: "Combo Box",
            YAMLName: "Dropdown",
            Purpose: "Allows selection from a list of options",
            ModernClassification: "Modern",
            StandardPrefix: "drp",
            Categories: "Input",
            Tags: ["Selection", "List", "Options"],
            WhyUse: "Provides a space-efficient way to select from predefined options"
        },
        {
            MenuName: "Combobox",
            CommonName: "Combo Box",
            AlternateName: "Autocomplete",
            YAMLName: "ComboBox",
            Purpose: "Combines dropdown and text input functionality",
            ModernClassification: "Modern",
            StandardPrefix: "cmb",
            Categories: "Input",
            Tags: ["Selection", "Input", "Autocomplete"],
            WhyUse: "Allows users to select from a list or enter custom values"
        },
        {
            MenuName: "Date picker",
            CommonName: "Date Picker",
            AlternateName: "Calendar Control",
            YAMLName: "DatePicker",
            Purpose: "Enables selection of dates",
            ModernClassification: "Modern",
            StandardPrefix: "date",
            Categories: "Input",
            Tags: ["Date", "Calendar", "Selection"],
            WhyUse: "Provides an intuitive interface for selecting dates"
        },
        {
            MenuName: "Checkbox",
            CommonName: "Checkbox",
            AlternateName: "Toggle Box",
            YAMLName: "Checkbox",
            Purpose: "Captures boolean (true/false) input",
            ModernClassification: "Modern",
            StandardPrefix: "chk",
            Categories: "Input",
            Tags: ["Boolean", "Toggle", "On/Off"],
            WhyUse: "Simple way to capture yes/no or true/false selections"
        },
        {
            MenuName: "Radio",
            CommonName: "Radio Button",
            AlternateName: "Option Button",
            YAMLName: "Radio",
            Purpose: "Allows selection of one option from a group",
            ModernClassification: "Modern",
            StandardPrefix: "rad",
            Categories: "Input",
            Tags: ["Selection", "Exclusive", "Group"],
            WhyUse: "Visually indicates mutually exclusive options in a group"
        },
        {
            MenuName: "Toggle",
            CommonName: "Toggle Switch",
            AlternateName: "Switch",
            YAMLName: "Toggle",
            Purpose: "Provides an on/off switch for settings",
            ModernClassification: "Modern",
            StandardPrefix: "tgl",
            Categories: "Input",
            Tags: ["Switch", "On/Off", "Boolean"],
            WhyUse: "Modern alternative to checkbox with clearer visual representation"
        },
        {
            MenuName: "Address input",
            CommonName: "Address Input",
            AlternateName: "Location Field",
            YAMLName: "AddressInput",
            Purpose: "Captures and validates address information",
            ModernClassification: "Modern",
            StandardPrefix: "addr",
            Categories: "Input",
            Tags: ["Address", "Location", "Geo"],
            WhyUse: "Specialized input for capturing formatted address information"
        },
        {
            MenuName: "Pen input",
            CommonName: "Signature Control",
            AlternateName: "Drawing Input",
            YAMLName: "PenInput",
            Purpose: "Captures handwritten input or signatures",
            ModernClassification: "Modern",
            StandardPrefix: "pen",
            Categories: "Input",
            Tags: ["Signature", "Drawing", "Handwriting"],
            WhyUse: "Enables capturing signatures or freehand drawing"
        },
        {
            MenuName: "Slider",
            CommonName: "Slider",
            AlternateName: "Range Control",
            YAMLName: "Slider",
            Purpose: "Selects a value from a continuous range",
            ModernClassification: "Modern",
            StandardPrefix: "sld",
            Categories: "Input",
            Tags: ["Range", "Selection", "Numeric"],
            WhyUse: "Intuitive way to select values from a continuous range"
        },
        {
            MenuName: "Rating",
            CommonName: "Rating Control",
            AlternateName: "Stars Rating",
            YAMLName: "Rating",
            Purpose: "Captures user ratings on a scale",
            ModernClassification: "Modern",
            StandardPrefix: "rat",
            Categories: "Input",
            Tags: ["Rating", "Stars", "Feedback"],
            WhyUse: "Visual way to capture user ratings or satisfaction levels"
        },
        {
            MenuName: "List box",
            CommonName: "List Box",
            AlternateName: "Selection List",
            YAMLName: "ListBox",
            Purpose: "Displays a scrollable list of selectable items",
            ModernClassification: "Modern",
            StandardPrefix: "lst",
            Categories: "Input",
            Tags: ["List", "Selection", "Multiple"],
            WhyUse: "Allows selecting single or multiple items from a visible list"
        },
        {
            MenuName: "Rich text editor",
            CommonName: "Rich Text Editor",
            AlternateName: "WYSIWYG Editor",
            YAMLName: "RichTextEditor",
            Purpose: "Captures formatted text with styling options",
            ModernClassification: "Modern",
            StandardPrefix: "rte",
            Categories: "Input",
            Tags: ["Rich Text", "Formatting", "HTML"],
            WhyUse: "Allows users to enter formatted text with styles and structure"
        },

        // Display Controls
        {
            MenuName: "HTML text",
            CommonName: "HTML Text",
            AlternateName: "Rich Text Display",
            YAMLName: "HtmlText",
            Purpose: "Displays formatted HTML content",
            ModernClassification: "Modern",
            StandardPrefix: "html",
            Categories: "Display",
            Tags: ["HTML", "Formatted", "Rich Text"],
            WhyUse: "Displays content with HTML formatting and styling"
        },
        {
            MenuName: "Icon",
            CommonName: "Icon",
            AlternateName: "Symbol",
            YAMLName: "Icon",
            Purpose: "Displays a graphical icon",
            ModernClassification: "Modern",
            StandardPrefix: "icn",
            Categories: "Display",
            Tags: ["Icon", "Symbol", "Graphic"],
            WhyUse: "Provides visual cues and compact representation of actions"
        },
        {
            MenuName: "Image",
            CommonName: "Image",
            AlternateName: "Picture",
            YAMLName: "Image",
            Purpose: "Displays images from various sources",
            ModernClassification: "Modern",
            StandardPrefix: "img",
            Categories: "Display",
            Tags: ["Image", "Picture", "Photo"],
            WhyUse: "Displays images from URLs, base64 data, or attachments"
        },
        {
            MenuName: "Progress Bar",
            CommonName: "Progress Bar",
            AlternateName: "Loading Indicator",
            YAMLName: "ProgressBar",
            Purpose: "Indicates progress of an operation",
            ModernClassification: "Modern",
            StandardPrefix: "prg",
            Categories: "Display",
            Tags: ["Progress", "Loading", "Status"],
            WhyUse: "Provides visual feedback about the completion status of operations"
        },
        {
            MenuName: "Spinner",
            CommonName: "Spinner",
            AlternateName: "Loading Icon",
            YAMLName: "Spinner",
            Purpose: "Indicates that an operation is in progress",
            ModernClassification: "Modern",
            StandardPrefix: "spn",
            Categories: "Display",
            Tags: ["Loading", "Waiting", "Processing"],
            WhyUse: "Compact indicator for operations with indeterminate completion time"
        },
        {
            MenuName: "Timer",
            CommonName: "Timer",
            AlternateName: "Clock Control",
            YAMLName: "Timer",
            Purpose: "Triggers actions at specified intervals",
            ModernClassification: "Modern",
            StandardPrefix: "tmr",
            Categories: "Display",
            Tags: ["Time", "Interval", "Automation"],
            WhyUse: "Executes actions at regular intervals or after delays"
        },

        // Media Controls
        {
            MenuName: "Image",
            CommonName: "Image",
            AlternateName: "Picture",
            YAMLName: "Image",
            Purpose: "Displays images from various sources",
            ModernClassification: "Modern",
            StandardPrefix: "img",
            Categories: "Media",
            Tags: ["Image", "Picture", "Photo"],
            WhyUse: "Displays images from URLs, base64 data, or attachments"
        },
        {
            MenuName: "Camera",
            CommonName: "Camera",
            AlternateName: "Photo Capture",
            YAMLName: "Camera",
            Purpose: "Captures photos using device camera",
            ModernClassification: "Modern",
            StandardPrefix: "cam",
            Categories: "Media",
            Tags: ["Camera", "Photo", "Capture"],
            WhyUse: "Enables capturing images directly within the app"
        },
        {
            MenuName: "Barcode reader",
            CommonName: "Barcode Scanner",
            AlternateName: "QR Code Reader",
            YAMLName: "BarcodeReader",
            Purpose: "Scans and reads barcodes and QR codes",
            ModernClassification: "Modern",
            StandardPrefix: "bar",
            Categories: "Media",
            Tags: ["Barcode", "QR", "Scanner"],
            WhyUse: "Allows scanning and decoding various barcode formats"
        },
        {
            MenuName: "Add picture",
            CommonName: "Image Uploader",
            AlternateName: "Picture Selector",
            YAMLName: "AddPicture",
            Purpose: "Enables users to upload or select images",
            ModernClassification: "Modern",
            StandardPrefix: "picup",
            Categories: "Media",
            Tags: ["Upload", "Select", "Image"],
            WhyUse: "Allows users to add images from various sources"
        },
        {
            MenuName: "Stream",
            CommonName: "Media Stream",
            AlternateName: "Video Stream",
            YAMLName: "Stream",
            Purpose: "Displays streaming media content",
            ModernClassification: "Modern",
            StandardPrefix: "strm",
            Categories: "Media",
            Tags: ["Stream", "Media", "Live"],
            WhyUse: "Displays live or recorded streaming media content"
        },
        {
            MenuName: "Video",
            CommonName: "Video Player",
            AlternateName: "Media Player",
            YAMLName: "Video",
            Purpose: "Plays video content",
            ModernClassification: "Modern",
            StandardPrefix: "vid",
            Categories: "Media",
            Tags: ["Video", "Player", "Media"],
            WhyUse: "Plays video content from various sources"
        },
        {
            MenuName: "Audio",
            CommonName: "Audio Player",
            AlternateName: "Sound Player",
            YAMLName: "Audio",
            Purpose: "Plays audio content",
            ModernClassification: "Modern",
            StandardPrefix: "aud",
            Categories: "Media",
            Tags: ["Audio", "Sound", "Player"],
            WhyUse: "Plays audio content from various sources"
        },
        {
            MenuName: "Microphone",
            CommonName: "Microphone",
            AlternateName: "Voice Recorder",
            YAMLName: "Microphone",
            Purpose: "Records audio using device microphone",
            ModernClassification: "Modern",
            StandardPrefix: "mic",
            Categories: "Media",
            Tags: ["Audio", "Recording", "Voice"],
            WhyUse: "Enables recording audio directly within the app"
        },
        {
            MenuName: "3D object",
            CommonName: "3D Object Viewer",
            AlternateName: "3D Model",
            YAMLName: "3DObject",
            Purpose: "Displays 3D models",
            ModernClassification: "Modern",
            StandardPrefix: "3d",
            Categories: "Media",
            Tags: ["3D", "Model", "Viewer"],
            WhyUse: "Visualizes and interacts with 3D models"
        },
        {
            MenuName: "Import",
            CommonName: "Import Control",
            AlternateName: "File Importer",
            YAMLName: "Import",
            Purpose: "Imports data or files into the app",
            ModernClassification: "Modern",
            StandardPrefix: "imp",
            Categories: "Media",
            Tags: ["Import", "Data", "Files"],
            WhyUse: "Enables importing external data or files"
        },
        {
            MenuName: "Export",
            CommonName: "Export Control",
            AlternateName: "File Exporter",
            YAMLName: "Export",
            Purpose: "Exports data or files from the app",
            ModernClassification: "Modern",
            StandardPrefix: "exp",
            Categories: "Media",
            Tags: ["Export", "Data", "Files"],
            WhyUse: "Enables exporting data or files to external formats"
        },
        {
            MenuName: "PDF viewer (experimental)",
            CommonName: "PDF Viewer",
            AlternateName: "Document Viewer",
            YAMLName: "PDFViewer",
            Purpose: "Displays PDF documents",
            ModernClassification: "Modern",
            StandardPrefix: "pdf",
            Categories: "Media",
            Tags: ["PDF", "Document", "Viewer"],
            WhyUse: "Displays PDF documents without requiring external apps"
        },

        // Charts Controls
        {
            MenuName: "Column chart",
            CommonName: "Column Chart",
            AlternateName: "Bar Chart (Vertical)",
            YAMLName: "ColumnChart",
            Purpose: "Displays data as vertical columns",
            ModernClassification: "Modern",
            StandardPrefix: "col",
            Categories: "Charts",
            Tags: ["Chart", "Columns", "Data Visualization"],
            WhyUse: "Visualizes and compares discrete data categories with vertical bars"
        },
        {
            MenuName: "Pie chart",
            CommonName: "Pie Chart",
            AlternateName: "Circle Chart",
            YAMLName: "PieChart",
            Purpose: "Displays data as slices of a circle",
            ModernClassification: "Modern",
            StandardPrefix: "pie",
            Categories: "Charts",
            Tags: ["Chart", "Pie", "Proportional"],
            WhyUse: "Shows proportional relationship between data points"
        },
        {
            MenuName: "Line chart",
            CommonName: "Line Chart",
            AlternateName: "Trend Chart",
            YAMLName: "LineChart",
            Purpose: "Displays data as connected points",
            ModernClassification: "Modern",
            StandardPrefix: "line",
            Categories: "Charts",
            Tags: ["Chart", "Line", "Trend"],
            WhyUse: "Visualizes trends and changes over continuous data"
        },
        {
            MenuName: "Bar chart",
            CommonName: "Bar Chart",
            AlternateName: "Horizontal Bar Chart",
            YAMLName: "BarChart",
            Purpose: "Displays data as horizontal bars",
            ModernClassification: "Modern",
            StandardPrefix: "bar",
            Categories: "Charts",
            Tags: ["Chart", "Bar", "Horizontal"],
            WhyUse: "Visualizes and compares discrete data categories with horizontal bars"
        },
        {
            MenuName: "Area chart",
            CommonName: "Area Chart",
            AlternateName: "Filled Line Chart",
            YAMLName: "AreaChart",
            Purpose: "Displays data as filled areas",
            ModernClassification: "Modern",
            StandardPrefix: "area",
            Categories: "Charts",
            Tags: ["Chart", "Area", "Filled"],
            WhyUse: "Shows cumulative totals over time with filled areas"
        },
        {
            MenuName: "Scatter chart",
            CommonName: "Scatter Chart",
            AlternateName: "Scatter Plot",
            YAMLName: "ScatterChart",
            Purpose: "Displays data as points on x/y coordinates",
            ModernClassification: "Modern",
            StandardPrefix: "scat",
            Categories: "Charts",
            Tags: ["Chart", "Scatter", "Points"],
            WhyUse: "Shows correlation between two variables"
        },
        {
            MenuName: "Combo chart",
            CommonName: "Combo Chart",
            AlternateName: "Mixed Chart",
            YAMLName: "ComboChart",
            Purpose: "Combines multiple chart types",
            ModernClassification: "Modern",
            StandardPrefix: "combo",
            Categories: "Charts",
            Tags: ["Chart", "Combined", "Multiple"],
            WhyUse: "Displays different data series with different chart types"
        },
        {
            MenuName: "Maps",
            CommonName: "Map Control",
            AlternateName: "Geographic Map",
            YAMLName: "Maps",
            Purpose: "Displays geographic data on a map",
            ModernClassification: "Modern",
            StandardPrefix: "map",
            Categories: "Charts",
            Tags: ["Map", "Geography", "Location"],
            WhyUse: "Visualizes data with geographic context"
        },

        // Artificial Intelligence Controls
        {
            MenuName: "AI Builder",
            CommonName: "AI Builder",
            AlternateName: "AI Components",
            YAMLName: "AIBuilder",
            Purpose: "Integrates AI capabilities into apps",
            ModernClassification: "Modern",
            StandardPrefix: "ai",
            Categories: "Artificial Intelligence",
            Tags: ["AI", "Machine Learning", "Automation"],
            WhyUse: "Adds pre-built AI capabilities without coding"
        },
        {
            MenuName: "Copilot answer",
            CommonName: "Copilot Answer",
            AlternateName: "AI Assistant Response",
            YAMLName: "CopilotAnswer",
            Purpose: "Displays AI-generated responses",
            ModernClassification: "Modern",
            StandardPrefix: "copa",
            Categories: "Artificial Intelligence",
            Tags: ["AI", "Copilot", "Assistant"],
            WhyUse: "Integrates Microsoft Copilot responses into apps"
        },
        {
            MenuName: "Business card reader",
            CommonName: "Business Card Scanner",
            AlternateName: "Contact Extractor",
            YAMLName: "BusinessCardReader",
            Purpose: "Scans and extracts data from business cards",
            ModernClassification: "Modern",
            StandardPrefix: "bcard",
            Categories: "Artificial Intelligence",
            Tags: ["Scanner", "OCR", "Business Card"],
            WhyUse: "Automatically extracts contact information from business cards"
        },
        {
            MenuName: "Text recognizer",
            CommonName: "OCR Scanner",
            AlternateName: "Text Extractor",
            YAMLName: "TextRecognizer",
            Purpose: "Extracts text from images",
            ModernClassification: "Modern",
            StandardPrefix: "ocr",
            Categories: "Artificial Intelligence",
            Tags: ["OCR", "Text Recognition", "Image to Text"],
            WhyUse: "Converts text in images to editable text"
        },
        {
            MenuName: "Form processor",
            CommonName: "Form Processor",
            AlternateName: "Document Analyzer",
            YAMLName: "FormProcessor",
            Purpose: "Extracts data from forms and documents",
            ModernClassification: "Modern",
            StandardPrefix: "form",
            Categories: "Artificial Intelligence",
            Tags: ["Form", "Document", "Extraction"],
            WhyUse: "Automatically extracts structured data from documents"
        },
        {
            MenuName: "Object detector",
            CommonName: "Object Detector",
            AlternateName: "Image Analyzer",
            YAMLName: "ObjectDetector",
            Purpose: "Identifies objects in images",
            ModernClassification: "Modern",
            StandardPrefix: "obj",
            Categories: "Artificial Intelligence",
            Tags: ["Object Detection", "Computer Vision", "Image Analysis"],
            WhyUse: "Detects and identifies objects within images"
        },
        {
            MenuName: "Text recognizer V2",
            CommonName: "Advanced OCR",
            AlternateName: "Enhanced Text Extractor",
            YAMLName: "TextRecognizerV2",
            Purpose: "Improved text extraction from images",
            ModernClassification: "Modern",
            StandardPrefix: "ocrv2",
            Categories: "Artificial Intelligence",
            Tags: ["OCR", "Text Recognition", "Advanced"],
            WhyUse: "More accurate and versatile text recognition from images"
        },

        // Mixed Reality Controls
        {
            MenuName: "View in 3D",
            CommonName: "3D Viewer",
            AlternateName: "3D Model Viewer",
            YAMLName: "ViewIn3D",
            Purpose: "Visualizes 3D models",
            ModernClassification: "Modern",
            StandardPrefix: "v3d",
            Categories: "Mixed Reality",
            Tags: ["3D", "Viewer", "Model"],
            WhyUse: "Displays interactive 3D models in the app"
        },
        {
            MenuName: "View in AR",
            CommonName: "AR Viewer",
            AlternateName: "Augmented Reality Viewer",
            YAMLName: "ViewInAR",
            Purpose: "Displays content in augmented reality",
            ModernClassification: "Modern",
            StandardPrefix: "ar",
            Categories: "Mixed Reality",
            Tags: ["AR", "Augmented Reality", "3D"],
            WhyUse: "Projects virtual objects into the real world using AR"
        },
        {
            MenuName: "Measure in AR",
            CommonName: "AR Measurement",
            AlternateName: "Augmented Reality Ruler",
            YAMLName: "MeasureInAR",
            Purpose: "Measures real-world objects using AR",
            ModernClassification: "Modern",
            StandardPrefix: "meas",
            Categories: "Mixed Reality",
            Tags: ["AR", "Measurement", "Ruler"],
            WhyUse: "Provides real-world measurements using augmented reality"
        },

        // Classic Controls
        {
            MenuName: "Button",
            CommonName: "Button",
            AlternateName: "Command Button",
            YAMLName: "Classic/Button",
            Purpose: "Executes actions when clicked",
            ModernClassification: "Classic",
            StandardPrefix: "btn",
            Categories: "Classic",
            Tags: ["Action", "OnSelect", "Classic"],
            WhyUse: "Allows a user to interact by triggering specific actions within an application"
        },
        {
            MenuName: "Text with artificial gallery",
            CommonName: "Text Gallery",
            AlternateName: "Text List",
            YAMLName: "Classic/TextWithArtificialGallery",
            Purpose: "Displays text in a gallery-like format",
            ModernClassification: "Classic",
            StandardPrefix: "txtgal",
            Categories: "Classic",
            Tags: ["Text", "Gallery", "List"],
            WhyUse: "Legacy way to display text in a repeating format"
        },
        {
            MenuName: "Blank horizontal gallery",
            CommonName: "Horizontal Gallery",
            AlternateName: "Horizontal List",
            YAMLName: "Classic/BlankHorizontalGallery",
            Purpose: "Displays data in a horizontal scrolling layout",
            ModernClassification: "Classic",
            StandardPrefix: "hgal",
            Categories: "Classic",
            Tags: ["Gallery", "Horizontal", "Scrolling"],
            WhyUse: "Legacy way to display records in a horizontal scrolling format"
        },
        {
            MenuName: "Edit form",
            CommonName: "Edit Form",
            AlternateName: "Data Entry Form",
            YAMLName: "Classic/EditForm",
            Purpose: "Provides form for editing data records",
            ModernClassification: "Classic",
            StandardPrefix: "efrm",
            Categories: "Classic",
            Tags: ["Form", "Edit", "Data Entry"],
            WhyUse: "Legacy way to edit records in a data source"
        },
        {
            MenuName: "Text input",
            CommonName: "Text Input",
            AlternateName: "Text Field",
            YAMLName: "Classic/TextInput",
            Purpose: "Captures text input from users",
            ModernClassification: "Classic",
            StandardPrefix: "txt",
            Categories: "Classic",
            Tags: ["Text", "Input", "Field"],
            WhyUse: "Legacy way to collect text data from users"
        },
        {
            MenuName: "Text label",
            CommonName: "Label",
            AlternateName: "Display label",
            YAMLName: "Label",
            Purpose: "Displays text",
            ModernClassification: "Classic",
            StandardPrefix: "lbl",
            Categories: "Classic",
            Tags: ["Paragraph", "Field Label", "OnSelect"],
            WhyUse: "The modern version does not have an OnSelect property/event"
        },
        {
            MenuName: "Combo box",
            CommonName: "Combo Box",
            AlternateName: "Dropdown with Input",
            YAMLName: "Classic/ComboBox",
            Purpose: "Combines dropdown and text input functionality",
            ModernClassification: "Classic",
            StandardPrefix: "cmb",
            Categories: "Classic",
            Tags: ["Selection", "Input", "Combo"],
            WhyUse: "Legacy way to select from a list or enter custom values"
        },
        {
            MenuName: "Date picker",
            CommonName: "Date Picker",
            AlternateName: "Calendar Control",
            YAMLName: "Classic/DatePicker",
            Purpose: "Enables selection of dates",
            ModernClassification: "Classic",
            StandardPrefix: "date",
            Categories: "Classic",
            Tags: ["Date", "Calendar", "Selection"],
            WhyUse: "Legacy date picker with calendar interface"
        },
        {
            MenuName: "Radio",
            CommonName: "Radio Button",
            AlternateName: "Option Button",
            YAMLName: "Classic/Radio",
            Purpose: "Allows selection of one option from a group",
            ModernClassification: "Classic",
            StandardPrefix: "rad",
            Categories: "Classic",
            Tags: ["Selection", "Exclusive", "Group"],
            WhyUse: "Legacy way to present mutually exclusive options"
        },
        {
            MenuName: "Slider",
            CommonName: "Slider",
            AlternateName: "Range Control",
            YAMLName: "Classic/Slider",
            Purpose: "Selects a value from a continuous range",
            ModernClassification: "Classic",
            StandardPrefix: "sld",
            Categories: "Classic",
            Tags: ["Range", "Selection", "Numeric"],
            WhyUse: "Legacy way to select values from a continuous range"
        },
        {
            MenuName: "Icon",
            CommonName: "Icon",
            AlternateName: "Classic Icon",
            YAMLName: "Classic/Icon",
            Purpose: "Displays one of 178 (or so) icons",
            ModernClassification: "Classic",
            StandardPrefix: "ico",
            Categories: "Classic",
            Tags: ["Icon", "Button", "OnSelect"],
            WhyUse: "The modern icon control does not have an OnSelect!",
            YAMLTemplate:
"- @@ControlName:
    Control: @@ControlClassName
    Properties:
      AccessibleLabel: =$""This is an {Lower(Last(Split(Self.Icon, "":"")).Value)} icon""
      Height: =40
      Color: =fxExp_Theme.Colors.Primary
      HoverColor: =App.Theme.Colors.PrimaryForeground
      HoverFill: =Self.Color
      Icon: =Icon.Save
      OnSelect: |+
        =Set(
            gblShowSpinner,
            true
        );
        //
        // Put code here
        //
        Set(
            gblShowSpinner,
            false
        );
      PaddingBottom: =Self.PaddingTop
      PaddingLeft: =Self.PaddingTop
      PaddingRight: =Self.PaddingTop
      PaddingTop: =4
      Tooltip: =$""This is an {Lower(Last(Split(Self.Icon, "":"")).Value)} icon""
      Width: =Self.Height"
        }
    ];
