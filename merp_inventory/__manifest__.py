# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2017 Ventor, Xpansa Group (<https://ventor.tech/>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'mERP Inventory Improvements',
    "version": "10.0.1.0.0",
    'author': 'Ventor, Xpansa Group',
    'website': 'https://ventor.tech/',
    'installable': True,
    'images': ['static/description/main_banner.png'],
    'description': """
Module allows to define default location that will be used for Inventory Adjustments instead of default 'WH/Stock'

""",
    'summary': 'Add small improvements to Inventory Adjustment process',
    'depends': [
        'merp_base'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/res_config.xml',
        'views/res_users.xml',
    ],
}
