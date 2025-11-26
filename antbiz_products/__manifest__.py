# -*- coding: utf-8 -*-
{
    'name': "Antbiz Products – Product UI Snippets",
    'summary': "Professional product UI snippets for Odoo Website & eCommerce.",
    'description': """
===========================
Antbiz Products – UI Snippets
===========================

Antbiz Products provides a clean and modern collection of product UI snippets 
to enhance the visual presentation of items on your Odoo Website or eCommerce.

This module adds drag-and-drop blocks to the Website Builder, allowing you to:
---------------------------------------------------------------------------
✔ Display products with attractive layouts  
✔ Add modern product grids, cards, and highlight blocks  
✔ Improve product visibility and user engagement  
✔ Customize snippets quickly without coding  
✔ Ensure responsive, lightweight and high-performance UI  

Ideal for businesses wanting to improve product display without heavy 
customization — simple, fast, efficient.

Key Features:
------------
- Beautiful product showcase snippets  
- Website Builder drag-and-drop integration  
- Mobile-friendly layouts  
- Easy customization  
- Works with any Odoo theme  
- Clean code design following Odoo guidelines  

Compatibility:
--------------
- Odoo 18+
- Works with standard Website & eCommerce modules

Support:
--------
For support, customization, or integration services, please contact:
Antbiz Vietnam – https://antbiz.vn
    """,

    'author': "Antbiz Vietnam",
    'website': "https://antbiz.vn",

    # Odoo App Store required fields:
    'category': 'Website/Website',
    'version': '1.0.0',
    'license': 'LGPL-3',

    # Pricing (Mandatory for Odoo Store)
    'price': 5.00,
    'currency': 'USD',
    'depends': ['base', 'website_sale', 'website'],
    'icon': 'static/description/icon.png',
    'data': [
        # Security
        'security/ir.model.access.csv',

        # Snippets
        'views/snippets/product_carousel_grid_snippet/options.xml',
        'views/snippets/product_carousel_grid_snippet/preview.xml',
        'views/snippets/product_carousel_grid_snippet/snippet.xml',
    ],
    'assets': {
       'web.assets_frontend': [
            'antbiz_products/static/src/snippets/s_product_carousel_grid_snippet/000.scss',
            'antbiz_products/static/src/scss/carousel.scss'
        ],

        # Web Assets support for the snippets of the Builder Block Configuration
        'website.assets_wysiwyg': [
            'antbiz_products/static/src/snippets/s_product_carousel_grid_snippet/constants.js',
            'antbiz_products/static/src/snippets/s_product_carousel_grid_snippet/options.js',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': False,
}
