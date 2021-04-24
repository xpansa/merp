# Copyright 2020 VentorTech OU
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0).

from odoo import models

import logging

_logger = logging.getLogger(__file__)


class StockPickingMixin(models.AbstractModel):
    _name = 'stock.picking.mixin'
    _description = 'Stock Picking Mixin'

    def _read_record(self, record_tuple):
        """
        record_tuple = (
            ('id', 100),
            ('_type', 'stock.move.line'),
        )

        id:: number (int)
        _type:: 'stock.move.line' or 'stock.package_level' (str)
        """
        record_dict = dict(record_tuple)
        record = self.env[record_dict['_type']].browse(record_dict['id'])
        record_dict.update(record.read()[0])
        return record_dict

    def serialize_record_merp(self, rec_id):
        """Record serialization for the mERP app."""
        try:
            stock_object = self.search([
                ('id', '=', int(rec_id)),
            ])
        except Exception as ex:
            _logger.error(ex)
            return []

        full_list, filtered_list = [], []

        for line in stock_object.operations_to_pick:
            full_list.append(line._get_operation_tuple())

        [filtered_list.append(rec) for rec in full_list if rec not in filtered_list]
        return [self._read_record(rec) for rec in filtered_list]
