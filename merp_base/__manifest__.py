# -*- coding: utf-8 -*-
# Copyright 2018 Ventor, Xpansa Group.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Ventor Base',
    'version': '12.0.1.1.0',
    'author': 'Ventor, Xpansa Group',
    'website': 'https://ventor.tech/',
    'installable': True,
    'images': ['static/description/main_banner.png'],
    'description': """
Base module that allow relation between Ventor modules
""",
    'summary': 'Base module that allow relation between Ventor modules',
    'depends': [
        'base',
        'stock',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/res_config.xml',
        'views/res_users.xml',
    ],
}
