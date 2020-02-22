import unittest
from src.commands.ls import Ls


class LsTestCase(unittest.TestCase):
    def test_without_args(self):
        ls = Ls([])
        self.assertEqual("docs\nsrc\nREADME.md\nmain.py\ntest", ls.execute(None))

    def test_with_args(self):
        ls = Ls(['test/resources', 'lol'])
        self.assertEqual("kek\nkeksik\nshort\nlong", ls.execute(None))

    def test_unknown_dir(self):
        ls = Ls(['kek', 'lol'])
        self.assertEqual("ls: kek: No such file or directory\n", ls.execute('kek'))
