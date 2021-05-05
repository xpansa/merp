# Copyright 2019 VentorTech OU
# Part of Ventor modules. See LICENSE file for full copyright and licensing details.

from odoo import models, api


class StockPackOperation(models.Model):
    _inherit = 'stock.move.line'

    @api.model
    def _compute_operation_valid(self):
        res = True
        if hasattr(super(StockPackOperation, self), '_compute_operation_valid'):
            res &= super(StockPackOperation, self)._compute_operation_valid()
        res &= self.qty_done != self.product_qty
        # res &= self.state not in ('draft', 'cancel', 'done')
        return res

    def _get_operation_attr(self, attr, flag):
        if not flag:
            return getattr(self, attr)
        return getattr((self.package_level_id or self), attr)

    def _get_operation_tuple(self):
        self.ensure_one()
        show_pack = self.picking_id.picking_type_id.show_entire_packs
        return (
            ('id', self._get_operation_attr('id', show_pack)),
            ('_type', self._get_operation_attr('_name', show_pack)),
        )
