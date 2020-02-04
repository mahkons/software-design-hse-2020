import os
from typing import List, Optional
from src.commands.command import Command


class External(Command):
    def __init__(self, args: List[str]):
        super().__init__(args)

    def execute(self, stdin) -> Optional[str]:
        if len(self.args) == 0:
            return
        try:
            if stdin is None:
                proc = os.subprocess.run([self.args[0], *(self.args[1:])], stdout=os.subprocess.PIPE)
            else:
                proc = os.subprocess.run([self.args[0], *(self.args[1:])], stdout=os.subprocess.PIPE, input=stdin.encode('utf-8'))
        except os.subprocess.CalledProcessError as e:
            raise Exception(self.args[0] + ': ' + e.stderr.decode('utf-8'))
        except FileNotFoundError:
            raise Exception(self.args[0] + ': command not found')
        return proc.stdout.decode('utf-8')