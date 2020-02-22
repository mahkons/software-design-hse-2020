import unittest
from src.commands.ls import Ls


class LsTestCase(unittest.TestCase):
    def test_without_args(self):
        ls = Ls([])
        self.assertEqual("README.md\ndocs\nmain.py\nsrc\ntest", '\n'.join(sorted(ls.execute(None).split('\n'))))

    def test_with_args(self):
        ls = Ls(['test/resources', 'lol'])
        self.assertEqual("kek\nkeksik\nlong\nshort", '\n'.join(sorted(ls.execute(None).split('\n'))))

    def test_unknown_dir(self):
        ls = Ls(['kek', 'lol'])
        self.assertEqual("ls: kek: No such file or directory\n", ls.execute('kek'))

