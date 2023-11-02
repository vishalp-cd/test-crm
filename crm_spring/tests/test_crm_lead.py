# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo.addons.crm.tests.common import TestCrmCommon
from odoo.tests.common import users
from datetime import datetime

class TestCRMLead(TestCrmCommon):

	@classmethod
	def setUpClass(cls):
		super(TestCRMLead, cls).setUpClass()
		# cls.test_birthdate = datetime.strptime('18-09-1992', '%d-%m-%Y').date()
	@users('user_sales_manager')
	def test_birthdate(self):
		lead = self.env['crm.lead'].create({
			'name': 'Lead 1',
			'country_id': self.env.ref('base.us').id,
			'birthdate': '1992-09-18',
			'type': 'lead',
			'email_from': 'vishal@gmail.com',
			'phone': '2049014244'
		})

		self.assertEqual(lead.birthdate.strftime("%Y-%m-%d"), '1992-09-18')
		self.assertEqual(lead.age, '31')

