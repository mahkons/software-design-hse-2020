from typing import List
from src.commands.command import Command


class Echo(Command):
    def __init__(self, args: List[str]):
        super().__init__(args)

    def execute(self, stdin) -> str:
        return ' '.join(self.args) + '\n'
