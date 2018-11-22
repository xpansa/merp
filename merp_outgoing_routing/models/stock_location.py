from odoo import models, fields, api


class StockLocation(models.Model):
    _inherit = "stock.location"

    removal_prio = fields.Integer(
        string='Removal Strategy Priority',
        default=0
    )

    strategy_sequence = fields.Integer(
        string='Sequence',
        help='Sequence based on warehouse location outgoing strategy/order',
        compute='_compute_outgoing_strategy_sequence',
        store=False
    )

    @api.multi
    def _compute_outgoing_strategy_sequence(self):

        strategy = self.env.user.company_id.outgoing_routing_strategy
        strategy_order = self.env.user.company_id.outgoing_routing_order

        if not strategy in self:
            return

        order = '%s %s' % (strategy, ['asc', 'desc'][strategy_order])
        res = self.search([], order=order)
        for sequence, location in enumerate(res):
                location.strategy_sequence = sequence
