# pylint: disable=missing-docstring
# Copyright 2020 VentorTech OU
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0).

{
    "name": "Mail Reply to Sender",
    "summary": "Emails in Odoo are sent to generic mail address",
    "version": "14.0.1.0.0",
    "category": "Tools",
    "website": "https://ventor.tech/",
    "author": "VentorTech OU",
    "license": "LGPL-3",
    "depends": [
        "sale",
        "base_automation",
    ],
    "data": [
        "data/auto_action.xml",
    ],
    "installable": True,
    "application": False,
}
