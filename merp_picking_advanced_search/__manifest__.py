# -*- coding: utf-8 -*-
# © 2016 Xpansa Group
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    'name': 'mERP Picking Advanced Search',
    "version": "10.0.1.0.0",
    'author': 'Xpansa Group',
    'website': 'http://xpansa.com',
    'installable': True,
    'images': ['static/description/icon.png'],
    'description': """
Advanced search for picking
===========================
 Search by products not moved
""",
    'summary': 'Advanced search for picking',
    'depends': [
        'base',
        'stock',
        'merp_base',
    ],
    'data': [
        'views/stock_picking.xml',
    ],
}
