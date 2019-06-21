# Copyright 2019 VentorTech OU
# Part of Ventor modules. See LICENSE file for full copyright and licensing details.

from odoo.tests.common import TransactionCase
from datetime import datetime


class TestMerpPickingWaveBase(TransactionCase):

    def setUp(self):
        super(TestMerpPickingWaveBase, self).setUp()
        self.location_1 = self.env['stock.location'].create({
            'name': 'test_location_1',
            'removal_prio': 2
        })
        self.location_2 = self.env['stock.location'].create({
            'name': 'test_location_2',
            'removal_prio': 3
        })
        self.location_3 = self.env['stock.location'].create({
            'name': 'test_location_3',
            'removal_prio': 1
        })
        self.location_4 = self.env['stock.location'].create({
            'name': 'test_location_4',
            'removal_prio': 4
        })
        company = self.env.user.company_id
        picking_type = self.env['stock.picking.type'].search([], limit=1)
        self.stock_picking = self.env['stock.picking'].create({
            'name': 'test_stock_picking',
            'location_id': self.location_1.id,
            'location_dest_id': self.location_2.id,
            'move_type': 'one',
            'company_id': company.id,
            'picking_type_id': picking_type.id
        })
        self.picking_batch = self.env['stock.picking.batch'].create({
            'name': 'test_stock_picking_batch',
            'picking_ids': [(4, self.stock_picking.id, 0)]
        })
        product_uom = company.currency_id
        products = self.env['product.template'].search([], limit=4)
        self.move_line_1 = self.env['stock.move.line'].create({
            'picking_id': self.stock_picking.id,
            'qty_done': 1.0,
            'location_id': self.location_1.id,
            'date': datetime.now(),
            'location_dest_id': self.location_2.id,
            'product_uom_qty': 20.0,
            'product_uom_id': product_uom.id,
            'product_id': products[0].id
        })
        self.move_line_2 = self.env['stock.move.line'].create({
            'picking_id': self.stock_picking.id,
            'qty_done': 2.0,
            'location_id': self.location_2.id,
            'date': datetime.now(),
            'location_dest_id': self.location_3.id,
            'product_uom_qty': 25.0,
            'product_uom_id': product_uom.id,
            'product_id': products[1].id
        })
        self.move_line_3 = self.env['stock.move.line'].create({
            'picking_id': self.stock_picking.id,
            'qty_done': 3.0,
            'location_id': self.location_3.id,
            'date': datetime.now(),
            'location_dest_id': self.location_1.id,
            'product_uom_qty': 15.0,
            'product_uom_id': product_uom.id,
            'product_id': products[2].id
        })
        self.move_line_4 = self.env['stock.move.line'].create({
            'picking_id': self.stock_picking.id,
            'qty_done': 10.0,
            'location_id': self.location_4.id,
            'date': datetime.now(),
            'location_dest_id': self.location_2.id,
            'product_uom_qty': 10.0,
            'product_uom_id': product_uom.id,
            'product_id': products[3].id
        })

    def test_related_pack_operations(self):
        picking_batch = self.env['stock.picking.batch'].browse(self.picking_batch.id)
        related_pack_operations = self.calculate_related_pack_operations()
        self.assertEqual(len(picking_batch.related_pack_operations), len(related_pack_operations))

    def test_operations_to_pick(self):
        picking_batch = self.env['stock.picking.batch'].browse(self.picking_batch.id)
        operations_to_pick = self.calculate_operations_to_pick()
        self.assertEqual(len(picking_batch.operations_to_pick), len(operations_to_pick))

    def test_sort_operations_to_pick(self):
        picking_batch = self.env['stock.picking.batch'].browse(self.picking_batch.id)
        operations_to_pick = self.calculate_operations_to_pick()
        sorted_operations_to_pick = self.sort_operations_to_pick(operations_to_pick)
        for i in range(len(picking_batch.operations_to_pick)):
            self.assertEqual(picking_batch.operations_to_pick[i].id, sorted_operations_to_pick[i].id)

    def calculate_related_pack_operations(self):
        picking_batch = self.env['stock.picking.batch'].browse(self.picking_batch.id)
        res = self.env['stock.move.line']
        for picking in picking_batch.picking_ids:
            for move_line in picking.move_line_ids:
                res += move_line
        return res

    def calculate_operations_to_pick(self):
        picking_batch = self.env['stock.picking.batch'].browse(self.picking_batch.id)
        res = self.env['stock.move.line']
        for picking in picking_batch.picking_ids:
            for move_line in picking.operations_to_pick:
                res += move_line
        return res

    def sort_operations_to_pick(self, operations_to_pick):
        strategy = self.env.user.company_id.outgoing_routing_strategy
        strategy_order = self.env.user.company_id.outgoing_routing_order
        return operations_to_pick.sorted(key=lambda r: getattr(r.location_id, strategy, 'None'), reverse=strategy_order)
