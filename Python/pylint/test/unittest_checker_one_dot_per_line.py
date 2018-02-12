"""Unit tests for Object Calisthenics rule 5: One dot per line."""

import astroid
from pylint.testutils import CheckerTestCase, Message
from checkers.one_dot_per_line import ChainedCallsChecker, ChainedPropertiesChecker


class TestChainedCallsChecker(CheckerTestCase):
    """Unit tests for calls only against names."""
    CHECKER_CLASS = ChainedCallsChecker

    def test_direct_calls(self):
        """Test that direct calls are left alone."""

        node = astroid.parse("""
        def global_method():
            pass

        class A(object):
            def __init__(self):
                self.instance = ""

            def method(self, argument):
                local = ""

                # Call and func is Name
                global_method()

                # Call and func is Attribute and expr is Name
                local.lower()
                argument.lower()
                self.method("")

                # Call and func is Attribute and expr is Call and func is Attribute and expr is Name
                self.method("").title

                # Call and func is Attribute and expr is Attribute and exp is Name "self"
                self.instance.lower()
        """)

        with self.assertNoMessages():
            self.walk(node.root())

    def test_call_after_call(self):
        """Test that chained calls after calls are found."""

        node = astroid.parse("""
        def global_method():
            return ""

        class A(object):
            def method(self, argument):
                # Call and func is Attribute and expr is Call and func is Name, OK
                global_method().lower()

                global_method().title().capitalize()
                self.method("").title().lower()

                return ""
        """)

        class_def = list(node.get_children())[1]
        fun_def = class_def.body[0]

        with self.assertAddsMessages(
            Message('chained-call', node=fun_def.body[1].value,
                    args=('title', 'capitalize',), ),
            Message('chained-call', node=fun_def.body[2].value,
                    args=('title', 'lower',), )):
            self.walk(node.root())

    def test_call2_after_attribute(self):
        """Test that chained calls after attribute are found."""

        node = astroid.parse("""
        global_instance = ""

        class A(object):
            def __init__(self):
                self.instance = ""

            def method(self, argument):
                local = ""

                global_instance.title().capitalize()
                local.upper().lower()
                argument.strip().lower()
                self.instance.lstrip().rstrip()

                return ""
        """)

        class_def = list(node.get_children())[1]
        fun_def = class_def.body[1]

        with self.assertAddsMessages(
            Message('chained-call', node=fun_def.body[1].value,
                    args=('title', 'capitalize',), ),
            Message('chained-call', node=fun_def.body[2].value,
                    args=('upper', 'lower',), ),
            Message('chained-call', node=fun_def.body[3].value,
                    args=('strip', 'lower',), ),
            Message('chained-call', node=fun_def.body[4].value,
                    args=('lstrip', 'rstrip',), )):
            self.walk(node.root())

    def test_call_after_attribute2(self):
        """Test that calls after chained attribute are found."""

        node = astroid.parse("""
        global_instance = ""

        class A(object):
            def __init__(self):
                self.instance = ""

            def method(self, argument):
                local = ""

                global_instance.x.capitalize()
                local.a.lower()
                argument.b.lower()
                self.instance.c.rstrip()
        """)

        class_def = list(node.get_children())[1]
        fun_def = class_def.body[1]

        with self.assertAddsMessages(
            Message('chained-call', node=fun_def.body[1].value,
                    args=('x', 'capitalize',), ),
            Message('chained-call', node=fun_def.body[2].value,
                    args=('a', 'lower',), ),
            Message('chained-call', node=fun_def.body[3].value,
                    args=('b', 'lower',), ),
            Message('chained-call', node=fun_def.body[4].value,
                    args=('c', 'rstrip',), )):
            self.walk(node.root())


class TestChainedPropertiesChecker(CheckerTestCase):
    """Unit tests for chained properties."""
    CHECKER_CLASS = ChainedPropertiesChecker

    def no_test_call_followed_by_property(self):
        """Test that calls followed by properties are found."""

        node = astroid.parse("""
        def global_method():
            return ""

        class A(object):
            def __init__(self):
                self.instance = ""

            def method(self, argument):
                local = ""

                global_method().title().capitalize
                #local.upper().lower
                #argument.strip().lower
                self.method("").title().lower
                #self.instance.lstrip().rstrip

                return ""
        """)

        class_def = list(node.get_children())[1]
        fun_def = class_def.body[1]

        with self.assertAddsMessages(
            Message('chained-property', node=fun_def.body[1].value,
                    args=('title', 'capitalize',), ),
            Message('chained-property', node=fun_def.body[2].value,
                    args=('upper', 'lower',), ),
            Message('chained-property', node=fun_def.body[3].value,
                    args=('strip', 'lower',), ),
            Message('chained-property', node=fun_def.body[4].value,
                    args=('title', 'lower',), ),
            Message('chained-property', node=fun_def.body[5].value,
                    args=('lstrip', 'rstrip',), )):
            self.walk(node.root())
