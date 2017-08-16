import sys

from mimesis.data import FOLDERS, PROGRAMMING_LANGS, PROJECT_NAMES
from mimesis.providers import BaseProvider
from mimesis.providers.personal import Personal
from mimesis.constants.platforms import PLATFORMS


class Path(BaseProvider):
    """Class that provides methods and property for generate paths."""
    def __init__(self, platform=sys.platform, *args, **kwargs):
        """
        :param platform: Required platform type ('linux2', 'darwin', 'win32',
        'win64').
        Supported platforms: mimesis/constant/platforms.py
        """
        super().__init__(*args, **kwargs)
        self.__p = Personal('en')
        self.platform = platform

    def root(self):
        """Generate a root dir path.

        :return: Root dir.
        :Example:
            /
        """
        for platform in PLATFORMS:
            if self.platform == PLATFORMS[platform]['name']:
                root = PLATFORMS[platform]['root']
                return root

    def home(self):
        """Generate a home path.

        :return: Home path.
        :Example:
            /home/
        """
        for platform in PLATFORMS:
            if self.platform == PLATFORMS[platform]['name']:
                home = PLATFORMS[platform]['home']
                return home

    def user(self, gender='female'):
        """Generate a random user.

        :param gender: Gender of user.
        :return: Path to user.
        :Example:
            /home/oretha
        """
        user = self.__p.name(gender)
        user = user.capitalize() if \
            self.platform == 'win32' else user.lower()
        return self.home() + user

    def users_folder(self, user_gender='female'):
        """Generate a random path to user's folders.

        :return: Path.
        :Example:
            /home/taneka/Pictures
        """
        folder = self.random.choice(FOLDERS)
        user = self.user(user_gender)
        for platform in PLATFORMS:
            if self.platform == PLATFORMS[platform]['name']:
                path_separator = PLATFORMS[platform]['path_separator']
                users_folder = (user + '{}' + folder).format(path_separator)
                return users_folder

    def dev_dir(self, user_gender='female'):
        """Generate a random path to development directory.

        :param user_gender: Path to dev directory.
        :return: Path.
        :Example:
            /home/sherrell/Development/Python/mercenary
        """
        dev_folder = self.random.choice(['Development', 'Dev'])
        stack = self.random.choice(PROGRAMMING_LANGS)
        user = self.user(user_gender)
        for platform in PLATFORMS:
            if self.platform == PLATFORMS[platform]['name']:
                path_separator = PLATFORMS[platform]['path_separator']
                dev_dir = (
                    user + '{}' + dev_folder + '{}' + stack
                ).format(path_separator, path_separator)
                return dev_dir

    def project_dir(self, user_gender='female'):
        """Generate a random path to project directory.

        :param user_gender: Gender of user.
        :return: Path to project.
        :Example:
            /home/sherika/Development/Falcon/mercenary
        """
        project = self.random.choice(PROJECT_NAMES)
        for platform in PLATFORMS:
            if self.platform == PLATFORMS[platform]['name']:
                path_separator = PLATFORMS[platform]['path_separator']
                project_dir = (
                    self.dev_dir(user_gender) + '{}' + project
                ).format(path_separator)
                return project_dir
