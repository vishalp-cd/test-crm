from odoo import models, fields, api, _, SUPERUSER_ID
from datetime import date, timedelta


class CrmLead(models.Model):
    _inherit = "crm.lead"


    birthdate = fields.Date(string="Birthdate")
    age = fields.Char(string="Age", compute="_compute_age")


    @api.depends('birthdate')
    def _compute_age(self):
        for res in self:
            cal_age = ''
            if res.birthdate:
                cal_age = (date.today() - res.birthdate) // timedelta(days=365.2425)
            res.age = cal_age



   
