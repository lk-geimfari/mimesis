# -*- coding: utf-8 -*-

"""Clothing data provider."""

from mimesis.providers.base import BaseProvider

__all__ = ['Clothing']


class Clothing(BaseProvider):
    """Class for generate data related to clothing."""

    class Meta:
        """Class for metadata."""

        name = 'clothing'

    def international_size(self) -> str:
        """Get a random size in international format.

        :return: Clothing size.
        """
        return self.random.choice(['L', 'M', 'S', 'XL',
                                   'XS', 'XXL', 'XXS', 'XXXL'])

    def european_size(self) -> int:
        """Generate a random clothing size in European format.

        :return: Clothing size.
        """
        return self.random.randint(38, 62)

    def custom_size(self, minimum: int = 40, maximum: int = 62) -> int:
        """Generate clothing size using custom format.

        :param minimum: Minimum value.
        :param maximum: Maximum value.
        :return: Clothing size.
        """
        return self.random.randint(minimum, maximum)
