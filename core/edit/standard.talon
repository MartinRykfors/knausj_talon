zoom in: edit.zoom_in()
zoom out: edit.zoom_out()
zoom reset: edit.zoom_reset()
scroll up: edit.page_up()
scroll down: edit.page_down()
copy that: edit.copy()
cut that: edit.cut()
(pace | paste) that: edit.paste()
(pace | paste) enter:
    edit.paste()
    key(enter)
(undo that | nope): edit.undo()
redo that: edit.redo()
paste match: edit.paste_match_style()
file save: edit.save()
file save (all | everything): edit.save_all()
padding: user.insert_between(" ", " ")
padding <user.symbol_key>+:
    insert(" ")
    user.insert_many(symbol_key_list)
    insert(" ")
slap: edit.line_insert_down()
slapper:
    edit.line_insert_down()
    edit.line_insert_down()

slow mode: mode.enable("user.slow")
fast mode: skip()

terminal repeat:
    user.switcher_focus("Terminal")
    sleep(300ms)
    user.terminal_run_last()
