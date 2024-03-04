from talon import Module, Context

mod = Module()
mod.list("custom_python_assertion", desc="custom python unittest assertion functions")

ctx = Context()
ctx.matches = "tag: user.work"
ctx.lists["user.custom_python_assertion"] = {
    "dispatched": "assertDispatched",
    "not dispatched signal": "assertNotDispatchedSignal",
    "is in": "assertIsIn",
    "sane event": "assertSaneEvent",
    "serializable": "assertSerializable",
    "published": "assertPublished",
    "not published": "assertNotPublished",
    "published signal": "assertPublishedSignal",
    "not published signal": "assertNotPublishedSignal",
    "message active": "assertMessageActive",
    "message inactive": "assertMessageInactive",
    "is armed": "assertIsArmed",
    "is disarmed": "assertIsDisarmed",
    "hidden": "assertHidden",
    "visible": "assertVisible",
    "get sensitive": "assertGetSensitive",
    "has role": "assertHasRole",
    "notification": "assertNotification",
    "signal updates widget": "assertSignalUpdatesWidget",
}


@ctx.capture(
    "user.python_assertion",
    rule="{user.python_assertion} | {user.custom_python_assertion}",
)
def python_assertion(m):
    return str(m)
