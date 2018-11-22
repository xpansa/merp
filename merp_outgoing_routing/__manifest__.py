# -*- coding: utf-8 -*-
# Copyright 2018 Ventor, Xpansa Group.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Ventor Outgoing Routing',
    "version": "12.0.1.0.0",
    'author': 'Ventor, Xpansa Group',
    'website': 'https://ventor.tech/',
    'installable': True,
    'images': ['static/description/main_banner.png'],
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
