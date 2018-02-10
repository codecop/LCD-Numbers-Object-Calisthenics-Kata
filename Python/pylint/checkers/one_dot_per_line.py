"""checks for Object Calisthenics rule 5: One dot per line."""

from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker


class OneDotPerLineChecker(BaseChecker):
    """TODO."""

    __implements__ = IAstroidChecker

    # configuration section name
    name = 'xno-else'
    priority = -1
    msgs = {
        'R1251': ('TODO ',
                  'xif-has-else',
                  'Object Calisthenics Rule 5'),
    }
    options = ()

    # @check_messages('if-has-else')
    # def visit_if(self, node):
    #     """check if for else"""
    #     if node.orelse:
    #         self.add_message('if-has-else', node=node)


def register(linter):
    """required method to auto register this checker """
    linter.register_checker(OneDotPerLineChecker(linter))
