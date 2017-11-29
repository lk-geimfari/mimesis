from typing import Optional

from mimesis.data import SI_PREFIXES, SI_PREFIXES_SYM
from mimesis.enums import PrefixSign, UnitName
from mimesis.providers.base import BaseProvider


class UnitSystem(BaseProvider):
    """Class for generating name of unit.
    """

    def unit(self, name: Optional[UnitName] = None, symbol=False):
        """Get unit name.

        :param name: Enum object UnitName.
        :param symbol: Return only symbol
        :return: Unit.
        """
        result = self._validate_enum(item=name, enum=UnitName)

        if symbol:
            return result[1]
        return result[0]

    def prefix(self, sign: Optional[PrefixSign] = None,
               symbol: bool = False) -> str:
        """Get a random prefix for the International System of Units (SI)

        :param sign: Sing of number (positive, negative)
        :param symbol: Return symbol of prefix.
        :return: Prefix for SI.
        :raises NonEnumerableError: if sign is not supported.

        :Example:
            mega
        """
        prefixes = SI_PREFIXES_SYM if \
            symbol else SI_PREFIXES

        key = self._validate_enum(item=sign, enum=PrefixSign)
        return self.random.choice(prefixes[key])
