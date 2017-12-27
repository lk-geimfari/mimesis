import os
import random
from typing import Any, List, Optional, Union

from mimesis.exceptions import NonEnumerableError

__all__ = ['Random', 'get_random_item', 'validate_enum']


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


def get_random_item(enum: Any, rnd: Optional[Random] = None) -> Any:
    """Get random item of enum object.

    :param enum: Enum object.
    :param rnd: Custom random object.
    :return: Random item of enum.
    """
    if rnd:
        return rnd.choice(list(enum))
    return random.choice(list(enum))


def validate_enum(item: Any, enum: Any, rnd: Optional[Random] = None) -> Any:
    """Validate enum parameter of method in subclasses of BaseProvider.

    :param item: Item of enum object.
    :param enum: Enum object.
    :param rnd: Custom random object.
    :return: Value of item.
    :raises NonEnumerableError: if ``item`` not in ``enum``.
    """

    if item is None:
        result = get_random_item(enum, rnd=rnd)
    elif item and isinstance(item, enum):
        result = item
    else:
        raise NonEnumerableError(enum)

    return result.value
