"""Cryptographic data provider."""

import hashlib
import secrets
from uuid import UUID, uuid4

from mimesis.datasets.int.cryptographic import WORDLIST
from mimesis.enums import Algorithm
from mimesis.providers.base import BaseProvider

__all__ = ["Cryptographic"]


class Cryptographic(BaseProvider):
    """Class that provides cryptographic data."""

    class Meta:
        name = "cryptographic"

    @staticmethod
    def uuid_object() -> UUID:
        """Generates UUID4 object.

        :return: UUID4 object.
        """
        return uuid4()

    def uuid(self) -> str:
        """Generates UUID4 string.

        :return: UUID4 as string.
        """
        return str(self.uuid_object())

    def hash(self, algorithm: Algorithm | None = None) -> str:  # noqa: A003
        """Generates random hash.

        To change hashing algorithm, pass parameter ``algorithm``
        with needed value of the enum object :class:`~mimesis.enums.Algorithm`

        .. warning:: Seed is not applicable to this method,
            because of its cryptographic-safe nature.

        :param algorithm: Enum object :class:`~mimesis.enums.Algorithm`.
        :return: Hash.
        :raises NonEnumerableError: When algorithm is unsupported.
        """
        key = self.validate_enum(algorithm, Algorithm)
        func = getattr(hashlib, key)
        value = func(self.uuid().encode())
        return str(value.hexdigest())

    @staticmethod
    def token_bytes(entropy: int = 32) -> bytes:
        """Generates byte string containing ``entropy`` bytes.

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
        """Generates a random text string, in hexadecimal.

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
        """Generates a random URL-safe text string, in Base64 encoding.

        The string has *entropy* random bytes.  If *entropy* is ``None``
        or not supplied, a reasonable default is used.

        .. warning:: Seed is not applicable to this method,
            because of its cryptographic-safe nature.

        :param entropy: Number of bytes (default: 32).
        :return: URL-safe token.
        """
        return secrets.token_urlsafe(entropy)

    def mnemonic_phrase(self) -> str:
        """Generates BIP-39 looking mnemonic phrase.

        :return: Mnemonic phrase.
        """
        length = self.random.choice([12, 24])
        phrases = self.random.choices(WORDLIST, k=length)
        return " ".join(phrases)
