# Odoo:
from odoo import SUPERUSER_ID, _, api


def migrate(cr, version):
    """Update calculated_warehouse for users"""

    env = api.Environment(cr, SUPERUSER_ID, {})
    users = env['res.users'].with_context(active_test=False).search([
            ('allowed_warehouse_ids', '=', False), 
            ('login', 'not in', ['__system__', 'default', 'portaltemplate']), 
            ('share','=',False)
            ])
    warehouses = env["stock.warehouse"].search([])
    for user in users:
        user.calculated_warehouse_ids = [(6, 0, warehouses.ids)]
