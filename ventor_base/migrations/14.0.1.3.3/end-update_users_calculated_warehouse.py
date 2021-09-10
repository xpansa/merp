# Odoo:
from odoo import SUPERUSER_ID, _, api


def migrate(cr, version):
    """Update calculated_warehouse for users"""

    env = api.Environment(cr, SUPERUSER_ID, {})
    users = env['res.users'].with_context(active_test=False).search([
            ('allowed_warehouse_ids', '=', False),
            ('share', '=', False)
            ])
    warehouses = env["stock.warehouse"].with_context(active_test=False).search([])
    for user in users:
        user.allowed_warehouse_ids = [(6, 0, warehouses.ids)]
