from mimesis.providers import BaseProvider


class ClothingSizes(BaseProvider):
    """Class for generate clothing sizes data"""

    def international(self):
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

    def european(self):
        """Generate a random clothing size in European format.

        :return: Clothing size.
        :Example:
            42
        """
        size = self.random.choice([i for i in range(40, 62) if i % 2 == 0])
        return size

    def custom(self, minimum=40, maximum=62):
        """Generate clothing size using custom format.

        :param minimum: Min value.
        :param maximum: Max value
        :return: Clothing size.
        :Example:
            44
        """
        return self.random.randint(int(minimum), int(maximum))
