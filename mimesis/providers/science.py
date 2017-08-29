from mimesis.data import MATH_FORMULAS
from mimesis.utils import pull

from .base import BaseProvider


class Science(BaseProvider):
    """Class for getting scientific data"""

    def __init__(self, *args, **kwargs):
        """
        :param locale: Current language.
        """
        super().__init__(*args, **kwargs)
        self._data = pull('science.json', self.locale)

    def math_formula(self):
        """Get a random mathematical formula.

        :return: Math formula.
        :Example:
            A = (ab)/2.
        """
        formula = self.random.choice(MATH_FORMULAS)
        return formula

    def chemical_element(self, name_only=True):
        """Generate a random chemical element.

        :param name_only: If False then will be returned dict.
        :return: Name of chemical element or dict.
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

    def scientific_article(self):
        """Generate a random link to scientific article on Wikipedia.

        :return: Link to article on Wikipedia.
        :Example:
            https://en.wikipedia.org/wiki/Black_hole
        """
        articles = self._data['article']
        return self.random.choice(articles)
