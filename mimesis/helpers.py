import os
import random


class Random(random.Random):
    """Custom Random() class for the possibility of extending."""

    def randints(self, amount: int=None, a: int=1, b: int=100) -> list:
        """Generate list of random integers.

        :param amount: Amount of elements.
        :param a: Minimum value of range.
        :param b: Maximum value of range.
        :return: List of random integers.
        """

        if not amount:
            amount = 3

        return [self.randint(a, b)
                for _ in range(amount)]

    @staticmethod
    def urandom(*args, **kwargs) -> bytes:
        """Return a bytes object containing random bytes."""
        return os.urandom(*args, **kwargs)
