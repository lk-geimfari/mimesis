# -*- coding: utf-8 -*-
import re

from mimesis.data import FOLDERS, PROGRAMMING_LANGS, PROJECT_NAMES


def test_root(path):
    result = path.root()
    assert 'C:\\', '/' == result


def test_home(path):
    result = path.home()
    assert 'С:\\Users\\', '/home/' == result


def test_user(path):
    user = path.user()
    pattern_dictionary = {
        'win32': '(C)(:)(\\\\)(Users)(\\\\).*[^(\\\\)]',
        'linux2': '(/)(home)(/).*',
    }
    if path.platform == 'win32':
        pattern = pattern_dictionary.get('win32')
    else:
        pattern = pattern_dictionary.get('linux2')
    result = re.search(pattern, user)
    assert isinstance(result, type(re.search('', ''))) is True


def directory_separator(path):
    slash_character = ''
    if path.platform == 'win32':
        slash_character = '\\'
    elif path.platform == 'linux2':
        slash_character = '/'
    return slash_character


def test_users_folder(path):
    folder = path.users_folder()
    folder = folder.split(directory_separator(path))
    assert len(folder) == 4
    assert folder[3] in FOLDERS


def test_dev_dir(path):
    dev_dir = path.dev_dir()
    dev_dir = dev_dir.split(directory_separator(path))
    assert len(dev_dir) == 5
    assert dev_dir[4] in PROGRAMMING_LANGS


def test_project_dir(path):
    project_path = path.project_dir()
    project_path = project_path.split(directory_separator(path))
    assert len(project_path) == 6
    assert project_path[5] in PROJECT_NAMES
