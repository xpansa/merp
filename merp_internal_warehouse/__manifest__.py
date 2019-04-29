# coding: utf-8
# Copyright 2019 VentorTech OU
# Part of Ventor modules. See LICENSE file for full copyright and licensing details.

{
    'name': 'Ventor Internal Warehouse',
    'version': '12.0.1.1.0',
    'author': 'Ventor, Xpansa Group',
    'website': 'https://ventor.tech/',
    'installable': True,
    'images': ['static/description/main_banner.png'],
    'description': """
Ventor Internal Warehouse
    """,
    'summary': 'Ventor Internal Warehouse',
    'depends': [
        'merp_base',
    ],
    'data': [
        'views/res_users.xml',
        'views/stock_warehouse.xml',
    ],
}
