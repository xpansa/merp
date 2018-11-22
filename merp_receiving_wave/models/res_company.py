from odoo import models, fields


class Company(models.Model):
    _inherit = 'res.company'

    wave_behavior_on_confirm = fields.Selection(
        [
            (0, 'Close pickings in wave with creation of backorders '
                'for incomplete pickings'),
            (1, 'Close pickings in wave without creating backorders')
        ],
        string='Behavior on Confirm', default=0)
