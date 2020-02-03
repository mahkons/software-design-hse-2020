import os
from typing import *


class Environment(object):
    def __init__(self, variables=None):
        if variables is None:
            variables = dict()
        self.variables: Dict[str, str] = variables

    def set_variable(self, name: str, value: str) -> None:
        self.variables[name] = value

    def get_variable(self, name: str) -> str:
        if self.variables.get(name) is not None:
            return self.variables.get(name)
        elif os.environ.get(name) is not None:
            return os.environ.get(name)
        else:
            raise Exception("Variable not found: " + name)

