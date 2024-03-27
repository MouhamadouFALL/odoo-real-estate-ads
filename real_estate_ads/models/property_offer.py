from odoo import models, fields, api, _
from datetime import timedelta

class PropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate property Offer"

    price = fields.Float(string="Price")
    status = fields.Selection(
        [('accepted', 'Accepted'), ('refused', 'Refused')],
        string="Status"
    )
    partner_id = fields.Many2one('res.partner', string="Customer")
    property_id = fields.Many2one('estate.property', string="Property")
    validity = fields.Integer(string="Validity")
    deadline = fields.Date(string="Deadline", compute='_compute_deadline', inverse='_inverse_dealdline')
    creation_date = fields.Date('Create Date')

    @api.depends('creation_date', 'validity')
    def _compute_deadline(self):
        for rec in self:
            if rec.creation_date:
                rec.deadline = rec.creation_date + timedelta(days=rec.validity)
            else:
                rec.deadline = False

    def _inverse_dealdline(self):
        for rec in self:
            rec.validity = (rec.deadline - rec.creation_date).days

