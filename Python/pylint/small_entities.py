from astroid import If
from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker


class SmallEntitiesChecker(BaseChecker):
    """checks for Object Calisthenics rule 7: Small entities
    """
    # copied from Pylint's MisdesignChecker in design_analysis.py

    __implements__ = IAstroidChecker

    # configuration section name
    name = 'small-entities'
    priority = -1
    msgs = {
        'R1207': ('Large entity "%s" (%s/%s statements)',
                  'large-entity',
                  'Object Calisthenics Rule 7'),
    }
    options = ()

    def __init__(self, linter=None):
        BaseChecker.__init__(self, linter)
        self._max_class_statements = 45 # config
        self._stmts = 0

    def visit_classdef(self, node):
        """reset statements counter"""
        self._stmts = 0

    # @check_messages('large-entity')
    def leave_classdef(self, node):
        """check number of overall statements"""

        # stop here for exception, metaclass and interface classes
        if node.type != 'class':
            return

        # check number of statements
        if self._stmts > self._max_class_statements:
            self.add_message('large-entity', node=node,
                             args=(node.name, self._stmts, self._max_class_statements))

    def visit_default(self, node):
        """default visit method increments the statements counter if
        necessary
        """
        if node.is_statement:
            self._stmts += 1

    def visit_tryexcept(self, node):
        """increments the statements counter for each branch"""
        branches = len(node.handlers)
        if node.orelse:
            branches += 1
        self._stmts += branches

    def visit_tryfinally(self, node):
        """increments the statements counter"""
        self._stmts += 2

    def visit_if(self, node):
        """increments the statements counter for each branch"""
        branches = 1
        # don't double count If nodes coming from some 'elif'
        if node.orelse and (len(node.orelse) > 1 or
                            not isinstance(node.orelse[0], If)):
            branches += 1
        self._stmts += branches


def register(linter):
    linter.register_checker(SmallEntitiesChecker(linter))
