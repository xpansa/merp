# -*- coding: utf-8 -*-
# © 2016 Xpansa Group
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    'name': 'mERP Inventory Improvements',
    "version": "8.0.1.0.0",
    'author': 'Xpansa Group',
    'website': 'http://xpansa.com',
    'installable': True,
    'images': ['static/description/icon.png'],
    'description': """
Module allows to define default location that will be used for Inventory Adjustments instead of deafult 'WH/Stock'

""",
    'summary': 'Add small improvements to Inventory Adjustment process',
    'depends': [
        'merp_base',
        'stock'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/res_config.xml',
        'views/res_users.xml',
    ],
}
