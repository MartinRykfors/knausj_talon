from talon import Context, Module, actions, app

ctx = Context()
ctx.matches = r"""
app: alacritty
"""


@ctx.action_class("edit")
class EditActions:
    def undo():
        pass
