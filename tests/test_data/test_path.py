# -*- coding: utf-8 -*-
import os
import sys
from unittest import TestCase

from elizabeth.core.elizabeth import Path
import elizabeth.core.interdata as common


class PathTest(TestCase):
    def setUp(self):
        self.path = Path()

    def tearDown(self):
        del self.path

    def test_root(self):
        root = self.path.root

        if sys.platform == 'win32':
            self.assertEqual('С:\\', root)
        else:
            self.assertEqual('/', '/')

    def test_home(self):
        if sys.platform == 'win32':
            self.assertEqual('С:\\Users\\', self.path.home)
        else:
            self.assertEqual('/home/', self.path.home)

    def test_user(self):
        user = self.path.user(gender='female')
        result = user.split(os.sep)
        self.assertTrue(len(result) == 3)

    def test_users_folder(self):
        folder = self.path.users_folder(user_gender='female')
        folder = folder.split(os.sep)
        self.assertTrue(len(folder) == 4)
        self.assertIn(folder[3], common.FOLDERS)

    def test_dev_dir(self):
        dev_dir = self.path.dev_dir(user_gender='female')
        # /home/yajaira/Development/Lua
        dev_dir = dev_dir.split(os.sep)
        self.assertTrue(len(dev_dir) == 5)
        self.assertIn(dev_dir[4], common.PROGRAMMING_LANGS)

    def test_project_dir(self):
        project_path = self.path.project_dir(user_gender='female')
        project_path = project_path.split(os.sep)
        self.assertTrue(len(project_path) == 6)
        # /home/sherika/Development/Falcon/mercenary
        self.assertIn(project_path[5], common.PROJECT_NAMES)
