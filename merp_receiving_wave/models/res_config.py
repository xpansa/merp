from odoo import api, models, fields


class StockConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    wave_behavior_on_confirm = fields.Selection(
        [
            (0, 'Close pickings in wave with creation of backorders '
                'for incomplete pickings'),
            (1, 'Close pickings in wave without creating backorders')
        ],
        string='Behavior on Confirm', default=0,
        related='company_id.wave_behavior_on_confirm',
        readonly=False)
