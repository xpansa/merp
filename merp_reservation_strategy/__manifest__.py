# Copyright 2020 VentorTech OU
# Part of Ventor modules. See LICENSE file for full copyright and licensing details.

{
    'name': 'Ventor Custom Reservation Strategy',
    "version": "13.0.1.0.0",
    'author': 'VentorTech',
    'website': 'https://ventor.tech/',
    'license': 'LGPL-3',
    'installable': True,
    'summary': 'Custom Reservation Strategy',
    'depends': [
        'merp_outgoing_routing',
    ],
    'data': [
        'views/res_config.xml',
    ],
}
