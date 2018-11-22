# -*- coding: utf-8 -*-
# Copyright 2018 Ventor, Xpansa Group.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Ventor Instant Move',
    "version": "12.0.1.0.0",
    'author': 'Ventor, Xpansa Group',
    'website': 'https://ventor.tech/',
    'installable': True,
    'images': ['static/description/main_banner.png'],
    'description': """
Ventor Instant Move
===================
The module allows using 'Instant Movements' menu on Ventor app for Odoo 11.
Using 'Instant Movements' menu user can move items from one location to another
(internal transfers) just in few clicks. Just scan an item,
choose the source and destination locations, change QTY and the movement is done.
""",
    'summary': 'Ventor Instant Move',
    'depends': [
        'merp_base',
    ],
    'data': [
        'views/res_users.xml',
    ],
}
