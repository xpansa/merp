# -*- coding: utf-8 -*-
# © 2016 Xpansa Group
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    'name': 'mERP Receiving Wave',
    "version": "9.0.1.0.0",
    'author': 'Xpansa Group',
    'website': 'http://xpansa.com',
    'installable': True,
    'images': ['static/description/icon.png'],
    'description': """
Allows configurable receiving wave
""",
    'summary': 'Allows configurable receiving wave',
    'depends': [
        'merp_picking_wave_base',
        'merp_receiving_wave_access_rights',
    ],
    'data': [
        'views/res_config.xml',
        'views/stock_picking_wave.xml',
    ],
}
