# Copyright 2020 VentorTech OU
# Part of Ventor modules. See LICENSE file for full copyright and licensing details.

from odoo import api, models
from odoo.tools.float_utils import float_compare


class StockQuant(models.Model):
    _inherit = 'stock.quant'

    @api.model
    def _reorder(self, quants, product_id):
        """ Reorders quants by product quantity in locations (and location priority)
        """
        required = self.env.context.get('merp_reservation_quantity', 0)
        rounding = product_id.uom_id.rounding
        strategy = self.env.user.company_id.outgoing_routing_strategy
        strategy_order = self.env.user.company_id.outgoing_routing_order

        locations = {}
        queues = [self.env['stock.quant'], self.env['stock.quant']] # (lprio, hprio)

        for quant in quants:
            locations.setdefault(quant.location_id, []).append(quant)

        for location in sorted(locations,
            key=lambda location: getattr(location, strategy, 'None'),
            reverse=int(strategy_order)
        ):
            location_quants = locations.get(location)
            quantity = sum([qt.quantity - qt.reserved_quantity for qt in location_quants])
            priority = float_compare(quantity, required, precision_rounding=rounding) >= 0
            for location_quant in location_quants:
                queues[priority] |= location_quant

        return queues[True] + queues[False]
