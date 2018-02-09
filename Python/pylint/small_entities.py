"""checks for Object Calisthenics rule 7: Small entities."""

from astroid import If
from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker


class SmallEntitiesChecker(BaseChecker):
    """checks for classes to be smaller than number of statements."""
    # copied from Pylint's MisdesignChecker in design_analysis.py

    __implements__ = IAstroidChecker

    # configuration section name
    name = 'small-entities'
    priority = -1
    msgs = {
        'R1271': ('Large entity "%s" (%s/%s statements)',
                  'large-entity',
                  'Object Calisthenics Rule 7'),
    }
    options = ()

    def __init__(self, linter=None):
        BaseChecker.__init__(self, linter)
        self._max_class_statements = 45  # TODO lazy config
        self._statements = 0

    def visit_classdef(self, node):  # pylint: disable=unused-argument
        """reset statements counter"""
        self._statements = 0

    # @check_messages('large-entity')
    def leave_classdef(self, node):
        """check number of overall statements"""

        # stop here for exception, metaclass and interface classes
        if node.type != 'class':
            return

        # check number of statements
        if self._statements > self._max_class_statements:
            self.add_message('large-entity', node=node,
                             args=(node.name, self._statements, self._max_class_statements))

    def visit_default(self, node):
        """default visit method increments the statements counter if
        necessary
        """
        if node.is_statement:
            self._statements += 1

    def visit_tryexcept(self, node):
        """increments the statements counter for each branch"""
        branches = len(node.handlers)
        if node.orelse:
            branches += 1
        self._statements += branches

    def visit_tryfinally(self, node):  # pylint: disable=unused-argument
        """increments the statements counter"""
        self._statements += 2

    def visit_if(self, node):
        """increments the statements counter for each branch"""
        branches = 1
        # don't double count If nodes coming from some 'elif'
        if node.orelse and (len(node.orelse) > 1 or
                            not isinstance(node.orelse[0], If)):
            branches += 1
        self._statements += branches


class SmallModulesChecker(BaseChecker):
    """checks for modules with less than number of classes."""

    __implements__ = IAstroidChecker

    # configuration section name
    name = 'small-modules'
    priority = -1
    msgs = {
        'R1272': ('Large module "%s" (%s/%s classes)',
                  'large-module',
                  'Object Calisthenics Rule 7'),
    }
    options = ()

    def __init__(self, linter=None):
        BaseChecker.__init__(self, linter)
        self._max_classes = 10  # TODO lazy config
        self._classes = 0

    def visit_module(self, node):  # pylint: disable=unused-argument
        """reset class counter"""
        self._classes = 0

    def leave_module(self, node):
        """check number of overall classes"""

        # check number of statements
        if self._classes > self._max_classes:
            self.add_message('large-module', node=node,
                             args=(node.name, self._classes, self._max_classes))

    def visit_classdef(self, node):  # pylint: disable=unused-argument
        """increments the class counter"""
        self._classes += 1


def register(linter):
    """required method to auto register this checker """
    linter.register_checker(SmallEntitiesChecker(linter))
    linter.register_checker(SmallModulesChecker(linter))
