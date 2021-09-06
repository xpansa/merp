# Copyright 2020 VentorTech OU
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0).

from odoo import api, models, fields


class StockWarehouse(models.Model):
    _inherit = 'stock.warehouse'

    is_internal = fields.Boolean(
        string='Is Internal Warehouse',
    )

    @api.model
    def create(self, vals):
        res = super(StockWarehouse, self).create(vals)
        res.update_users_calculated_warehouse()
        return res
    
    def update_users_calculated_warehouse(self):
        users = self.env['res.users'].with_context(active_test=False).search([
            ('allowed_warehouse_ids', '=', False), 
            ('login', 'not in', ['__system__', 'default', 'portaltemplate']), 
            ('share','=',False)])
        for user in users:
            user.sudo().calculated_warehouse_ids = [(4, self.id)]
