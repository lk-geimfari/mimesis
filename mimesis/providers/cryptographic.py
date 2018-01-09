import hashlib
import uuid
from typing import Optional

from mimesis.enums import Algorithm
from mimesis.providers.base import BaseDataProvider
from mimesis.providers.text import Text
from mimesis.typing import Bytes


class Cryptographic(BaseDataProvider):
    """This class provides support cryptographic data.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__words = Text('en')._data['words']

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
        key = self._validate_enum(algorithm, Algorithm)

        if hasattr(hashlib, key):
            fn = getattr(hashlib, key)
            return fn(self.uuid().encode()).hexdigest()

    def bytes(self, entropy: int = 32) -> Bytes:
        """Get a random byte string containing *entropy* bytes.

        The string has *entropy* random bytes, each byte converted to two
        hex digits.

        :param entropy: Number of bytes.
        :return: Bytes.
        :rtype: bytes
        """
        return bytes(self.random.getrandbits(8)
                     for _ in range(entropy))

    def token(self, entropy: int = 32) -> str:
        """Return a random text string, in hexadecimal.

        :param entropy: Number of bytes.
        :return: Token.
        """
        return self.bytes(entropy).hex()

    @staticmethod
    def salt() -> str:
        """Generate salt (not cryptographically safe) using uuid4().

        :return: Salt.
        """
        return uuid.uuid4().hex

    def mnemonic_code(self, length: int = 12) -> str:
        """Generate pseudo mnemonic code.

        :param length: Length of code (number of words).
        :return: Mnemonic code.
        """
        words = self.__words['normal']
        return ' '.join(self.random.choice(words) for _ in range(length))
