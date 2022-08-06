"""Data related to the development."""

import typing as t

from mimesis.data import LICENSES, OS, PROGRAMMING_LANGS, PROJECT_NAMES
from mimesis.enums import DSNType, TLDType
from mimesis.providers.base import BaseProvider
from mimesis.providers.internet import Internet

__all__ = ["Development"]


class Development(BaseProvider):
    """Class for getting fake data for Developers."""

    def __init__(self, *args: t.Any, **kwargs: t.Any) -> None:
        super().__init__(*args, **kwargs)
        self._internet = Internet(*args, **kwargs)

    class Meta:
        """Class for metadata."""

        name: t.Final[str] = "development"

    def dsn(self, dsn_type: t.Optional[DSNType] = None, **kwargs: t.Any) -> str:
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

    def version(self, calver: bool = False, pre_release: bool = False) -> str:
        """Generate version number.

        :param calver: Calendar versioning.
        :param pre_release: Pre-release.
        :return: Version.

        :Example:
            0.2.1
        """
        if calver:
            major = self.random.randint(2016, 2018)
            minor, patch = self.random.randints(2, 1, 10)
        else:
            major, minor, patch = self.random.randints(3, 0, 10)

        version = f"{major}.{minor}.{patch}"

        if pre_release:
            suffix = self.random.choice(("alpha", "beta", "rc"))
            number = self.random.randint(1, 11)
            version = f"{version}-{suffix}.{number}"

        return version

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
