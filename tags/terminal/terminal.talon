tag: terminal
-
# tags should be activated for each specific terminal in the respective talon file
tag(): user.affirmative

lisa: user.terminal_list_directories()
lisa all: user.terminal_list_all_directories()
katie [<user.text>]: user.terminal_change_directory(text or "")
katie (up | upward | upwards): user.terminal_change_directory("..")
clear screen: user.terminal_clear_screen()
run last: user.terminal_run_last()
abort: user.terminal_kill_all()
history: user.terminal_history()
bang <user.number_string>:
    insert("!{number_string}")
