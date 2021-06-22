# Copyright 2020 VentorTech OU
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0).

from . import models
from . import tests


def _auto_fill_settings(cr, registry):
    """
    This hook updates Ventor Settings in Operation Types
    """

    cr.execute(
        """
        UPDATE stock_picking_type
        SET
            change_destination_location = True,
            show_next_product = CASE code when 'incoming' THEN False ELSE True END
        """
    )
