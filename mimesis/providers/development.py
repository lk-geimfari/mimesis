"""Data related to the development."""

import typing as t
from datetime import datetime

from mimesis.data import (
    LICENSES,
    OS,
    PROGRAMMING_LANGS,
    STAGES,
    SYSTEM_QUALITY_ATTRIBUTES,
)
from mimesis.enums import DSNType
from mimesis.providers.base import BaseProvider
from mimesis.providers.internet import Internet

__all__ = ["Development"]


class Development(BaseProvider):
    """Class for getting fake data for Developers."""

    def __init__(self, *args: t.Any, **kwargs: t.Any) -> None:
        super().__init__(*args, **kwargs)
        self._internet = Internet(
            random=self.random,
            *args,
            **kwargs,
        )
        self.__now = datetime.now()

    class Meta:
        name = "development"

    def dsn(self, dsn_type: DSNType | None = None, **kwargs: t.Any) -> str:
        """Generates a random DSN (Data Source Name).

        :param dsn_type: DSN type.
        :param kwargs: Additional arguments for Internet.hostname().
        """
        hostname = self._internet.hostname(**kwargs)
        scheme, port = self.validate_enum(dsn_type, DSNType)
        return f"{scheme}://{hostname}:{port}"

    def software_license(self) -> str:
        """Get a random software license.

        :return: License name.

        :Example:
            The BSD 3-Clause License.
        """
        return self.random.choice(LICENSES)

    def calver(self) -> str:
        """Generate a random calendar versioning string.

        :return: Calendar versioning string.

        :Example:
            2016.11.08
        """
        year = self.random.randint(2016, self.__now.year)
        month = self.random.randint(1, 12)
        day = self.random.randint(1, 29)
        return f"{year}.{month}.{day}"

    def version(self) -> str:
        """Generate a random semantic versioning string.

        :return: Semantic versioning string.

        :Example:
            0.2.1
        """
        major, minor, patch = self.random.randints(n=3, a=0, b=100)
        return f"{major}.{minor}.{patch}"

    def stage(self) -> str:
        """Generate a random stage of development.

        :return: Release stage.

        :Example:
            Alpha.
        """
        return self.random.choice(STAGES)

    def programming_language(self) -> str:
        """Get a random programming language from the list.

        :return: Programming language.

        :Example:
            Erlang.
        """
        return self.random.choice(PROGRAMMING_LANGS)

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
        return self.random.choice([True, False])

    def system_quality_attribute(self) -> str:
        """Get a random system quality attribute.

        Within systems engineering, quality attributes are realized
        non-functional requirements used to evaluate the performance
        of a system. These are sometimes named "ilities" after the
        suffix many of the words share.

        :return: System quality attribute.
        """
        return self.random.choice(SYSTEM_QUALITY_ATTRIBUTES)

    def ility(self) -> str:
        """Get a random system quality attribute.

        An alias for system_quality_attribute().
        """
        return self.system_quality_attribute()
