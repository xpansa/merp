from odoo import fields, models, api


class StockPickingType(models.Model):
    _inherit = "stock.picking.type"

    confirm_source_location = fields.Boolean(
        string="Confirm source location",
        help="The dot next to the field gets yellow color means user have "
             "to confirm it. User has to scan a barcode of source location"
    )

    change_source_location = fields.Boolean(
        string="Change source location",
        help="User can change default source location to pick item from another location. "
             "Works only if 'Confirm source location' setting is active"
    )

    show_next_product = fields.Boolean(
        string="Show next product",
        help="Product field will show the next product to be picked. "
             "Use the setting during picking and delivery. "
             "It is recommended to disable the setting for the reception area",
    )

    confirm_product = fields.Boolean(
        string="Confirm product",
        help="The dot next to the field gets yellow color means user have to confirm it. "
             "User has to scan a barcode of product"
    )

    apply_default_lots = fields.Boolean(
        string="Apply default lots",
        help="If it's on, you don't need to scan lot number to confirm it. "
             "On receipts the app will create default Odoo lots and apply them to the product. "
             "On delivery zone you don't need to confirm lots and "
             "they will be taken Odoo by default"
    )

    transfer_more_items = fields.Boolean(
        string="Transfer more items",
        help="Allows moving more items than expected (for example kg of meat, etc)"
    )

    confirm_destination_location = fields.Boolean(
        string="Confirm destination location",
        help="The dot next to the field gets yellow color means user have to confirm it. "
             "User has to scan a barcode of destination location"
    )

    change_destination_location = fields.Boolean(
        string="Change destination location",
        help="If this setting is active a user can change destination location "
             "while receiving to be placed at any available location",
    )

    manage_packages = fields.Boolean(
        string="Manage packages",
        help="Scan source (destination) packages right after scanning source (destination) "
             "location. Use it if you move from one package to another or pick items from "
             "packages or pallets. Works only if package management settings is active on Odoo side"
    )

    manage_product_owner = fields.Boolean(
        string="Manage product owner",
        help="Allow scan product owner. You can specify product owner while moving items. "
             "Working only with 'Consignment' setting on Odoo side"
    )

    @api.model
    def create(self, vals):
        if 'code' in vals:
            vals['show_next_product'] = vals['code'] != "incoming"
            vals['change_destination_location'] = True

        return super(StockPickingType, self).create(vals)

    @api.onchange('confirm_source_location')
    def _onchange_confirm_source_location(self):
        if not self.confirm_source_location:
            self.change_source_location = False

    def get_ventor_settings(self):
        return {
            "id": self.id,
            "name": self.name,
            "settings": {
                "confirm_source_location": self.confirm_source_location,
                "change_source_location": self.change_source_location,
                "show_next_product": self.show_next_product,
                "confirm_product": self.confirm_product,
                "apply_default_lots": self.apply_default_lots,
                "transfer_more_items": self.transfer_more_items,
                "confirm_destination_location": self.confirm_destination_location,
                "change_destination_location": self.change_destination_location,
                "manage_packages": self.manage_packages,
                "manage_product_owner": self.manage_product_owner,
            }
        }
