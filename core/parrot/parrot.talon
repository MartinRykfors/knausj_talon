parrot(cluck):
	core.repeat_phrase(1)
	user.flash_repeat()

parrot(tut):
	user.flash_cancel()
	user.cancel_in_flight_phrase()
