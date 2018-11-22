# -*- coding: utf-8 -*-
# Copyright 2018 Ventor, Xpansa Group.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Ventor Stock Picking Report (sorted)',
    "version": "12.0.1.0.0",
    'author': 'Ventor, Xpansa Group',
    'website': 'https://ventor.tech/',
    'installable': True,
    'images': ['static/description/main_banner.png'],
    'description': """
Sort Pack Operations within Stock Picking report
""",
    'summary': 'Sort pack operations in report',
    'depends': [
        'merp_picking_wave',
    ],
    'data': [
        'views/report_stockpicking.xml',
    ],
}
