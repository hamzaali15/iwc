from . import __version__ as app_version

app_name = "iwc"
app_title = "Integrated Waves Contracting"
app_publisher = "Hamza Ali"
app_description = "Integrated Waves Contracting"
app_email = "malikhamzaali48@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/iwc/css/iwc.css"
# app_include_js = "/assets/iwc/js/iwc.js"

# include js, css files in header of web template
# web_include_css = "/assets/iwc/css/iwc.css"
# web_include_js = "/assets/iwc/js/iwc.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "iwc/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
    "Timesheet" : "public/js/timesheet.js"
    }
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "iwc.utils.jinja_methods",
#	"filters": "iwc.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "iwc.install.before_install"
# after_install = "iwc.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "iwc.uninstall.before_uninstall"
# after_uninstall = "iwc.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "iwc.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
	"Salary Slip": "iwc.hook_events.salary_slip.OverrideSalarySlip"
}

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Timesheet": {
		"validate": "iwc.hook_events.timesheet.calculate_total_amounts",
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"iwc.tasks.all"
#	],
#	"daily": [
#		"iwc.tasks.daily"
#	],
#	"hourly": [
#		"iwc.tasks.hourly"
#	],
#	"weekly": [
#		"iwc.tasks.weekly"
#	],
#	"monthly": [
#		"iwc.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "iwc.install.before_tests"

# Overriding Methods
# ------------------------------
#
override_whitelisted_methods = {
	"hrms.payroll.doctype.salary_slip.salary_slip.make_salary_slip_from_timesheet": "iwc.hook_events.salary_slip.make_salary_slip_from_timesheet"
}
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "iwc.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["iwc.utils.before_request"]
# after_request = ["iwc.utils.after_request"]

# Job Events
# ----------
# before_job = ["iwc.utils.before_job"]
# after_job = ["iwc.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"iwc.auth.validate"
# ]
