# Copyright 2021 VentorTech OU
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0).


# Odoo:
from odoo import api, fields, models


class StockLocation(models.Model):
    _inherit = "stock.location"

    warehouse_id = fields.Many2one("stock.warehouse", "Warehouse", copy=False)

    @api.model
    def create(self, vals):
        res = super(StockLocation, self).create(vals)
        res.update_warehouse()
        return res

    def action_update_warehouse(self):
        """Server action for update warehouse on location."""
        for record in self:
            domain = [("view_location_id", "parent_of", record.ids)]
            record.warehouse_id = self.env["stock.warehouse"].search(domain, limit=1)

    def write(self, vals):
        if vals.get("location_id"):
            self.update_warehouse(vals)
        res = super(StockLocation, self).write(vals)
        return res

    def update_warehouse(self, vals=None):
        warehouse_id = (
            self.env["stock.location"]
            .search([("id", "=", vals and vals.get("location_id") or self.location_id.id)], limit=1)
            .warehouse_id
        )
        self.warehouse_id = warehouse_id
        return True
