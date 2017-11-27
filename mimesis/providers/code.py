from typing import Optional

from mimesis.enums import ISBNFormat, EANFormat
from mimesis.exceptions import NonEnumerableError
from mimesis.data import (
    EAN_MASKS,
    IMEI_TACS,
    ISBN_GROUPS,
    ISBN_MASKS,
    LOCALE_CODES,
)
from mimesis.providers.base import BaseProvider
from mimesis.utils import luhn_checksum, custom_code


class Code(BaseProvider):
    """Class that provides methods for generating codes (isbn, asin & etc.)"""

    def __init__(self, *args, **kwargs):
        """
        :param locale: Current locale.
        """
        super().__init__(*args, **kwargs)

    def locale_code(self) -> str:
        """Get a random locale code (MS-LCID).
        See Windows Language Code Identifier Reference for more information.

        :return: Locale code.

        :Example:
            de-ch
        """
        locale = self.random.choice(LOCALE_CODES)
        return locale

    @staticmethod
    def issn(mask: str = '####-####') -> str:
        """Generate a random International Standard Serial Number (ISSN).

        :param str mask: Mask of ISSN.
        :return: ISSN.
        """
        return custom_code(mask=mask)

    def isbn(self, fmt: Optional[ISBNFormat] = None) -> str:
        """Generate ISBN for current locale. Default is ISBN 10,
        but you also can use ISBN-13.

        :param str fmt: ISBN format.
        :return: ISBN.
        :raises NonEnumerableError: if fmt is not enum ISBNFormat.

        :Example:
            132-1-15411-375-8.
        """
        if fmt is None:
            fmt = ISBNFormat.get_random_item()

        if fmt and fmt in ISBNFormat:
            result_fmt = ISBN_MASKS[fmt.value]
            if self.locale in ISBN_GROUPS:
                mask = result_fmt.format(
                    ISBN_GROUPS[self.locale])
            else:
                mask = result_fmt.format(
                    ISBN_GROUPS['default'])

            return custom_code(mask=mask)
        else:
            raise NonEnumerableError(ISBNFormat)

    @staticmethod
    def ean(fmt: Optional[EANFormat] = None) -> str:
        """Generate EAN (European Article Number) code. Default is
        EAN-13, but you also can use EAN-8.

        :param str fmt: Format of EAN.
        :return: EAN.
        :raises NonEnumerableError: if fmt is not enum EANFormat.

        :Example:
            3953753179567.
        """

        if fmt is None:
            fmt = EANFormat.get_random_item()

        if fmt and fmt in EANFormat:
            mask = EAN_MASKS[fmt.value]
            return custom_code(mask=mask)
        else:
            raise NonEnumerableError(EANFormat)

    def imei(self) -> str:
        """Generate a random IMEI (International Mobile Station Equipment Identity).

        :return: IMEI.

        :Example:
            353918052107063
        """
        num = self.random.choice(IMEI_TACS) + custom_code(mask='######')
        return num + luhn_checksum(num)

    def pin(self, mask: str = '####') -> str:
        """Generate a random PIN code.

        :param str mask: Mask of pin code.
        :return: PIN code.

        :Example:
            5241.
        """
        return custom_code(mask=mask)
