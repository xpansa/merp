# Copyright 2020 VentorTech OU
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0).

from odoo import models, fields, api


class StockInventory(models.Model):
    _name = 'stock.inventory'
    _inherit = ['stock.inventory', 'stock.location.mixin']

    def _onchange_company_id(self):
        super(StockInventory, self)._onchange_company_id(default)
        # Apply logic only in multi-location environment
        if self.user_has_groups('stock.group_stock_multi_locations'):
            location_id = self._get_default_location_warehouse()
            if location_id:
                self.location_ids = location_id
