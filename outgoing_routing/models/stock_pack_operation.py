# Copyright 2020 VentorTech OU
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0).

from odoo import models, api


class StockPackOperation(models.Model):
    _inherit = 'stock.move.line'

    @api.model
    def _compute_operation_valid(self):
        res = True
        if hasattr(super(StockPackOperation, self), '_compute_operation_valid'):
            res &= super(StockPackOperation, self)._compute_operation_valid()
        res &= self.qty_done != self.product_qty
        return res

    def _get_attr(self, attr_name, flag):
        if not flag:
            return getattr(self, attr_name)
        return getattr((self.package_level_id or self), attr_name)

    def _get_operation_tuple(self, flag):
        self.ensure_one()
        return (
            ('id', self._get_attr('id', flag)),
            ('_type', self._get_attr('_name', flag)),
        )
