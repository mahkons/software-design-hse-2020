from typing import List

from src.commands.command import Command


class Cat(Command):

    def __init__(self, args: List[str]):
        super().__init__(args)

    def execute(self, stdin) -> str:
        if len(self.args) == 0 and stdin is not None:
            return stdin
        try:
            with open(self.args[0], 'r') as fin:
                return fin.read()
        except IOError as exception:
            raise Exception("cat: " + exception)
