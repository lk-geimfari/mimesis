import os
import random
from typing import Any, List, Union


class Random(random.Random):
    """Custom Random() class for the possibility of extending."""

    def randints(self, amount: int = 3,
                 a: int = 1, b: int = 100) -> List[int]:
        """Generate list of random integers.

        :param int amount: Amount of elements.
        :param int a: Minimum value of range.
        :param int b: Maximum value of range.
        :return: List of random integers.
        :rtype: list
        :raises ValueError: if amount less or equal to zero.
        """

        if amount <= 0:
            raise ValueError('Amount out of range.')

        return [self.randint(a, b)
                for _ in range(amount)]

    @staticmethod
    def urandom(*args: Any, **kwargs: Any) -> bytes:
        """Return a bytes object containing random bytes

        :return: Bytes.
        :rtype: bytes
        """
        return os.urandom(*args, **kwargs)

    def schoice(self, seq: Union[tuple, list], end: int = 10) -> str:
        """Choice function which returns string created from sequence.

        :param seq: Sequence of letters or digits.
        :type seq: tuple or list
        :param int end: Max value.
        :return: Single string.
        """
        seq = [self.choice(seq) for _ in range(end)]
        return ''.join(seq)
