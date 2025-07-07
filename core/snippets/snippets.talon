fabricate {user.snippet}: user.insert_snippet_by_name(snippet)

fabrication {user.snippet_with_phrase} <user.text>:
    user.insert_snippet_by_name_with_phrase(snippet_with_phrase, text)
