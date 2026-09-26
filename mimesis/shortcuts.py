"""This module provides internal utility functions."""


def luhn_checksum(num: str) -> str:
    """Calculate a checksum for num using the Luhn algorithm.

    Used to validate credit card numbers, IMEI numbers,
    and other identification numbers.

    :param num: The number to calculate a checksum for as a string.
    :return: Checksum for number.
    """
    check = 0
    for i, s in enumerate(reversed(num)):
        sx = int(s)
        if i % 2 == 0:
            sx *= 2
        if sx > 9:
            sx -= 9
        check += sx
    return str(check * 9 % 10)


def gs1_checksum(num: str) -> str:
    """Calculate a check digit with the GS1 modulo 10 algorithm.

    Used by EAN-8, EAN-13, ISBN-13 and UPC, which share the same weighting:
    the digits are weighted 3, 1, 3, 1 ... counting from the right.

    This is not the same algorithm as :func:`luhn_checksum`, which is why
    credit card and IMEI numbers cannot use it.

    :param num: The number to calculate a check digit for as a string.
    :return: Check digit.
    """
    total = sum((3, 1)[i % 2] * int(digit) for i, digit in enumerate(reversed(num)))
    return str((10 - total) % 10)


def mod11_checksum(num: str) -> str:
    """Calculate a check digit with the modulo 11 algorithm.

    Used by ISBN-10 and ISSN, whose check digit may be the letter ``X`` when
    the computed value would be 10. The digits are weighted from
    ``len(num) + 1`` down to 2, left to right.

    :param num: The number to calculate a check digit for as a string.
    :return: Check digit, either a digit or ``X``.
    """
    length = len(num)
    total = sum((length + 1 - i) * int(digit) for i, digit in enumerate(num))
    check = (11 - total) % 11
    return "X" if check == 10 else str(check)
