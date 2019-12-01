# -*- coding: utf-8 -*-

"""Provides data related to numbers."""

from typing import List, Union

from mimesis.providers.base import BaseProvider

__all__ = ['Numbers']


class Numbers(BaseProvider):
    """Class for generating numbers."""

    class Meta:
        """Class for metadata."""

        name = 'numbers'

    def floats(self, start: float = 0, end: float = 1, n: int = 2,
               rounding: int = 15) -> List[float]:
        """Generate a list of 10^n random float numbers.

        :param start: Start range.
        :param end: End range.
        :param n: Raise 10 to the 'n' power.
        :param rounding: Max number of decimal digits.
        :return: The list of floating-point numbers.
        """
        return [self.random.uniform(start, end, rounding)
                for _ in range(10 ** int(n))]

    def integers(self, start: int = 0, end: int = 10,
                 length: int = 10) -> List[int]:
        """Generate a list of random integers.

        Integers can be negative or positive numbers.
        .. note: You can use both positive and negative numbers.

        :param start: Start.
        :param end: End.
        :param length: Length of list.
        :return: List of integers.

        :Example:
            [-20, -19, -18, -17]
        """
        return self.random.randints(
            length, start, end)

    def complexnums(self, start_real: float = 0, end_real: float = 1,
                    start_imag: float = 0, end_imag: float = 1,
                    rounding_real: int = 15, rounding_imag: int = 15,
                    length: int = 10) -> List[complex]:
        """Generate a list of random complex numbers.

        :param start_real: Start real range.
        :param end_real: End real range.
        :param start_imag: Start imaginary range.
        :param end_imag: End imaginary range.
        :param rounding_real: Rounding real part.
        :param rounding_imag: Roungind imaginary part.
        :param length: Length of the list.
        :return: A list of random complex numbers.
        """
        return [
            complex(self.random.uniform(start_real, end_real, rounding_real),
                    self.random.uniform(start_imag, end_imag, rounding_imag))
            for _ in range(length)]

    @staticmethod
    def primes(start: int = 1, end: int = 999) -> List[int]:
        """Generate a list of prime numbers.

        :param start: First value of range.
        :param end: Last value of range.
        :return: A list of prime numbers from start to end.
        """
        # TODO: It should generate random primes with passed length.
        sieve_size = (end // 2 - 1) if end % 2 == 0 else (end // 2)
        sieve = [True] * sieve_size

        primes = []  # list of primes
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

    def digit(self, to_bin: bool = False) -> Union[str, int]:
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

    def between(self, minimum: int = 1, maximum: int = 1000) -> int:
        """Generate a random number between minimum and maximum.

        :param minimum: Minimum of range.
        :param maximum: Maximum of range.
        :return: Number.
        """
        return self.random.randint(minimum, maximum)
