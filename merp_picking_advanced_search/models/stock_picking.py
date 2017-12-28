from openerp import models, api, fields


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    product_id_not_moved = fields.Many2many(
        'product.product', string='Product Not Moved',
        compute='_compute_products_not_moved', related=False, store=True)

    @api.one
    @api.depends('move_line_ids.qty_done')
    def _compute_products_not_moved(self):
        res = self.env['product.product']
        for operation in self.move_line_ids:
            if operation.qty_done < operation.product_qty:
                res += operation.product_id
        self.product_id_not_moved = res
