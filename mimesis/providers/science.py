"""Provides pseudo-scientific data."""

from mimesis.providers.base import BaseProvider


__all__ = ["Science"]


class Science(BaseProvider):
    """Class for generating pseudo-scientific data."""

    class Meta:
        name = "science"

    def rna_sequence(self, length: int = 10) -> str:
        """Generates a random RNA sequence.

        :param length: Length of block.
        :return: RNA sequence.

        :Example:
            AGUGACACAA
        """
        return "".join(self.random.choices("UCGA", k=length))

    def dna_sequence(self, length: int = 10) -> str:
        """Generates a random DNA sequence.

        :param length: Length of block.
        :return: DNA sequence.

        :Example:
            GCTTTAGACC
        """
        return "".join(self.random.choices("TCGA", k=length))
