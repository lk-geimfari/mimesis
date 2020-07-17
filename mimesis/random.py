# -*- coding: utf-8 -*-

"""Implements various helpers which are used in the various data providers.

This module contains custom ``Random()`` class where implemented a lot of
methods which are not included in standard ``random.Random()``,
but frequently used in this project.

Also there are implemented function ``get_random_item()`` which helps
get a random item of the enum object.

"""

import os
import random as random_module
import secrets
import string
import uuid
from typing import Any, List, Optional

__all__ = ['Random', 'get_random_item', 'random']


class Random(random_module.Random):
    """Custom class for the possibility of extending.

    The class is a subclass of the class ``Random()`` from the module ``random``
    of the standard library, which provides the custom methods.

    """

    def randints(self, amount: int = 3,
                 a: int = 1, b: int = 100) -> List[int]:
        """Generate list of random integers.

        :param amount: Amount of elements.
        :param a: Minimum value of range.
        :param b: Maximum value of range.
        :return: List of random integers.
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
        """
        return os.urandom(*args, **kwargs)

    def generate_string(self, str_seq: str, length: int = 10) -> str:
        """Generate random string created from string sequence.

        :param str_seq: String sequence of letters or digits.
        :param length: Max value.
        :return: Single string.
        """
        return ''.join(self.choice(str_seq) for _ in range(length))

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

        if char_code == digit_code:
            raise ValueError('You cannot use the same '
                             'placeholder for digits and chars!')

        def random_int(a: int, b: int) -> int:
            b = b - a
            return int(self.random() * b) + a

        _mask = mask.encode()
        code = bytearray(len(_mask))
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

    def randstr(self, unique: bool = False,
                length: Optional[int] = None) -> str:
        """Generate random string value.

        This method can be especially useful when you need to generate
        only unique values in your provider. Just pass parameter unique=True.

        Basically, this method is just a simple wrapper around uuid.uuid4().

        :param unique: Generate only unique values.
        :param length: Length of string. Default range is (min=16, max=128).
        :return: Random string.

        """
        if unique:
            return str(uuid.uuid4().hex)

        if length is None:
            length = self.randint(16, 128)

        _string = string.ascii_letters + string.digits
        _string = ''.join(
            secrets.choice(_string) for _ in range(length)
        )
        return _string


def get_random_item(enum: Any, rnd: Optional[Random] = None) -> Any:
    """Get random item of enum object.

    :param enum: Enum object.
    :param rnd: Custom random object.
    :return: Random item of enum.
    """
    if rnd and isinstance(rnd, Random):
        return rnd.choice(list(enum))
    return random_module.choice(list(enum))


# Compat
# See: https://github.com/lk-geimfari/mimesis/issues/469
random = Random()
