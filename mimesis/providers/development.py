from mimesis.data import (BACKEND, CONTAINER, FRONTEND, LICENSES, NOSQL, OS,
                          PROGRAMMING_LANGS, SQL)
from mimesis.providers.base import BaseProvider


class Development(BaseProvider):
    """Class for getting fake data for Developers."""

    def software_license(self) -> str:
        """Get a random software license from list.

        :return: License name.

        :Example:
            The BSD 3-Clause License.
        """
        return self.random.choice(LICENSES)

    def version(self, pre_release: bool = False) -> str:
        """Generate a random version information.

        :param pre_release: Pre-release.
        :return: The version of software.

        :Example:
            0.11.3-alpha.1
        """
        major, minor, patch = self.random.randints(3, 0, 10)
        version = '{}.{}.{}'.format(major, minor, patch)

        if pre_release:
            suffixes = ('alpha', 'beta', 'rc')
            suffix = self.random.choice(suffixes)
            number = self.random.randint(1, 11)
            return '{}-{}.{}'.format(version, suffix, number)

        return version

    def database(self, nosql: bool = False) -> str:
        """Get a random database name.

        :param bool nosql: only NoSQL databases.
        :return: Database name.

        :Example:
            PostgreSQL.
        """
        if nosql:
            return self.random.choice(NOSQL)
        return self.random.choice(SQL)

    def container(self) -> str:
        """Get a random containerization system.

        :return: Containerization system.

        :Example:
            Docker.
        """
        return self.random.choice(CONTAINER)

    def version_control_system(self) -> str:
        """Get a random version control system.

        :return: Version control system

        :Example:
            Git
        """
        vcs = ('Git', 'Subversion')
        return self.random.choice(vcs)

    def programming_language(self) -> str:
        """Get a random programming language from the list.

        :return: Programming language.

        :Example:
            Erlang.
        """
        return self.random.choice(PROGRAMMING_LANGS)

    def backend(self) -> str:
        """Get a random backend stack.

        :return: Stack.

        :Example:
            Elixir/Phoenix
        """
        return self.random.choice(BACKEND)

    def frontend(self) -> str:
        """Get a random front-end stack.

        :return: Stack.

        :Example:
            JS/React.
        """
        return self.random.choice(FRONTEND)

    def os(self) -> str:
        """Get a random operating system or distributive name.

        :return: The name of OS.

        :Example:
            Gentoo
        """
        return self.random.choice(OS)

    def boolean(self) -> bool:
        """Get a random boolean value.

        :return: True of False.
        """
        values = (0, 1)
        value = self.random.choice(values)
        return bool(value)
