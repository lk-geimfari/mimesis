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
from mimesis.shortcuts import gs1_checksum, luhn_checksum, mod11_checksum


__all__ = ["Code"]


class Code(BaseProvider):
    """A class that provides methods for generating codes."""

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

        The last character of the mask is replaced by the mod 11 check digit,
        which may be the letter ``X``.

        :param mask: Mask of ISSN.
        :return: ISSN.
        """
        payload = self.random.generate_string_by_mask(mask=mask[:-1])
        # The mask may contain separators for readability, but a check digit is
        # computed over the digits alone.
        digits = "".join(char for char in payload if char.isdigit())
        return payload + mod11_checksum(digits)

    def isbn(
        self, fmt: ISBNFormat | None = None, locale: Locale = Locale.DEFAULT
    ) -> str:
        """Generates an ISBN for the current locale.

        To change ISBN format, pass parameter ``code`` with needed value of
        the enum object :class:`~mimesis.enums.ISBNFormat`

        :param fmt: ISBN format.
        :param locale: Locale code.
        :return: ISBN.
        :raises NonEnumerableError: if code is not enum ISBNFormat.
        """
        fmt_value = self.validate_enum(item=fmt, enum=ISBNFormat)
        mask = ISBN_MASKS[fmt_value].format(ISBN_GROUPS[locale.value])
        payload = self.random.generate_string_by_mask(mask[:-1])
        # The mask may contain separators for readability, but a check digit is
        # computed over the digits alone.
        digits = "".join(char for char in payload if char.isdigit())
        if fmt_value == "isbn-13":
            return payload + gs1_checksum(digits)
        return payload + mod11_checksum(digits)

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
        payload = self.random.generate_string_by_mask(mask=mask[:-1])
        return payload + gs1_checksum(payload)

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
