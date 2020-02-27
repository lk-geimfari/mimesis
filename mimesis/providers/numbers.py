# -*- coding: utf-8 -*-

"""Provides data related to numbers."""

from decimal import Decimal
from typing import List

from mimesis.enums import NumTypes
from mimesis.providers.base import BaseProvider

__all__ = ['Numbers']


class Numbers(BaseProvider):
    """Class for generating numbers."""

    class Meta:
        """Class for metadata."""

        name = 'numbers'

    def float_number(self, start: float = -1000.0,
                     end: float = 1000.0, precision: int = 15) -> float:
        """Generate random float number in range [start, end].

        :param start: Start range.
        :param end:  End range.
        :param precision: Round a number to a given
            precision in decimal digits, default is 15.
        :return: Float.
        """
        return self.random.uniform(start, end, precision)

    def floats(self, start: float = 0, end: float = 1,
               n: int = 10, precision: int = 15) -> List[float]:
        """Generate a list of random float numbers.

        :param start: Start range.
        :param end: End range.
        :param n: Length of the list.
        :param precision: Round a number to a given
            precision in decimal digits, default is 15.
        :return: The list of floating-point numbers.
        """
        return [self.float_number(start, end, precision) for _ in range(n)]

    def integer_number(self, start: int = -1000, end: int = 1000) -> int:
        """Generate random integer from start to end.

        :param start: Start range.
        :param end: End range.
        :return: Integer.
        """
        return self.random.randint(start, end)

    def integers(self, start: int = 0, end: int = 10,
                 n: int = 10) -> List[int]:
        """Generate a list of random integers.

        Integers can be negative or positive numbers.
        .. note: You can use both positive and negative numbers.

        :param start: Start.
        :param end: End.
        :param n: Length of list.
        :return: List of integers.

        :Example:
            [-20, -19, -18, -17]
        """
        return self.random.randints(n, start, end)

    def complex_number(self, start_real: float = 0.0,
                       end_real: float = 1.0,
                       start_imag: float = 0.0,
                       end_imag: float = 1.0,
                       precision_real: int = 15,
                       precision_imag: int = 15) -> complex:
        """Generate random complex number.

        :param start_real: Start real range.
        :param end_real: End real range.
        :param start_imag: Start imaginary range.
        :param end_imag: End imaginary range.
        :param precision_real:  Round a real part of
            number to a given precision.
        :param precision_imag:  Round the imaginary part of
            number to a given precision.
        :return: Complex numbers.
        """
        real_part = self.random.uniform(start_real, end_real, precision_real)
        imag_part = self.random.uniform(start_imag, end_imag, precision_imag)
        return complex(real_part, imag_part)

    def complexes(self, start_real: float = 0, end_real: float = 1,
                  start_imag: float = 0, end_imag: float = 1,
                  precision_real: int = 15, precision_imag: int = 15,
                  n: int = 10) -> List[complex]:
        """Generate a list of random complex numbers.

        :param start_real: Start real range.
        :param end_real: End real range.
        :param start_imag: Start imaginary range.
        :param end_imag: End imaginary range.
        :param precision_real:  Round a real part of
            number to a given precision.
        :param precision_imag:  Round the imaginary part of
            number to a given precision.
        :param n: Length of the list.
        :return: A list of random complex numbers.
        """
        numbers = []
        for _ in range(n):
            numbers.append(
                self.complex_number(
                    start_real=start_real,
                    end_real=end_real,
                    start_imag=start_imag,
                    end_imag=end_imag,
                    precision_real=precision_real,
                    precision_imag=precision_imag,
                ),
            )
        return numbers

    def decimal_number(self, start: float = -1000.0,
                       end: float = 1000.0) -> Decimal:
        """Generate random decimal number.

        :param start:  Start range.
        :param end: End range.
        :return: Decimal object.
        """
        return Decimal.from_float(self.float_number(start, end))

    def decimals(self, start: float = 0.0,
                 end: float = 1000.0, n: int = 10) -> List[Decimal]:
        """Generate decimal number as Decimal objects.

        :param start: Start range.
        :param end: End range.
        :param n: Length of the list.
        :return: A list of random decimal numbers.
        """
        return [self.decimal_number(start, end) for _ in range(n)]

    def matrix(self, m: int = 10, n: int = 10,
               num_type: NumTypes = NumTypes.FLOATS, **kwargs) -> List[List]:
        """Generate m x n matrix with random numbers.

        This method works with variety of types,
        so you can pass method-specific **kwargs.

        See code for more details.

        :param m: Number of rows.
        :param n: Number of columns.
        :param num_type: NumTypes enum object.
        :param kwargs: Other method-specific arguments.
        :return: A matrix of random numbers.
        """
        key = self._validate_enum(num_type, NumTypes)
        kwargs.update({'n': n})
        method = getattr(self, key)
        return [method(**kwargs) for _ in range(m)]
