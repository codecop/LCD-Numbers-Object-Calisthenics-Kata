# see https://breadcrumbscollector.tech/writing-custom-checkers-for-pylint/
# see https://pylint.readthedocs.io/en/latest/how_tos/custom_checkers.html
from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker


class NoElseChecker(BaseChecker):
    __implements__ = IAstroidChecker

    name = 'no-else'
    priority = -1
    msgs = {
        'R1202': ('Don\'t use the ELSE keyword',
                  'if-has-else',
                  'Object Calisthenics Rule 2'),
    }
    options = ()

    def visit_if(self, node):
        if node.orelse:
            self.add_message('if-has-else', node=node)


def register(linter):
    linter.register_checker(NoElseChecker(linter))
