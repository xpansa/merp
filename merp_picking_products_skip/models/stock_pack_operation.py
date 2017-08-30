from openerp import models, fields


class StockPackOperation(models.Model):
    _inherit = 'stock.pack.operation'

    skipped = fields.Boolean('Skipped',
    	help='Products is skipped in pickings and picking waves')
