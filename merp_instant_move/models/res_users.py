from odoo import models, fields


class res_users(models.Model):
    _inherit = 'res.users'

    instant_add_more = fields.Boolean(
        string='Instant Move: \'add more\' automatically',
        help='Perform \'add more\' actions automatically',
        default=False,
    )
