from mimesis.data import (BACKEND, CONTAINER, FRONTEND, LICENSES, NOSQL, OS,
                          PROGRAMMING_LANGS, SQL)
from mimesis.providers.base import BaseProvider


class Development(BaseProvider):
    """Class for getting fake data for Developers."""

    def software_license(self) -> str:
        """Get a random software license from list.

        :return: License name.
        :rtype: str

        :Example:
            The BSD 3-Clause License.
        """
        return self.random.choice(LICENSES)

    def version(self) -> str:
        """Generate a random version information.

        :return: The version of software.
        :rtype: str

        :Example:
            0.11.3.
        """
        n = (self.random.randint(0, 11) for _ in range(3))
        return '{}.{}.{}'.format(*n)

    def database(self, nosql: bool = False) -> str:
        """Get a random database name.

        :param bool nosql: only NoSQL databases.
        :return: Database name.
        :rtype: str

        :Example:
            PostgreSQL.
        """
        if nosql:
            return self.random.choice(NOSQL)
        return self.random.choice(SQL)

    def container(self) -> str:
        """Get a random containerization system.

        :return: Containerization system.
        :rtype: str

        :Example:
            Docker.
        """
        return self.random.choice(CONTAINER)

    def version_control_system(self) -> str:
        """Get a random version control system.

        :return: Version control system
        :rtype: str

        :Example:
            Git
        """
        return self.random.choice(['Git', 'Subversion'])

    def programming_language(self) -> str:
        """Get a random programming language from the list.

        :return: Programming language.
        :rtype: str

        :Example:
            Erlang.
        """
        return self.random.choice(PROGRAMMING_LANGS)

    def backend(self) -> str:
        """Get a random backend stack.

        :return: Stack.
        :rtype: str

        :Example:
            Elixir/Phoenix
        """
        return self.random.choice(BACKEND)

    def frontend(self) -> str:
        """Get a random front-end stack.

        :return: Stack.
        :rtype: str

        :Example:
            JS/React.
        """
        return self.random.choice(FRONTEND)

    def os(self) -> str:
        """Get a random operating system or distributive name.

        :return: The name of OS.
        :rtype: str

        :Example:
            Gentoo
        """
        return self.random.choice(OS)

    def stackoverflow_question(self) -> str:
        """Generate a random question id for StackOverFlow
        and return url to a question.

        :return: URL to a question.
        :rtype: str

        :Example:
            http://stackoverflow.com/questions/1726403
        """
        post_id = self.random.randint(1000000, 9999999)
        url = 'http://stackoverflow.com/questions/{0}'
        return url.format(post_id)
