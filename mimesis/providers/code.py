"""The data provider of a variety of codes."""

from typing import Optional

from mimesis.data import (EAN_MASKS, IMEI_TACS, ISBN_GROUPS, ISBN_MASKS,
                          LOCALE_CODES)
from mimesis.enums import EANFormat, ISBNFormat
from mimesis.providers.base import BaseDataProvider
from mimesis.utils import luhn_checksum

__all__ = ['Code']


class Code(BaseDataProvider):
    """Class that provides methods for generating codes."""

    def __init__(self, *args, **kwargs):
        """Initialize attributes.

        :param locale: Current locale.
        """
        super().__init__(*args, **kwargs)

    def locale_code(self) -> str:
        """Get a random locale code (MS-LCID).

        See Windows Language Code Identifier Reference
        for more information.

        :return: Locale code.

        :Example:

        >>> code = Code()
        >>> locale_code = code.locale_code()
        >>> locale_code in LOCALE_CODES
        True
        """
        return self.random.choice(LOCALE_CODES)

    def issn(self, mask: str = '####-####') -> str:
        """Generate a random ISSN.

        :param mask: Mask of ISSN.
        :return: ISSN.

        :Example:

        >>> code = Code()
        >>> issn = code.issn()
        >>> len(issn) == 9
        True
        """
        return self.random.custom_code(mask=mask)

    def isbn(self, fmt: Optional[ISBNFormat] = None) -> str:
        """Generate ISBN for current locale.

        To change ISBN format, pass parameter ``fmt`` with needed value of
        the enum object :class:`~mimesis.enums.ISBNFormat`

        :param fmt: ISBN format.
        :return: ISBN.
        :raises NonEnumerableError: if fmt is not enum ISBNFormat.

        :Example:

        >>> code = Code()
        >>> isbn = code.isbn()
        >>> isinstance(isbn, str)
        True
        """
        fmt_value = self._validate_enum(item=fmt, enum=ISBNFormat)
        mask = ISBN_MASKS[fmt_value].format(
            ISBN_GROUPS[self.locale])
        return self.random.custom_code(mask)

    def ean(self, fmt: Optional[EANFormat] = None) -> str:
        """Generate EAN.

        To change EAN format, pass parameter ``fmt`` with needed value of
        the enum object :class:`~mimesis.enums.EANFormat`.

        :param fmt: Format of EAN.
        :return: EAN.
        :raises NonEnumerableError: if fmt is not enum EANFormat.

        :Example:

        >>> code = Code()
        >>> ean = code.ean()
        >>> 8 <=len(ean) <= 13
        True
        """
        key = self._validate_enum(
            item=fmt,
            enum=EANFormat,
        )
        mask = EAN_MASKS[key]
        return self.random.custom_code(mask=mask)

    def imei(self) -> str:
        """Generate a random IMEI.

        :return: IMEI.

        :Example:

        >>> code = Code()
        >>> imei = code.imei()
        >>> len(imei) <= 15
        True
        """
        num = self.random.choice(IMEI_TACS)
        num = num + str(self.random.randint(100000, 999999))
        return num + luhn_checksum(num)

    def pin(self, mask: str = '####') -> str:
        """Generate a random PIN code.

        :param mask: Mask of pin code.
        :return: PIN code.

        :Example:

        >>> code = Code()
        >>> pin_code = code.pin()
        >>> len(pin_code) == 4
        True
        """
        return self.random.custom_code(mask=mask)
