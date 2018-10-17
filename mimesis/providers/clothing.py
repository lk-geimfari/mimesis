"""Clothing sizes data provider."""

from mimesis.providers.base import BaseDataProvider

__all__ = ['ClothingSize']


class ClothingSize(BaseDataProvider):
    """Class for generate clothing sizes data."""

    def international_size(self) -> str:
        """Get a random size in international format.

        :return: Clothing size.

        :Example:

        >>> size = ClothingSize()
        >>> int_size = size.international_size()
        >>> len(int_size) <= 4
        True
        """
        return self.random.choice(['L', 'M', 'S', 'XL',
                                   'XS', 'XXL', 'XXS', 'XXXL'])

    def european_size(self) -> int:
        """Generate a random clothing size in European format.

        :return: Clothing size.

        :Example:

        >>> size = ClothingSize()
        >>> eur_size = size.european_size()
        >>> 38 <= eur_size <= 62
        True
        """
        return self.random.randint(38, 62)

    def custom_size(self, minimum: int = 40, maximum: int = 62) -> int:
        """Generate clothing size using custom format.

        :param minimum: Minimum value.
        :param maximum: Maximum value.
        :return: Clothing size.

        :Example:

        >>> size = ClothingSize()
        >>> custom_size = size.custom_size(51, 53)
        >>> 51 <= custom_size <= 53
        True
        """
        return self.random.randint(minimum, maximum)
