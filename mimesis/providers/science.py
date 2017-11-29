from typing import Union

from mimesis.data import MATH_FORMULAS
from mimesis.providers.base import BaseProvider
from mimesis.utils import pull


class Science(BaseProvider):
    """Class for getting scientific data"""

    def __init__(self, *args, **kwargs):
        """
        :param str locale: Current language.
        """
        super().__init__(*args, **kwargs)
        self._data = pull('science.json', self.locale)

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

        :param bool name_only: If False then will be returned dict.
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
        """Generate random atomic number

        :return: Atomic number

        :Example:
            92
        """
        return self.random.randint(1, 119)

    def scientific_article(self) -> str:
        """Generate a random link to scientific article on Wikipedia.

        :return: Link to article on Wikipedia.

        :Example:
            https://en.wikipedia.org/wiki/Black_hole
        """
        articles = self._data['article']
        return self.random.choice(articles)

    def rna(self, length: int = 10) -> str:
        """Generate random RNA sequence.

        :param int length: Length of block
        :return: RNA sequence.

        :Example:
            AGUGACACAA
        """
        letters = ['U', 'C', 'G', 'A']
        return self.random.schoice(letters, length)

    def dna(self, length: int = 10) -> str:
        """Generate random DNA sequence.

        :param int length: Length of block
        :return: DNA sequence.

        :Example:
            GCTTTAGACC
        """
        letters = ['T', 'C', 'G', 'A']
        return self.random.schoice(letters, length)
