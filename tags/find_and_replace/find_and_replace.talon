tag: user.find_and_replace
-
(rummage | recon) this: user.find("")
(rummage | recon) this (pace | paste):
    user.find("")
    sleep(25ms)
    edit.paste()
(rummage | recon) this <user.text>: user.find(text)
(rummage | recon) (all | everything): user.find_everywhere("")
(rummage | recon) (all | everything) (pace | paste):
    user.find_everywhere("")
    sleep(25ms)
    edit.paste()
(rummage | recon) (all | everything) <user.text>: user.find_everywhere(text)
(rummage | recon) case: user.find_toggle_match_by_case()
(rummage | recon) word: user.find_toggle_match_by_word()
(rummage | recon) expression: user.find_toggle_match_by_regex()
(rummage | recon) next: user.find_next()
(rummage | recon) previous: user.find_previous()
replace this [<user.text>]: user.replace(text or "")
replace all: user.replace_everywhere("")
replace <user.text> all: user.replace_everywhere(text)
replace confirm that: user.replace_confirm()
replace confirm all: user.replace_confirm_all()

#quick replace commands, modeled after jetbrains
clear last <user.text> [over]:
    user.select_previous_occurrence(text)
    sleep(100ms)
    edit.delete()
clear next <user.text> [over]:
    user.select_next_occurrence(text)
    sleep(100ms)
    edit.delete()
clear last clip:
    user.select_previous_occurrence(clip.text())
    edit.delete()
clear next clip:
    user.select_next_occurrence(clip.text())
    sleep(100ms)
    edit.delete()
comment last <user.text> [over]:
    user.select_previous_occurrence(text)
    sleep(100ms)
    code.toggle_comment()
comment last clip:
    user.select_previous_occurrence(clip.text())
    sleep(100ms)
    code.toggle_comment()
comment next <user.text> [over]:
    user.select_next_occurrence(text)
    sleep(100ms)
    code.toggle_comment()
comment next clip:
    user.select_next_occurrence(clip.text())
    sleep(100ms)
    code.toggle_comment()
go last <user.text> [over]:
    user.select_previous_occurrence(text)
    sleep(100ms)
    edit.right()
go last clip:
    user.select_previous_occurrence(clip.text())
    sleep(100ms)
    edit.right()
go next <user.text> [over]:
    user.select_next_occurrence(text)
    edit.right()
go next clip:
    user.select_next_occurrence(clip.text())
    edit.right()
paste last <user.text> [over]:
    user.select_previous_occurrence(text)
    sleep(100ms)
    edit.right()
    edit.paste()
paste next <user.text> [over]:
    user.select_next_occurrence(text)
    sleep(100ms)
    edit.right()
    edit.paste()
replace last <user.text> [over]:
    user.select_previous_occurrence(text)
    sleep(100ms)
    edit.paste()
replace next <user.text> [over]:
    user.select_next_occurrence(text)
    sleep(100ms)
    edit.paste()
select last <user.text> [over]: user.select_previous_occurrence(text)
select next <user.text> [over]: user.select_next_occurrence(text)
select last clip: user.select_previous_occurrence(clip.text())
select next clip: user.select_next_occurrence(clip.text())
