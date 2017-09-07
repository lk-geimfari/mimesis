from binascii import hexlify
import hashlib
import uuid
import os

from mimesis.exceptions import UnsupportedAlgorithm
from mimesis.providers import BaseProvider


class Cryptographic(BaseProvider):
    """This class provides support cryptographic data.
    """

    def uuid(self):
        """Generate random UUID.

        :return: UUID
        """
        return str(uuid.UUID(int=self.random.getrandbits(128)))

    def hash(self, algorithm='sha1'):
        """Generate random hash.

        :param algorithm:
            Hashing algorithm ('md5', 'sha1', 'sha224', 'sha256',
            'sha384', 'sha512').
        :return: Hash.
        """
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

    def bytes(self, entropy=None):
        """Get a random byte string containing *entropy* bytes.

        The string has *entropy* random bytes, each byte converted to two
        hex digits.

        :param entropy:
        :return: Bytes.
        """
        if entropy is None:
            entropy = 32

        return os.urandom(entropy)

    def token(self, entropy=None):
        """Return a random text string, in hexadecimal.

        :param entropy: Number of bytes.
        :return: Token.
        """
        return hexlify(self.bytes(entropy)).decode('ascii')
