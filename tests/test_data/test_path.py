# -*- coding: utf-8 -*-
import os
from unittest.mock import patch

from elizabeth.data import FOLDERS, PROGRAMMING_LANGS, PROJECT_NAMES


def test_root(path):
    platform_patcher = patch('sys.platform', 'win32')
    platform_patcher.start()
    assert 'С:\\' == path.root
    platform_patcher.stop()

    platform_patcher = patch('sys.platform', 'linux2')
    platform_patcher.start()
    assert '/' == path.root
    platform_patcher.stop()


def test_home(path):
    platform_patcher = patch('sys.platform', 'win32')
    platform_patcher.start()
    assert 'С:\\Users\\' == path.home
    platform_patcher.stop()

    platform_patcher = patch('sys.platform', 'linux2')
    platform_patcher.start()
    assert '/home/' == path.home
    platform_patcher.stop()


def test_user(path):
    user = path.user(gender='female')
    result = user.split(os.sep)
    assert len(result) == 3


def test_users_folder(path):
    folder = path.users_folder(user_gender='female')
    folder = folder.split(os.sep)
    assert len(folder) == 4
    assert folder[3] in FOLDERS


def test_dev_dir(path):
    dev_dir = path.dev_dir(user_gender='female')
    # /home/yajaira/Development/Lua
    dev_dir = dev_dir.split(os.sep)
    assert len(dev_dir) == 5
    assert dev_dir[4] in PROGRAMMING_LANGS


def test_project_dir(path):
    project_path = path.project_dir(user_gender='female')
    project_path = project_path.split(os.sep)
    assert len(project_path) == 6
    # /home/sherika/Development/Falcon/mercenary
    assert project_path[5] in PROJECT_NAMES
