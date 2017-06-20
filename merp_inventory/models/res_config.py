from openerp import api, models, fields


class StockConfigSettings(models.TransientModel):
    _inherit = 'stock.config.settings'
 
    default_inventory_location = fields.Many2one('stock.location',
        string='Default Inventory Location')
    
    @api.model
    def get_default_inventory_values(self, fields):
        company = self.env.user.company_id
        return {
            'default_inventory_location': company.default_inventory_location.id,
        }

    @api.multi
    def set_company_inventory_values(self):
        company = self.env.user.company_id
        company.default_inventory_location = self.default_inventory_location
