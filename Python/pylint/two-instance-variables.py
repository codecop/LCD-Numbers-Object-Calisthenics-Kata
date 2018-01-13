# see https://breadcrumbscollector.tech/writing-custom-checkers-for-pylint/
# see https://pylint.readthedocs.io/en/latest/how_tos/custom_checkers.html
import six
from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker


class TwoInstanceVariablesChecker(BaseChecker):
    __implements__ = IAstroidChecker

    name = 'two-instance-variables'
    priority = -1
    msgs = {
        'R1281': ('More than two instance variables in class "%s". Split this class.',
                  'more-than-two-instance-variables',
                  'Object Calisthenics Rule 8'),
    }
    options = ()

    def visit_classdef(self, node):
        attribute_count = 0

        for attr, anodes in six.iteritems(node.instance_attrs):
            if not any(node.instance_attr_ancestors(attr)):
                # print attr, anodes[0]
                attribute_count += 1

        if attribute_count > 2:
            self.add_message('more-than-two-instance-variables', node=node, args=(node.name,))


def register(linter):
    """required method to auto register this checker"""
    linter.register_checker(TwoInstanceVariablesChecker(linter))
