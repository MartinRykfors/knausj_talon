from talon import Module, actions

mod = Module()


@mod.action_class
class Actions:
    def sleep():
        """Sleep Talon"""
        actions.speech.disable()
        actions.user.notify_sleep()

    def wake():
        """Wake Talon"""
        actions.speech.enable()
        actions.user.notify_wake()
