from talon import Context, Module

mod = Module()
ctx = Context()

mod.list("svn_command", desc="Subversion commands.")

ctx.lists["self.svn_command"] = {
    "add": "add",
    "auth": "auth",
    "blame": "blame",
    "cat": "cat",
    "changelist": "changelist",
    "checkout": "checkout",
    "cleanup": "cleanup",
    "commit": "commit",
    "copy": "copy",
    "delete": "delete",
    "diff": "diff",
    "export": "export",
    "import": "import",
    "info": "info",
    "list": "list",
    "lock": "lock",
    "log": "log",
    "merge": "merge",
    "mergeinfo": "mergeinfo",
    "mkdir": "mkdir",
    "move": "move",
    "patch": "patch",
    "propdel": "propdel",
    "propedit": "propedit",
    "propget": "propget",
    "proplist": "proplist",
    "propset": "propset",
    "relocate": "relocate",
    "resolve": "resolve",
    "resolved": "resolved",
    "revert": "revert",
    "revert everything": "revert -R .",
    "status": "status",
    "switch": "switch",
    "unlock": "unlock",
    "up": "up",
    "update": "update",
    "upgrade": "upgrade",
}
