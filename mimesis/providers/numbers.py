import array

from mimesis.providers.base import BaseProvider
from mimesis.typing import Array, Number


class Numbers(BaseProvider):
    """Class for generating numbers"""

    def floats(self, n: int = 2, type_code: str = 'f',
               to_list: bool = False) -> Array:
        """Generate an array of random float number of 10**n.

        +-----------+----------------+--------------+----------------------+
        | Type Code | C Type         | Storage size | Value range          |
        +===========+================+==============+======================+
        | 'f'       | floating point | 4 byte       | 1.2E-38 to 3.4E+38   |
        +-----------+----------------+--------------+----------------------+
        | 'd'       | floating point | 8 byte       | 2.3E-308 to 1.7E+308 |
        +-----------+----------------+--------------+----------------------+

        :param int n: Raise 10 to the 'n' power.
        :param str type_code: A code of type.
        :param bool to_list: Convert array to list.

        .. note:: When you work with large numbers, it is better not to use
            this option, because type 'array' much faster than 'list'.

        :return: An array of floating-point numbers.
        :rtype: Array
        """

        # TODO: compare array and list
        nums = array.array(type_code, (self.random.random()
                                       for _ in range(10 ** int(n))))
        return nums.tolist() if to_list else nums

    @staticmethod
    def primes(start: int = 1, end: int = 999) -> list:
        """Generate a list of prime numbers from start to end.

        :param int start: First value of range.
        :param int end: Last value of range.
        :return: A list of prime numbers from start to end.
        :rtype: list
        """
        sieve_size = (end // 2 - 1) if end % 2 == 0 else (end // 2)
        sieve = [True] * sieve_size

        primes = []     # list of primes
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

        :param bool to_bin: If True then convert to binary.
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

        :param int minimum: Minimum of range.
        :param int maximum: Maximum of range.
        :return: Number.
        """
        num = self.random.randint(int(minimum), int(maximum))
        return num

    def rating(self, maximum: float = 5.0) -> float:
        """Generate random rating for something.

        :param float maximum: Minimum value (default is 5.0).
        :return: Rating.

        :Example:
            4.7
        """
        res = '{0:0.1f}'.format(self.random.uniform(0, maximum))
        return float(res)
