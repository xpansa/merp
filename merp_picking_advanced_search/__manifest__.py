# -*- coding: utf-8 -*-
# Copyright 2018 Ventor, Xpansa Group.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Ventor Picking Advanced Search',
    "version": "12.0.1.0.0",
    'author': 'Ventor, Xpansa Group',
    'website': 'https://ventor.tech/',
    'installable': True,
    'images': ['static/description/main_banner.png'],
    'description': """
Advanced search for picking
===========================
 Search by products not moved
""",
    'summary': 'Advanced search for picking',
    'depends': [
        'merp_base',
    ],
    'data': [
        'views/stock_picking.xml',
    ],
}
