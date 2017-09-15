# -*- coding: utf-8 -*-
# © 2016 Xpansa Group
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    'name': 'mERP Picking Product Skip',
    "version": "8.0.1.0.0",
    'author': 'Xpansa Group',
    'website': 'http://xpansa.com',
    'installable': True,
    'images': ['static/description/icon.png'],
    'description': """
Allows smart skip of products in pickings
""",
    'summary': 'Allows smart skip of products in pickings',
    'depends': [
        'stock',
        'merp_base',
    ],
    'data': [
        'views/stock_picking.xml',
    ],
}
