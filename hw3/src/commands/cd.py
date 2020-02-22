import os
from typing import List, Optional
from src.commands.command import Command


class Cd(Command):
    """
    Cd command
    Changes current directory to first argument, or $HOME  if arglist is empty
    """
    def __init__(self, args: List[str]):
        """
        Initializes command with args
        :param args: list of tokens
        """
        super(Cd, self).__init__(args)

    def execute(self, stdin: Optional[str]) -> str:
        """
        Executes 'cd' command with given input (input is always ignored)
        :param stdin: command input
        """
        if len(self.args) == 0:
            os.chdir("~")
        else:
            os.chdir(self.args[0])
