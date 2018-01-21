# -*- coding: utf-8 -*-
import re

import pytest

from mimesis import Path
from mimesis.data import FOLDERS, PROGRAMMING_LANGS, PROJECT_NAMES


class TestPath(object):
    def test_root(self, path):
        result = path.root()
        assert 'C:\\', '/' == result

    def test_home(self, path):
        result = path.home()
        assert 'С:\\Users\\', '/home/' == result

    def test_user(self, path):
        user = path.user()
        pattern_dictionary = {
            'win32': '(C)(:)(\\\\)(Users)(\\\\).*[^(\\\\)]',
            'linux': '(/)(home)(/).*',
        }
        if path.platform == 'win32':
            pattern = pattern_dictionary.get('win32')
        else:
            pattern = pattern_dictionary.get('linux')
        result = re.search(pattern, user)
        assert isinstance(result, type(re.search('', ''))) is True

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
    TIMES = 5

    @pytest.fixture
    def _paths(self, seed):
        return Path(seed=seed), Path(seed=seed)

    def test_root(self, _paths):
        p1, p2 = _paths
        for _ in range(self.TIMES):
            assert p1.root() == p2.root()

    def test_home(self, _paths):
        p1, p2 = _paths
        for _ in range(self.TIMES):
            assert p1.home() == p2.home()

    def test_user(self, _paths):
        p1, p2 = _paths
        for _ in range(self.TIMES):
            assert p1.user() == p2.user()

    def test_users_folder(self, _paths):
        p1, p2 = _paths
        for _ in range(self.TIMES):
            assert p1.users_folder() == p2.users_folder()

    def test_dev_dir(self, _paths):
        p1, p2 = _paths
        for _ in range(self.TIMES):
            assert p1.dev_dir() == p2.dev_dir()

    def test_project_dir(self, _paths):
        p1, p2 = _paths
        for _ in range(self.TIMES):
            assert p1.project_dir() == p2.project_dir()
