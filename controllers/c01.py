# -*- coding: utf-8 -*-

def home():
	time = request.now
	form = FORM(
		INPUT(
			_type = "submit",
			_value = "Update Displayed Time",
			)
		)
	if (form.process().accepted):
		redirect(
			URL(
				a = "current_time",
				c = "c01",
				f = "home",
				)
			)
	return dict(
		form = form,
		time = time,
		)
