import sys
from typing import Union

from mimesis.data import (FOLDERS, PLATFORMS, PROGRAMMING_LANGS, PROJECT_NAMES,
                          USERNAMES)
from mimesis.providers.base import BaseProvider


class Path(BaseProvider):
    """Class that provides methods and property for generate paths."""

    def __init__(self, platform: str = sys.platform, *args, **kwargs) -> None:
        """
        :param str platform:
            Required platform type ('linux2', 'darwin', 'win32', 'win64').
            Supported platforms: mimesis/constant/platforms.py
        """
        super().__init__(*args, **kwargs)
        self.platform = platform

    def root(self) -> Union[str, None]:
        """Generate a root dir path.

        :return: Root dir.
        :rtype: str or None

        :Example:
            /
        """
        for platform in PLATFORMS:
            if self.platform == PLATFORMS[platform]['name']:
                root = PLATFORMS[platform]['root']
                return root
        return None

    def home(self) -> Union[str, None]:
        """Generate a home path.

        :return: Home path.
        :rtype: str or None

        :Example:
            /home/
        """
        for platform in PLATFORMS:
            if self.platform == PLATFORMS[platform]['name']:
                home = PLATFORMS[platform]['home']
                return home
        return None

    def user(self) -> Union[str, None]:
        """Generate a random user.

        :return: Path to user.
        :rtype: str or None
        :Example:
            /home/oretha
        """
        user = self.random.choice(USERNAMES)
        user = user.capitalize() if \
            self.platform == 'win32' else user.lower()
        return '{home}{user}'.format(
            home=self.home(),
            user=user,
        )

    def users_folder(self) -> Union[str, None]:
        """Generate a random path to user's folders.

        :return: Path.
        :rtype: str or None

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
        return None

    def dev_dir(self) -> Union[str, None]:
        """Generate a random path to development directory.

        :return: Path.
        :rtype: str or None

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
        return None

    def project_dir(self) -> Union[str, None]:
        """Generate a random path to project directory.

        :return: Path to project.
        :rtype: str or None

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
        return None
