# Copyright 2020 VentorTech OU
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0).

from odoo import models, fields


class Company(models.Model):
    _inherit = 'res.company'

    outgoing_routing_strategy = fields.Selection(
        [
            # path should be valid for both stock pickings and quants
            ('location_id.removal_prio', 'Location removal priority'),
            ('location_id.name', 'Location name'),
            ('product_id.name', 'Product name'),
        ],
        string='Picking Strategy', default='location_id.name')

    outgoing_routing_order = fields.Selection(
        [
            ('0', 'Ascending (A-Z)'),
            ('1', 'Descending (Z-A)'),
        ],
        string='Picking Order', default='0')

    stock_reservation_strategy = fields.Selection(
        [
            ('base', 'By Picking Strategy'),
            ('quantity', 'By Quantity'),
            ('none', 'Default'),
        ],
        string='Reservation Strategy', default='base')
