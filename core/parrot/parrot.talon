parrot(cluck):
	user.notify('repeat')
	core.repeat_phrase(1)

parrot(tut):
	user.cancel_in_flight_phrase()
	user.notify('cancel')
