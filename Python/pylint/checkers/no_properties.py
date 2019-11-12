"""checks for Object Calisthenics rule 9: No properties."""

import six
from astroid import Decorators, Name, Attribute
from pylint.checkers import BaseChecker
from pylint.checkers.utils import check_messages
from pylint.interfaces import IAstroidChecker


class NoPublicAttributesChecker(BaseChecker):
    """checks for public attributes - all fields must be private."""

    __implements__ = IAstroidChecker

    # configuration section name
    name = 'no-public-attributes'
    priority = -1
    msgs = {
        'R1291': ('Public attribute "%s" in class "%s"',
                  'has-public-attributes',
                  'Object Calisthenics Rule 9'),
    }
    options = ()

    @check_messages('has-public-attributes')
    def visit_classdef(self, node):
        """check visibility (name) of class attributes"""
        for attr, _ in six.iteritems(node.instance_attrs):
            if not any(node.instance_attr_ancestors(attr)):
                if not attr.startswith('_'):
                    self.add_message('has-public-attributes', node=node,
                                     args=(attr, node.name,))


class NoPropertiesChecker(BaseChecker):
    """checks for properties - do not use property decorator or property
       method in class scope."""

    __implements__ = IAstroidChecker

    # configuration section name
    name = 'no-properties'
    priority = -1
    msgs = {
        'R1292': ('Decorator defines a property "%s"',
                  'has-properties',
                  'Object Calisthenics Rule 9'),
    }
    options = ()

    def __init__(self, linter=None):
        BaseChecker.__init__(self, linter)
        self._in_class = False
        self._in_function = False

    @check_messages('has-properties')
    def visit_functiondef(self, node):
        """check if for property decorator"""
        self._in_function = True

        decorators = list(node.get_children())[0]

        if isinstance(decorators, Decorators):
            if self._contains_property(decorators):
                self.add_message('has-properties', node=node, args=(node.name,))

    def _contains_property(self, decorators):  # pylint: disable=no-self-use
        for decorator in decorators.nodes:
            # print(decorator)
            if isinstance(decorator, Name):
                if decorator.name == 'property':
                    return True
            if isinstance(decorator, Attribute):
                if decorator.attrname == 'setter' or decorator.attrname == 'getter':
                    return True

        return False

    def leave_functiondef(self, node):  # pylint: disable=unused-argument
        """remember being outside function"""
        self._in_function = False

    def visit_classdef(self, node):  # pylint: disable=unused-argument
        """remember being inside class"""
        self._in_class = True

    def leave_classdef(self, node):  # pylint: disable=unused-argument
        """remember being outside class"""
        self._in_class = False

    @check_messages('has-properties')
    def visit_call(self, node):
        """check for call to property method in class scope"""
        if not self._in_class or self._in_function:
            return

        target = node.func  # node is astroid.node_classes.Call
        if isinstance(target, Name):
            callee = target.name
            if callee == 'property':
                method = node.args[0]
                self.add_message('has-properties', node=node, args=(method.name,))


def register(linter):
    """required method to auto register this checker """
    linter.register_checker(NoPublicAttributesChecker(linter))
    linter.register_checker(NoPropertiesChecker(linter))
