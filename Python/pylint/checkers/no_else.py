"""checks for Object Calisthenics rule 2: Don't use the ELSE keyword."""

# see https://breadcrumbscollector.tech/writing-custom-checkers-for-pylint/
# see https://pylint.readthedocs.io/en/latest/how_tos/custom_checkers.html
from pylint.checkers import BaseChecker
from pylint.checkers.utils import check_messages
from pylint.interfaces import IAstroidChecker


class NoElseChecker(BaseChecker):
    """checks for else keyword."""

    __implements__ = IAstroidChecker

    # configuration section name
    name = 'no-else'
    priority = -1
    msgs = {
        'R1221': ('Don\'t use the ELSE keyword',
                  'if-has-else',
                  'Object Calisthenics Rule 2'),
    }
    options = ()

    @check_messages('if-has-else')
    def visit_if(self, node):
        """check if for else"""
        if node.orelse:
            self.add_message('if-has-else', node=node)


def register(linter):
    """required method to auto register this checker """
    linter.register_checker(NoElseChecker(linter))
