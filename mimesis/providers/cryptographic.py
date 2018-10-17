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

        :Example:

        >>> crypto = Cryptographic()
        >>> uid = crypto.uuid()
        >>> len(uid) == 36
        True
        """
        bits = self.random.getrandbits(128)
        return str(uuid.UUID(int=bits, version=version))

    def hash(self, algorithm: Optional[Algorithm] = None) -> str:  # noqa: A003
        """Generate random hash.

        To change hashing algorithm, pass parameter ``algorithm``
        with needed value of the enum object :class:`~mimesis.enums.Algorithm`

        :param algorithm: Enum object :class:`~mimesis.enums.Algorithm`.
        :return: Hash.
        :raises NonEnumerableError: if algorithm is not supported.

        :Example:

        >>> crypto = Cryptographic()
        >>> md5 = crypto.hash(Algorithm.MD5)
        >>> len(md5) == 32
        True
        >>> sha1 = crypto.hash(Algorithm.SHA1)
        >>> len(sha1) == 40
        True
        >>> sha224 = crypto.hash(Algorithm.SHA224)
        >>> len(sha224) == 56
        True
        >>> sha256 = crypto.hash(Algorithm.SHA256)
        >>> len(sha256) == 64
        True
        >>> sha384 = crypto.hash(Algorithm.SHA384)
        >>> len(sha384) == 96
        True
        >>> sha512 = crypto.hash(Algorithm.SHA512)
        >>> len(sha512) == 128
        True
        """
        key = self._validate_enum(algorithm, Algorithm)

        if hasattr(hashlib, key):
            fn = getattr(hashlib, key)
            return fn(self.uuid().encode()).hexdigest()

    def bytes(self, entropy: int = 32) -> Bytes:  # noqa: A003
        """Generate byte string containing ``entropy`` bytes.

        The string has ``entropy`` random bytes, each byte
        converted to two hex digits.

        :param entropy: Number of bytes.
        :return: Bytes.

        :Example:

        >>> crypto = Cryptographic()
        >>> _bytes = crypto.bytes(entropy=8)
        >>> len(_bytes) == 8
        True
        """
        return bytes(self.random.getrandbits(8)
                     for _ in range(entropy))

    def token(self, entropy: int = 32) -> str:
        """Generate hexadecimal string.

        :param entropy: Number of bytes.
        :return: Token.

        :Example:

        >>> crypto = Cryptographic()
        >>> token = crypto.token(entropy=32)
        >>> len(token) == 64
        True
        """
        return self.bytes(entropy).hex()

    def salt(self, size: int = 16) -> str:
        """Generate salt chars (not cryptographically safe).

        :param size: Salt size.
        :return: Salt.

        :Example:

        >>> crypto = Cryptographic()
        >>> salt = crypto.salt(size=128)
        >>> len(salt) == 128
        True
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

        :Example:

        >>> crypto = Cryptographic()
        >>> phrase = crypto.mnemonic_phrase(length=2)
        >>> phrases = phrase.split(' ')
        >>> len(phrases) == 2
        True
        """
        words = self.__words['normal']
        return ' '.join(self.random.choice(words) for _ in range(length))
