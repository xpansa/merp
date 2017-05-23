from openerp import models, fields


class StockConfigSettings(models.TransientModel):
    _inherit = 'stock.config.settings'

    module_merp_custom_access_rights = fields.Boolean(
        'Enable Custom Access Rights for mERP Warehouse App')

    module_merp_receiving_wave = fields.Boolean('Enable Receiving Wave')
    module_merp_picking_wave = fields.Boolean('Enable Picking Wave')

