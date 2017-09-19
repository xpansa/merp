# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2017 Xpansa Group (<http://xpansa.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields, api


class StockLocation(models.Model):
    _inherit = "stock.location"

    removal_prio = fields.Integer(
        string='Removal Strategy Priority',
        default=0
    )

    strategy_sequence = fields.Integer(
        string='Sequence',
        help='Sequence based on warehouse location outgoing strategy/order',
        compute='_compute_outgoing_strategy_sequence',
        store=False
    )

    @api.multi
    def _compute_outgoing_strategy_sequence(self):

        strategy = self.env.user.company_id.outgoing_routing_strategy
        strategy_order = self.env.user.company_id.outgoing_routing_order

        if not strategy in self:
        	return

        order = '%s %s' % (strategy, ['asc', 'desc'][strategy_order])
    	res = self.search([], order=order)
    	for sequence, location in enumerate(res):
    		location.strategy_sequence = sequence
