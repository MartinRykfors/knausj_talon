tag: user.splits
-
# split right:
#     user.split_window_right()
#     app.notify("deprecated")
split star: user.split_window_right()

# split left:
#     user.split_window_left()
#     app.notify("deprecated")
split port: user.split_window_left()

# split down:
#     user.split_window_down()
#     app.notify("deprecated")
split sink: user.split_window_down()

# split up:
#     user.split_window_up()
#     app.notify("deprecated")
split climb: user.split_window_up()

split (vertically | vertical): user.split_window_vertically()
split (horizontally | horizontal): user.split_window_horizontally()
split flip: user.split_flip()
split max: user.split_maximize()
split reset: user.split_reset()
split window: user.split_window()
split clear: user.split_clear()
split clear all: user.split_clear_all()
crossing: user.split_cycle()
split next: user.split_next()
split last: user.split_last()
split cycle: user.split_cycle()
go split <number>: user.split_number(number)
