# Copyright 2020 VentorTech OU
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0).

from odoo import models


class ProductTemplate(models.Model):
    _name = 'product.template'
    _inherit = ['product.template', 'stock.location.mixin']

    def action_update_quantity_on_hand(self):
        res = super(ProductTemplate, self).action_update_quantity_on_hand()
        default_location_id = self._get_default_location_warehouse()
        if default_location_id:
            res['context'].update({'default_location_id': default_location_id})
        return res
