from openerp import models, fields


class StockConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    module_merp_outgoing_routing = fields.Boolean(
        'Outgoing Routing')

    module_merp_custom_access_rights = fields.Boolean(
        'Custom Access Rights')

    module_merp_receiving_wave_access_rights = fields.Boolean(
        'Receiving Wave Access Rights')
    module_merp_receiving_wave = fields.Boolean(
        'Receiving Wave')

    module_merp_picking_wave_access_rights = fields.Boolean(
        'Picking Wave Access Rights')
    module_merp_picking_wave = fields.Boolean(
        'Picking Wave')

    module_merp_picking_products_skip = fields.Boolean(
        'Smart Skip of Products')

    module_merp_instant_move = fields.Boolean(
        'Instant Move')

    module_merp_inventory = fields.Boolean(
        'mERP Inventory')
