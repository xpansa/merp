# Copyright 2020 VentorTech OU
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0).

from odoo import models, fields


class ResUsers(models.Model):
    _inherit = 'res.users'

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
