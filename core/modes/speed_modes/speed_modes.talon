fast mode:
    mode.disable("user.slow_mode")
    mode.disable("user.medium_mode")
    mode.enable("user.fast_mode")

medium mode:
    mode.disable("user.slow_mode")
    mode.enable("user.medium_mode")
    mode.disable("user.fast_mode")

slow mode:
    mode.enable("user.slow_mode")
    mode.disable("user.medium_mode")
    mode.disable("user.fast_mode")

default mode:
    mode.disable("user.slow_mode")
    mode.disable("user.medium_mode")
    mode.disable("user.fast_mode")

speed check: user.speed_check()
