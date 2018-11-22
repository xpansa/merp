# -*- coding: utf-8 -*-
# Copyright 2018 Ventor, Xpansa Group.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Ventor Receiving Wave Access Rights',
    "version": "12.0.1.0.0",
    'author': 'Ventor, Xpansa Group',
    'website': 'https://ventor.tech/',
    'installable': True,
    'images': ['static/description/main_banner.png'],
    'description': """
Ventor Receiving Wave Access Rights
""",
    'summary': 'Ventor Receiving Wave Access Rights',
    'depends': [
        'merp_custom_access_rights',
    ],
    'data': [
        'security/groups.xml',
    ],
}
