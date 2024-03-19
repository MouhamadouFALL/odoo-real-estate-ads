from odoo import fields, models


class Property(models.Model):
    _name = 'estate.property'

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
    postcode = fields.Char(string="Postcode")
    date_availability = fields.Date(string="Available from")
    expected_price = fields.Float(string="Expected price")
    best_offer = fields.Float(string="Best Offer")
    selling_price = fields.Float(string="Selling Price")
    bedrooms = fields.Integer(string="Bedrooms")
    living_area = fields.Integer(string="Living Area(sqm)")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Garage", default=False)
    garden = fields.Boolean(string="Gaden", default=False)
    garden_area = fields.Integer(string="Gaden Area")
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'south'),
        ('east', 'East'),
        ('west', 'West')], string="Garden Orientation")