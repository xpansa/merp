# -*- coding: utf-8 -*-
# Copyright 2018 Ventor, Xpansa Group.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Ventor Custom Access Rights',
    "version": "12.0.1.0.0",
    'author': 'Ventor, Xpansa Group',
    'website': 'https://ventor.tech/',
    'installable': True,
    'images': ['static/description/main_banner.png'],
    'description': """
Ventor Custom Access Rights
""",
    'summary': 'Ventor Custom Access Rights',
    'depends': [
        'merp_base',
    ],
    'data': [
        'security/groups.xml',
        'views/res_users.xml',
    ],
}
