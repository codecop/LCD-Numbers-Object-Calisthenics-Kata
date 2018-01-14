from pylint.checkers import BaseChecker
from pylint.checkers.utils import check_messages
from pylint.interfaces import IAstroidChecker


class SmallEntitiesChecker(BaseChecker):
    """checks for sign of poor/misdesign:
    * number of methods, attributes, local variables...
    * size, complexity of functions, methods
    """
    # see Pylint's MisdesignChecker in design_analysis.py

    __implements__ = IAstroidChecker

    # configuration section name
    name = 'small-entities'
    msgs = MSGS
    priority = -1
    options = (('max-args',
                {'default': 5, 'type': 'int', 'metavar': '<int>',
                 'help': 'Maximum number of arguments for function / method'}
                ),
               ('max-locals',
                {'default': 15, 'type': 'int', 'metavar': '<int>',
                 'help': 'Maximum number of locals for function / method body'}
                ),
               ('max-returns',
                {'default': 6, 'type': 'int', 'metavar': '<int>',
                 'help': 'Maximum number of return / yield for function / '
                         'method body'}
                ),
               ('max-branches',
                {'default': 12, 'type': 'int', 'metavar': '<int>',
                 'help': 'Maximum number of branch for function / method body'}
                ),
               ('max-statements',
                {'default': 50, 'type': 'int', 'metavar': '<int>',
                 'help': 'Maximum number of statements in function / method '
                         'body'}
                ),
               ('max-parents',
                {'default': 7,
                 'type': 'int',
                 'metavar': '<num>',
                 'help': 'Maximum number of parents for a class (see R0901).'}
                ),
               ('max-attributes',
                {'default': 7,
                 'type': 'int',
                 'metavar': '<num>',
                 'help': 'Maximum number of attributes for a class \
(see R0902).'}
                ),
               ('min-public-methods',
                {'default': 2,
                 'type': 'int',
                 'metavar': '<num>',
                 'help': 'Minimum number of public methods for a class \
(see R0903).'}
                ),
               ('max-public-methods',
                {'default': 20,
                 'type': 'int',
                 'metavar': '<num>',
                 'help': 'Maximum number of public methods for a class \
(see R0904).'}
                ),
               ('max-bool-expr',
                {'default': 5,
                 'type': 'int',
                 'metavar': '<num>',
                 'help': 'Maximum number of boolean expressions in a if '
                         'statement'}
                ),
               )

    def __init__(self, linter=None):
        BaseChecker.__init__(self, linter)
        self._stmts = 0

    @check_messages('too-many-ancestors', 'too-many-instance-attributes',
                    'too-few-public-methods', 'too-many-public-methods')
    def visit_classdef(self, node):
        """check size of inheritance hierarchy and number of instance attributes
        """
        nb_parents = len(list(node.ancestors()))
        if nb_parents > self.config.max_parents:
            self.add_message('too-many-ancestors', node=node,
                             args=(nb_parents, self.config.max_parents))

        if len(node.instance_attrs) > self.config.max_attributes:
            self.add_message('too-many-instance-attributes', node=node,
                             args=(len(node.instance_attrs),
                                   self.config.max_attributes))

    @check_messages('too-few-public-methods', 'too-many-public-methods')
    def leave_classdef(self, node):
        """check number of public methods"""

        # stop here for exception, metaclass and interface classes
        if node.type != 'class':
            return
        pass

    @check_messages('too-many-return-statements', 'too-many-branches',
                    'too-many-arguments', 'too-many-locals',
                    'too-many-statements', 'keyword-arg-before-vararg')
    def visit_functiondef(self, node):
        """check function name, docstring, arguments, redefinition,
        variable names, max locals
        """
        # init branch and returns counters
        self._returns.append(0)
        # check number of arguments
        args = node.args.args
        ignored_argument_names = self._ignored_argument_names
        if args is not None:
            ignored_args_num = 0
            if ignored_argument_names:
                ignored_args_num = sum(1 for arg in args if ignored_argument_names.match(arg.name))

            argnum = len(args) - ignored_args_num
            if argnum > self.config.max_args:
                self.add_message('too-many-arguments', node=node,
                                 args=(len(args), self.config.max_args))
        else:
            ignored_args_num = 0
        # check number of local variables
        locnum = len(node.locals) - ignored_args_num
        if locnum > self.config.max_locals:
            self.add_message('too-many-locals', node=node,
                             args=(locnum, self.config.max_locals))
        # init statements counter
        self._stmts = 1

    visit_asyncfunctiondef = visit_functiondef

    @check_messages('too-many-return-statements', 'too-many-branches',
                    'too-many-arguments', 'too-many-locals',
                    'too-many-statements')
    def leave_functiondef(self, node):
        """most of the work is done here on close:
        checks for max returns, branch, return in __init__
        """
        returns = self._returns.pop()
        if returns > self.config.max_returns:
            self.add_message('too-many-return-statements', node=node,
                             args=(returns, self.config.max_returns))
        branches = self._branches[node]
        if branches > self.config.max_branches:
            self.add_message('too-many-branches', node=node,
                             args=(branches, self.config.max_branches))
        # check number of statements
        if self._stmts > self.config.max_statements:
            self.add_message('too-many-statements', node=node,
                             args=(self._stmts, self.config.max_statements))

    leave_asyncfunctiondef = leave_functiondef

    def visit_return(self, _):
        """count number of returns"""
        if not self._returns:
            return  # return outside function, reported by the base checker
        self._returns[-1] += 1

    def visit_default(self, node):
        """default visit method -> increments the statements counter if
        necessary
        """
        if node.is_statement:
            self._stmts += 1

    def visit_tryexcept(self, node):
        """increments the branches counter"""
        branches = len(node.handlers)
        if node.orelse:
            branches += 1
        self._inc_branch(node, branches)
        self._stmts += branches

    def visit_tryfinally(self, node):
        """increments the branches counter"""
        self._inc_branch(node, 2)
        self._stmts += 2

    @check_messages('too-many-boolean-expressions')
    def visit_if(self, node):
        """increments the branches counter and checks boolean expressions"""
        self._check_boolean_expressions(node)
        branches = 1
        # don't double count If nodes coming from some 'elif'
        if node.orelse and (len(node.orelse) > 1 or
                                not isinstance(node.orelse[0], If)):
            branches += 1
        self._inc_branch(node, branches)
        self._stmts += branches

    def _check_boolean_expressions(self, node):
        """Go through "if" node `node` and counts its boolean expressions

        if the "if" node test is a BoolOp node
        """
        condition = node.test
        if not isinstance(condition, BoolOp):
            return
        nb_bool_expr = _count_boolean_expressions(condition)
        if nb_bool_expr > self.config.max_bool_expr:
            self.add_message('too-many-boolean-expressions', node=condition,
                             args=(nb_bool_expr, self.config.max_bool_expr))



def register(linter):
    linter.register_checker(SmallEntitiesChecker(linter))
