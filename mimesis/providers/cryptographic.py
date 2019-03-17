# -*- coding: utf-8 -*-

"""Cryptographic data provider."""

import hashlib
import secrets
import uuid

from mimesis.enums import Algorithm
from mimesis.providers.base import BaseProvider
from mimesis.providers.text import Text

__all__ = ['Cryptographic']


class Cryptographic(BaseProvider):
    """Class that provides cryptographic data."""

    def __init__(self, *args, **kwargs) -> None:
        """Initialize attributes.

        :param seed: Seed.
        """
        super().__init__(*args, **kwargs)
        self.__words = Text('en')._data.get('words', {})

    class Meta:
        """Class for metadata."""

        name = 'cryptographic'

    def uuid(self, version: int = None) -> str:
        """Generate random UUID.

        :param version: UUID version.
        :return: UUID
        """
        bits = self.random.getrandbits(128)
        return str(uuid.UUID(int=bits, version=version))

    def hash(self, algorithm: Algorithm = None) -> str:  # noqa: A003
        """Generate random hash.

        To change hashing algorithm, pass parameter ``algorithm``
        with needed value of the enum object :class:`~mimesis.enums.Algorithm`

        :param algorithm: Enum object :class:`~mimesis.enums.Algorithm`.
        :return: Hash.
        :raises NonEnumerableError: if algorithm is not supported.
        """
        key = self._validate_enum(algorithm, Algorithm)

        if hasattr(hashlib, key):
            fn = getattr(hashlib, key)
            return fn(self.uuid().encode()).hexdigest()

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
    def token_urlsafe(entropy: int = 32):
        """Return a random URL-safe text string, in Base64 encoding.

        The string has *entropy* random bytes.  If *entropy* is ``None``
        or not supplied, a reasonable default is used.

        .. warning:: Seed is not applicable to this method,
            because of its cryptographic-safe nature.

        :param entropy: Number of bytes (default: 32).
        :return: URL-safe token.
        """
        return secrets.token_urlsafe(entropy)

    def mnemonic_phrase(self, length: int = 12) -> str:
        """Generate pseudo mnemonic phrase.

        :param length: Number of words.
        :return: Mnemonic code.
        """
        words = self.__words['normal']
        return ' '.join(self.random.choice(words) for _ in range(length))
