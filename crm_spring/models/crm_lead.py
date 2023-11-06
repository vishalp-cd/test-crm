from odoo import models, fields, api, _, SUPERUSER_ID
from datetime import date, timedelta


class CrmLead(models.Model):
    _inherit = "crm.lead"


    birthdate = fields.Date(string="Birthdate")
    age = fields.Char(string="Age", compute="_compute_age")
    first_name = fields.Char(string="Name")
    last_name = fields.Char(string="Last Name")
    name = fields.Char(compute="_compute_name")


    @api.depends
    def _compute_name(self):
        for res in self:
            name = ""
            if res.first_name:
                name += res.first_name
            if res.last_name:
                name += "-" + res.last_name
            res.name = name


    @api.depends('birthdate')
    def _compute_age(self):
        for res in self:
            # import pdb
            # pdb.set_trace()
            cal_age = ''
            if res.birthdate:
                cal_age = (date.today() - res.birthdate) // timedelta(days=365.2425)
            res.age = str(cal_age - 3)



   
