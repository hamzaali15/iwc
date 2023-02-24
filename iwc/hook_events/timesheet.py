# Copyright (c) 2022, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt


from frappe.utils import flt


def calculate_total_amounts(self, method):
	self.ot_hours = 0.0
	self.regular_hours = 0.0
	self.total_hours = 0.0
	for d in self.get("time_logs"):
		self.ot_hours += flt(d.ot)
		self.regular_hours += flt(d.hours)
	self.total_hours += flt(self.ot_hours if self.ot_hours else 0 + self.regular_hours if self.regular_hours else 0)