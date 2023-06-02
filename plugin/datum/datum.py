from talon import Context, Module
from ...core.user_settings import get_list_from_csv

mod = Module()
ctx = Context()

mod.list("datum", desc="List with common info to insert")
mod.list("datum_local", desc="List with local info to insert (not source controlled)")

ctx.lists["self.datum"] = get_list_from_csv(
    "datum.csv", headers=("datum", "spoken"), default={}
)

ctx.lists["self.datum_local"] = get_list_from_csv(
    "datum.local.csv", headers=("datum", "spoken"), default={}
)


@mod.capture(rule="( {user.datum} | {user.datum_local})")
def any_datum(m) -> str:
    "any datum"
    return str(m)
