# Copyright 2020 VentorTech OU
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0).

from . import models
from odoo import api, SUPERUSER_ID

def _post_init_hook(cr, registry):
    """
    This hook updates Ventor Settings in Operation Types
    And adds to all users to Ventor - Administrator Role
    """
    env = api.Environment(cr, SUPERUSER_ID, {})

    all_stock_inventory_ids = env["stock.inventory"].search(
        [
            ("location_ids", "!=", False),
        ]
    )
    for stock_inv in all_stock_inventory_ids:
        warehouse_ids = stock_inv.location_ids.mapped("warehouse_id")
        if len(warehouse_ids) == 1:
            stock_inv.warehouse_id = warehouse_ids

    users_model = env['res.users']

    values = [(4, user.id) for user in users_model.search([])]
    env.ref('ventor_base.ventor_role_admin').users = values

    cr.execute(
        """
        UPDATE stock_picking_type
        SET
            change_destination_location = True,
            show_next_product = CASE code when 'incoming' THEN False ELSE True END
        """
    )
