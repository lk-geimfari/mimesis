# -*- coding: utf-8 -*-
import re

import pytest

from mimesis import Path
from mimesis.data import FOLDERS, PROGRAMMING_LANGS, PROJECT_NAMES


class TestPath(object):

    def test_root(self, path):
        result = path.root()
        assert result == 'C:\\' or result == '/'

    def test_home(self, path):
        result = path.home()
        assert result == 'C:\\Users' or result == '/home'

    def test_user(self, path):
        user = path.user()

        pattern = r'C:\\Users\\[A-Z].*' if path.platform == 'win32' \
                  else r'/home/[a-z].'

        result = re.search(pattern, user)
        assert result

    def directory_separator(self, path):
        slash_character = ''
        if path.platform == 'win32':
            slash_character = '\\'
        elif path.platform == 'linux':
            slash_character = '/'
        return slash_character

    def test_users_folder(self, path):
        folder = path.users_folder()
        folder = folder.split(self.directory_separator(path))
        assert len(folder) == 4
        assert folder[3] in FOLDERS

    def test_dev_dir(self, path):
        dev_dir = path.dev_dir()
        dev_dir = dev_dir.split(self.directory_separator(path))
        assert len(dev_dir) == 5
        assert dev_dir[4] in PROGRAMMING_LANGS

    def test_project_dir(self, path):
        project_path = path.project_dir()
        project_path = project_path.split(self.directory_separator(path))
        assert len(project_path) == 6
        assert project_path[5] in PROJECT_NAMES


class TestSeededPath(object):

    @pytest.fixture
    def p1(self, seed):
        return Path(seed=seed)

    @pytest.fixture
    def p2(self, seed):
        return Path(seed=seed)

    def test_root(self, p1, p2):
        assert p1.root() == p2.root()

    def test_home(self, p1, p2):
        assert p1.home() == p2.home()

    def test_user(self, p1, p2):
        assert p1.user() == p2.user()

    def test_users_folder(self, p1, p2):
        assert p1.users_folder() == p2.users_folder()

    def test_dev_dir(self, p1, p2):
        assert p1.dev_dir() == p2.dev_dir()

    def test_project_dir(self, p1, p2):
        assert p1.project_dir() == p2.project_dir()
