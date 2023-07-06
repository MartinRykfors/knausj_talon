from talon import speech_system, actions, cron
import subprocess

c = None

def on_pre_phrase(phrase):
    global c
    words = phrase.get("phrase")

    if words and actions.speech.enabled():
        if c:
            cron.cancel(c)
            c = None
        text = " ".join(words)
        subprocess.check_call(
            ("polybar-msg", "action", "subtitle", "send", text)
        )
        c = cron.after(f"5000ms", lambda: subprocess.check_call(
            ("polybar-msg", "action", "subtitle", "send")
        ))

speech_system.register("pre:phrase", on_pre_phrase)
