from openerp import api, models, fields


class StockConfigSettings(models.TransientModel):
    _inherit = 'stock.config.settings'

    outgoing_wave_behavior_on_confirm = fields.Selection(
        [
            (0, 'Close pickings in wave with creation of backorders '
                'for incomplete pickings'),
            (1, 'Close pickings in wave without creating backorders'),
            (2, 'Move wave to "On Hold" if not all pickings are confirmed')
        ],
        string='Behavior on Confirm', default=0)

    outgoing_routing_strategy = fields.Selection(
        [
            ('name', 'Sort by source locations in alphabetical order'),
        ],
        string='Routing Strategy', default='name')

    outgoing_routing_order = fields.Selection(
        [
            (0, 'Ascending (A-Z)'),
            (1, 'Descending (Z-A)'),
        ],
        string='Routing Order', default=0)

    @api.model
    def get_default_company_picking_values(self, fields):
        company = self.env.user.company_id
        return {
            'outgoing_wave_behavior_on_confirm': company.outgoing_wave_behavior_on_confirm,
            'outgoing_routing_strategy': company.outgoing_routing_strategy,
            'outgoing_routing_order': company.outgoing_routing_order,
        }

    @api.multi
    def set_company_picking_values(self):
        company = self.env.user.company_id
        company.outgoing_wave_behavior_on_confirm = self.outgoing_wave_behavior_on_confirm
        company.outgoing_routing_strategy = self.outgoing_routing_strategy
        company.outgoing_routing_order = self.outgoing_routing_order
