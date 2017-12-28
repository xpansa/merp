from openerp import api, models, fields


class User(models.Model):
    _inherit = 'res.users'
 
    default_inventory_location = fields.Many2one('stock.location',
        string='Default Inventory Location')
