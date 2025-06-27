from talon import Module, actions

mod = Module()


@mod.action_class
class Actions:
    def sleep():
        """Sleep Talon"""
        actions.speech.disable()

    def wake():
        """Wake Talon"""
        actions.speech.enable()
