# -*- coding: utf-8 -*-
# © 2016 Xpansa Group
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    'name': 'mERP Picking Wave Base Module',
    "version": "10.0.1.0.0",
    'author': 'Xpansa Group',
    'website': 'http://xpansa.com',
    'installable': True,
    'images': ['static/description/icon.png'],
    'description': """
Allows configurable picking and receiving wave
""",
    'summary': 'Allows configurable picking/picking wave',
    'depends': [
        'base',
        'stock_picking_wave',
        'merp_base',
        'merp_custom_access_rights',
        'merp_picking_advanced_search',
    ],
    'data': [
        'security/groups.xml',
        'views/stock_picking.xml',
        'views/stock_picking_wave.xml'
    ],
}
