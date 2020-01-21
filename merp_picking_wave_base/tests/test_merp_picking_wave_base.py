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
        product_uom = self.env['uom.uom'].search([], limit=1, order='id')
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
        self.assertEqual(len(self.picking_batch.related_pack_operations), 4)

    def test_operations_to_pick(self):
        self.assertEqual(len(self.picking_batch.operations_to_pick), 3)

    def test_sort_alphabet_a_z(self):
        outgoing_routing_strategy = 'name'
        outgoing_routing_order = '0'
        self.set_way_outgoing_routing(outgoing_routing_strategy, outgoing_routing_order)

        locations_name = self.stock_picking.mapped('operations_to_pick.location_id.name')
        self.assertEqual(locations_name[0], 'test_location_1')
        self.assertEqual(locations_name[1], 'test_location_2')
        self.assertEqual(locations_name[2], 'test_location_3')

    def test_sort_alphabet_z_a(self):
        outgoing_routing_strategy = 'name'
        outgoing_routing_order = '1'
        self.set_way_outgoing_routing(outgoing_routing_strategy, outgoing_routing_order)

        locations_name = self.stock_picking.mapped('operations_to_pick.location_id.name')
        self.assertEqual(locations_name[0], 'test_location_3')
        self.assertEqual(locations_name[1], 'test_location_2')
        self.assertEqual(locations_name[2], 'test_location_1')

    def test_sort_removal_priority_a_z(self):
        outgoing_routing_strategy = 'removal_prio'
        outgoing_routing_order = '0'
        self.set_way_outgoing_routing(outgoing_routing_strategy, outgoing_routing_order)

        locations_removal_prio = self.stock_picking \
            .mapped('operations_to_pick.location_id.removal_prio')
        self.assertEqual(locations_removal_prio[0], 1)
        self.assertEqual(locations_removal_prio[1], 2)
        self.assertEqual(locations_removal_prio[2], 3)

    def test_sort_removal_priority_z_a(self):
        outgoing_routing_strategy = 'removal_prio'
        outgoing_routing_order = '1'
        self.set_way_outgoing_routing(outgoing_routing_strategy, outgoing_routing_order)

        locations_removal_prio = self.stock_picking \
            .mapped('operations_to_pick.location_id.removal_prio')
        self.assertEqual(locations_removal_prio[0], 3)
        self.assertEqual(locations_removal_prio[1], 2)
        self.assertEqual(locations_removal_prio[2], 1)

    def set_way_outgoing_routing(self, outgoing_routing_strategy, outgoing_routing_order):
        config = self.env['res.config.settings'].create({
            'outgoing_routing_strategy': outgoing_routing_strategy,
            'outgoing_routing_order': outgoing_routing_order
        })
        config.execute()
