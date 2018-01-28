"""Implements various helpers which are used in the various data providers.

This module contains custom ``Random()`` class where implemented a lot of
methods which are not included in standard ``random.Random()``,
but frequently used in this project.

Also there are implemented function ``get_random_item()`` which helps
get a random item of the enum object.

"""

import os
import random
from typing import Any, List, Optional, Sequence

__all__ = ['Random', 'get_random_item']


class Random(random.Random):
    """Custom class for the possibility of extending.

    The class is a subclass of the class ``Random()`` from the module ``random``
    of the standard library, which provides the custom methods.

    """

    def multiple_choice(self, seq: Sequence[Any], amount: int = 2) -> list:
        """Multiple choices of elements from the sequence.

        Choice an element from sequence ``seq``
        in an amount of ``amount``.

        :param seq: Sequence of elements.
        :param amount: Amount of elements.
        :return: List of elements.
        """
        return [self.choice(seq) for _ in range(amount)]

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

        return [int(self.random() * (b - a)) + a
                for _ in range(amount)]

    @staticmethod
    def urandom(*args: Any, **kwargs: Any) -> bytes:
        """Return a bytes object containing random bytes.

        :return: Bytes.
        :rtype: bytes
        """
        return os.urandom(*args, **kwargs)

    def schoice(self, seq: str, end: int = 10) -> str:
        """Choice function which returns string created from sequence.

        :param seq: Sequence of letters or digits.
        :type seq: tuple or list
        :param end: Max value.
        :return: Single string.
        """
        return ''.join(self.choice(list(seq))
                       for _ in range(end))

    def custom_code(self, mask: str = '@###',
                    char: str = '@', digit: str = '#') -> str:
        """Generate custom code using ascii uppercase and random integers.

        :param mask: Mask of code.
        :param char: Placeholder for characters.
        :param digit: Placeholder for digits.
        :return: Custom code.
        """
        char_code = ord(char)
        digit_code = ord(digit)
        code = bytearray(len(mask))

        def random_int(a: int, b: int) -> int:
            b = b - a
            return int(self.random() * b) + a

        _mask = mask.encode()
        for i, p in enumerate(_mask):
            if p == char_code:
                a = random_int(65, 91)  # A-Z
            elif p == digit_code:
                a = random_int(48, 58)  # 0-9
            else:
                a = p
            code[i] = a
        return code.decode()

    def uniform(self, a: float, b: float, precision: int = 15) -> float:
        """Get a random number in the range [a, b) or [a, b] depending on rounding.

        :param a: Minimum value.
        :param b: Maximum value.
        :param precision: Round a number to a given
            precision in decimal digits, default is 15.
        """
        return round(a + (b - a) * self.random(), precision)


def get_random_item(enum: Any, rnd: Optional[Random] = None) -> Any:
    """Get random item of enum object.

    :param enum: Enum object.
    :param rnd: Custom random object.
    :return: Random item of enum.
    """
    if rnd and isinstance(rnd, Random):
        return rnd.choice(list(enum))
    return random.choice(list(enum))
