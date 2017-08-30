# -*- coding: utf-8 -*-
# © 2016 Xpansa Group
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    'name': 'mERP Picking Wave Access Rights',
    "version": "9.0.1.0.0",
    'author': 'Xpansa Group',
    'website': 'http://xpansa.com',
    'installable': True,
    'images': ['static/description/icon.png'],
    'description': """
mERP Picking Wave Access Rights
""",
    'summary': 'mERP Picking Wave Access Rights',
    'depends': [
        'merp_custom_access_rights',
    ],
    'data': [
        'security/groups.xml',
    ],
}
