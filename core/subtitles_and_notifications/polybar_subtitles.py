from talon import speech_system, actions, cron, Module
import subprocess


mod = Module()

clear_subtitle = None
clear_cancel = None
clear_repeat = None


@mod.action_class
class Actions:
    def flash_cancel():
        """Flash cancel symbol"""
        global clear_cancel

        if clear_cancel:
            cron.cancel(clear_cancel)
            clear_cancel = None
        actions.user.clear_subtitle()
        subprocess.check_call(("polybar-msg", "action", "#cancel.module_show"))
        clear_cancel = cron.after(
            f"500ms",
            lambda: subprocess.check_call(
                ("polybar-msg", "action", "#cancel.module_hide")
            ),
        )

    def flash_repeat():
        """Flash repeat symbol"""
        global clear_repeat

        if clear_repeat:
            cron.cancel(clear_repeat)
            clear_repeat = None
        actions.user.clear_subtitle()
        subprocess.check_call(("polybar-msg", "action", "#repeat.module_show"))
        clear_repeat = cron.after(
            f"500ms",
            lambda: subprocess.check_call(
                ("polybar-msg", "action", "#repeat.module_hide")
            ),
        )

    def show_as_subtitle(text: str):
        """Display text in the subtitle bar"""
        global clear_subtitle

        if clear_subtitle:
            cron.cancel(clear_subtitle)
            clear_subtitle = None
        subprocess.check_call(("polybar-msg", "action", "subtitle", "send", text))
        clear_subtitle = cron.after(
            f"5000ms",
            actions.user.clear_subtitle,
        )

    def clear_subtitle():
        """Clear the subtitle bar"""
        global clear_subtitle
        subprocess.check_call(
            (
                "polybar-msg",
                "action",
                "subtitle",
                "send",
            )
        )
        if clear_subtitle:
            cron.cancel(clear_subtitle)
            clear_subtitle = None


def on_pre_phrase(phrase):
    global clear_subtitle

    words = phrase.get("phrase")

    if words and actions.speech.enabled():
        if clear_subtitle:
            cron.cancel(clear_subtitle)
            clear_subtitle = None
        text = " ".join(words)
        actions.user.show_as_subtitle(text)


speech_system.register("pre:phrase", on_pre_phrase)
