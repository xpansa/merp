# Copyright 2020 VentorTech OU
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0).

from odoo import models, fields, api


class StockLocationMixin(models.Model):
    _name = 'stock.location.mixin'
    _description = """Implement a method below for 
                      the product.template and
                      stock.inventory models"""

    def _get_default_location_warehouse(self):
        default_location_id = (
            self.env.user.default_inventory_location and
            self.env.user.default_inventory_location.id
        ) or False

        if not default_location_id:
            default_location_id = (
                self.env.user.company_id.stock_inventory_location and
                self.env.user.company_id.stock_inventory_location.id
            ) or False
        return default_location_id
