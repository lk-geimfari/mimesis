# -*- coding: utf-8 -*-

"""Cryptographic data provider."""

import hashlib
import secrets
from typing import Any, Final, Optional
from uuid import UUID, uuid4

from mimesis.enums import Algorithm
from mimesis.locales import Locale
from mimesis.providers.base import BaseProvider
from mimesis.providers.text import Text

__all__ = ["Cryptographic"]


class Cryptographic(BaseProvider):
    """Class that provides cryptographic data."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize attributes.

        :param seed: Seed.
        """
        super().__init__(*args, **kwargs)
        self._text = Text(locale=Locale.EN, seed=self.seed)

    class Meta:
        """Class for metadata."""

        name: Final[str] = "cryptographic"

    @staticmethod
    def uuid_object() -> UUID:
        """Generate UUID4 object.

        :return: UUID4 object.
        """
        return uuid4()

    def uuid(self) -> str:
        """Generate UUID4 string.

        :return: UUID4 as string.
        """
        return str(self.uuid_object())

    def hash(self, algorithm: Optional[Algorithm] = None) -> str:  # noqa: A003
        """Generate random hash.

        To change hashing algorithm, pass parameter ``algorithm``
        with needed value of the enum object :class:`~mimesis.enums.Algorithm`

        .. warning:: Seed is not applicable to this method,
            because of its cryptographic-safe nature.

        :param algorithm: Enum object :class:`~mimesis.enums.Algorithm`.
        :return: Hash.
        :raises NonEnumerableError: When algorithm is unsupported.
        """
        key = self.validate_enum(algorithm, Algorithm)

        if hasattr(hashlib, key):
            fn = getattr(hashlib, key)
            return fn(self.uuid().encode()).hexdigest()  # type: ignore

    @staticmethod
    def token_bytes(entropy: int = 32) -> bytes:
        """Generate byte string containing ``entropy`` bytes.

        The string has ``entropy`` random bytes, each byte
        converted to two hex digits.

        .. warning:: Seed is not applicable to this method,
            because of its cryptographic-safe nature.

        :param entropy: Number of bytes (default: 32).
        :return: Random bytes.
        """
        return secrets.token_bytes(entropy)

    @staticmethod
    def token_hex(entropy: int = 32) -> str:
        """Return a random text string, in hexadecimal.

        The string has *entropy* random bytes, each byte converted to two
        hex digits.  If *entropy* is ``None`` or not supplied, a reasonable
        default is used.

        .. warning:: Seed is not applicable to this method,
            because of its cryptographic-safe nature.

        :param entropy: Number of bytes (default: 32).
        :return: Token.
        """
        return secrets.token_hex(entropy)

    @staticmethod
    def token_urlsafe(entropy: int = 32) -> str:
        """Return a random URL-safe text string, in Base64 encoding.

        The string has *entropy* random bytes.  If *entropy* is ``None``
        or not supplied, a reasonable default is used.

        .. warning:: Seed is not applicable to this method,
            because of its cryptographic-safe nature.

        :param entropy: Number of bytes (default: 32).
        :return: URL-safe token.
        """
        return secrets.token_urlsafe(entropy)

    def mnemonic_phrase(self, length: int = 12, separator: Optional[str] = None) -> str:
        """Generate pseudo mnemonic phrase.

        Please, keep in mind that this method generates
        crypto-insecure values.

        :param separator: Separator of phrases (Default is " ").
        :param length: Number of words.
        :return: Mnemonic phrase.
        """
        if not separator:
            separator = " "

        words = self._text.words(quantity=length)
        return "{}".format(separator).join(words)
