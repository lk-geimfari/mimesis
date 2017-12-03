from typing import List

from mimesis.providers.base import BaseProvider
from mimesis.typing import Number


class Numbers(BaseProvider):
    """Class for generating numbers"""

    def floats(self, n: int = 2) -> List[float]:
        """Generate an array of random float number of 10 ** n.

        :param n: Raise 10 to the 'n' power.
        :return: The list of floating-point numbers.
        :rtype: List of floats
        """
        nums = [self.random.random()
                for _ in range(10 ** int(n))]
        return nums

    @staticmethod
    def primes(start: int = 1, end: int = 999) -> List[int]:
        """Generate a list of prime numbers from start to end.

        :param start: First value of range.
        :param end: Last value of range.
        :return: A list of prime numbers from start to end.
        :rtype: list
        """
        sieve_size = (end // 2 - 1) if end % 2 == 0 else (end // 2)
        sieve = [True] * sieve_size

        primes = []  # list of primes
        # add 2 to the list if it's in the given range
        if end >= 2:
            primes.append(2)
        for i in range(sieve_size):
            if sieve[i]:
                value_at_i = i * 2 + 3
                primes.append(value_at_i)
                for j in range(i, sieve_size, value_at_i):
                    sieve[j] = False

        chop_index = 0
        for i in range(len(primes)):
            if primes[i] >= start:
                chop_index = i
                break
        return primes[chop_index:]

    def digit(self, to_bin: bool = False) -> Number:
        """Get a random digit.

        :param to_bin: If True then convert to binary.
        :return: Digit.
        :rtype: str or int

        :Example:
            4.
        """
        digit = self.random.randint(0, 9)

        if to_bin:
            return bin(digit)

        return digit

    def between(self, minimum: int = 1, maximum: int = 1000) -> int:
        """Generate a random number between minimum and maximum.

        :param minimum: Minimum of range.
        :param maximum: Maximum of range.
        :return: Number.
        """
        num = self.random.randint(int(minimum), int(maximum))
        return num

    def rating(self, maximum: float = 5.0) -> float:
        """Generate random rating for something.

        :param maximum: Maximum value (default is 5.0).
        :return: Rating.

        :Example:
            4.7
        """
        res = '{0:0.1f}'.format(self.random.uniform(0, maximum))
        return float(res)
