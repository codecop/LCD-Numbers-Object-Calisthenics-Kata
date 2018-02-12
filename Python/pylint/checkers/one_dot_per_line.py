"""checks for Object Calisthenics rule 5: One dot per line."""

import astroid
from pylint.checkers import BaseChecker
from pylint.checkers.utils import check_messages
from pylint.interfaces import IAstroidChecker


class ChainedCallsChecker(BaseChecker):
    """checks chain with call in the end."""

    __implements__ = IAstroidChecker

    # configuration section name
    name = 'nested-call'
    priority = -1
    msgs = {
        'R1251': ('Chained "%s" followed by call "%s"',
                  'chained-call',
                  'Object Calisthenics Rule 5'),
    }
    options = ()

    @check_messages('chained-call')
    def visit_call(self, node):
        """check call's func"""

        func = node.func
        if isinstance(func, astroid.node_classes.Attribute):
            name2 = func.attrname
            expr = func.expr

            if isinstance(expr, astroid.node_classes.Call):
                # call after another call
                name1 = '?'
                func = expr.func
                if isinstance(func, astroid.node_classes.Attribute):
                    name1 = func.attrname
                    if isinstance(func.expr, astroid.node_classes.Name) and \
                                    func.expr.name=='self':
                        # this is a self function
                        return
                elif isinstance(func, astroid.node_classes.Name):
                    # this is a global function call
                    return
                self.add_message('chained-call', node=node, args=(name1, name2), )

            elif isinstance(expr, astroid.node_classes.Attribute):
                # call after an attribute
                name1 = expr.attrname
                if isinstance(expr.expr, astroid.node_classes.Name) and \
                              expr.expr.name=='self':
                    # this is a self function
                    return

                self.add_message('chained-call', node=node, args=(name1, name2), )


class ChainedPropertiesChecker(BaseChecker):
    """checks chain with attribute in the end."""

    __implements__ = IAstroidChecker

    # configuration section name
    name = 'nested-attribute'
    priority = -1
    msgs = {
        'R1252': ('Chained "%s" followed by attribute "%s"',
                  'chained-attribute',
                  'Object Calisthenics Rule 5'),
    }
    options = ()

    @check_messages('chained-attribute')
    def visit_attribute(self, node):
        """check attributes expr"""
        name2 = node.attrname

        expr = node.expr
        if isinstance(expr, astroid.node_classes.Attribute):
            name1 = expr.attrname
            expr = expr.expr

            if isinstance(expr, astroid.node_classes.Call):
                # attribute after another call
                self.add_message('chained-attribute', node=node, args=(name1, name2), )

            elif isinstance(expr, astroid.node_classes.Name):
                if expr.name == 'self':
                    # this is a self function
                    return
                # global or local name
                self.add_message('chained-attribute', node=node, args=(name1, name2), )

            elif isinstance(expr, astroid.node_classes.Attribute):
                # self.instance
                self.add_message('chained-attribute', node=node, args=(name1, name2), )


def register(linter):
    """required method to auto register this checker """
    linter.register_checker(ChainedCallsChecker(linter))
    linter.register_checker(ChainedPropertiesChecker(linter))
