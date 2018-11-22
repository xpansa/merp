# -*- coding: utf-8 -*-
# Copyright 2018 Ventor, Xpansa Group.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Ventor Picking Wave Product Skip',
    "version": "12.0.1.0.0",
    'author': 'Ventor, Xpansa Group',
    'website': 'https://ventor.tech/',
    'installable': True,
    'images': ['static/description/main_banner.png'],
    'description': """
Allows smart skip of products in picking waves
""",
    'summary': 'Allows smart skip of products in picking waves',
    'depends': [
        'merp_picking_products_skip',
        'merp_picking_wave_base',
    ],
    'data': [
        'views/stock_picking.xml',
    ],
}
