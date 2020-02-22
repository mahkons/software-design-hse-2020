import unittest
import mock
import os
from pyfakefs import fake_filesystem_unittest

from src.commands import Cd


class CdTestCase(fake_filesystem_unittest.TestCase):
    def setUp(self):
        self.setUpPyfakefs()
        os.makedirs(os.path.expanduser("~"))
        os.makedirs("/a/b")

    def test_without_args(self):
        cd = Cd([])
        self.assertEqual("", cd.execute(None))
        self.assertEqual(os.path.expanduser("~"), os.getcwd())

    def test_with_args(self):
        cd = Cd(['a/b', 'lol'])
        self.assertEqual("", cd.execute(None))
        self.assertEqual("/a/b", os.getcwd())

    def test_unknown_dir(self):
        cd = Cd(['kek', 'lol'])
        self.assertEqual("cd: kek: No such file or directory\n", cd.execute('kek'))
        self.assertEqual("/", os.getcwd())

