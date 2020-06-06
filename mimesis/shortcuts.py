# -*- coding: utf-8 -*-

"""This module is provide internal util functions."""

__all__ = ['luhn_checksum']


def luhn_checksum(num: str) -> str:
    """Calculate a checksum for num using the Luhn algorithm.

    :param num: The number to calculate a checksum for as a string.
    :return: Checksum for number.
    """
    check = 0
    for i, s in enumerate(reversed(num)):
        sx = int(s)
        sx = sx * 2 if i % 2 == 0 else sx
        sx = sx - 9 if sx > 9 else sx
        check += sx
    return str(check * 9 % 10)
