# Copyright 2019 VentorTech OU
# Part of Ventor modules. See LICENSE file for full copyright and licensing details.

from odoo.tests.common import TransactionCase
from datetime import datetime


class TestPickingAdvancedSearch(TransactionCase):

    def setUp(self):
        super(TestPickingAdvancedSearch, self).setUp()
        self.location_1 = self.env['stock.location'].create({
            'name': 'test_location_1',
            'removal_prio': 2
        })
        self.location_2 = self.env['stock.location'].create({
            'name': 'test_location_2',
            'removal_prio': 1
        })
        company = self.env.user.company_id
        picking_type = self.env['stock.picking.type'].search([], limit=1)
        self.stock_picking_1 = self.env['stock.picking'].create({
            'name': 'test_stock_picking_1',
            'location_id': self.location_1.id,
            'location_dest_id': self.location_2.id,
            'move_type': 'one',
            'company_id': company.id,
            'picking_type_id': picking_type.id
        })
        self.stock_picking_2 =self.env['stock.picking'].create({
            'name': 'test_stock_picking_2',
            'location_id': self.location_2.id,
            'location_dest_id': self.location_1.id,
            'move_type': 'one',
            'company_id': company.id,
            'picking_type_id': picking_type.id
        })
        self.stock_picking_3 = self.env['stock.picking'].create({
            'name': 'test_stock_picking_3',
            'location_id': self.location_2.id,
            'location_dest_id': self.location_1.id,
            'move_type': 'one',
            'company_id': company.id,
            'picking_type_id': picking_type.id
        })
        product_uom = company.currency_id
        products = self.env['product.template'].search([], limit=3)
        self.move_line_1 = self.env['stock.move.line'].create({
            'picking_id': self.stock_picking_1.id,
            'qty_done': 10.0,
            'location_id': self.location_1.id,
            'date': datetime.now(),
            'location_dest_id': self.location_2.id,
            'product_uom_qty': 20.0,
            'product_uom_id': product_uom.id,
            'product_id': products[0].id
        })
        self.move_line_2 = self.env['stock.move.line'].create({
            'picking_id': self.stock_picking_2.id,
            'qty_done': 25.0,
            'location_id': self.location_2.id,
            'date': datetime.now(),
            'location_dest_id': self.location_1.id,
            'product_uom_qty': 25.0,
            'product_uom_id': product_uom.id,
            'product_id': products[1].id
        })
        self.move_line_3 = self.env['stock.move.line'].create({
            'picking_id': self.stock_picking_3.id,
            'qty_done': 10.0,
            'location_id': self.location_2.id,
            'date': datetime.now(),
            'location_dest_id': self.location_1.id,
            'product_uom_qty': 10.0,
            'product_uom_id': product_uom.id,
            'product_id': products[2].id
        })
        self.move_line_4 = self.env['stock.move.line'].create({
            'picking_id': self.stock_picking_3.id,
            'qty_done': 10.0,
            'location_id': self.location_1.id,
            'date': datetime.now(),
            'location_dest_id': self.location_2.id,
            'product_uom_qty': 15.0,
            'product_uom_id': product_uom.id,
            'product_id': products[1].id
        })

    def test_check_product_not_moved(self):
        stock_pickings = self.env['stock.picking'].browse([self.stock_picking_1.id, self.stock_picking_2.id, self.stock_picking_3.id])
        for stock_picking in stock_pickings:
            products_not_moved = self.compute_products_not_moved(stock_picking)
            self.assertEqual(len(stock_picking.product_id_not_moved), len(products_not_moved))

    def compute_products_not_moved(self, stock_picking):
        stock_picking.ensure_one()
        products = self.env['product.product']
        for move_line in stock_picking.move_line_ids:
            if move_line.qty_done < move_line.product_qty:
                products += move_line.product_id
        return products
