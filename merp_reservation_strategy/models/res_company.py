# Copyright 2020 VentorTech OU
# Part of Ventor modules. See LICENSE file for full copyright and licensing details.

from odoo import models, fields


class Company(models.Model):
    _inherit = 'res.company'

    custom_reservation_strategy = fields.Boolean(
        string='Custom Reservation Strategy')
