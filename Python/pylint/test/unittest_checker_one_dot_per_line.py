"""Unit tests for Object Calisthenics rule 5: One dot per line."""

import astroid


# from astroid.as_string import AsStringVisitor
# from checkers.one_dot_per_line import OneDotPerLineChecker
# from pylint.testutils import CheckerTestCase


# class TestOneDotPerLineChecker(CheckerTestCase):
#     """Unit tests for TODO."""
#     CHECKER_CLASS = OneDotPerLineChecker
#
#     def xtest_call_call(self):
#         """Test that if is left alone."""
#
#         node = astroid.parse("""
#         get_x().get_y()
#         """)
#
#         print node
#         print list(node.get_children())[0]
#         print list(node.get_children())[0].value
#         print list(node.get_children())[0].value.func
#         print list(node.get_children())[0].value.func.expr
#         assert False
#
#     def test_field_call(self):
#         """Test that if is left alone."""
#
#         node = astroid.parse("""
#         a.get_y()
#         """)
#
#         print "dump"
#         print astroid.as_string.dump(node.root())
#
#         print "walk"
#         asv = AsStringVisitor('    ')  # astroid.as_string
#         walk(asv, node.root())
#
#         print node
#         print list(node.get_children())[0]
#         print list(node.get_children())[0].value
#         print list(node.get_children())[0].value.func
#         print list(node.get_children())[0].value.func.expr
#         assert False
#
#
# def walk(visitor, astroid):
#     print visitor(astroid)
#
#     # recurse on children
#     for child in astroid.get_children():
#         walk(visitor, child)

def dump(astroid, intent=0):
    name = type(astroid).__name__
    open = "<" + name + ">"
    close = "</" + name + ">"

    space = "    " * intent
    print space + open

    inner_space = "    " * (intent + 1)

    print inner_space + astroid.instance_attrs

    print inner_space + "<!--"
    print inner_space + str(astroid)
    print inner_space + "-->"

    for child in astroid.get_children():
        dump(child, intent + 1)

    print space + close


node = astroid.parse("""
    a.get_y()
    """)

dump(node.root())
