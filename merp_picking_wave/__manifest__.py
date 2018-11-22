# -*- coding: utf-8 -*-
# Copyright 2018 Ventor, Xpansa Group.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Ventor Picking Wave',
    "version": "12.0.1.0.0",
    'author': 'Ventor, Xpansa Group',
    'website': 'https://ventor.tech/',
    'installable': True,
    'images': ['static/description/main_banner.png'],
    'description': """
Allows configurable picking wave
""",
    'summary': 'Allows configurable picking wave',
    'depends': [
        'merp_picking_wave_core',
    ],
    'data': [
        'views/res_config.xml',
        'views/stock_picking_wave.xml',
        'wizard/message_wizard.xml'
    ],
}
