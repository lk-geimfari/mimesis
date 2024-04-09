"""Data related to the development."""

import typing as t
from datetime import datetime

from mimesis.datasets import (
    LICENSES,
    OS,
    PROGRAMMING_LANGS,
    STAGES,
    SYSTEM_QUALITY_ATTRIBUTES,
)
from mimesis.providers.base import BaseProvider

__all__ = ["Development"]


class Development(BaseProvider):
    """Class for getting fake data for Developers."""

    def __init__(self, *args: t.Any, **kwargs: t.Any) -> None:
        super().__init__(*args, **kwargs)

    class Meta:
        name = "development"

    def software_license(self) -> str:
        """Generates a random software license.

        :return: License name.

        :Example:
            The BSD 3-Clause License.
        """
        return self.random.choice(LICENSES)

    def calver(self) -> str:
        """Generates a random calendar versioning string.

        :return: Calendar versioning string.

        :Example:
            2016.11.08
        """
        year = self.random.randint(2016, datetime.now().year)
        month = self.random.randint(1, 12)
        day = self.random.randint(1, 29)
        return f"{year}.{month}.{day}"

    def version(self) -> str:
        """Generates a random semantic versioning string.

        :return: Semantic versioning string.

        :Example:
            0.2.1
        """
        major, minor, patch = self.random.randints(n=3, a=0, b=100)
        return f"{major}.{minor}.{patch}"

    def stage(self) -> str:
        """Generates a random stage of development.

        :return: Release stage.

        :Example:
            Alpha.
        """
        return self.random.choice(STAGES)

    def programming_language(self) -> str:
        """Generates a random programming language from the list.

        :return: Programming language.

        :Example:
            Erlang.
        """
        return self.random.choice(PROGRAMMING_LANGS)

    def os(self) -> str:
        """Generates a random operating system or distributive name.

        :return: The name of OS.

        :Example:
            Gentoo
        """
        return self.random.choice(OS)

    def boolean(self) -> bool:
        """Generates a random boolean value.

        :return: True of False.
        """
        return self.random.choice([True, False])

    def system_quality_attribute(self) -> str:
        """Generates a random system quality attribute.

        Within systems engineering, quality attributes are realized
        non-functional requirements used to evaluate the performance
        of a system. These are sometimes named "ilities" after the
        suffix many of the words share.

        :return: System quality attribute.
        """
        return self.random.choice(SYSTEM_QUALITY_ATTRIBUTES)

    def ility(self) -> str:
        """Generates a random system quality attribute.

        An alias for :meth:`~mimesis.Development.system_quality_attribute`.
        """
        return self.system_quality_attribute()
