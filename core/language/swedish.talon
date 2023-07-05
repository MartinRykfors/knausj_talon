mode: dictation
language: sv
-
settings():
    speech.engine = 'webspeech'
    speech.language = 'sv_SE'

avslut:
    mode.disable("dictation")
    mode.disable("user.swedish")
    mode.enable("command")

<phrase>: insert("{phrase} ")
