# -*- coding: utf-8 -*-
# Copyright 2018 Ventor, Xpansa Group.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Ventor Picking Product Skip',
    "version": "12.0.1.0.0",
    'author': 'Ventor, Xpansa Group',
    'website': 'https://ventor.tech/',
    'installable': True,
    'images': ['static/description/main_banner.png'],
    'description': """
Allows smart skip of products in pickings
""",
    'summary': 'Allows smart skip of products in pickings',
    'depends': [
        'merp_base',
    ],
    'data': [
        'views/stock_picking.xml',
    ],
}
