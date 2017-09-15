# -*- coding: utf-8 -*-
# © 2016 Xpansa Group
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    'name': 'mERP Outgoing Routing',
    "version": "8.0.1.0.0",
    'author': 'Xpansa Group',
    'website': 'http://xpansa.com',
    'installable': True,
    'images': ['static/description/icon.png'],
    'description': """
Adds Outgoing Routing options
=============================
name: sort by source location name (in alphabetical order)
removal_prio: sort by location removal strategy priority field
""",
    'summary': 'Adds Outgoing Routing options',
    'depends': [
        'merp_base',
    ],
    'data': [
        'views/res_config.xml',
        'views/stock.xml',
        'views/picking.xml'
    ],
}
