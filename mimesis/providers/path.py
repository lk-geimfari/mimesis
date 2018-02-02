"""Provides data related to paths."""

import sys
from typing import Union

from mimesis.data import (FOLDERS, PLATFORMS, PROGRAMMING_LANGS, PROJECT_NAMES,
                          USERNAMES)
from mimesis.providers.base import BaseDataProvider

__all__ = ['Path']


class Path(BaseDataProvider):
    """Class that provides methods and property for generate paths."""

    def __init__(self, platform: str = sys.platform, *args, **kwargs) -> None:
        """Initialize attributes.

        Supported platforms: 'linux', 'darwin', 'win32', 'win64'.

        :param platform: Required platform type.
        """
        super().__init__(*args, **kwargs)
        self.platform = platform

    def root(self) -> Union[str, None]:
        """Generate a root dir path.

        :return: Root dir.

        :Example:
            /
        """
        for platform in PLATFORMS:
            if self.platform == PLATFORMS[platform]['name']:
                root = PLATFORMS[platform]['root']
                return root

    def home(self) -> Union[str, None]:
        """Generate a home path.

        :return: Home path.

        :Example:
            /home/
        """
        for platform in PLATFORMS:
            if self.platform == PLATFORMS[platform]['name']:
                home = PLATFORMS[platform]['home']
                return home

    def user(self) -> Union[str, None]:
        """Generate a random user.

        :return: Path to user.

        :Example:
            /home/oretha
        """
        user = self.random.choice(USERNAMES)
        user = user.capitalize() if \
            self.platform == 'win32' else user.lower()
        return '{}{}'.format(self.home(), user)

    def users_folder(self) -> Union[str, None]:
        """Generate a random path to user's folders.

        :return: Path.

        :Example:
            /home/taneka/Pictures
        """
        folder = self.random.choice(FOLDERS)
        user = self.user()
        for platform in PLATFORMS:
            if self.platform == PLATFORMS[platform]['name']:
                sep = PLATFORMS[platform]['path_separator']
                return '{user}{sep}{folder}'.format(
                    user=user,
                    sep=sep,
                    folder=folder,
                )

    def dev_dir(self) -> Union[str, None]:
        """Generate a random path to development directory.

        :return: Path.

        :Example:
            /home/sherrell/Development/Python/mercenary
        """
        folder = self.random.choice(['Development', 'Dev'])
        stack = self.random.choice(PROGRAMMING_LANGS)
        for platform in PLATFORMS:
            if self.platform == PLATFORMS[platform]['name']:
                sep = PLATFORMS[platform]['path_separator']
                return '{user}{sep}{folder}{sep}{stack}'.format(
                    user=self.user(),
                    sep=sep,
                    folder=folder,
                    stack=stack,
                )

    def project_dir(self) -> Union[str, None]:
        """Generate a random path to project directory.

        :return: Path to project.

        :Example:
            /home/sherika/Development/Falcon/mercenary
        """
        project = self.random.choice(PROJECT_NAMES)
        dev_dir = self.dev_dir()
        for platform in PLATFORMS:
            if self.platform == PLATFORMS[platform]['name']:
                sep = PLATFORMS[platform]['path_separator']

                return '{dev_dir}{sep}{project}'.format(
                    dev_dir=dev_dir,
                    sep=sep,
                    project=project,
                )
