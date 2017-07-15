import array

from .base import BaseProvider


class Numbers(BaseProvider):
    """Class for generating numbers"""

    def floats(self, n=2, type_code='f', to_list=False):
        """Generate an array of random float number of 10**n.

        +-----------+----------------+--------------+----------------------+
        | Type Code | C Type         | Storage size | Value range          |
        +===========+================+==============+======================+
        | 'f'       | floating point | 4 byte       | 1.2E-38 to 3.4E+38   |
        +-----------+----------------+--------------+----------------------+
        | 'd'       | floating point | 8 byte       | 2.3E-308 to 1.7E+308 |
        +-----------+----------------+--------------+----------------------+

        :param n: Raise 10 to the 'n' power.
        :param type_code: A code of type.
        :param to_list: Convert array to list.

        .. note:: When you work with large numbers, it is better not to use
            this option, because type 'array' much faster than 'list'.

        :return: An array of floating-point numbers.
        """
        nums = array.array(type_code, (self.random.random()
                                       for _ in range(10 ** int(n))))
        return nums.tolist() if to_list else nums

    @staticmethod
    def primes(start=1, end=999, to_list=False):
        """Generate an array of prime numbers of 10 ** n.

        +------------+-----------------+--------------+--------------------+
        | Type Code | C Type           | Storage size | Value range        |
        +===========+==================+==============+====================+
        | 'L'       | unsigned integer | 4 byte       | 0 to 4,294,967,295 |
        +-----------+------------------+--------------+--------------------+

        :param start: First value of range.
        :param end: Last value of range.
        :param to_list: Convert array to list.
        :return: An array of floating-point numbers.
        """
        nums = array.array('L', (i for i in range(start, end) if i % 2))
        return nums.tolist() if to_list else nums

    def digit(self, to_bin=False):
        """Get a random digit.

        :param to_bin: If True then convert to binary.
        :return: Digit.
        :Example:
            4.
        """
        digit = self.random.randint(0, 9)

        if to_bin:
            return bin(digit)

        return digit

    def between(self, minimum=1, maximum=1000):
        """Generate a random number between minimum and maximum.

        :param minimum: Minimum of range.
        :param maximum: Maximum of range
        :return: Number
        """
        num = self.random.randint(int(minimum), int(maximum))
        return num

    def rating(self, maximum=5.0):
        """Generate random rating for something.

        :param maximum: Minimum value (default is 5.0).
        :return: Rating.
        :rtype: float
        :Example:
            4.7
        """
        res = '{0:0.1f}'.format(self.random.uniform(0, float(maximum)))
        return float(res)
