from odoo import models, fields, api, _


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    operations_to_pick = fields.Many2many(
        'stock.move.line', relation='picking_operations_to_pick',
        string='Operations to Pick',
        compute='_compute_operations_to_pick', store=False)

    strategy_order_r = fields.Char(string='Strategy Order',
        compute='_compute_operations_to_pick', store=False)

    @api.one
    @api.depends('move_line_ids',
                 'move_line_ids.location_id',
                 'move_line_ids.qty_done')
    def _compute_operations_to_pick(self):
        strategy = self.env.user.company_id.outgoing_routing_strategy
        strategy_order = self.env.user.company_id.outgoing_routing_order
        res = self.env['stock.move.line']
        for operation in res.search([('picking_id', '=', self.id)]):
            if operation._compute_operation_valid():
                res += operation
        self.operations_to_pick = res.sorted(
            key=lambda r: getattr(r.location_id, strategy, 'None'),
            reverse=strategy_order
        )

        settings = self.env['res.company'].fields_get(
            ['outgoing_routing_strategy', 'outgoing_routing_order'])
        strategies = settings['outgoing_routing_strategy']['selection']
        orders = settings['outgoing_routing_order']['selection']
        self.strategy_order_r = _('Strategy Order: ') + ', '.join([
            dict(strategies)[strategy].lower(),
            dict(orders)[strategy_order].lower()
        ])
