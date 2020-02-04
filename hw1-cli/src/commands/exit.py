import sys
from typing import List
from src.commands.command import Command


class Exit(Command):
    def __init__(self, args: List[str]):
        super().__init__(args)

    def execute(self, stdin) -> None:
        sys.exit(0)
