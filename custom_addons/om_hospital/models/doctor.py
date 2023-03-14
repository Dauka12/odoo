from odoo import api, fields, models

class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _description = "Doctor Records"
    name = fields.Char(string='Name',required = True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')

