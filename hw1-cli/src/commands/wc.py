from typing import List

from src.commands.command import Command


class Wc(Command):
    def __init__(self, args: List[str]):
        super().__init__(args)

    def execute(self, stdin) -> str:
        if len(self.args) == 0 and stdin is not None:
            return self._get_statistics(stdin)
        else:
            result = []
            for filename in self.args:
                try:
                    with open(self.args[0], 'r') as fin:
                        result.append(self._get_statistics(fin.read()) + ' ' + filename)
                except IOError as exception:
                    raise Exception("wc: " + exception)
            return '\n'.join(result)

    @staticmethod
    def _get_statistics(text) -> str:
        lines = text.count('\n') + 1
        words = len(text.split())
        chars = len(text)
        return f'    {lines}    {words}    {chars}'
