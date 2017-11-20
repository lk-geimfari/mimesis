from binascii import hexlify
import hashlib
import uuid

from mimesis.exceptions import UnsupportedAlgorithm
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

    def hash(self, algorithm: str = 'sha1') -> str:
        """Generate random hash.

        :param str algorithm:
            Hashing algorithm ('md5', 'sha1', 'sha224', 'sha256',
            'sha384', 'sha512').
        :return: Hash.
        :raises UnsupportedAlgorithm: if algorithm is not supported.
        """
        # TODO: Enums here
        algorithm = algorithm.lower().strip()

        if algorithm in hashlib.algorithms_guaranteed:
            if hasattr(hashlib, algorithm):
                fn = getattr(hashlib, algorithm)
                _hash = fn(self.uuid().encode())
                return _hash.hexdigest()
        else:
            raise UnsupportedAlgorithm(
                'Algorithm {0} is does not support. Use: {1}'.format(
                    algorithm, ', '.join(hashlib.algorithms_guaranteed)),
            )

    def bytes(self, entropy: int = 32) -> Bytes:
        """Get a random byte string containing *entropy* bytes.

        The string has *entropy* random bytes, each byte converted to two
        hex digits.

        :param int entropy: Number of bytes.
        :return: Bytes.
        :rtype: bytes
        """
        return self.random.urandom(entropy)

    def token(self, entropy: int = 32) -> str:
        """Return a random text string, in hexadecimal.

        :param int entropy: Number of bytes.
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
