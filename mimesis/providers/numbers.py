import array

from mimesis.providers.base import BaseProvider
from mimesis.typing import Array, Number


initial_primes = [2]


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
        global initial_primes

        # if request is inside initial_primes return a subset of it.
        if (end <= initial_primes[-1]):
            return [p for p in initial_primes if start <= p <= end]

        # remove case when start == 1
        if (start < 2):
            start = 2

        # create a sieve and remove all non-primes from it
        sieve = [True] * (end - start)
        for p in Numbers.primes(1, int(end**0.5) + 1):
            s = max(p**2, start + (p - start % p) % p)
            for i in range(s - start, end - start, p):
                sieve[i] = False

        # create a list of primes from the sieve
        primes_list = [i + start for i, x in enumerate(sieve) if x]

        # update the list of initial primes when bigger one is available
        if (start <= 2 and primes_list > initial_primes):
            initial_primes = primes_list

        return [p for p in primes_list if start <= p <= end]

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
        res = '{0:0.1f}'.format(self.random.uniform(0, float(maximum)))
        return float(res)
