from talon import actions, cron, Module, Context
import subprocess


mod = Module()
mod.tag("eww", desc="tag for enabling eww notifications and subtitles")

clear_subtitle = None
clear_cancel = None
clear_repeat = None
clear_warn = None


ctx_eww = Context()
ctx_eww.matches = r"""
tag: user.eww
"""


@ctx_eww.action_class("user")
class PolybarNotificationActions:
    def flash_cancel():
        """Flash cancel symbol"""
        global clear_cancel

        if clear_cancel:
            cron.cancel(clear_cancel)
            clear_cancel = None
        subprocess.check_call(("eww", "update", "cancel=true"))
        clear_cancel = cron.after(
            f"500ms",
            lambda: subprocess.check_call(
                ("eww", "update", "cancel=false")
            ),
        )

    def flash_repeat():
        """Flash repeat symbol"""
        global clear_repeat

        if clear_repeat:
            cron.cancel(clear_repeat)
            clear_repeat = None
        subprocess.check_call(("eww", "update", "repeat=true"))
        clear_repeat = cron.after(
            f"500ms",
            lambda: subprocess.check_call(
                ("eww", "update", "repeat=false")
            ),
        )

    def show_as_subtitle(text: str):
        """Display text in the subtitle bar"""
        global clear_subtitle

        if clear_subtitle:
            cron.cancel(clear_subtitle)
            clear_subtitle = None
        subprocess.check_call(("eww", "update", f'''subtitle={text}'''))
        clear_subtitle = cron.after(
            f"5000ms",
            actions.user.clear_subtitles,
        )

    def clear_subtitles():
        """Clear the subtitle bar"""
        global clear_subtitle
        subprocess.check_call(
            (
                "eww", "update", 'subtitle='
            )
        )
        if clear_subtitle:
            cron.cancel(clear_subtitle)
            clear_subtitle = None

    def notify_sleep():
        """Notify Talon asleep"""
        subprocess.check_call(("eww", "update", "listen=false"))

    def notify_wake():
        """Notify Talon awake"""
        subprocess.check_call(("eww", "update", "listen=true"))

    def notify_deprecated():
        """Notify usage of deprecated function"""
        flash_square("#ffa000")

    def notify_deprecated():
        """Notify usage of deprecated function"""
        global clear_warn

        if clear_warn:
            cron.cancel(clear_warn)
            clear_warn = None
        subprocess.check_call(("eww", "update", "warn=true"))
        clear_warn = cron.after(
            f"2000ms",
            lambda: subprocess.check_call(
                ("eww", "update", "warn=false")
            ),
        )
