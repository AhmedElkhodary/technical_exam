from odoo import api, fields, models, _
from datetime import datetime, timedelta, date


class StudentRegistration(models.Model):

    _name = "registration.student"
    _description = "Registration Student"

    reg_code = fields.Char(string="Reg_Code", index="True", readonly="True", default=lambda self: 'New')
    student_id = fields.Many2one("res.partner", string="Student", required="True")
    phone = fields.Char(string="Phone", related="student_id.phone")
    date = fields.Date(string="Date", required='True')
    age = fields.Integer(string="Age", store=True, compute='_compute_age')
    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.company.currency_id, readonly=True)
    amount = fields.Monetary(string="Amount", required=True, index=True, default="0")
    state = fields.Selection([('draft', 'Draft'),
                              ('confirmed', 'Confirmed'),
                              ('invoiced', 'Invoiced'),
                              ('canceled', 'Canceled')
                              ], string='State', default='draft', readonly='True')


    @api.model
    def create(self, vals):
        vals['reg_code'] = self.env['ir.sequence'].next_by_code('registration.sequence')

        return super(StudentRegistration, self).create(vals)

    date_of_birth = fields.Date(related="student_id.birth_date")

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year - (
                            (today.month, today.day) < (rec.date_of_birth.month, rec.date_of_birth.day))
            else:
                rec.age = 0

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirmed'

    def action_cancel(self):
        for rec in self:
            rec.state = 'canceled'

    # def action_invoice(self):
    #     for rec in  self:
    #         rec.state = 'invoiced'


    def action_view_reg_invoices(self):
        return {
            'name': _('Invoices List'),
            'type': 'ir.actions.act_window',
            'view_mode': 'list,form',
            'context': {'default_res_partner_id': self.student_id},
            'res_model': 'account.move',
            'domain': [('partner_id.id', '=', self.student_id.id)],
            'target': 'current',
            # 'view_id': self.env.ref('account.view_move_form').id,
            # 'res_id': self.invoice_id.id,
        }

