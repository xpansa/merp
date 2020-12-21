# Copyright 2020 VentorTech OU
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0).

from odoo import models, fields, api, _
from odoo import http
from odoo.exceptions import Warning
import base64
import struct
import logging

_logger = logging.getLogger(__name__)

LOGOTYPE_W = 500
LOGOTYPE_H = 500


class VentorConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    logotype_file = fields.Binary('Ventor Application Logo File')
    logotype_name = fields.Char('Ventor Application Logo Filename')

    module_outgoing_routing = fields.Boolean(
        string='Outgoing Routing'
    )

    module_picking_wave = fields.Boolean(
        string='Picking Wave',
    )

    module_picking_products_skip = fields.Boolean(
        string='Smart Skip of Products',
    )

    module_instant_move = fields.Boolean(
        string='Instant Move',
    )

    add_barcode_on_view = fields.Boolean(
        string='Add a Barcode Field on a Stock Location Form',
    )

    base_version = fields.Char(
        string='Base Module Version',
        compute='_compute_base_version',
        store=False,
    )

    inventory_location = fields.Many2one(
        'stock.location',
        string='Default Inventory Location',
        readonly=False,
        related='company_id.stock_inventory_location'
    )

    @api.depends('company_id')
    def _compute_base_version(self):
        manifest = http.addons_manifest.get('ventor_base', None)
        version = manifest['version'].split('.')
        self.base_version = '.'.join(version[-3:])

    @api.model
    def get_values(self):
        res = super(VentorConfigSettings, self).get_values()

        conf = self.env['ventor.config'].sudo()

        logo = conf.get_param('logo.file', default=None)
        name = conf.get_param('logo.name', default=None)

        res.update({
            'logotype_file': logo or False,
            'logotype_name': name or False
        })

        view_with_barcode = self.env.ref('ventor_base.view_location_form_inherit_additional_barcode')
        res['add_barcode_on_view'] = view_with_barcode.active

        return res

    def set_values(self):
        res = super(VentorConfigSettings, self).set_values()

        conf = self.env['ventor.config'].sudo()

        self._validate_logotype()
        conf.set_param('logo.file', self.logotype_file or False)
        conf.set_param('logo.name', self.logotype_name or False)

        view_with_barcode = self.env.ref('ventor_base.view_location_form_inherit_additional_barcode')
        view_with_barcode.active = self.add_barcode_on_view

        return res

    def _validate_logotype(self):
        if not self.logotype_file:
            return False

        dat = base64.decodebytes(self.logotype_file)

        png = (dat[:8] == b'\211PNG\r\n\032\n' and (dat[12:16] == b'IHDR'))
        if not png:
            raise Warning(_('Apparently, the logotype is not a .png file.'))

        width, height = struct.unpack('>LL', dat[16:24])
        if int(width) < LOGOTYPE_W or int(height) < LOGOTYPE_H:
            raise Warning(_('The logotype can\'t be less than {}x{} px.'.format(LOGOTYPE_W, LOGOTYPE_H)))

        return True
