import sys
from typing import List
from src.commands.command import Command


class Exit(Command):
    """
    Exit command
    Exits shell
    """
    def __init__(self, args: List[str]):
        """
        Initializes command with args
        :param args: list of tokens
        """
        super().__init__(args)

    def execute(self, stdin) -> None:
        """
        Executes 'exit' command
        :param stdin: command input (always ignored)
        """
        sys.exit(0)
