"""This module provides internal util functions."""


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
