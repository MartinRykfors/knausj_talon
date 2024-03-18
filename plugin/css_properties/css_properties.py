from talon import Context, Module

mod = Module()
ctx = Context()

mod.list("css_property", desc="CSS properties")
mod.list("css_value", desc="CSS values")
mod.list("css_function", desc="CSS functions")