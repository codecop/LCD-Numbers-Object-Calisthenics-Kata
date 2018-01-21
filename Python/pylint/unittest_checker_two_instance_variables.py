import astroid
from pylint.testutils import CheckerTestCase, Message
from two_instance_variables import TwoInstanceVariablesChecker


class TestTwoInstanceVariablesChecker(CheckerTestCase):
    """Unit tests for the two instance variables checker."""
    CHECKER_CLASS = TwoInstanceVariablesChecker

    def test_allow_if(self):
        """Test that two fields are left alone."""

        node = astroid.parse("""
        class GoodFieldsSample(object):
            def __init__(self):
                self._a = 0
                self._b = 0

            def three_fields(self):
                if self._a == self._b:
                    self._a = 0
        """)

        with self.assertNoMessages():
            self.walk(node.root())

    def test_find_three_fields(self):
        """Test that three fields are flagged."""

        node = astroid.parse("""
        class BadFieldsSample(object):
            def __init__(self):
                self._a = 0
                self._b = 0
                self._third_field = 0

            def three_fields(self):
                self._third_field = 0
                self._b = self._third_field
                if self._a == self._b:
                    self._a = self._third_field
        """)

        def first(n, i=0):
            return list(n.get_children())[i]

        class_def = first(node)

        with self.assertAddsMessages(
                Message('more-than-two-instance-variables', node=class_def, args=('BadFieldsSample',), )):
            self.walk(node.root())
