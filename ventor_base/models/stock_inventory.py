# Copyright 2020 VentorTech OU
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0).

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class StockInventory(models.Model):
    _name = 'stock.inventory'
    _inherit = ['stock.inventory', 'stock.location.mixin']

    warehouse_id = fields.Many2one('stock.warehouse', 'Warehouse', required=False)

    def _onchange_company_id(self):
        super(StockInventory, self)._onchange_company_id(default)
        # Apply logic only in multi-location environment
        if self.user_has_groups('stock.group_stock_multi_locations'):
            location_id = self._get_default_location_warehouse()
            if location_id:
                self.location_ids = location_id

    @api.constrains("warehouse_id", "location_ids")
    def _check_locations(self):
        if self.warehouse_id and self.location_ids and self.warehouse_id != self.location_ids.mapped("warehouse_id"):
            raise ValidationError(
                        _(
                            "You defined warehouse for the inventory '{}', but locations contain "
                            "different warehouse(s) in it. "
                            "Please, leave Warehouse field empty, or define proper one.".format(self.display_name)
                        )
                    )

    def _update_location(self):
        if not self.warehouse_id and len(self.location_ids.mapped("warehouse_id")) == 1:
            self.warehouse_id = self.location_ids.mapped("warehouse_id")
        if self.warehouse_id and not self.location_ids:
            self.location_ids = self.warehouse_id.view_location_id

    @api.model
    def create(self, vals):
        res = super(StockInventory, self).create(vals)
        res._update_location()
        return res

    def write(self, vals):
        res = super(StockInventory, self).write(vals)
        self._update_location()
        return res

class InventoryLine(models.Model):
    _inherit = "stock.inventory.line"
    _description = "Inventory Line"

    @api.constrains("prod_lot_id", "product_qty")
    def _check_product_lot(self):
        """ check product lot/serial except for stock_fix_lot """
        for product in self:
            if (
                not product.product_qty
                or not product.company_id.force_lot_validation_on_inventory_adjustment
                or (product.env.context.get("skip_product_lot_check") and not product.product_qty)
            ):
                return
            if product.product_tracking in ("lot", "serial") and not product.prod_lot_id:
                    raise ValidationError(
                        _(
                            "You need to supply a Lot/Serial number for product: %s",
                            product.product_id.display_name,
                        )
                    )
