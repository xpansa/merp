# -*- coding: utf-8 -*-

from odoo.tests.common import TransactionCase


class TestCheckDefaultLocation(TransactionCase):

    def setUp(self):
        super(TestCheckDefaultLocation, self).setUp()
        self.location = self.env['stock.location'].create({
            'name': 'test_location'
        })
        self.user = self.env['res.users'].create({
            'name': 'test_user',
            'login': 'test_user',
            'email': 'test.user@email.com',
            'sel_groups_42_43_44': 42,
            'sel_groups_19_20': 20
        })
        self.company = self.env['res.company'].create({
            'name': 'test_company',
            'stock_inventory_location': self.location.id
        })
        self.product = self.env['product.template'].create({
            'name': 'new_product'
        })

    def test_check_stock_inventory_location(self):
        self.user.write({
            'company_id': self.company.id,
            'company_ids': [(4, self.company.id, 0)]
        })
        product = self.env['product.template'].sudo(self.user.id).browse(self.product.id)
        res = product.action_update_quantity_on_hand()
        self.assertEqual(self.location.id, res['context'].get('default_location_id'))

    def test_check_default_inventory_location(self):
        self.user.write({
            'default_inventory_location': self.location.id
        })
        product = self.env['product.template'].sudo(self.user.id).browse(self.product.id)
        res = product.action_update_quantity_on_hand()
        self.assertEqual(self.location.id, res['context'].get('default_location_id'))
