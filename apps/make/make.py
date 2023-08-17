from talon import Context, Module

mod = Module()
ctx = Context()

mod.list("make_target", desc="Common make targets.")

ctx.lists["self.make_target"] = {
    "build": "build",
    "flake": "flake",
    "flake updated": "flake-updated",
    "flake up": "flake-updated",
    "test": "test",
}
