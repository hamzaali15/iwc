frappe.ui.form.on('Timesheet', {
	validate: function (frm, cdt, cdn) {
		var d = locals[cdt][cdn];
		var total_working_hours = 0;
		var total_overtime_hours = 0;
		frm.set_value("total_hours", 0);
		$.each(frm.doc.time_logs, function(i, d){
			if (d.hours) {
				total_working_hours += d.hours;
			}
			if (d.ot) {
				total_overtime_hours += d.ot;
			}
			frm.set_value("regular_hours", total_working_hours);
			frm.set_value("ot_hours", total_overtime_hours);
			if(frm.doc.regular_hours && frm.doc.ot_hours) {
				frm.set_value("total_hours", frm.doc.regular_hours+frm.doc.ot_hours);
			}
			else if(frm.doc.regular_hours && !frm.doc.ot_hours) {
				frm.set_value("total_hours", frm.doc.regular_hours);
			}
			else if(!frm.doc.regular_hours && frm.doc.ot_hours) {
				frm.set_value("total_hours", frm.doc.ot_hours);
			}
		});
	}
});

frappe.ui.form.on('Timesheet Detail', {
	hours: function(frm, cdt, cdn) {
		var d = locals[cdt][cdn];
		var total_working_hours = 0;
		$.each(frm.doc.time_logs, function(i, d){
			if (d.hours) {
				total_working_hours += d.hours;
			}
			frm.set_value("regular_hours", total_working_hours);
			if(frm.doc.regular_hours && frm.doc.ot_hours) {
				frm.set_value("total_hours", frm.doc.regular_hours+frm.doc.ot_hours);
			}
			if(frm.doc.regular_hours && !frm.doc.ot_hours) {
				frm.set_value("total_hours", frm.doc.regular_hours);
			}
			if(!frm.doc.regular_hours && frm.doc.ot_hours) {
				frm.set_value("total_hours", frm.doc.ot_hours);
			}
		});
	},
	ot: function(frm, cdt, cdn) {
		var d = locals[cdt][cdn];
		var total_overtime_hours = 0;
		$.each(frm.doc.time_logs, function(i, d){
			if (d.ot) {
				total_overtime_hours += d.ot;
			}
			frm.set_value("ot_hours", total_overtime_hours);
			if(frm.doc.regular_hours && frm.doc.ot_hours) {
				frm.set_value("total_hours", frm.doc.regular_hours+frm.doc.ot_hours);
			}
			if(frm.doc.regular_hours && !frm.doc.ot_hours) {
				frm.set_value("total_hours", frm.doc.regular_hours);
			}
			if(!frm.doc.regular_hours && frm.doc.ot_hours) {
				frm.set_value("total_hours", frm.doc.ot_hours);
			}
		});
	},
});