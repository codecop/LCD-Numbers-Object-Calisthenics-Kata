"""Unit tests for Object Calisthenics rule 5: One dot per line."""

import astroid
from pylint.testutils import CheckerTestCase, Message
from checkers.one_dot_per_line import ChainedCallsChecker, ChainedPropertiesChecker


class TestChainedCallsChecker(CheckerTestCase):
    """Unit tests for chains ending in cals."""
    CHECKER_CLASS = ChainedCallsChecker

    def test_direct_calls(self):
        """Test that direct calls are left alone."""

        node = astroid.parse("""
        import mm

        global_instance = ""

        def global_method():
            pass

        class A(object):
            def __init__(self):
                self.instance = ""

            def method(self, argument):
                local = ""

                # Call and func is Name
                global_method()
                # Call and func is Attribute and expr is Call and func is Name, OK
                global_method().lower()

                mm.method()
                mm.method().lower()
                mm.a.lower()

                global_instance.lower()

                # Call and func is Attribute and expr is Name
                local.lower()
                argument.lower()
                self.method("")

                # Call and func is Attribute and expr is Call and func is Attribute and expr is Name
                self.method("").title()

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
                global_method().title().capitalize()
                self.method("").title().lower()

                return ""
        """)

        class_def = list(node.get_children())[1]
        fun_def = class_def.body[0]

        with self.assertAddsMessages(
            Message('chained-call', node=fun_def.body[0].value,
                    args=('title', 'capitalize',), ),
            Message('chained-call', node=fun_def.body[1].value,
                    args=('title', 'lower',), )):
            self.walk(node.root())

    def test_call_after_attribute(self):
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

    def test_attribute_after_attribute(self):
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

    def test_attribute_after_call(self):
        """Test that calls after attributes after calls are found."""

        node = astroid.parse("""
        def global_method():
            return ""

        class A(object):
            def method(self, argument):
                global_method().a.capitalize()
                self.method("").a.lower()
                return ""
        """)

        class_def = list(node.get_children())[1]
        fun_def = class_def.body[0]

        with self.assertAddsMessages(
            Message('chained-call', node=fun_def.body[0].value,
                    args=('a', 'capitalize',), ),
            Message('chained-call', node=fun_def.body[1].value,
                    args=('a', 'lower',), )):
            self.walk(node.root())

    def test_namespace(self):
        """Test that namespaces are left alone."""

        node = astroid.parse("""
        import os

        os.path.join("", "")
        """)

        with self.assertNoMessages():
            self.walk(node.root())


class TestChainedPropertiesChecker(CheckerTestCase):
    """Unit tests for chained properties."""
    CHECKER_CLASS = ChainedPropertiesChecker

    def test_direct_attributes(self):
        """Test that direct calls are left alone."""

        node = astroid.parse("""
        import mm

        global_instance = ""

        def global_method():
            pass

        class A(object):
            def __init__(self):
                self.instance = ""

            def method(self, argument):
                local = ""

                global_method().a
                global_instance.a

                mm.a
                mm.a.b
                mm.method().b

                local.a
                argument.a
                self.instance

                self.method("").a

                self.instance.a
        """)

        with self.assertNoMessages():
            self.walk(node.root())

    def test_call_after_call(self):
        """Test that attributes after calls are found."""

        node = astroid.parse("""
        def global_method():
            return ""

        class A(object):
            def method(self, argument):
                global_method().title().a
                self.method("").title().b
                return ""
        """)

        class_def = list(node.get_children())[1]
        fun_def = class_def.body[0]

        with self.assertAddsMessages(
            Message('chained-attribute', node=fun_def.body[0].value,
                    args=('title', 'a',), ),
            Message('chained-attribute', node=fun_def.body[1].value,
                    args=('title', 'b',), )):
            self.walk(node.root())

    def test_call_after_attribute(self):
        """Test that attributes after calls after attribute are found."""

        node = astroid.parse("""
        global_instance = ""

        class A(object):
            def __init__(self):
                self.instance = ""

            def method(self, argument):
                local = ""

                global_instance.title().a
                local.upper().b
                argument.strip().c
                self.instance.lstrip().d

                return ""
        """)

        class_def = list(node.get_children())[1]
        fun_def = class_def.body[1]

        with self.assertAddsMessages(
            Message('chained-attribute', node=fun_def.body[1].value,
                    args=('title', 'a',), ),
            Message('chained-attribute', node=fun_def.body[2].value,
                    args=('upper', 'b',), ),
            Message('chained-attribute', node=fun_def.body[3].value,
                    args=('strip', 'c',), ),
            Message('chained-attribute', node=fun_def.body[4].value,
                    args=('lstrip', 'd',), )):
            self.walk(node.root())

    def test_attribute_after_attribute(self):
        """Test that attributes after chained attribute are found."""

        node = astroid.parse("""
        global_instance = ""

        class A(object):
            def __init__(self):
                self.instance = ""

            def method(self, argument):
                local = ""

                global_instance.a.x
                local.b.y
                argument.c.z
                self.instance.d.w
        """)

        class_def = list(node.get_children())[1]
        fun_def = class_def.body[1]

        with self.assertAddsMessages(
            Message('chained-attribute', node=fun_def.body[1].value,
                    args=('a', 'x',), ),
            Message('chained-attribute', node=fun_def.body[2].value,
                    args=('b', 'y',), ),
            Message('chained-attribute', node=fun_def.body[3].value,
                    args=('c', 'z',), ),
            Message('chained-attribute', node=fun_def.body[4].value,
                    args=('d', 'w',), )):
            self.walk(node.root())

    def test_attribute_after_call(self):
        """Test that attributes after attributes after calls are found."""

        node = astroid.parse("""
        def global_method():
            return ""

        class A(object):
            def method(self, argument):
                global_method().a.x
                self.method("").a.y
                return ""
        """)

        class_def = list(node.get_children())[1]
        fun_def = class_def.body[0]

        with self.assertAddsMessages(
            Message('chained-attribute', node=fun_def.body[0].value,
                    args=('a', 'x',), ),
            Message('chained-attribute', node=fun_def.body[1].value,
                    args=('a', 'y',), )):
            self.walk(node.root())
