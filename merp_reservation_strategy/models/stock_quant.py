# Copyright 2020 VentorTech OU
# Part of Ventor modules. See LICENSE file for full copyright and licensing details.

from odoo import api, models


class StockQuant(models.Model):
    _inherit = 'stock.quant'

    @api.model
    def _update_reserved_quantity(self, product_id, location_id, quantity, lot_id=None, package_id=None, owner_id=None, strict=False):
        """ Updates reserved quantity in quants
        """
        if self.env.user.company_id.custom_reservation_strategy:
            self = self.with_context(merp_reservation_strategy='custom', merp_reservation_quantity=quantity)

        return super(StockQuant, self)._update_reserved_quantity(product_id, location_id, quantity, lot_id, package_id, owner_id, strict)

    def _gather(self, product_id, location_id, lot_id=None, package_id=None, owner_id=None, strict=False):
        """ Gather (and reorder, if required) quants
        """
        context = dict(self.env.context)
        quants = super(StockQuant, self)._gather(product_id, location_id, lot_id=lot_id, package_id=package_id, owner_id=owner_id, strict=strict)

        if context.get('merp_reservation_strategy'):
            quants = self._reorder(quants, product_id)

        if context.get('merp_reservation_strategy'):
            del context['merp_reservation_strategy']
        if context.get('merp_reservation_quantity'):
            del context['merp_reservation_quantity']
        self = self.with_context(context)

        return quants

    def _reorder(self, quants, product_id):
        """ Reorders quants by location removal priority (default)
        """
        strategy = self.env.user.company_id.outgoing_routing_strategy
        strategy_order = self.env.user.company_id.outgoing_routing_order

        return quants.sorted(
            key=lambda op: getattr(op.location_id, strategy, 'None'),
            reverse=int(strategy_order)
        )
