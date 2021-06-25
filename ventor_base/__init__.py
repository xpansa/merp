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
