from talon import Module, settings, app

mod = Module()


@mod.action_class
class Actions:
    def speed_check():
        """Print the current timeout"""
        app.notify("Speech timeout: {} s".format(settings.get("speech.timeout")))
