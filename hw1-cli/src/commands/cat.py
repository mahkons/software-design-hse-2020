import os
from typing import List, Optional

from src.commands.command import Command


class Cat(Command):

    def __init__(self, args: List[str]):
        super().__init__(args)

    def execute(self, stdin: Optional[str]) -> str:
        if len(self.args) == 0 and stdin is not None:
            return stdin
        result = ''
        for filename in self.args:
            if os.path.isfile(filename):
                with open(filename, 'r') as fin:
                    result += fin.read()
            elif os.path.isdir(filename):
                result += f'cat: {filename}: Is a directory\n'
            else:
                result += f'cat: {filename}: No such file or directory\n'
        return result
