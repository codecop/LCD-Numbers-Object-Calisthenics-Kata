"""Unit tests for the no-else checker."""
import astroid
from pylint.testutils import CheckerTestCase, Message
from no_else import NoElseChecker


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
                if self._a > 1:
                    self._a = 1
        """)

        with self.assertNoMessages():
            self.walk(node.root())

    # @set_config(exclude_protected=('_meta', '_manager'))
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

        def first(node, i=0):
            """Return first/i-th child of children nodes."""
            return list(node.get_children())[i]

        class_def = first(node)
        fun_def = class_def.body[1]
        if_def = fun_def.body[1]

        with self.assertAddsMessages(Message('if-has-else', node=if_def)):
            self.walk(node.root())
