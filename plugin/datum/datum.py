from talon import Context, Module, actions, imgui, ui
from ...core.user_settings import track_csv_list

mod = Module()
mod.tag("datum_list_open", "tag for showing the datum list gui")
ctx = Context()

mod.list("datum", desc="List with common info to insert")
mod.list("datum_local", desc="List with local info to insert (not source controlled)")

@track_csv_list(
    "datum.csv",
    headers=("datum", "spoken"),
)
def on_update_datum(values):
    ctx.lists["self.datum"] = values

@track_csv_list(
    "datum.local.csv",
    headers=("datum", "spoken"),
)
def on_update_datum_local(values):
    ctx.lists["self.datum_local"] = values

@mod.capture(rule="( {user.datum} | {user.datum_local})")
def any_datum(m) -> str:
    "any datum"
    return str(m)


@imgui.open(y=ui.main_screen().y)
def gui(gui: imgui.GUI):
    gui.text("Global")
    gui.line()
    for key in sorted(ctx.lists["self.datum"].keys()):
        gui.text(key)
    gui.spacer()

    gui.text("Local")
    gui.line()
    for key in sorted(ctx.lists["self.datum_local"].keys()):
        gui.text(key)
    gui.spacer()

    if gui.button("datum hide"):
        actions.user.datum_list_toggle()


@mod.action_class
class Actions:
    def datum_list_toggle():
        """Toggle datum list gui"""
        if gui.showing:
            ctx.tags = []
            gui.hide()
        else:
            ctx.tags = ["user.datum_list_open"]
            gui.show()
