"""Pseudo-cryptographic data provider."""

import hashlib
import json
import time
import typing as t
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

    def jwt(
        self, payload: dict[str, t.Any] | None = None, algorithm: str = "HS256"
    ) -> str:
        """Generate JWT-like token structure for testing.

        :param payload: JWT payload (claims).
        :param algorithm: JWT algorithm (default: HS256).
            If None, generates default payload.
        :return: JWT-like token string.

        Example:

            >>> from mimesis import Cryptographic
            >>> crypto = Cryptographic()
            >>> crypto.jwt()
            'eyJhbGc...'
            >>> crypto.jwt(payload={'user_id': 123, 'role': 'admin'})
            'eyJhbGc...'
        """
        header = {
            "alg": algorithm,
            "typ": "JWT",
        }

        if payload is None:
            payload = {
                "sub": self.uuid(),
                "name": "Test User",
                "iat": int(time.time()),
                "exp": int(time.time()) + 3600,
            }

        header_b64 = urlsafe_b64encode(json.dumps(header).encode()).decode().rstrip("=")
        payload_b64 = (
            urlsafe_b64encode(json.dumps(payload).encode()).decode().rstrip("=")
        )
        signature = urlsafe_b64encode(self.token_bytes(32)).decode().rstrip("=")
        return f"{header_b64}.{payload_b64}.{signature}"

    def api_key(self, prefix: str = "", length: int = 32, fmt: str = "hex") -> str:
        """Generate API key.

        :param prefix: Optional prefix (e.g., `sk_`, `pk_`, `api_`).
        :param length: Length of the random part (default: 32).
        :param fmt: Format of the key - 'hex' or 'base64' (default: 'hex').
        :return: API key string.
        :raises ValueError: If format is not 'hex' or 'base64'.

        Example:

            >>> from mimesis import Cryptographic
            >>> crypto = Cryptographic()
            >>> crypto.api_key()
            'a3d2f5e8b9c1d4e7f0a2b5c8d1e4f7a0'
            >>> crypto.api_key(prefix='sk_')
            'sk_a3d2f5e8b9c1d4e7f0a2b5c8d1e4f7a0'
            >>> crypto.api_key(prefix='pk_', format='base64')
            'pk_dGVzdGluZ3Rlc3Rpbmc'
        """
        if fmt == "hex":
            key = self.token_hex(length // 2)
        elif fmt == "base64":
            key = self.token_urlsafe(length)[:length]
        else:
            raise ValueError(f"Unknown format: {fmt}. Use 'hex' or 'base64'.")

        return f"{prefix}{key}" if prefix else key

    def certificate_fingerprint(self, algorithm: str = "sha256") -> str:
        """Generate certificate fingerprint.

        :param algorithm: Hash algorithm - 'sha256' or 'sha1'.
        :return: Certificate fingerprint in colon-separated hex format.
        :raises ValueError: If algorithm is not supported.

        Example:

            >>> from mimesis import Cryptographic
            >>> crypto = Cryptographic()
            >>> crypto.certificate_fingerprint()
            'A3:D2:F5:E8:B9:C1:D4:E7:F0:A2:B5:C8:D1:E4:F7:A0'
            >>> crypto.certificate_fingerprint(algorithm='sha1')
            'A3:D2:F5:E8:B9:C1:D4:E7:F0:A2:B5:C8:D1:E4:F7:A0:B1:C2:D3:E4'
        """
        if algorithm == "sha256":
            hex_str = self.token_hex(32)
        elif algorithm == "sha1":
            hex_str = self.token_hex(20)
        else:
            raise ValueError(f"Unknown algorithm: {algorithm}. Use 'sha256' or 'sha1'.")

        return ":".join(hex_str[i : i + 2] for i in range(0, len(hex_str), 2)).upper()
