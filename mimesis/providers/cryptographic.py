"""Pseudo-cryptographic data provider."""

import hashlib
from base64 import urlsafe_b64encode
from uuid import UUID

from mimesis.datasets.int.cryptographic import WORDLIST
from mimesis.enums import Algorithm
from mimesis.providers.base import BaseProvider

__all__ = ["Cryptographic"]


class Cryptographic(BaseProvider):
    """Class that provides **pseudo**-cryptographic data."""

    class Meta:
        name = "cryptographic"

    def uuid_object(self) -> UUID:
        """Generates UUID4 object.

        :return: UUID4 object.
        """
        rand_bits = self.random.getrandbits(128)
        return UUID(int=rand_bits, version=4)

    def uuid(self) -> str:
        """Generates UUID4 string.

        :return: UUID4 as string.
        """
        return str(self.uuid_object())

    def hash(self, algorithm: Algorithm | None = None) -> str:  # noqa: A003
        """Generates random hash.

        To change hashing algorithm, pass parameter ``algorithm``
        with needed value of the enum object :class:`~mimesis.enums.Algorithm`

        :param algorithm: Enum object :class:`~mimesis.enums.Algorithm`.
        :return: Hash.
        :raises NonEnumerableError: When algorithm is unsupported.
        """
        key = self.validate_enum(algorithm, Algorithm)
        func = getattr(hashlib, key)
        value = func(self.uuid().encode())
        return str(value.hexdigest())

    def token_bytes(self, entropy: int = 32) -> bytes:
        """Generates byte string containing ``entropy`` bytes.

        The string has ``entropy`` random bytes, each byte
        converted to two hex digits.

        :param entropy: Number of bytes (default: 32).
        :return: Random bytes.
        """
        return bytes([self.random.randint(0, 255) for _ in range(entropy)])

    def token_hex(self, entropy: int = 32) -> str:
        """Generates a random text string, in hexadecimal.

        The string has *entropy* random bytes, each byte converted to two
        hex digits.  If *entropy* is ``None`` or not supplied, a reasonable
        default is used.

        :param entropy: Number of bytes (default: 32).
        :return: Token.
        """
        return self.token_bytes(entropy).hex()

    def token_urlsafe(self, entropy: int = 32) -> str:
        """Generates a random URL-safe text string, in Base64 encoding.

        The string has *entropy* random bytes.  If *entropy* is ``None``
        or not supplied, a reasonable default is used.

        :param entropy: Number of bytes (default: 32).
        :return: URL-safe token.
        """
        token = self.token_bytes(entropy)
        return urlsafe_b64encode(token).rstrip(b"=").decode()

    def mnemonic_phrase(self) -> str:
        """Generates BIP-39 looking mnemonic phrase.

        :return: Mnemonic phrase.
        """
        length = self.random.choice([12, 24])
        phrases = self.random.choices(WORDLIST, k=length)
        return " ".join(phrases)
