from odoo import api, fields, models
from datetime import datetime
from odoo.exceptions import  ValidationError


class PartnerInherit(models.Model):

    _inherit = "res.partner"

    is_student = fields.Boolean("Is_Student", default=True)
    birth_date = fields.Date(required="1")

    @api.constrains('birth_date')
    def date_constrains(self):
        b_date = self.birth_date.strftime('%Y-%m-%d')
        d_date = datetime.today().strftime('%Y-%m-%d')
        if b_date >= d_date:
            raise ValidationError("Invalid DateOfBirth")


class InvInherit(models.Model):

    _inherit = "account.move"

    registration_id = fields.Many2one("registration.student")


