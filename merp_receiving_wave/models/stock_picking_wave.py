from openerp import models, fields, api


class PickingWave(models.Model):
    _inherit = 'stock.picking.wave'

    @api.multi
    def done(self):
        picking_obj = self.env['stock.picking']
        create_backorder = \
            self.env.user.company_id.wave_behavior_on_confirm == 0

        if not create_backorder:
            # i.e. close pickings in wave without creating backorders
            return super(PickingWave, self).done()

        # else close pickings in wave with creation of backorders for incomplete pickings
        for wave in self:
            for picking in wave.picking_ids:
                if picking.state in ('cancel', 'done'):
                    continue
                if picking.state == 'draft' \
                        or all([x.qty_done == 0.0
                                for x in picking.pack_operation_ids]):
                    # In draft or with no pack operations edited yet,
                    # remove from wave
                    picking.wave_id = False
                    continue

                for pack in picking.pack_operation_ids:
                    if pack.qty_done > 0:
                        pack.product_qty = pack.qty_done
                    else:
                        pack.unlink()
                picking.do_transfer()

                # Find backorder and remove it from wave
                back_orders = picking_obj.search([
                    ('backorder_id', '=', picking.id)])
                back_orders.write({'wave_id': False})

        return super(PickingWave, self).done()
