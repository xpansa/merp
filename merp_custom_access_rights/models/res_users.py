from openerp import models, fields


class res_users(models.Model):
    _inherit = 'res.users'

    stock_location_id = fields.Many2one(
        'stock.location',
        string='Force Source Location for Instant Move',
        required=False,
    )
