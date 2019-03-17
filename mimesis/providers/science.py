# -*- coding: utf-8 -*-

"""Provides pseudo-scientific data."""

from typing import Union

from mimesis.data import MATH_FORMULAS
from mimesis.providers.base import BaseDataProvider

__all__ = ['Science']


class Science(BaseDataProvider):
    """Class for generating pseudo-scientific data."""

    def __init__(self, *args, **kwargs):
        """Initialize attributes.

        :param locale: Current language.
        :param seed: Seed.
        """
        super().__init__(*args, **kwargs)
        self._datafile = 'science.json'
        self.pull(self._datafile)

    class Meta:
        """Class for metadata."""

        name = 'science'

    def math_formula(self) -> str:
        """Get a random mathematical formula.

        :return: Math formula.

        :Example:
            A = (ab)/2.
        """
        formula = self.random.choice(MATH_FORMULAS)
        return formula

    def chemical_element(self, name_only: bool = True) -> Union[dict, str]:
        """Generate a random chemical element.

        :param name_only: If False then will be returned dict.
        :return: Name of chemical element or dict.
        :rtype: dict or str

        :Example:
            {'Symbol': 'S', 'Name': 'Sulfur', 'Atomic number': '16'}
        """
        elements = self._data['chemical_element']
        nm, sm, an = self.random.choice(elements).split('|')

        if not name_only:
            return {
                'name': nm.strip(),
                'symbol': sm.strip(),
                'atomic_number': an.strip(),
            }

        return nm.strip()

    def atomic_number(self) -> int:
        """Generate random atomic number.

        :return: Atomic number

        :Example:
            92
        """
        return self.random.randint(1, 119)

    def rna_sequence(self, length: int = 10) -> str:
        """Generate a random RNA sequence.

        :param length: Length of block.
        :return: RNA sequence.

        :Example:
            AGUGACACAA
        """
        return self.random.schoice('UCGA', length)

    def dna_sequence(self, length: int = 10) -> str:
        """Generate a random DNA sequence.

        :param length: Length of block.
        :return: DNA sequence.

        :Example:
            GCTTTAGACC
        """
        return self.random.schoice('TCGA', length)
