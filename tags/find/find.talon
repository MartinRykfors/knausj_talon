tag: user.find
-
recon this: user.find("")
recon this (pace | paste):
    user.find("")
    sleep(25ms)
    edit.paste()
recon this <user.text>: user.find(text)
recon next: user.find_next()
recon previous: user.find_previous()
