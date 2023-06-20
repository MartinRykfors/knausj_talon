tag: browser
#browser.host: crackingthecryptic.com
win.title: /Sven's Web App/
-

actual:
    key(;)
    sleep(50ms)

corner:
    key(q)
    sleep(50ms)

center:
    key(j)
    sleep(50ms)

(color | colors):
    key(k)
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
