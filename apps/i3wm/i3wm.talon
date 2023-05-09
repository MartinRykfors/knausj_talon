# NOTE: If you want to use i3wm you must enable the tag settings.talon. i.e.: `tag(): user.i3wm`
os: linux
tag: user.i3wm
-
try work <number_small>: user.i3wm_switch_to_workspace(number_small)
try flip: user.i3wm_switch_to_workspace("back_and_forth")
try work star: user.i3wm_switch_to_workspace("next")
try work port: user.i3wm_switch_to_workspace("prev")

try port: user.i3wm_focus("left")
try star: user.i3wm_focus("right")
try climb: user.i3wm_focus("up")
try sink: user.i3wm_focus("down")
try kill kill: app.window_close()
try stacking: user.i3wm_layout("stacking")
try default: user.i3wm_layout()
try tabbed: user.i3wm_layout("tabbed")

try reload: user.i3wm_reload()
try restart: user.i3wm_restart()

# (full screen | scuba): user.i3wm_fullscreen()
# toggle floating: user.i3wm_float()
# focus floating: user.i3wm_focus("mode_toggle")
try center window: user.i3wm_move_position("center")
try parent: user.i3wm_focus("parent")
try child: user.i3wm_focus("child")

try wide: user.i3wm_widen()
try tall: user.i3wm_lengthen()
try (slim | narrow): user.i3wm_slim()
try short: user.i3wm_shorten()

try horizontal shell:
    user.i3wm_split("h")
    user.i3wm_shell()

try vertical shell:
    user.i3wm_split("v")
    user.i3wm_shell()

try shell: user.i3wm_shell()

try move [work] <number_small>:
    user.i3wm_move_to_workspace(number_small)
try move flip: user.i3wm_move_to_workspace("back_and_forth")
try move port: user.i3wm_move("left")
try move star: user.i3wm_move("right")
try move climb: user.i3wm_move("up")
try move sink: user.i3wm_move("down")

try horizontal: user.i3wm_split("h")
try vertical: user.i3wm_split("v")

try make scratch: user.i3wm_move("scratchpad")
try scratch: user.i3wm_show_scratchpad()
try next scratch:
    user.i3wm_show_scratchpad()
    user.i3wm_show_scratchpad()
try new scratch:
    user.i3wm_shell()
    sleep(200ms)
    user.i3wm_move("scratchpad")
    user.i3wm_show_scratchpad()

# these rely on the user settings for the mod key. see i3wm.py Actions class
try launch: user.i3wm_launch()
try launch <user.text>:
    user.i3wm_launch()
    sleep(100ms)
    insert("{text}")
try lock screen: user.i3wm_lock()
