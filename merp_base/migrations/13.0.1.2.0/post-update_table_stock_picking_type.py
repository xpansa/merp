def migrate(cr, version):
    """
    Updates Ventor Settings in Operation Types
    """

    cr.execute(
        """
        UPDATE stock_picking_type
        SET
            change_destination_location = True,
            show_next_product = CASE code when 'incoming' THEN False ELSE True END
        """
    )
