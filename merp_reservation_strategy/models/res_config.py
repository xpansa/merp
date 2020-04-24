# Copyright 2020 VentorTech OU
# Part of Ventor modules. See LICENSE file for full copyright and licensing details.

from odoo import models, fields


class StockConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    custom_reservation_strategy = fields.Boolean(
        string='Custom Reservation Strategy',
        related='company_id.custom_reservation_strategy',
        readonly=False)
