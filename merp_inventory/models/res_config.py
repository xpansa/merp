from openerp import api, models, fields


class StockConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    default_inventory_location = fields.Many2one('stock.location',
        string='Default Inventory Location',
        related='company_id.default_inventory_location')
