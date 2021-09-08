# Copyright 2020 VentorTech OU
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0).

import json

from odoo import models, fields, api


class ResUsers(models.Model):
    _inherit = 'res.users'

    allowed_warehouse_ids = fields.Many2many(
        comodel_name='stock.warehouse',
        string='Allowed Warehouses',
        help='Leave empty to allow users to work in all warehouses',
    )

    calculated_warehouse_ids = fields.Many2many(
        'stock.warehouse',
        'res_user_warehouse_calculated_rel',
        column1='res_users_id',
        column2='stock_warehouse_id',
        string='Calculated Warehouses',
        readonly=True,
        compute="_compute_warehouses",
        compute_sudo=False,
        store=True,
    )

    default_inventory_location = fields.Many2one(
        comodel_name='stock.location',
        string='Default Inventory Location',
    )

    default_warehouse = fields.Many2one(
        comodel_name='stock.warehouse',
        string='Default Warehouse For Ventor App'
    )

    stock_location_id = fields.Many2one(
        'stock.location',
        string='Force Source Location for Instant Move',
        required=False,
    )

    allow_to_change_force_source_location = fields.Boolean(
        string='Allow to change Force Source Location',
    )

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

    @api.depends("allowed_warehouse_ids")
    def _compute_warehouses(self):
        for user in self:
            if user.allowed_warehouse_ids:
                user.calculated_warehouse_ids = [(6, 0, user.allowed_warehouse_ids.ids)]
            else:
                user.calculated_warehouse_ids = [(6, 0, self.env["stock.warehouse"].search([]).ids)]
