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
            os.chdir(os.path.expanduser("~"))
        else:
            dirname = self.args[0]
            if os.path.isdir(dirname):
                os.chdir(dirname)
            elif os.path.isfile(dirname):
                return f'cd: {dirname}: Is a file'
            else:
                return f'cd: {dirname}: No such file or directory\n'
        return ''
