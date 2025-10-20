"""Provides data related to paths."""

import sys
import typing as t
from pathlib import PurePosixPath, PureWindowsPath

from mimesis.datasets import (
    FOLDERS,
    PLATFORMS,
    PROGRAMMING_LANGS,
    PROJECT_NAMES,
    USERNAMES,
)
from mimesis.providers.base import BaseProvider

__all__ = ["Path"]


class Path(BaseProvider):
    """Class that provides methods and property for generate paths."""

    def __init__(
        self,
        platform: str = sys.platform,
        *args: t.Any,
        **kwargs: t.Any,
    ) -> None:
        """Initialize attributes.

        Supported platforms: 'linux', 'darwin', 'win32', 'win64', 'freebsd'.

        :param platform: Required platform type.
        """
        super().__init__(*args, **kwargs)
        if platform.startswith("freebsd"):
            platform = "freebsd"
        self.platform = platform
        self._pathlib_home = (
            PureWindowsPath() if platform.startswith("win") else PurePosixPath()
        )
        self._pathlib_home /= PLATFORMS[platform]["home"]

    class Meta:
        name = "path"

    def root(self) -> str:
        """Generates a root dir path.

        :return: Root dir.

        :Example:
            /
        """
        return str(self._pathlib_home.parent)

    def home(self) -> str:
        """Generates a home path.

        :return: Home path.

        :Example:
            /home
        """
        return str(self._pathlib_home)

    def user(self) -> str:
        """Generates a random user.

        :return: Path to user.

        :Example:
            /home/oretha
        """
        user = self.random.choice(USERNAMES)
        user = user.capitalize() if self.platform.startswith("win") else user.lower()
        return str(self._pathlib_home / user)

    def users_folder(self) -> str:
        """Generates a random path to user's folders.

        :return: Path.

        :Example:
            /home/taneka/Pictures
        """
        user = self.user()
        folder = self.random.choice(FOLDERS)
        return str(self._pathlib_home / user / folder)

    def dev_dir(self) -> str:
        """Generates a random path to development directory.

        :return: Path.

        :Example:
            /home/sherrell/Development/Python
        """
        user = self.user()
        folder = self.random.choice(["Development", "Dev"])
        stack = self.random.choice(PROGRAMMING_LANGS)
        return str(self._pathlib_home / user / folder / stack)

    def project_dir(self) -> str:
        """Generates a random path to project directory.

        :return: Path to project.

        :Example:
            /home/sherika/Development/Falcon/mercenary
        """
        dev_dir = self.dev_dir()
        project = self.random.choice(PROJECT_NAMES)
        return str(self._pathlib_home / dev_dir / project)
