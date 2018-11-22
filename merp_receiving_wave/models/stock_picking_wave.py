from odoo import api, models, _


class PickingWave(models.Model):
    _inherit = 'stock.picking.batch'

    @api.multi
    def done_incoming(self):
        picking_obj = self.env['stock.picking']
        behavior = self.env.user.company_id.wave_behavior_on_confirm
        
        # i.e. close pickings in wave with/without creating backorders
        for wave in self:
            for picking in wave.picking_ids:
                if picking.state in ('cancel', 'done'):
                    continue
                if picking.state == 'draft' \
                        or all([x.qty_done == 0.0
                                for x in picking.move_line_ids]):
                    # In draft or with no pack operations edited yet,
                    # remove from wave
                    picking.batch_id = False
                    continue
                picking.action_done()
                backorder_pick = self.env['stock.picking'].search([('backorder_id', '=', picking.id)])
                if backorder_pick:
                    backorder_pick.write({'batch_id': False})
                    if behavior == 1:
                        # i.e. close pickings in wave without creating backorders
                        backorder_pick.action_cancel()
                        picking.message_post(body=_("Back order <em>%s</em> <b>cancelled</b>.") % (backorder_pick.name))    

        return super(PickingWave, self).done()
