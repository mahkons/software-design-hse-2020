import re
from typing import List

from src.commands.cat import Cat
from src.commands.echo import Echo
from src.commands.exit import Exit
from src.commands.external import External
from src.commands.pwd import Pwd
from src.commands.wc import Wc
from src.environment import Environment


class Executor(object):
    ASSIGNMENT_PATTERN = r'[a-zA-Z]+?=\w*'

    COMMANDS = {'cat': Cat,
                'echo': Echo,
                'exit': Exit,
                'pwd': Pwd,
                'wc': Wc}

    def __init__(self, environment: Environment):
        self.environment = environment

    def execute(self, commands: List[List[str]]):
        if len(commands) == 1 and len(commands[0]) == 1 and re.match(self.ASSIGNMENT_PATTERN, commands[0][0]):
            name, value = commands[0][0].split('=')
            self.environment.set_variable(name, value)

        stdin = None
        for command in commands[::-1]:
            status, new_stdin = self._call_command(command, stdin)
            if not status:
                return new_stdin
            else:
                stdin = new_stdin
        if stdin is not None:
            return

    def _call_command(self, command: List[str], stdin: str) -> (bool, str):
        try:
            if command[0] in self.COMMANDS.keys():
                builtin = self.COMMANDS[command[0]](command[1:])
                new_stdin = builtin.execute(stdin)
            else:
                external = External(command)
                new_stdin = external.execute(stdin)
        except Exception as exception:
            return False, exception
        return True, new_stdin
