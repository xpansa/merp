# -*- coding: utf-8 -*-
# © 2016 Xpansa Group
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    'name': 'mERP Base',
    "version": "8.0.1.0.0",
    'author': 'Xpansa Group',
    'website': 'http://xpansa.com',
    'installable': True,
    'images': ['static/description/icon.png'],
    'description': """
Base module that allow relation between mERP modules
""",
    'summary': 'Base module that allow relation between mERP modules',
    'depends': [
        'base',
        'stock',
    ],
    'data': [
        'views/res_config.xml',
        'views/res_users.xml',
    ],
}
