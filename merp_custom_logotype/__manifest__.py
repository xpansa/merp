# -*- coding: utf-8 -*-
# Copyright 2018 Ventor, Xpansa Group.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Custom Mobile Logo',
    "version": "12.0.1.0.0",
    'author': 'Ventor, Xpansa Group',
    'website': 'https://ventor.tech/',
    'installable': True,
    'images': ['static/description/main_banner.png'],
    'description': """
Adds customer logotype for Ventor/mERP App
""",
    'summary': 'Custom Mobile Logo',
    'depends': [
        'merp_base',
    ],
    'data': [
        'views/merp_config.xml',
    ],
}
