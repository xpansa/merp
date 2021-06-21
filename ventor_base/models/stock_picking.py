from odoo import fields, models


class StockPickingType(models.Model):
    _inherit = 'stock.picking.type'

    confirm_source_location = fields.Boolean(
        string='Confirm source location',

    )

# Confirm source location
# The dot next to the field gets yellow color means user have to confirm it. User has to scan a barcode of source location
#
# Change source location
# User can change default source location to pick item from another location. Works only if \"Confirm source location\" setting is active
#
# Show next product
# Product field will show the next product to be picked. Use the setting during picking and delivery. It is recommended to disable the setting for the reception area
#
#
# Confirm product
# The dot next to the field gets yellow color means user have to confirm it. User has to scan a barcode of product
#
# Apply default lots
# If it\'s on, you don\'t need to scan lot number to confirm it. On receipts the app will create default Odoo lots and apply them to the product. On delivery zone you don\'t need to confirm lots and they will be taken Odoo by default
#
# Transfer more items
# Allows moving more items than expected (for example kg of meat, etc)
#
# Confirm destination location
# The dot next to the field gets yellow color means user have to confirm it. User has to scan a barcode of destination location
#
# Change destination location
# If this setting is active a user can change destination location while receiving to be placed at any available location
#
# Manage packages
# Scan source (destination) packages right after scanning source (destination) location. Use it if you move from one package to another or pick items from packages or pallets. Works only if package management settings is active on Odoo side
#
# Manage product owner
# Allow scan product owner. You can specify product owner while moving items. Working only with \"Consignment\" setting on Odoo side