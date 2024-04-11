"""The data provider of a variety of codes."""

from mimesis.datasets import (
    EAN_MASKS,
    IMEI_TACS,
    ISBN_GROUPS,
    ISBN_MASKS,
    LOCALE_CODES,
)
from mimesis.enums import EANFormat, ISBNFormat
from mimesis.locales import Locale
from mimesis.providers.base import BaseProvider
from mimesis.shortcuts import luhn_checksum

__all__ = ["Code"]


class Code(BaseProvider):
    """A class, which provides methods for generating codes."""

    class Meta:
        name = "code"

    def locale_code(self) -> str:
        """Generates a random locale code (MS-LCID).

        See Windows Language Code Identifier Reference
        for more information.

        :return: Locale code.
        """
        return self.random.choice(LOCALE_CODES)

    def issn(self, mask: str = "####-####") -> str:
        """Generates a random ISSN.

        :param mask: Mask of ISSN.
        :return: ISSN.
        """
        return self.random.generate_string_by_mask(mask=mask)

    def isbn(
        self, fmt: ISBNFormat | None = None, locale: Locale = Locale.DEFAULT
    ) -> str:
        """Generates ISBN for current locale.

        To change ISBN format, pass parameter ``code`` with needed value of
        the enum object :class:`~mimesis.enums.ISBNFormat`

        :param fmt: ISBN format.
        :param locale: Locale code.
        :return: ISBN.
        :raises NonEnumerableError: if code is not enum ISBNFormat.
        """
        fmt_value = self.validate_enum(item=fmt, enum=ISBNFormat)
        mask = ISBN_MASKS[fmt_value].format(ISBN_GROUPS[locale.value])
        return self.random.generate_string_by_mask(mask)

    def ean(self, fmt: EANFormat | None = None) -> str:
        """Generates EAN.

        To change an EAN format, pass parameter ``code`` with needed value of
        the enum object :class:`~mimesis.enums.EANFormat`.

        :param fmt: Format of EAN.
        :return: EAN.
        :raises NonEnumerableError: if code is not enum EANFormat.
        """
        key = self.validate_enum(
            item=fmt,
            enum=EANFormat,
        )
        mask = EAN_MASKS[key]
        return self.random.generate_string_by_mask(mask=mask)

    def imei(self) -> str:
        """Generates a random IMEI.

        :return: IMEI.
        """
        num = self.random.choice(IMEI_TACS)
        num += str(self.random.randint(100000, 999999))
        return num + luhn_checksum(num)

    def pin(self, mask: str = "####") -> str:
        """Generates a random PIN code.

        :param mask: Mask of pin code.
        :return: PIN code.
        """
        return self.random.generate_string_by_mask(mask=mask)
