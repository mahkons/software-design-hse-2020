import os
from typing import List, Optional
from src.commands.command import Command


class Ls(Command):
    """
    Ls command
    List directories and files in directory specified by first argument if there is any
    or current directory otherwise
    """
    def __init__(self, args: List[str]):
        """
        Initializes command with args
        :param args: list of tokens
        """
        super(Ls, self).__init__(args)

    def execute(self, stdin: Optional[str]) -> str:
        """
        Executes 'ls' command with given input (input is always ignored)
        :param stdin: command input
        return concatenated list of directories and files
        """
        if len(self.args) == 0:
            dirs = os.listdir()
        else:
            dirs = os.listdir(self.args[0])

        delimiter = '\n'
        return delimiter.join(dirs)

