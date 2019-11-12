"""Unit tests for Object Calisthenics rule 7: Small entities."""

import astroid
from pylint.testutils import CheckerTestCase, Message
from checkers.small_entities import SmallEntitiesChecker, SmallModulesChecker


class TestSmallEntitiesChecker(CheckerTestCase):
    """Unit tests for the small entities checker."""
    CHECKER_CLASS = SmallEntitiesChecker

    def test_class_short_enough(self):
        node = astroid.parse("""
        class JustOkSizeSample(object):
            def __init__(self):
        """ + self._class_statements(1) + """ # 2.

            def method(self):  # 3.
        """ + self._class_statements(45 - 3))

        with self.assertNoMessages():
            self.walk(node.root())

    def _class_statements(self, num):  # pylint: disable=no-self-use
        return """
                self._a = 1
        """ * num

    def test_class_too_long(self):
        node = astroid.parse("""
        class Large(object):
            def __init__(self):
        """ + self._class_statements(1) + """ # 2.

            def method(self):  # 3.
        """ + self._class_statements(45 - 3) + """
                self._a = 1 # one too much
        """)

        class_def = list(node.get_children())[0]

        with self.assertAddsMessages(Message('large-entity',
                                             node=class_def, args=('Large', 46, 45), )):
            self.walk(node.root())

    def test_module_too_long(self):
        node = astroid.parse("""
        def method():  # 1.
        """ + self._module_statements(45 - 1) + """
            abc = 1 # one too much
        """)

        module_def = node

        with self.assertAddsMessages(Message('large-module',
                                             node=module_def, args=('', 46, 45), )):
            self.walk(node.root())

    def _module_statements(self, num):  # pylint: disable=no-self-use
        return """
            abc = 1
        """ * num

    def test_module_not_too_long(self):
        node = astroid.parse("""
        def method(self):  # 1.
        """ + self._module_statements(45 - 1))

        with self.assertNoMessages():
            self.walk(node.root())

    def test_class_not_counted_to_module_before(self):  # pylint: disable=invalid-name
        node = astroid.parse("""
        def method(self):  # 1.
        """ + self._module_statements(45 - 1) + """

        class JustOkInSize(object):
            def method(self):  # 1.
        """ + self._class_statements(45 - 1) + """
        """)

        with self.assertNoMessages():
            self.walk(node.root())

    def test_class_not_counted_to_module_after(self):  # pylint: disable=invalid-name
        node = astroid.parse("""
        class JustOkInSize(object):
            def method(self):  # 1.
        """ + self._class_statements(45 - 1) + """

        def method(self):  # 1.
        """ + self._module_statements(45 - 1) + """
        """)

        with self.assertNoMessages():
            self.walk(node.root())


class TestSmallModulesChecker(CheckerTestCase):
    """Unit tests for the small modules checker."""
    CHECKER_CLASS = SmallModulesChecker

    def test_few_classes(self):
        node = astroid.parse("""
        class A(object):
            pass

        class B(object):
            pass

        class C(object):
            pass
        """)

        with self.assertNoMessages():
            self.walk(node.root())

    def test_too_many_classes(self):
        node = astroid.parse("""
        class A(object):
            pass

        class B(object):
            pass

        class C(object):
            pass

        class D(object):
            pass

        class E(object):
            pass

        class F(object):
            pass

        class G(object):
            pass

        class H(object):
            pass

        class I(object):
            pass

        class J(object):
            pass

        class K(object):  # too many
            pass
        """)

        module_def = node

        with self.assertAddsMessages(Message('too-many-classes',
                                             node=module_def, args=('', 11, 10), )):
            self.walk(node.root())
