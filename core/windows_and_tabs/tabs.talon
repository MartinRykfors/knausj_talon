tag: user.tabs
-
buffer (open | new): app.tab_open()
buffer (last | previous): app.tab_previous()
buffer next: app.tab_next()
buffer close: user.tab_close_wrapper()
buffer (reopen | restore): app.tab_reopen()
go buffer <number>: user.tab_jump(number)
go buffer final: user.tab_final()
buffer (duplicate | clone): user.tab_duplicate()
