"""checks for Object Calisthenics rule 7: Small entities."""

from astroid import If
from pylint.checkers import BaseChecker
from pylint.checkers.utils import check_messages
from pylint.interfaces import IAstroidChecker


class SmallEntitiesChecker(BaseChecker):
    """checks for classes and modules to be smaller than number of statements."""
    # copied from Pylint's MisdesignChecker in design_analysis.py

    __implements__ = IAstroidChecker

    # configuration section name
    name = 'small-entities'
    priority = -1
    msgs = {
        'R1271': ('Large entity "%s" (%s/%s statements)',
                  'large-entity',
                  'Object Calisthenics Rule 7'),
        'R1272': ('Large module "%s" (%s/%s statements)',
                  'large-module',
                  'Object Calisthenics Rule 7'),
    }
    options = ()

    def __init__(self, linter=None):
        BaseChecker.__init__(self, linter)
        self._max_class_statements = 45  # TODO lazy config
        self._module_statements = 0
        self._class_statements = 0

    def visit_module(self, node):  # pylint: disable=unused-argument
        """reset module statements counter"""
        self._module_statements = 0

    @check_messages('large-module')
    def leave_module(self, node):
        """check number of module statements"""
        if self._module_statements > self._max_class_statements:
            self.add_message('large-module', node=node,
                             args=(node.name, self._module_statements, self._max_class_statements))

    def visit_classdef(self, node):  # pylint: disable=unused-argument
        """reset class statements counter"""
        self._class_statements = 0

    @check_messages('large-entity')
    def leave_classdef(self, node):
        """check number of class statements"""

        # do not count class stuff inside module
        self._module_statements -= self._class_statements

        # stop here for exception, metaclass and interface classes
        if node.type != 'class':
            return

        # check number of statements
        if self._class_statements > self._max_class_statements:
            self.add_message('large-entity', node=node,
                             args=(node.name, self._class_statements, self._max_class_statements))

    def visit_default(self, node):
        """default visit method increments the statements counter"""
        if node.is_statement:
            self._inc(1)

    def visit_tryexcept(self, node):
        """increments the statements counter for each branch"""
        branches = len(node.handlers)
        if node.orelse:
            branches += 1
        self._inc(branches)

    def visit_tryfinally(self, node):  # pylint: disable=unused-argument
        """increments the statements counter"""
        self._inc(2)

    def visit_if(self, node):
        """increments the statements counter for each branch"""
        branches = 1
        # don't double count If nodes coming from some 'elif'
        if node.orelse and (len(node.orelse) > 1 or
                            not isinstance(node.orelse[0], If)):
            branches += 1
        self._inc(branches)

    def _inc(self, branches):
        self._class_statements += branches
        self._module_statements += branches


class SmallModulesChecker(BaseChecker):
    """checks for modules to have less than number of classes."""

    __implements__ = IAstroidChecker

    # configuration section name
    name = 'small-modules'
    priority = -1
    msgs = {
        'R1273': ('Too many classes in module "%s" (%s/%s classes)',
                  'too-many-classes',
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

    @check_messages('too-many-classes')
    def leave_module(self, node):
        """check number of overall classes"""

        # check number of statements
        if self._classes > self._max_classes:
            self.add_message('too-many-classes', node=node,
                             args=(node.name, self._classes, self._max_classes))

    def visit_classdef(self, node):  # pylint: disable=unused-argument
        """increments the class counter"""
        self._classes += 1


def register(linter):
    """required method to auto register this checker """
    linter.register_checker(SmallEntitiesChecker(linter))
    linter.register_checker(SmallModulesChecker(linter))
