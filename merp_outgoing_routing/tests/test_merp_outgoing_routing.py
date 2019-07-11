# Copyright 2019 VentorTech OU
# Part of Ventor modules. See LICENSE file for full copyright and licensing details.

from odoo.tests.common import TransactionCase
from datetime import datetime


class TestMerpOutgoingRouting(TransactionCase):

    def setUp(self):
        super(TestMerpOutgoingRouting, self).setUp()
        self.user = self.env['res.users'].create({
            'name': 'test_user',
            'login': 'test_user'
        })
        self.ventor_worker = self.env.ref('merp_custom_access_rights.ventor_role_wh_worker')
        self.ventor_worker.write({'users': [(4, self.user.id)]})
        self.inventory_manager = self.env.ref('stock.group_stock_manager')
        self.inventory_manager.write({'users': [(4, self.user.id)]})
        self.administration_settings = self.env.ref('base.group_system')
        self.administration_settings.write({'users': [(4, self.user.id)]})
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
            'location_dest_id': self.location_2.id,
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

    def test_sort_alphabet_a_z(self):
        outgoing_routing_strategy = 'name'
        outgoing_routing_order = 0
        self.check_sort(outgoing_routing_strategy, outgoing_routing_order)

    def test_sort_alphabet_z_a(self):
        outgoing_routing_strategy = 'name'
        outgoing_routing_order = 1
        self.check_sort(outgoing_routing_strategy, outgoing_routing_order)

    def test_sort_removal_priority_a_z(self):
        outgoing_routing_strategy = 'removal_prio'
        outgoing_routing_order = 0
        self.check_sort(outgoing_routing_strategy, outgoing_routing_order)

    def test_sort_removal_priority_z_a(self):
        outgoing_routing_strategy = 'removal_prio'
        outgoing_routing_order = 1
        self.check_sort(outgoing_routing_strategy, outgoing_routing_order)

    def check_sort(self, outgoing_routing_strategy, outgoing_routing_order):
        config = self.env['res.config.settings'].create({
            'outgoing_routing_strategy': outgoing_routing_strategy,
            'outgoing_routing_order': outgoing_routing_order
        })
        config.execute()
        picking = self.env['stock.picking'].sudo(self.user.id).browse(self.stock_picking.id)
        sort_move_lines = self.sort_by_locations(outgoing_routing_strategy, outgoing_routing_order)
        for line in range(len(picking.operations_to_pick)):
            self.assertEqual(picking.operations_to_pick[line].id, sort_move_lines[line].id)

    def sort_by_locations(self, outgoing_routing_strategy, outgoing_routing_order):
        move_lines = self.env['stock.move.line']
        for line in move_lines.browse([self.move_line_1.id, self.move_line_2.id, self.move_line_3.id, self.move_line_4.id]):
            if line.qty_done != line.product_qty:
                move_lines += line
        return move_lines.sorted(key=lambda line: getattr(line.location_id, outgoing_routing_strategy, 'None'), reverse=outgoing_routing_order)
