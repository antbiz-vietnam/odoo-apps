# Antbiz Dynamic Products Snippet

A custom Odoo Website snippet for displaying dynamic product content in a carousel or grid layout. This snippet extends Odoo's dynamic snippet engine and provides a clean UI for showcasing products.

## Features

- Dynamic product list rendering
- Carousel/Grid layout
- Custom title and description
- "See All" link support
- Editor preview template included
- Integrated into the Website Builder under the **Products** group

## Templates Overview

| Template ID                                | Purpose                                                                    |
| ------------------------------------------ | -------------------------------------------------------------------------- |
| `s_antb_dynamic_products_snippet_template` | Base template defining snippet layout, structure, messages, and container. |
| `s_antb_dynamic_products_snippet`          | Wrapper configuring snippet name and loading preview template.             |
| `snippets`                                 | Adds the snippet to the Website Builder sidebar.                           |

## Installation

1. Add this module to your Odoo addons path.
2. Update the app list.
3. Install the module from Odoo.

## Usage

1. Navigate to **Website → Edit**.
2. Drag **Products Carousel Grid** from the _Products_ group.
3. Configure dynamic snippet filter + template.
4. Content will render automatically based on your configuration.

## Notes

- A filter and a template must be set; otherwise, the warning message will appear.
- Preview template is required for editor display.

## License

MIT or your project license.
