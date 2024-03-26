from odoo import models, fields, api, _


class PropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate property Offer"

    price = fields.Float(string="Price")
    status = fields.Selection(
        [('accepted', 'Accepted'), ('refused', 'Refused')],
        string="Status"
    )
    partner_id = fields.Many2one('res.partner', stirng="Customer")
    property_id = fields.Many2one('estate.property', string="Property")