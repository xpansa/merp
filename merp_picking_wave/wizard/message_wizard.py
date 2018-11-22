from odoo import models, fields, api, _


class message_wizard(models.TransientModel):
    _name = 'message.wizard'

    message = fields.Text('Message')

    @api.model
    def default_get(self, fields):
        return {
            'message': self.env.context.get('message')
        }

    @api.multi
    def wizard_view(self):
        view = self.env.ref('merp_picking_wave.view_message_wizard')

        return {
            'name': _('Message'),
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'message.wizard',
            'views': [(view.id, 'form')],
            'view_id': view.id,
            'target': 'new',
            # 'res_id': self.ids[0],
            'context': self.env.context,
        }
