from openerp import models, fields, api


class StockPackOperation(models.Model):
    _inherit = 'stock.pack.operation'

    @api.model
    def _compute_operation_valid(self):
        res = True
        if hasattr(super(StockPackOperation, self), '_compute_operation_valid'):
            res &= super(StockPackOperation, self)._compute_operation_valid()
        res &= self.qty_done != self.product_qty
        # res &= self.state not in ('draft', 'cancel', 'done')
        return res
