"""Unit tests for Object Calisthenics rule 7: Small entities."""

import astroid
from pylint.testutils import CheckerTestCase, Message
from small_entities import SmallEntitiesChecker


class TestSmallEntitiesChecker(CheckerTestCase):
    """Unit tests for the small entities checker."""
    CHECKER_CLASS = SmallEntitiesChecker

    def test_short_enough(self):
        node = astroid.parse("""
        class JustOkSizeSample(object):
            def __init__(self):
        """ + self.statements(1) + # 2
        """

            def method1(self):  # 3
        """ + self.statements(42)  # = 45
        )

        with self.assertNoMessages():
            self.walk(node.root())

    def statements(self, num):
        return """
                self._a = 1
        """ * num

    def test_too_long(self):
        node = astroid.parse("""
        class Large(object):
            def __init__(self):
        """ + self.statements(1) + # 2
        """

            def method1(self):  # 3
        """ + self.statements(42) + # = 45
        """
                self._a = 1 # one too much
        """)

        class_def = list(node.get_children())[0]

        with self.assertAddsMessages(
            Message('large-entity', node=class_def, args=('Large', 46, 45), )):
            self.walk(node.root())
