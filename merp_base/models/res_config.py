# Copyright 2019 VentorTech OU
# Part of Ventor modules. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api
from odoo import http

import logging
_logger = logging.getLogger(__name__)


class StockConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    module_merp_outgoing_routing = fields.Boolean(
        string='Outgoing Routing'
    )

    module_merp_custom_access_rights = fields.Boolean(
        string='Custom Access Rights',
    )

    module_merp_picking_wave = fields.Boolean(
        string='Picking Wave',
    )

    module_merp_picking_products_skip = fields.Boolean(
        string='Smart Skip of Products',
    )

    module_merp_instant_move = fields.Boolean(
        string='Instant Move',
    )

    module_merp_custom_logotype = fields.Boolean(
        string='Use Custom Logo',
    )

    merp_version = fields.Char(
        string='Ventor/mERP Version',
        compute='_compute_merp_version',
        store=False,
    )

    module_two_factor_otp_auth = fields.Boolean(
        string='Use Two Factor Authentication',
    )

    module_merp_default_locations = fields.Boolean(
        string='Use Advanced Locations',
    )

    @api.depends('company_id')
    def _compute_merp_version(self):
        self.env.cr.execute(
            "SELECT latest_version FROM ir_module_module WHERE name='merp_base'"
        )
        result = self.env.cr.fetchone()
        full_version = result and result[0]
        split_value = full_version and full_version.split('.')
        self.merp_version = split_value and '.'.join(split_value[-3:])
