from talon import Module, actions
import subprocess

mod = Module()


@mod.action_class
class Actions:
    def sleep():
        """Sleep Talon"""
        actions.speech.disable()
        subprocess.check_call(("polybar-msg", "action", "#talon_on.module_hide"))
        subprocess.check_call(("polybar-msg", "action", "#talon_off.module_show"))

    def wake():
        """Sleep Talon"""
        actions.speech.enable()
        subprocess.check_call(("polybar-msg", "action", "#talon_off.module_hide"))
        subprocess.check_call(("polybar-msg", "action", "#talon_on.module_show"))
        actions.user.show_as_subtitle("󰒳  ")
