"""Unit tests for Object Calisthenics rule 2: Don't use the ELSE keyword."""

import astroid
from pylint.testutils import CheckerTestCase, Message
from checkers.no_else import NoElseChecker


class TestNoElseChecker(CheckerTestCase):
    """Unit tests for the no-else checker."""
    CHECKER_CLASS = NoElseChecker

    def test_allow_if(self):
        """Test that if is left alone."""

        node = astroid.parse("""
        class IfSample(object):
            def __init__(self):
                self._a = 0

            def uses_else(self):
                self._a = 1
                if self._a > 1:
                    self._a = 1
        """)

        with self.assertNoMessages():
            self.walk(node.root())

    def test_find_else(self):
        """Test that else keyword is flagged."""

        node = astroid.parse("""
        class ElseSample(object):
            def __init__(self):
                self._a = 0

            def uses_else(self):
                self._a = 1
                if self._a > 1:
                    self._a = 1
                else:
                    self._a = 2
        """)

        class_def = list(node.get_children())[0]
        fun_def = class_def.body[1]
        if_def = fun_def.body[1]

        with self.assertAddsMessages(Message('if-has-else', node=if_def)):
            self.walk(node.root())
