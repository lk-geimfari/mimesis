import os
import random

from typing import List, Any


class Random(random.Random):
    """Custom Random() class for the possibility of extending."""

    def randints(self, amount: int = 3, a: int = 1, b: int = 100) -> List[int]:
        """Generate list of random integers.

        :param amount: Amount of elements.
        :param a: Minimum value of range.
        :param b: Maximum value of range.
        :return: List of random integers.
        :rtype: list
        """

        if amount <= 0:
            raise ValueError('Amount out of range.')

        return [self.randint(a, b)
                for _ in range(amount)]

    @staticmethod
    def urandom(*args: Any, **kwargs: Any) -> bytes:
        """Return a bytes object containing random bytes."""
        return os.urandom(*args, **kwargs)
