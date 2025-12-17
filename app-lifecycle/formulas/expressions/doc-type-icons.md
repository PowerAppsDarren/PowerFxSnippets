---
title: "File Type Icons"
description: "Generate URLs for file type icons based on file extensions."
category: "app-lifecycle"
subcategory: "formulas"
tags:
  - icons
  - file-types
  - ui
  - sharepoint
  - expression
difficulty: beginner
products:
  - power-apps-canvas
author: "Darren Neese"
created: 2025-11-19
updated: 2025-11-19
license: "MIT"
---

# File Type Icons

The list will include various icon names, each corresponding to a different file type or application. Some examples you might see include:

|   File Type  | Icon    |   File Type  | Icon    |
| --- | --- |--- | --- |
| "folder"|  ![Doc Icon](https://static2.sharepointonline.com/files/fabric/assets/item-types/24/folder.svg){height=40px}   |.one|  ![Doc Icon](https://static2.sharepointonline.com/files/fabric/assets/item-types/24/one.svg){height=40px}   |
| .accdb  |  ![Doc Icon](https://static2.sharepointonline.com/files/fabric/assets/item-types/24/accdb.svg){height=40px}   |.pdf|  ![Doc Icon](https://static2.sharepointonline.com/files/fabric/assets/item-types/24/pdf.svg){height=40px}   |
| .csv    |  ![Doc Icon](https://static2.sharepointonline.com/files/fabric/assets/item-types/24/csv.svg){height=40px}   |"photo"|  ![Doc Icon](https://static2.sharepointonline.com/files/fabric/assets/item-types/24/photo.svg){height=40px}   |
| .docx   |  ![Doc Icon](https://static2.sharepointonline.com/files/fabric/assets/item-types/24/docx.svg){height=40px}   |.pptx|  ![Doc Icon](https://static2.sharepointonline.com/files/fabric/assets/item-types/24/pptx.svg){height=40px}   |
| .html   |  ![Doc Icon](https://static2.sharepointonline.com/files/fabric/assets/item-types/24/html.svg){height=40px}   |.txt|  ![Doc Icon](https://static2.sharepointonline.com/files/fabric/assets/item-types/24/txt.svg){height=40px}   |
| "video"   |  ![Doc Icon](https://static2.sharepointonline.com/files/fabric/assets/item-types/24/video.svg){height=40px}   |.xlsx|  ![Doc Icon](https://static2.sharepointonline.com/files/fabric/assets/item-types/24/xlsx.svg){height=40px}   |
| .zip   |  ![Doc Icon](https://static2.sharepointonline.com/files/fabric/assets/item-types/24/zip.svg){height=40px}   |||

## Add This to Your Application

```JavaScript
$"https://static2.sharepointonline.com/files/fabric/assets/item-types/24/{" FILE_EXTENSION_HERE "}.svg"
```

## Final Considerations

I hope you have found this helpful. If you need any help with the Power Platform, don't hesitate to email us at [support@superpowerlabs.co](support@superpowerlabs.co).
