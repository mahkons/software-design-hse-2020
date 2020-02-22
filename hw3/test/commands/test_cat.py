import unittest
from src.commands.cat import Cat


class CatTestCase(unittest.TestCase):

    short_file_path = 'test/resources/short'
    long_file_path = 'test/resources/long'

    def test_short_stdin(self):
        cat = Cat([])
        stdin = 'kek'
        self.assertEqual(stdin, cat.execute(stdin))

    def test_long_stdin(self):
        cat = Cat([])
        stdin = 'kek\nlol\narbidol'
        self.assertEqual(stdin, cat.execute(stdin))

    def test_short_file(self):
        cat = Cat([self.short_file_path])
        with open(self.short_file_path, 'r') as f:
            self.assertEqual(f.read(), cat.execute(None))

    def test_long_file(self):
        cat = Cat([self.long_file_path])
        with open(self.long_file_path, 'r') as f:
            self.assertEqual(f.read(), cat.execute(None))

    def test_several_files(self):
        cat = Cat([self.short_file_path, self.long_file_path])
        with open(self.short_file_path, 'r') as f1, open(self.long_file_path, 'r') as f2:
            self.assertEqual(f1.read() + f2.read(), cat.execute(None))

    def test_directory(self):
        directory_path = 'test/resources'
        cat = Cat([directory_path])
        self.assertEqual('cat: test/resources: Is a directory\n', cat.execute(None))

    def test_file_not_exist(self):
        file_path = 'kek'
        cat = Cat([file_path])
        self.assertEqual('cat: kek: No such file or directory\n', cat.execute(None))
