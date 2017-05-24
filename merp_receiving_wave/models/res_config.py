from openerp import api, models, fields


class StockConfigSettings(models.TransientModel):
    _inherit = 'stock.config.settings'

    wave_behavior_on_confirm = fields.Selection(
        [
            (0, 'Close pickings in wave with creation of backorders '
                'for incomplete pickings'),
            (1, 'Close pickings in wave without creating backorders')
        ],
        string='Behavior on Confirm', default=0)

    @api.model
    def get_default_company_receiving_values(self, fields):
        company = self.env.user.company_id
        return {
            'wave_behavior_on_confirm': company.wave_behavior_on_confirm,
        }

    @api.multi
    def set_company_receiving_values(self):
        company = self.env.user.company_id
        company.wave_behavior_on_confirm = self.wave_behavior_on_confirm

