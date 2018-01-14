"""checks for Object Calisthenics rule 9: No properties."""
import six
from pylint.checkers import BaseChecker
from pylint.checkers.utils import check_messages
from pylint.interfaces import IAstroidChecker


class NoPublicAttributesChecker(BaseChecker):
    """checks for public attributes."""

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
    """checks for properties."""

    __implements__ = IAstroidChecker

    # configuration section name
    name = 'no-properties'
    priority = -1
    msgs = {
        'R1292': ('Class "%s" defines properties',
                  'has-properties',
                  'Object Calisthenics Rule 9'),
    }
    options = ()

    @check_messages('has-properties')
    def visit_if(self, node):
        """check if for else"""
        if False and node.orelse:
            self.add_message('has-properties', node=node, args=(node.name,))


def register(linter):
    """required method to auto register this checker """
    linter.register_checker(NoPublicAttributesChecker(linter))
    linter.register_checker(NoPropertiesChecker(linter))
