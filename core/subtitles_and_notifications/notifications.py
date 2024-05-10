from talon import speech_system, actions, cron, Module, Context, app, registry, scope
import subprocess


mod = Module()
last_known_sleeping = None


@mod.action_class
class Actions:
    def flash_cancel():
        """Flash cancel symbol"""

    def flash_repeat():
        """Flash repeat symbol"""

    def show_as_subtitle(text: str):
        """Display text in the subtitle bar"""

    def clear_subtitles():
        """Clear the subtitle bar"""

    def notify_sleep():
        """Notify Talon asleep"""

    def notify_wake():
        """Notify Talon awake"""

    def notify_deprecated():
        """Notify usage of deprecated function"""


def on_pre_phrase(phrase):
    words = phrase.get("phrase")

    if words and actions.speech.enabled():
        actions.user.clear_subtitles()
        actions.user.show_as_subtitle(" ".join(words))


def on_update_contexts():
    global last_known_sleeping
    modes = scope.get("mode")
    is_sleeping = "sleep" in modes
    if last_known_sleeping is None:
        last_known_sleeping = is_sleeping
        return

    if is_sleeping != last_known_sleeping:
        last_known_sleeping = is_sleeping
        if last_known_sleeping:
            actions.user.notify_sleep()
        else:
            actions.user.notify_wake()


def on_ready():
    registry.register("update_contexts", on_update_contexts)


speech_system.register("pre:phrase", on_pre_phrase)
app.register("ready", on_ready)
