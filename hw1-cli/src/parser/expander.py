import re

from src.environment import Environment
from src.parser.parse_utils import find_in_double_quotes


class Expander(object):
    def __init__(self, environment: Environment):
        self.environment = environment

    def expand(self, expression: str) -> str:
        return self._expand_variables(expression)

    def _expand_variables(self, expression: str) -> str:
        for index in find_in_double_quotes(expression, '$')[::-1]:
            name = ''
            i = index + 1
            while i < len(expression) and re.match(r'[a-z]|[A-Z]|[0-9]|_', expression[i]):
                name += expression[i]
                i += 1
            expression = expression[:index] + self.environment.get_variable(name) + expression[index + len(name) + 1:]
        return expression
