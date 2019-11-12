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

    def _is_collection(self, assign_nodes):  # pylint: disable=no-self-use
        assigned_values = [list(node.parent.get_children())[1] for node in assign_nodes]
        # print assigned_values

        collection_asts = [astroid.node_classes.List,  # []
                           astroid.node_classes.Tuple,  # ()
                           astroid.node_classes.Dict,
                           astroid.scoped_nodes.ListComp,
                           astroid.scoped_nodes.SetComp]

        for value in assigned_values:
            if isinstance(value, astroid.node_classes.Const):
                # short circuit most values
                continue

            for collection_ast in collection_asts:
                if isinstance(value, collection_ast):
                    return True

            if isinstance(value, astroid.node_classes.Call):
                target = value.func
                if isinstance(target, astroid.node_classes.Name):
                    callee = target.name
                    if callee == 'list' or callee == 'set' or callee == 'dict':  # list() or # set()
                        return True

            # if not isinstance(value, astroid.node_classes.Const):
            #     print('unknown assignment value type ', value)

        return False


def register(linter):
    """required method to auto register this checker """
    linter.register_checker(FirstClassCollectionsChecker(linter))
