"""Unit tests for Object Calisthenics rule 9: No properties."""

import astroid
from pylint.testutils import CheckerTestCase, Message
from checkers.no_properties import NoPropertiesChecker, NoPublicAttributesChecker


class TestNoPublicAttributesChecker(CheckerTestCase):
    """Unit tests for the no public attributes checker."""
    CHECKER_CLASS = NoPublicAttributesChecker

    def test_private_property(self):
        node = astroid.parse("""
        class GoodProperties(object):
            def __init__(self):
                self._field1 = 0
                self._field2 = 0
        """)

        with self.assertNoMessages():
            self.walk(node.root())

    def test_public_property(self):
        node = astroid.parse("""
        class Bad(object):
            def __init__(self):
                self.public_property = 0
        """)

        class_def = list(node.get_children())[0]

        with self.assertAddsMessages(Message('has-public-attributes', node=class_def,
                                             args=('public_property', 'Bad',), )):
            self.walk(node.root())


class TestNoPropertiesChecker(CheckerTestCase):
    """Unit tests for the no properties checker."""
    CHECKER_CLASS = NoPropertiesChecker

    def test_annotated_get_property(self):
        node = astroid.parse("""
        class Bad(object):
            def __init__(self):
                self._temperature = 0

            @property
            def temperature(self):
                return self._temperature
        """)

        class_def = list(node.get_children())[0]
        fun_def = list(class_def.get_children())[2]

        with self.assertAddsMessages(Message('has-properties', node=fun_def,
                                             args=('temperature',), )):
            self.walk(node.root())

    def test_annotated_set_property(self):
        node = astroid.parse("""
        class Bad(object):
            def __init__(self):
                self._temperature = 0

            @temperature.setter
            def temperature(self, value):
                if value < -273:
                    raise ValueError("Temperature below -273 is not possible")
                self._temperature = value
        """)

        class_def = list(node.get_children())[0]
        fun_def = list(class_def.get_children())[2]

        with self.assertAddsMessages(Message('has-properties', node=fun_def,
                                             args=('temperature',), )):
            self.walk(node.root())

    def test_declared_property(self):
        node = astroid.parse("""
        class Bad(object):
            def __init__(self):
                self._temperature = 0

            def get_temperature(self):
                return self._temperature

            def set_temperature(self, value):
                if value < -273:
                    raise ValueError("Temperature below -273 is not possible")
                self._temperature = value

            temperature = property(get_temperature, set_temperature)
        """)

        class_def = list(node.get_children())[0]
        assign_def = list(class_def.get_children())[4]
        call_def = assign_def.value

        with self.assertAddsMessages(Message('has-properties', node=call_def,
                                             args=('get_temperature',), )):
            self.walk(node.root())
