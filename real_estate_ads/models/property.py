from odoo import fields, models, api


class Property(models.Model):
    _name = 'estate.property'
    _description = 'Estate properties'

    name = fields.Char(string="Name")
    type_id = fields.Many2one('estate.property.type', string="Property Type")
    tag_ids = fields.Many2many('estate.property.tag', string="Tags")
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
        ('west', 'West')], default="north")

    offer_ids = fields.One2many('estate.property.offer', 'property_id')
    sales_id = fields.Many2one('res.users', string="Salesman")
    buyer_id = fields.Many2one('res.partner', string="Buyer")

    total_area = fields.Integer(string="Total Area")

    # calcule du total area avec onchange
    @api.onchange('living_area', 'garden_area')
    def _onchange_total_area(self):
        self.total_area = self.living_area + self.garden_area

    # @api.depends('living_area', 'garden_area')
    # def _compute_total_area(self):
    #     for rec in self:
    #         rec.total_area = rec.living_area + rec.garden_area
    #
    # total_area = fields.Integer(string="Total Area", compute=_compute_total_area)


class PropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Property Type'

    name = fields.Char(string="Property Type", required=True)


class PropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Property Tag"

    name = fields.Char(string="Property Tag", required=True)
