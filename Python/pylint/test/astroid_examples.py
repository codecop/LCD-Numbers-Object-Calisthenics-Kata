"""Exploring Astroid's AST."""

from __future__ import print_function
import re
import astroid


def to_code(astroid_node):
    """Display the parsed tree as code. Build into Astroid."""
    visitor = astroid.as_string.AsStringVisitor("    ")
    print(visitor(astroid_node))


def traverse(astroid_node, visitor):
    """Traverse the AST and visit all nodes"""
    visitor.visit(astroid_node)
    for child in astroid_node.get_children():
        traverse(child, visitor)
    visitor.leave(astroid_node)


class DumpAsXmlVisitor(object):
    """Visit all nodes as XML as done by PMD."""

    def __init__(self):
        self._number_spaces = 0

    def visit(self, astroid_node):
        print(self._open_tag(astroid_node))
        self._number_spaces += 1
        print(self._details(astroid_node))

    def _intent(self):
        return "    " * self._number_spaces

    def _open_tag(self, obj):
        name = type(obj).__name__
        tag = "<" + name + ">"
        return self._intent() + tag

    def _details(self, astroid_node):
        lines = re.split("\n", str(astroid_node))
        indented_details = ("\n" + self._intent() + "     ").join(lines)
        return self._intent() + "<!-- " + indented_details + " -->"

    def leave(self, obj):
        self._number_spaces -= 1
        print(self._close_tag(obj))

    def _close_tag(self, obj):
        name = type(obj).__name__
        tag = "</" + name + ">"
        return self._intent() + tag


def dump(astroid_node):
    """Dump the AST as XML as done by PMD."""
    traverse(astroid_node, DumpAsXmlVisitor())


if __name__ == '__main__':
    NODE = astroid.parse("""
        import os.path

        os.path.join("", "")
        """)

    # print("\n\ncode")
    # to_code(node.root())

    print("\n\nxml")
    dump(NODE.root())
