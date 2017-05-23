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

from openerp import api, models


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    @api.model
    def sort_printer_picking_list(self, pack_operation_ids):
        """ sort list of pack operations by configured field
        """
        strategy = self.env.user.company_id.outgoing_routing_strategy
        strategy_order = self.env.user.company_id.outgoing_routing_order

        return pack_operation_ids.sorted(
            key=lambda r: getattr(r.location_id, strategy, 'None'),
            reverse=strategy_order
        )
