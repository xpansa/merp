# -*- coding: utf-8 -*-
# Copyright 2018 Ventor, Xpansa Group.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Ventor Picking Wave Base Module',
    "version": "12.0.1.0.0",
    'author': 'Ventor, Xpansa Group',
    'website': 'https://ventor.tech/',
    'installable': True,
    'images': ['static/description/main_banner.png'],
    'description': """
Allows configurable picking and receiving wave
""",
    'summary': 'Allows configurable picking/picking wave',
    'depends': [
        'stock_picking_batch',
        'merp_base',
        'merp_custom_access_rights',
        'merp_picking_advanced_search',
        'merp_outgoing_routing'
    ],
    'data': [
        'views/stock_picking_wave.xml',
        'views/res_config.xml'
    ],
}
