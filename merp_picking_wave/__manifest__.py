# -*- coding: utf-8 -*-
# © 2016 Xpansa Group
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    'name': 'mERP Picking Wave',
    "version": "10.0.1.0.0",
    'author': 'Xpansa Group',
    'website': 'http://xpansa.com',
    'installable': True,
    'images': ['static/description/icon.png'],
    'description': """
Allows configurable picking wave
""",
    'summary': 'Allows configurable picking wave',
    'depends': [
        'merp_picking_wave_base',
    ],
    'data': [
        'security/groups.xml',
        'views/res_config.xml',
        'views/stock_picking_wave.xml',
        'wizard/message_wizard.xml'
    ],
}
