# UI/UX Design Guidelines

## 23 Essential Web Development UI/UX Hacks

### 1. Core Design Principles & Attributes

#### 1.1 General Element Behavior

- Directive: Apply the `contenteditable` attribute to any HTML element to allow users to modify its content directly on the page.
- Directive: Use the `inert` attribute to make an element and all its children nonfunctional (buttons, links, and input fields are disabled; element is ignored by screen readers).
- Directive: Use the `<pre>` tag to display text exactly as written in HTML, preserving all spaces and line breaks, typically for code blocks.

#### 1.2 Aspect Ratio & Responsiveness

- Directive: Set up CSS or HTML ratios to ensure elements, such as thumbnails or image galleries, maintain a specific aspect ratio while remaining responsive.

### 2. Color & Theming (HSL Focus)

#### 2.1 Color Format Standard

- Directive: Adopt **HSL** (Hue, Saturation, Lightness) as the primary color format because it is more intuitive and easier to manipulate programmatically than Hex or RGB.
- Technical Rule: Hue (H) represents the color’s position on the color wheel (0-360 degrees).
- Technical Rule: Manipulate Saturation (S) to control how colorful the hue is.
- Technical Rule: Control brightness using the Lightness (L) value (make it darker or lighter).

#### 2.2 Shade Generation & Combinations

- Directive: Generate shades by adjusting the Saturation and Lightness values.
- Actionable: To generate a lighter color for a hover state, simply **increase the lightness (L)** value using code.
- Actionable: Create tertiary and accent colors by calculating a 120-degree arc, moving 60 degrees left and right of the primary color Hue.

#### 2.3 Dark Mode Implementation

- Directive: Implement automatic adaptation to the user's system color scheme using a single media query.
- Guideline: Utilize HSL for accent colors to retain better control over contrast when displayed on a dark background.

### 3. Native HTML Components & Accessibility

#### 3.1 Modals and Popups

- Element Directive: Wrap popup content using the native `<dialog>` tag (hides it by default).
- JavaScript API: Display the popup using the built-in function: `element.showModal()`.
- Closing: The modal can be closed by pressing the Escape key or by calling the built-in function `element.close()` on a closing button.

#### 3.2 Forms and Inputs

- Technique: Use the `<datalist>` element in conjunction with an `<input>` field to provide type-ahead suggestions without needing custom JavaScript or CSS.
- Optimization: Apply the `inputmode` attribute on input fields to trigger the most appropriate virtual keyboard (e.g., numeric, email) on mobile devices for improved user experience.

#### 3.3 Status and Collapsible Content

- Element Structure: Use the native `<details>` (wrapper) and `<summary>` (visible text) tags for collapsible content; hidden elements are placed within `<details>`.
- Element Structure: Use the native `<progress>` or `<meter>` tags, defining a `max` value and the `current` value to display progress.
- Technique: Implement basic tooltips using the standard HTML `title` attribute on any element to display text on hover.

### 4. Media, Performance, and Advanced CSS

#### 4.1 Asset Optimization

- Format Directive: Convert raster images to **WEBP format** to maintain quality while reducing file size by half.
- Directive: Use **SVGs** (Scalable Vector Graphics) for icons and illustrations; they are lightweight, editable like standard HTML elements, and respond natively to dark mode styling.
- Technique: Use the `<picture>` element with a `<source>` element and a media query to load specific, smaller image versions for mobile devices.
- Technique: Convert the logo into a `favicon.ico` file and place it in the root or public folder; browsers automatically request it.

#### 4.2 Typography & CSS Details

- Directive: Style lists using a single line of CSS to manage markers and text alignment.
- Technique: Use the `text-underline-offset` property to adjust the position of text underlines, ensuring the text remains readable.

#### 4.3 Advanced Effects and Best Practices

- Technique: Create 3D rotation effects by rotating the element on the X or Y axis and controlling the intensity of the rotation by setting the CSS `perspective` property (defining the distance from the element).
- Best Practice: Prevent issues on touch devices by wrapping problematic hover effects inside a media query, creating a separate, specific version for touch screens.
