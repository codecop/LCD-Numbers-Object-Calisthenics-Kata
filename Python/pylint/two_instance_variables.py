"""checks for Object Calisthenics rule 8: Only two instance variables."""

# see https://pylint.readthedocs.io/en/latest/how_tos/custom_checkers.html
import six
from pylint.checkers import BaseChecker
from pylint.checkers.utils import check_messages
from pylint.interfaces import IAstroidChecker


class TwoInstanceVariablesChecker(BaseChecker):
    """checks for number of instance variables."""

    __implements__ = IAstroidChecker

    # configuration section name
    name = 'two-instance-variables'
    priority = -1
    msgs = {
        'R1281': ('More than two instance variables in class "%s"',
                  'more-than-two-instance-variables',
                  'Object Calisthenics Rule 8'),
    }
    options = ()

    @check_messages('more-than-two-instance-variables')
    def visit_classdef(self, node):
        """check number of class attributes"""
        attribute_count = 0

        for attr, _ in six.iteritems(node.instance_attrs):
            if not any(node.instance_attr_ancestors(attr)):
                # print attr, anodes[0]
                attribute_count += 1

        if attribute_count > 2:
            self.add_message('more-than-two-instance-variables', node=node, args=(node.name,))


def register(linter):
    """required method to auto register this checker """
    linter.register_checker(TwoInstanceVariablesChecker(linter))
