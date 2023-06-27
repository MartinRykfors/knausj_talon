from talon import Context, Module

mod = Module()
ctx = Context()

mod.list("fabric_command", desc="Fabric commands.")

ctx.lists["self.fabric_command"] = {
    "restart": "restart",
    "reboot": "reboot",
    "list": "ls",
    "activate": "activate",
    "deactivate": "deactivate",
    "push": "push",
    "build": "build",
    "define": "define",
    "undefine": "undefine",
    "log": "log",
    "select": "select",
    "virtual": "vnc",
    "shell": "ssh",
}

@mod.capture(rule="{user.fabric_command}+")
def fabric_commands(m) -> str:
    """A non-empty sequence of fabric command arguments."""
    return " ".join(m.fabric_command_list)
