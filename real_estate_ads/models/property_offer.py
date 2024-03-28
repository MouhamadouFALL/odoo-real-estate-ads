from odoo import models, fields, api, _
from datetime import timedelta
from odoo.exceptions import ValidationError

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

    _sql_constraints = [
        ('check_validity', 'CHECK(validity > 0)', 'The validity must be positive.')
    ]
    # Decorator model
    # @api.model
    # def _set_create_date(self):
    #     return fields.Date.today()
    
    # creation_date = fields.Date('Create Date', default=_set_create_date)
    creation_date = fields.Date('Create Date')

    @api.model_create_multi
    def create(self, values):
        for rec in self:
            if not rec.get('creation_date'):
                rec.creation_date = fields.Date.today()
        
        return super(PropertyOffer, self).create(values)



    @api.depends('creation_date', 'validity')
    def _compute_deadline(self):
        for rec in self:
            if rec.creation_date:
                rec.deadline = rec.creation_date + timedelta(days=rec.validity)
            else:
                rec.deadline = False

    def _inverse_dealdline(self):
        for rec in self:
            if rec.deadline and rec.creation_date:
                rec.validity = (rec.deadline - rec.creation_date).days
            else:
                rec.validity = False

    # suppression automatique des données (enregistrements)
    @api.autovacuum
    def _clean_offers(self):
        self.search([('status', '=', 'refused')]).unlink()

    # Les decorateurs permettent de faire des traitements sur les champs
        
    # décorateur @api.constrains()
        @api.constrains('validity')
        def _check_validity(self):
            for rec in self:
                if rec.deadline < rec.creation_date:
                    raise ValidationError(_('The deadline must be after the creation date.'))
                    # raise models.ValidationError(_('The deadline must be after the creation date.'))
                if rec.validity < 0:
                    raise ValidationError(_('The validity must be positive.'))
                    # raise models.ValidationError(_('The validity must be positive.'))

    ### Decorateurs
        # @api.depends_context()
        # @api.depends()
        # @api.onchanges()
        # @api.constrains()        
    

