from talon import speech_system, actions, cron, Module, Context
import subprocess


mod = Module()


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


def on_pre_phrase(phrase):
    words = phrase.get("phrase")

    if words and actions.speech.enabled():
        actions.user.clear_subtitles()
        actions.user.show_as_subtitle(" ".join(words))


speech_system.register("pre:phrase", on_pre_phrase)
