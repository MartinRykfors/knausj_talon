tag: user.tabs
-
(tab | buffer) (open | new): app.tab_open()
(tab | buffer) (last | previous): app.tab_previous()
(tab | buffer) next: app.tab_next()
(tab | buffer) close: user.tab_close_wrapper()
(tab | buffer) (reopen | restore): app.tab_reopen()
go (tab | buffer) <number>: user.tab_jump(number)
go (tab | buffer) final: user.tab_final()
(tab | buffer) duplicate: user.tab_duplicate()
