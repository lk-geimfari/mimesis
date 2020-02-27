# -*- coding: utf-8 -*-

"""The data provider of a variety of codes."""

from typing import Optional

from mimesis.data import (
    EAN_MASKS,
    IMEI_TACS,
    ISBN_GROUPS,
    ISBN_MASKS,
    LOCALE_CODES,
)
from mimesis.enums import EANFormat, ISBNFormat
from mimesis.providers.base import BaseProvider
from mimesis.shortcuts import luhn_checksum

__all__ = ['Code']


class Code(BaseProvider):
    """A class, which provides methods for generating codes."""

    def __init__(self, *args, **kwargs):
        """Initialize attributes.

        :param locale: Current locale.
        """
        super().__init__(*args, **kwargs)

    class Meta:
        """Class for metadata."""

        name = 'code'

    def locale_code(self) -> str:
        """Get a random locale code (MS-LCID).

        See Windows Language Code Identifier Reference
        for more information.

        :return: Locale code.
        """
        return self.random.choice(LOCALE_CODES)

    def issn(self, mask: str = '####-####') -> str:
        """Generate a random ISSN.

        :param mask: Mask of ISSN.
        :return: ISSN.
        """
        return self.random.custom_code(mask=mask)

    def isbn(self, fmt: Optional[ISBNFormat] = None,
             locale: str = 'en') -> str:
        """Generate ISBN for current locale.

        To change ISBN format, pass parameter ``fmt`` with needed value of
        the enum object :class:`~mimesis.enums.ISBNFormat`

        :param fmt: ISBN format.
        :param locale: Locale code.
        :return: ISBN.
        :raises NonEnumerableError: if fmt is not enum ISBNFormat.
        """
        fmt_value = self._validate_enum(item=fmt, enum=ISBNFormat)
        mask = ISBN_MASKS[fmt_value].format(
            ISBN_GROUPS[locale])
        return self.random.custom_code(mask)

    def ean(self, fmt: Optional[EANFormat] = None) -> str:
        """Generate EAN.

        To change EAN format, pass parameter ``fmt`` with needed value of
        the enum object :class:`~mimesis.enums.EANFormat`.

        :param fmt: Format of EAN.
        :return: EAN.
        :raises NonEnumerableError: if fmt is not enum EANFormat.
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
        """
        num = self.random.choice(IMEI_TACS)
        num = num + str(self.random.randint(100000, 999999))
        return num + luhn_checksum(num)

    def pin(self, mask: str = '####') -> str:
        """Generate a random PIN code.

        :param mask: Mask of pin code.
        :return: PIN code.
        """
        return self.random.custom_code(mask=mask)
