import os
import random
from typing import Any, List, Union

__all__ = ['Random']


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

        return [int(self.random() * (b - a)) + a
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

    def custom_code(self, mask: str = '@###',
                    char: str = '@', digit: str = '#') -> str:
        """Generate custom code using ascii uppercase and random integers.
        :param mask: Mask of code.
        :param char: Placeholder for characters.
        :param digit: Placeholder for digits.
        :return: Custom code.
        :Example:
            5673-AGFR-SFSFF-1423-4/AD.
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
