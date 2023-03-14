from odoo import api, fields, models

class HospitalPersonal(models.Model):
    _name = "hospital.personal"
    _description = "Personal Records"
    name = fields.Char(string='Name',required = True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([('male','Male'),('female','Female')],string='Gender')