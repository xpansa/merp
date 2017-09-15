from openerp import models, fields, api, exceptions, _


class PickingWave(models.Model):
    _inherit = 'stock.picking.wave'

    warehouse_id = fields.Many2one(
        'stock.warehouse', string='Related Warehouse',
        required=False)

    view_location_id = fields.Many2one(
        'stock.location', string='Related Warehouse View',
        related='warehouse_id.view_location_id', readonly=True)

    location_id = fields.Many2one(
        'stock.location', string='Related Location',
        required=False)

    picking_wave_type = fields.Many2one(
        'stock.picking.type', string='Wave Type',
        readonly=True, required=False)

    state = fields.Selection(selection_add=[('on_hold', 'On Hold')])

    @api.onchange('picking_ids')
    def onchange_picking_ids(self):
        if self.picking_ids:
            self.picking_wave_type = self.picking_ids[0].picking_type_id.id

    @api.multi
    def done(self):
        res = True
        if self.env.context.get('sub_done_called'):
            return super(PickingWave, self).done()
        ws_to_done = dict.fromkeys(['incoming', 'outgoing', 'internal'], self.env['stock.picking.wave'])
        for w in self:
            if w.picking_wave_type and \
               w.picking_wave_type.warehouse_id.pick_type_id.id == w.picking_wave_type.id and \
               w.picking_wave_type.warehouse_id.delivery_steps != 'ship_only':
                ws_to_done['outgoing'] += w
            elif w.picking_wave_type:
                ws_to_done[w.picking_wave_type.code] += w

        for code in ws_to_done.keys():
            #fetch {
            #     'incoming': list of stock.picking.wave,
            #     'outgoing': list of stock.picking.wave,
            #     'internal': list of stock.picking.wave
            # } and call done_*(incoming or internal or outgoing) dynamically
            sub_res = getattr(ws_to_done[code].with_context(sub_done_called=True), 'done_%s' % code)()
            if type(sub_res) == dict and sub_res.get('message', ''):
                res = sub_res['message']

        return res

    @api.multi
    def confirm_picking(self):
        # This method overried to avoid Exception "Nothing to check the availability for."
        # from module stock model stock.picking method action_assign
        # in case of wave contains pickings in different states
        # e.g. Ready to Transfer and Transferred
        self.write({'state': 'in_progress'})
        for wave in self:
            wave.picking_ids.filtered(lambda p: p.state == 'draft').action_confirm()
            for pick in wave.picking_ids:
                move_ids = pick.move_lines.filtered(lambda x: x.state not in ('draft', 'cancel', 'done'))
                if move_ids:
                    move_ids.action_assign()
                if not pick.pack_operation_ids:
                    pick.do_prepare_partial()
        return True

    @api.multi
    def done_incoming(self):
        # override this method in subclasses
        return super(PickingWave, self).done()        

    @api.multi
    def done_outgoing(self):
        # override this method in subclasses
        return super(PickingWave, self).done()

    @api.multi
    def done_internal(self):
        # override this method in subclasses
        return super(PickingWave, self).done()


class ProcurementGroup(models.Model):
    _inherit = 'procurement.group'

    picking_ids = fields.One2many('stock.picking', 'group_id', 'Pickings')


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    first_proc_picking = fields.Many2one('stock.picking',
        string='First picking from the same procurement group',
        readonly=True, store=True, compute='_compute_first_proc_picking')
    wave_location_id = fields.Many2one('stock.location', string='Wave Location',
        readonly=True, store=True, related='first_proc_picking.wave_id.location_id')

    @api.multi
    @api.depends('group_id', 'group_id.picking_ids')
    def _compute_first_proc_picking(self):
        for picking in self:
            res = self.search([('group_id', '=', picking.group_id.id)], order='id asc', limit=1)
            if res:
                picking.first_proc_picking = res[0]

    @api.model
    def create(self, vals):
        picking = super(StockPicking, self).create(vals)
        if not picking.wave_id:
            return picking
        if not picking.wave_id.picking_wave_type:
            picking.wave_id.write({'picking_wave_type': picking.picking_type_id.id})
        elif picking.wave_id.picking_wave_type.id != picking.picking_type_id.id:
            raise exceptions.Warning(_('''Picking cannot be added. 
                All pickings in the current picking wave should be from zone %s
                ''' % picking.wave_id.picking_wave_type.name))
        return picking

    @api.multi
    def write(self, vals):
        res = super(StockPicking, self).write(vals)
        for picking in self:
            if not picking.wave_id:
                continue
            if not picking.wave_id.picking_wave_type:
                picking.wave_id.write({'picking_wave_type': picking.picking_type_id.id})
            elif picking.wave_id.picking_wave_type.id != picking.picking_type_id.id:
                raise exceptions.Warning(_('''Picking cannot be added. 
                    All pickings in the current picking wave should be from zone %s
                    ''' % picking.wave_id.picking_wave_type.name))
        return res
