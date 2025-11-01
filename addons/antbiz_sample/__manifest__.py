# -*- coding: utf-8 -*-
{
    "name": "Telegram Chat Integration",
    "summary": "Integrate Telegram messaging directly into Odoo for real-time chat and customer communication.",
    "version": "1.0.0",
    'author': "AntBiz",
    'website': "mailto:support@antbiz.vn",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales/CRM',
    'version': '0.1',
    "license": "LGPL-3",
    "description": """
Telegram Chat Integration for Odoo
===================================

Integrate your Odoo system with Telegram and communicate seamlessly with your customers and team members. 
Send, receive, and manage Telegram messages directly from your Odoo dashboard.

Key Features:
--------------
- Two-way communication between Odoo and Telegram.
- Automatic message linking with contacts, leads, or helpdesk tickets.
- Real-time message notifications inside Odoo.
- Simple configuration using your Telegram Bot Token.
- Secure integration using the official Telegram Bot API.

Compatibility:
--------------
- Odoo 18.0
- Community

Privacy and Security:
---------------------
- Uses Telegram Bot API over HTTPS.
- No external data collection or third-party sharing.
- Fully compliant with Odoo Apps Store Data Protection Policy.

Support:
---------
For support or inquiries, please contact:
mailto:support@antbiz.vn
""",

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    # 'live_test_url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',

    # 'price': 49.99,
    # 'currency': 'USD',
    # 'support': 'mailto:support@antbiz.vn',
}

