from src.parser.splitter import Splitter
from src.parser.expander import Expander
from src.environment import Environment, List


class Parser(object):
    def __init__(self, environment: Environment):
        self.environment = environment

    def parse(self, expression: str) -> List[List[str]]:
        expander = Expander(self.environment)
        splitter = Splitter()
        return splitter.split(expander.expand(expression))