"""Unit tests for Object Calisthenics rule 7: Small entities."""

import astroid
from pylint.testutils import CheckerTestCase, Message
from small_entities import SmallEntitiesChecker, SmallModulesChecker


class TestSmallEntitiesChecker(CheckerTestCase):
    """Unit tests for the small entities checker."""
    CHECKER_CLASS = SmallEntitiesChecker

    def test_short_enough(self):
        node = astroid.parse("""
        class JustOkSizeSample(object):
            def __init__(self):
        """ + self.statements(1) + """ # 2.

            def method(self):  # 3.
        """ + self.statements(45 - 3))

        with self.assertNoMessages():
            self.walk(node.root())

    def statements(self, num):  # pylint: disable=no-self-use
        return """
                self._a = 1
        """ * num

    def test_too_long(self):
        node = astroid.parse("""
        class Large(object):
            def __init__(self):
        """ + self.statements(1) + """ # 2.

            def method(self):  # 3.
        """ + self.statements(45 - 3) + """
                self._a = 1 # one too much
        """)

        class_def = list(node.get_children())[0]

        with self.assertAddsMessages(
            Message('large-entity', node=class_def, args=('Large', 46, 45), )):
            self.walk(node.root())


class TestSmallModulesChecker(CheckerTestCase):
    """Unit tests for the small modules checker."""
    CHECKER_CLASS = SmallModulesChecker

    def test_few_classes(self):
        node = astroid.parse("""
        class A:
            pass

        class B:
            pass

        class C:
            pass
        """)

        with self.assertNoMessages():
            self.walk(node.root())

    def test_too_many_classes(self):
        node = astroid.parse("""
        class A:
            pass

        class B:
            pass

        class C:
            pass

        class D:
            pass

        class E:
            pass

        class F:
            pass

        class G:
            pass

        class H:
            pass

        class I:
            pass

        class J:
            pass

        class K:  # too many
            pass
        """)

        module_def = node

        with self.assertAddsMessages(
            Message('large-module', node=module_def, args=('', 11, 10), )):
            self.walk(node.root())
