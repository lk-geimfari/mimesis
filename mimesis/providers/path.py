# -*- coding: utf-8 -*-

"""Provides data related to paths."""

import sys
from pathlib import PurePosixPath, PureWindowsPath

from mimesis.data import (
    FOLDERS,
    PLATFORMS,
    PROGRAMMING_LANGS,
    PROJECT_NAMES,
    USERNAMES,
)
from mimesis.providers.base import BaseProvider

__all__ = ['Path']


class Path(BaseProvider):
    """Class that provides methods and property for generate paths."""

    def __init__(self, platform: str = sys.platform, *args, **kwargs) -> None:
        """Initialize attributes.

        Supported platforms: 'linux', 'darwin', 'win32', 'win64'.

        :param platform: Required platform type.
        """
        super().__init__(*args, **kwargs)
        self.platform = platform
        self._pathlib_home = PureWindowsPath() if 'win' in platform \
                             else PurePosixPath()
        self._pathlib_home /= PLATFORMS[platform]['home']

    class Meta:
        """Class for metadata."""

        name = 'path'

    def root(self) -> str:
        """Generate a root dir path.

        :return: Root dir.

        :Example:
            /
        """
        return str(self._pathlib_home.parent)

    def home(self) -> str:
        """Generate a home path.

        :return: Home path.

        :Example:
            /home
        """
        return str(self._pathlib_home)

    def user(self) -> str:
        """Generate a random user.

        :return: Path to user.

        :Example:
            /home/oretha
        """
        user = self.random.choice(USERNAMES)
        user = user.capitalize() if 'win' in self.platform else user.lower()
        return str(self._pathlib_home / user)

    def users_folder(self) -> str:
        """Generate a random path to user's folders.

        :return: Path.

        :Example:
            /home/taneka/Pictures
        """
        user = self.user()
        folder = self.random.choice(FOLDERS)
        return str(self._pathlib_home / user / folder)

    def dev_dir(self) -> str:
        """Generate a random path to development directory.

        :return: Path.

        :Example:
            /home/sherrell/Development/Python
        """
        user = self.user()
        folder = self.random.choice(['Development', 'Dev'])
        stack = self.random.choice(PROGRAMMING_LANGS)
        return str(self._pathlib_home / user / folder / stack)

    def project_dir(self) -> str:
        """Generate a random path to project directory.

        :return: Path to project.

        :Example:
            /home/sherika/Development/Falcon/mercenary
        """
        dev_dir = self.dev_dir()
        project = self.random.choice(PROJECT_NAMES)
        return str(self._pathlib_home / dev_dir / project)
