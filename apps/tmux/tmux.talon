tag: user.tmux
and tag:
-
tag(): user.splits

# external commands
multiplexer: "tmux "

multiplexer list: "tmux ls"

multiplexer new [<user.text>]:
    insert("tmux new -s ")
    insert(text or "")

multiplexer attach [<user.text>]:
    insert("tmux attach -t ")
    insert(text or "")

multiplexer attach [<user.text>] here:
    session = text or ""
    insert("tmux attach-session -c . -t {session}")

multiplexer kill [<user.text>]:
    insert("tmux kill-session -t ")
    insert(text or "")


# commands for when inside tmux
^multiplexer detach$:
    user.tmux_keybind("d")

mux sessions:
    user.tmux_keybind("s")

mux name session:
    user.tmux_keybind("$")

mux window new:
    user.tmux_keybind("c")

mux window <number>:
    user.tmux_keybind("{number}")

mux window previous:
    user.tmux_keybind("p")

mux window next:
    user.tmux_keybind("n")

mux window rename:
    user.tmux_keybind(",")

mux window close:
    user.tmux_keybind("&")

mux split horizontal:
    user.tmux_keybind("%")

mux split vertical:
    user.tmux_keybind('"')

mux pane next:
    user.tmux_keybind("o")

mux <user.arrow_key>:
    user.tmux_keybind("{arrow_key}")

mux pane close:
    user.tmux_keybind("x")

mux surf <number>:
    user.tmux_execute_command("join-pane -t :{number}")

mux bang:
    user.tmux_keybind("!")

mux pane numbers:
    user.tmux_execute_command("display-panes -d 0")