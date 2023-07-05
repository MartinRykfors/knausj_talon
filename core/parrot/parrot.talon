parrot(cluck):
	user.flash_notify('green')
	core.repeat_phrase(1)

parrot(tut):
	user.cancel_in_flight_phrase()
	user.flash_notify('red')
