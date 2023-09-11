app: vscode
-

write phrase <user.text> <user.cursorless_destination>:
    user.cursorless_insert(cursorless_destination, text)

write <user.format_text> <user.cursorless_destination>:
    user.cursorless_insert(cursorless_destination, format_text)

write word <user.word> (and <user.word>)* <user.cursorless_destination>:
    user.cursorless_insert(cursorless_destination, word_list)

write symbol <user.symbol_key> (and <user.symbol_key>)* <user.cursorless_destination>:
    user.cursorless_insert(cursorless_destination, symbol_key_list)