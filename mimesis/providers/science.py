"""Provides pseudo-scientific data."""

import typing as t

from mimesis.data import SI_PREFIXES, SI_PREFIXES_SYM
from mimesis.enums import MeasureUnit, MetricPrefixSign
from mimesis.providers.base import BaseProvider

__all__ = ["Science"]


class Science(BaseProvider):
    """Class for generating pseudo-scientific data."""

    class Meta:
        """Class for metadata."""

        name: t.Final[str] = "science"

    def rna_sequence(self, length: int = 10) -> str:
        """Generate a random RNA sequence.

        :param length: Length of block.
        :return: RNA sequence.

        :Example:
            AGUGACACAA
        """
        return self.random.generate_string("UCGA", length)

    def dna_sequence(self, length: int = 10) -> str:
        """Generate a random DNA sequence.

        :param length: Length of block.
        :return: DNA sequence.

        :Example:
            GCTTTAGACC
        """
        return self.random.generate_string("TCGA", length)

    def measure_unit(
        self,
        name: t.Optional[MeasureUnit] = None,
        symbol: bool = False,
    ) -> str:
        """Get unit name from International System of Units.

        :param name: Enum object UnitName.
        :param symbol: Return only symbol
        :return: Unit.
        """
        result: t.Tuple[str, str] = self.validate_enum(
            item=name,
            enum=MeasureUnit,
        )

        if symbol:
            return result[1]
        return result[0]

    def metric_prefix(
        self, sign: t.Optional[MetricPrefixSign] = None, symbol: bool = False
    ) -> str:
        """Get a random prefix for the International System of Units.

        :param sign: Sing of prefix (positive/negative).
        :param symbol: Return the symbol of the prefix.
        :return: Metric prefix for SI measure units.
        :raises NonEnumerableError: if sign is not supported.

        :Example:
            mega
        """
        prefixes = SI_PREFIXES_SYM if symbol else SI_PREFIXES

        key = self.validate_enum(item=sign, enum=MetricPrefixSign)
        return self.random.choice(prefixes[key])
