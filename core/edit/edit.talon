
find it: edit.find()

find next: edit.find_next()

port: edit.left()

star: edit.right()

climb: edit.up()

sink: edit.down()

landing: edit.file_end()

cruise: edit.file_start()

# deleting
clear line: edit.delete_line()

clear word: edit.delete_word()

zoom in: edit.zoom_in()
zoom out: edit.zoom_out()
zoom reset: edit.zoom_reset()
scroll up: edit.page_up()
scroll down: edit.page_down()
copy that: edit.copy()
# cut that: edit.cut()
# (pace | paste) that: edit.paste()
# (pace | paste) enter:
#     edit.paste()
#     key(enter)
nope: edit.undo()
redo that: edit.redo()
# paste match: edit.paste_match_style()
disk it: edit.save()
disk all: edit.save_all()

slap: edit.line_insert_down()
slapper:
    edit.line_insert_down()
    edit.line_insert_down()
