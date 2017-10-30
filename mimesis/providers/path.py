import sys
from typing import Union

from mimesis.constants.platforms import PLATFORMS
from mimesis.data import FOLDERS, PROGRAMMING_LANGS, PROJECT_NAMES, USERNAMES
from mimesis.providers.base import BaseProvider


class Path(BaseProvider):
    """Class that provides methods and property for generate paths."""

    def __init__(self, platform: str = sys.platform, *args, **kwargs) -> None:
        """
        :param platform:
            Required platform type ('linux2', 'darwin', 'win32', 'win64').
            Supported platforms: mimesis/constant/platforms.py
        """
        super().__init__(*args, **kwargs)
        self.platform = platform

    def root(self) -> Union[str, None]:
        """Generate a root dir path.

        :return: Root dir.
        :rtype: types.Union[str, None]

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
        :rtype: types.Union[str, None]
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
        :rtype: types.Union[str, None]
        :Example:
            /home/oretha
        """
        user = self.random.choice(USERNAMES)
        user = user.capitalize() if \
            self.platform == 'win32' else user.lower()
        return self.home() + user

    def users_folder(self) -> Union[str, None]:
        """Generate a random path to user's folders.

        :return: Path.
        :rtype: types.Union[str, None]
        :Example:
            /home/taneka/Pictures
        """
        folder = self.random.choice(FOLDERS)
        user = self.user()
        for platform in PLATFORMS:
            if self.platform == PLATFORMS[platform]['name']:
                path_separator = PLATFORMS[platform]['path_separator']
                users_folder = (user + '{}' + folder).format(path_separator)
                return users_folder

    def dev_dir(self) -> Union[str, None]:
        """Generate a random path to development directory.

        :return: Path.
        :rtype: str

        :Example:
            /home/sherrell/Development/Python/mercenary
        """
        dev_folder = self.random.choice(['Development', 'Dev'])
        stack = self.random.choice(PROGRAMMING_LANGS)
        user = self.user()
        for platform in PLATFORMS:
            if self.platform == PLATFORMS[platform]['name']:
                path_separator = PLATFORMS[platform]['path_separator']
                dev_dir = (
                    user + '{}' + dev_folder + '{}' + stack
                ).format(path_separator, path_separator)
                return dev_dir

    def project_dir(self) -> Union[str, None]:
        """Generate a random path to project directory.

        :return: Path to project.
        :rtype: str

        :Example:
            /home/sherika/Development/Falcon/mercenary
        """
        project = self.random.choice(PROJECT_NAMES)
        for platform in PLATFORMS:
            if self.platform == PLATFORMS[platform]['name']:
                path_separator = PLATFORMS[platform]['path_separator']
                project_dir = (
                    self.dev_dir() + '{}' + project
                ).format(path_separator)
                return project_dir
