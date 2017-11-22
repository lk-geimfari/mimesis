from binascii import hexlify
import hashlib
import uuid
from typing import Optional

from mimesis.enums import Algorithm
from mimesis.exceptions import NonEnumerableError
from mimesis.providers.base import BaseProvider
from mimesis.typing import Bytes


class Cryptographic(BaseProvider):
    """This class provides support cryptographic data.
    """

    def uuid(self) -> str:
        """Generate random UUID.

        :return: UUID
        """
        bits = self.random.getrandbits(128)
        return str(uuid.UUID(int=bits))

    def hash(self, algorithm: Optional[Algorithm] = None) -> str:
        """Generate random hash.

        :param algorithm: Enum object Algorithm.
        :return: Hash.
        :raises NonEnumerableError: if algorithm is not supported.
        """

        if algorithm is None:
            algorithm = Algorithm.get_random_item()

        if algorithm in Algorithm:
            if hasattr(hashlib, algorithm.value):
                fn = getattr(hashlib, algorithm.value)
                _hash = fn(self.uuid().encode())
                return _hash.hexdigest()
        else:
            raise NonEnumerableError(Algorithm)

    def bytes(self, entropy: int = 32) -> Bytes:
        """Get a random byte string containing *entropy* bytes.

        The string has *entropy* random bytes, each byte converted to two
        hex digits.

        :param entropy: Number of bytes.
        :return: Bytes.
        :rtype: bytes
        """
        return self.random.urandom(entropy)

    def token(self, entropy: int = 32) -> str:
        """Return a random text string, in hexadecimal.

        :param entropy: Number of bytes.
        :return: Token.
        """
        token = hexlify(self.bytes(entropy))
        return token.decode('ascii')

    @staticmethod
    def salt() -> str:
        """Generate salt (not cryptographically safe) using uuid4().

        :return: Salt.
        """
        return uuid.uuid4().hex
