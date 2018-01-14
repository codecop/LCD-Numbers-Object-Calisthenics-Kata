"""checks for Object Calisthenics rule 4: First class collections."""

import astroid
import six
from pylint.checkers import BaseChecker
from pylint.checkers.utils import check_messages
from pylint.interfaces import IAstroidChecker


class FirstClassCollectionsChecker(BaseChecker):
    """checks for collection attributes to be the only field."""

    __implements__ = IAstroidChecker

    # configuration section name
    name = 'first-class-collections'
    priority = -1
    msgs = {
        'R1241': ('Collection field in class "%s" must be first class',
                  'collection-not-first-class',
                  'Object Calisthenics Rule 4'),
    }
    options = ()

    @check_messages('collection-not-first-class')
    def visit_classdef(self, node):
        """check class attributes"""
        attribute_count = 0
        has_collection = False

        for attr, anodes in six.iteritems(node.instance_attrs):
            if not any(node.instance_attr_ancestors(attr)):
                # print attr, '=', list(anodes[0].parent.get_children())[1]
                attribute_count += 1
                has_collection = has_collection or self._is_collection(anodes)

        if has_collection and attribute_count > 1:
            self.add_message('collection-not-first-class', node=node, args=(node.name,))

    def _is_collection(self, assign_nodes):
        assigned_values = [list(node.parent.get_children())[1] for node in assign_nodes]
        # print assigned_values
        for value in assigned_values:
            if isinstance(value, astroid.node_classes.List):  # []
                return True
            if isinstance(value, astroid.scoped_nodes.ListComp):
                return True
            if isinstance(value, astroid.scoped_nodes.SetComp):
                return True
            if isinstance(value, astroid.node_classes.Call):
                callee = value.func.name
                if callee == 'list' or callee == 'set':  # list() or # set()
                    return True
                    # print value
        return False


def register(linter):
    """required method to auto register this checker """
    linter.register_checker(FirstClassCollectionsChecker(linter))
