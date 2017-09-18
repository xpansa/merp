from openerp import models, fields, api, _


class PickingWave(models.Model):
    _inherit = 'stock.picking.wave'

    @api.multi
    def done_outgoing(self):
        picking_obj = self.env['stock.picking']
        message_obj = self.env['message.wizard']
        behavior = self.env.user.company_id.outgoing_wave_behavior_on_confirm

        if behavior == 1:
            # i.e. close pickings in wave without creating backorders
            return super(PickingWave, self).done()

        elif behavior == 0:
            # i.e. close pickings in wave with creation of backorders for incomplete pickings
            for wave in self:
                for picking in wave.picking_ids:
                    if picking.state in ('cancel', 'done'):
                        continue
                    if picking.state == 'draft' \
                            or all([x.qty_done == 0.0
                                    for x in picking.pack_operation_product_ids]):
                        # In draft or with no pack operations edited yet,
                        # remove from wave
                        picking.wave_id = False
                        continue
                    if not picking.pack_operation_product_ids:
                        picking.do_prepare_partial()
                    for pack in picking.pack_operation_product_ids.with_context(no_recompute=True):
                        pack.product_qty = pack.qty_done
                    picking.do_transfer()

                    # Find backorder and remove it from wave
                    back_orders = picking_obj.search([
                        ('backorder_id', '=', picking.id)])
                    back_orders.write({'wave_id': False})
            return super(PickingWave, self).done()

        elif behavior == 2:
            # i.e. move wave to on hold if not all pickings are confirmed
            message = ''
            on_hold = False
            for wave in self:
                for picking in wave.picking_ids:
                    if picking.state in ('cancel', 'done'):
                        continue
                    elif picking.state != 'assigned':
                        break
                    else:
                        if not picking.pack_operation_product_ids:
                            picking.do_prepare_partial()
                        all_processed = True
                        if picking.pack_operation_product_ids.filtered(lambda o: o.qty_done < o.product_qty):
                            on_hold = True
                        else:
                            picking.do_transfer()

                if on_hold:
                    wave.write({'state': 'on_hold'})
                    message = _('''
Not all products were found in wave pickings.
Wave is moved to "On Hold" for manual processing.
                    ''')
                elif wave.picking_ids:
                    super(PickingWave, self).done()
                    message = _('All pickings were confirmed!')

            if message:
                return {
                    'message': message_obj.with_context(message=message).wizard_view()
                }
            else:
                return True


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    @api.model
    def search_pickings_to_pick(self, name, warehouse_id):
        warehouse = self.env['stock.warehouse'].browse(warehouse_id)
        if warehouse.delivery_steps == 'ship_only':
            picking_type_id = warehouse.out_type_id.id
        else:
            picking_type_id = warehouse.pick_type_id.id
        return self.search_read(domain=[
            ('picking_type_id', '=', picking_type_id),
            ('state', 'in', ('assigned', 'partially_available')),
            '|',
            ('name', '=', name),
            ('origin','=', name)])
