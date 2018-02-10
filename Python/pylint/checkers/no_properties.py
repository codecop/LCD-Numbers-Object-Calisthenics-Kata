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
                    self.add_message('has-public-attributes', node=node, args=(attr, node.name,))


class NoPropertiesChecker(BaseChecker):
    """checks for properties - do not use property decorator."""

    __implements__ = IAstroidChecker

    # configuration section name
    name = 'no-properties'
    priority = -1
    msgs = {
        'R1292': ('Declarator defines a property "%s"',
                  'has-properties',
                  'Object Calisthenics Rule 9'),
    }
    options = ()

    @check_messages('has-properties')
    def visit_functiondef(self, node):
        """check if for property decorator"""
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


def register(linter):
    """required method to auto register this checker """
    linter.register_checker(NoPublicAttributesChecker(linter))
    linter.register_checker(NoPropertiesChecker(linter))
