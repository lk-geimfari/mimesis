import os
import sys

from mimesis.data import FOLDERS, PROGRAMMING_LANGS, PROJECT_NAMES
from mimesis.providers import BaseProvider
from mimesis.providers.personal import Personal


class Path(BaseProvider):
    """Class that provides methods and property for generate paths."""

    def __init__(self, *args, **kwargs):
        # TODO: platform should be a parameter
        super().__init__(*args, **kwargs)
        self.__p = Personal('en')

    @property
    def root(self):
        """Generate a root dir path.

        :return: Root dir.
        :Example:
            /
        """
        if sys.platform == 'win32':
            return 'С:\\'
        else:
            return '/'

    @property
    def home(self):
        """Generate a home path.

        :return: Home path.
        :Example:
            /home/
        """
        if sys.platform == 'win32':
            return self.root + 'Users\\'
        else:
            return self.root + 'home/'

    def user(self, gender='female'):
        """Generate a random user.

        :param gender: Gender of user.
        :return: Path to user.
        :Example:
            /home/oretha
        """
        user = self.__p.name(gender)
        user = user.capitalize() if \
            sys.platform == 'win32' else user.lower()
        return self.home + user

    def users_folder(self, user_gender='female'):
        """Generate a random path to user's folders.

        :return: Path.
        :Example:
            /home/taneka/Pictures
        """
        folder = self.random.choice(FOLDERS)
        user = self.user(user_gender)
        return os.path.join(user, folder)

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

        return os.path.join(user, dev_folder, stack)

    def project_dir(self, user_gender='female'):
        """Generate a random path to project directory.

        :param user_gender: Gender of user.
        :return: Path to project.
        :Example:
            /home/sherika/Development/Falcon/mercenary
        """
        project = self.random.choice(PROJECT_NAMES)
        return os.path.join(
            self.dev_dir(user_gender), project)
