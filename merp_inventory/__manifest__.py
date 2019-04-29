# -*- coding: utf-8 -*-
# Copyright 2018 Ventor, Xpansa Group.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Ventor Inventory Improvements',
    "version": "12.0.1.0.0",
    'author': 'Ventor, Xpansa Group',
    'website': 'https://ventor.tech/',
    'installable': True,
    'images': ['static/description/main_banner.png'],
    'description': """
Module allows to define default location that will be used for Inventory Adjustments instead of default 'WH/Stock'

""",
    'summary': 'Add small improvements to Inventory Adjustment process',
    'depends': [
        'merp_base',
        'merp_custom_access_rights'
    ],
    'data': [
        'views/res_config.xml',
        'views/res_users.xml',
        'views/stock_inventory.xml',
    ],
}
