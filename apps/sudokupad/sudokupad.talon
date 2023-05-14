tag: browser
#browser.host: crackingthecryptic.com
win.title: /Sven's Web App/
-

actual:
    key(z)
    sleep(50ms)

corner:
    key(x)
    sleep(50ms)

center:
    key(c)
    sleep(50ms)

color:
    key(v)
    sleep(50ms)

<user.number_string>: "{number_string}"

(include | take) <user.arrow_keys>:
    key("shift:down")
    user.move_cursor(arrow_keys)
    key("shift:up")

<user.arrow_key> box:
    user.move_cursor(arrow_key)
    user.move_cursor(arrow_key)
    user.move_cursor(arrow_key)
