# Copyright 2020 VentorTech OU
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0).

import json

from odoo import models, fields


class ResUsers(models.Model):
    _inherit = 'res.users'

    custom_package_name = fields.Char(
        string='Custom package name'
    )

    ventor_global_settings = fields.Text(
        string='Global Settings',
        readonly=True,
        compute='_compute_global_settings'
    )

    ventor_user_settings = fields.Text(
        string='User Settings'
    )

    def __init__(self, pool, cr):
        """
        Adding access rights on ventor_global_settings and ventor_user_settings
        """

        readable_fields = ['ventor_global_settings', 'ventor_user_settings', 'custom_package_name']
        writable_fields = ['ventor_user_settings']

        init_res = super().__init__(pool, cr)
        type(self).SELF_READABLE_FIELDS = type(self).SELF_READABLE_FIELDS + readable_fields
        type(self).SELF_WRITEABLE_FIELDS = type(self).SELF_WRITEABLE_FIELDS + writable_fields
        return init_res

    def _compute_global_settings(self):
        settings = []

        for stock_picking_type in self.env['stock.picking.type'].search([]):
            settings.append(stock_picking_type.get_ventor_settings())

        self.ventor_global_settings = json.dumps(
            obj={'operation_types': settings},
            indent='    ',
            sort_keys=True
        )
