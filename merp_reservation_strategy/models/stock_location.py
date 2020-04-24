# Copyright 2020 VentorTech OU
# Part of Ventor modules. See LICENSE file for full copyright and licensing details.

from odoo import api, models


class Location(models.Model):
    _inherit = "stock.location"

    @api.onchange('location_id')
    def _onchange_parent_location(self):
        self.removal_prio = self.location_id.removal_prio

