import sys

from src.environment import Environment
from src.executor import Executor
from src.parser.parser import Parser


class Interpreter(object):
    def __init__(self):
        self.environment = Environment()
        self.parser = Parser(self.environment)
        self.executor = Executor(self.environment)

    def interpret(self):
        while True:
            try:
                sys.stdout.write(f'{self._get_current_directory()}$ ')
                sys.stdout.flush()

                stdout = self.executor.execute(self.parser.parse(sys.stdin.readline()[:-1]))
                sys.stdout.write(stdout)
            except KeyboardInterrupt:
                sys.stdout.write('\n')

    def _get_current_directory(self):
        home = self.environment.get_variable('HOME')
        working_dir = self.environment.get_variable('PWD')
        if working_dir.find(home) == 0 and (len(home) == len(working_dir) or working_dir[len(home)] == '/'):
            working_dir = working_dir.replace(home, '~')
        return working_dir
