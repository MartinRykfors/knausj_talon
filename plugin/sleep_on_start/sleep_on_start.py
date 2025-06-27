from talon import actions, app


def on_launch():
    actions.mode.enable("command")
    actions.mode.disable("dictation")
    actions.user.sleep()


app.register("launch", on_launch)
