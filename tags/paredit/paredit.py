from talon import Module

mod = Module()
mod.tag("paredit", desc="tag for interacting with paredit")

@mod.action_class
class Actions:
    def splice_sexp_kill_forward():
        """Splice sexp, killing forward"""

    def splice_sexp_kill_backward():
        """Splice sexp, killing backward"""
