from mimesis.providers.base import BaseProvider


class ClothingSizes(BaseProvider):
    """Class for generate clothing sizes data"""

    def international_size(self) -> str:
        """Get a random size in international format.

        :return: Clothing size.

        :Example:
            XXL.
        """
        sizes = (
            'L',
            'M',
            'S',
            'XL',
            'XS',
            'XXL',
            'XXS',
            'XXXL',
        )

        return self.random.choice(sizes)

    def european_size(self) -> int:
        """Generate a random clothing size in European format.

        :return: Clothing size.

        :Example:
            42
        """
        sizes = [i for i in range(40, 62) if i % 2 == 0]
        return self.random.choice(sizes)

    def custom_size(self, minimum: int = 40, maximum: int = 62) -> int:
        """Generate clothing size using custom format.

        :param int minimum: Minimum value.
        :param int maximum: Maximum value.
        :return: Clothing size.

        :Example:
            44
        """
        return self.random.randint(minimum, maximum)
