"""Cryptographic data provider."""

import hashlib
import string
import uuid
from typing import Optional

from mimesis.enums import Algorithm
from mimesis.providers.base import BaseDataProvider
from mimesis.providers.text import Text
from mimesis.typing import Bytes

__all__ = ['Cryptographic']


class Cryptographic(BaseDataProvider):
    """Class that provides cryptographic data."""

    def __init__(self, *args, **kwargs) -> None:
        """Initialize attributes.

        :param seed: Seed.
        """
        super().__init__(*args, **kwargs)
        self.__words = Text('en')._data['words']
        self.__chars = string.ascii_letters + string.digits + string.punctuation

    def uuid(self, version: Optional[int] = None) -> str:
        """Generate random UUID.

        :param version: UUID version.
        :return: UUID
        """
        bits = self.random.getrandbits(128)
        return str(uuid.UUID(int=bits, version=version))

    def hash(self, algorithm: Optional[Algorithm] = None) -> str:
        """Generate random hash.

        :param algorithm: Enum object ``Algorithm``.
        :return: Hash.
        :raises NonEnumerableError: if algorithm is not supported.
        """
        key = self._validate_enum(algorithm, Algorithm)

        if hasattr(hashlib, key):
            fn = getattr(hashlib, key)
            return fn(self.uuid().encode()).hexdigest()

    def bytes(self, entropy: int = 32) -> Bytes:
        """Generate byte string containing *entropy* bytes.

        The string has *entropy* random bytes, each byte
        converted to two hex digits.

        :param entropy: Number of bytes.
        :return: Bytes.
        :rtype: bytes
        """
        return bytes(self.random.getrandbits(8)
                     for _ in range(entropy))

    def token(self, entropy: int = 32) -> str:
        """Generate hexadecimal string.

        :param entropy: Number of bytes.
        :return: Token.
        """
        return self.bytes(entropy).hex()

    def salt(self, size: int = 16) -> str:
        """Generate salt chars (not cryptographically safe).

        :param size: Salt size.
        :return: Salt.
        """
        char_sequence = [
            self.random.choice(self.__chars)
            for _ in range(size)
        ]
        return ''.join(char_sequence)

    def mnemonic_phrase(self, length: int = 12) -> str:
        """Generate pseudo mnemonic phrase.

        :param length: Number of words.
        :return: Mnemonic code.
        """
        words = self.__words['normal']
        return ' '.join(self.random.choice(words) for _ in range(length))
