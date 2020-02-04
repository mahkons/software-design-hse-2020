from typing import List, Tuple, Optional

from src.CLI_exception import CLIException
from src.commands.command import Command


class Wc(Command):
    def __init__(self, args: List[str]):
        super().__init__(args)

    def execute(self, stdin) -> str:
        if len(self.args) == 0 and stdin is not None:
            return self._get_formatted_statistics(*self._get_statistics(stdin))
        else:
            result = []
            total_lines = total_words = total_chars = 0
            for filename in self.args:
                try:
                    with open(self.args[0], 'r') as fin:
                        lines, words, chars = self._get_statistics(fin.read())
                        result.append(self._get_formatted_statistics(lines, words, chars, filename) + ' ' + filename)
                        total_lines += lines
                        total_words += words
                        total_chars += chars
                except IOError as exception:
                    raise CLIException("wc: " + exception)
            if len(self.args) > 1:
                result.append(self._get_formatted_statistics(total_lines, total_words, total_chars, 'total'))
            return '\n'.join(result)

    @staticmethod
    def _get_statistics(text: str) -> Tuple[int, int, int]:
        lines = text.count('\n') + 1
        words = len(text.split())
        chars = len(text)
        return lines, words, chars

    @staticmethod
    def _get_formatted_statistics(lines: int, words: int, chars: int, name: Optional[str] = None) -> str:
        if name is not None:
            return f'    {lines}    {words}    {chars} {name}'
        else:
            return f'    {lines}    {words}    {chars}'
