import unittest
from src.commands.cat import Cat


class CatTestCase(unittest.TestCase):
    def test_short_stdin(self):
        cat = Cat([])
        stdin = 'kek'
        self.assertEqual(stdin, cat.execute(stdin))

    def test_long_stdin(self):
        cat = Cat([])
        stdin = 'kek\nlol\narbidol'
        self.assertEqual(stdin, cat.execute(stdin))

    def test_short_file(self):
        short_file_path = '../resources/short'
        cat = Cat([short_file_path])
        stdin = open(short_file_path, 'r').read()
        self.assertEqual(stdin, cat.execute(None))

    def test_long_file(self):
        long_file_path = '../resources/long'
        cat = Cat([long_file_path])
        stdin = open(long_file_path, 'r').read()
        self.assertEqual(stdin, cat.execute(None))

    def test_several_files(self):
        short_file_path = '../resources/short'
        long_file_path = '../resources/long'
        cat = Cat([short_file_path, long_file_path])
        stdin1 = open(short_file_path, 'r').read()
        stdin2 = open(long_file_path, 'r').read()
        self.assertEqual(stdin1 + stdin2, cat.execute(None))
