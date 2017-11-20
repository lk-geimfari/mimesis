from mimesis.data import IMEI_TACS, ISBN_GROUPS, LOCALE_CODES
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

    def isbn(self, fmt: str = 'isbn-10') -> str:
        """Generate ISBN for current locale. Default is ISBN 10,
        but you also can use ISBN-13.

        :param str fmt: ISBN format.
        :return: ISBN.

        :Example:
            132-1-15411-375-8.
        """
        groups = ISBN_GROUPS

        # TODO: Enums here

        mask = '###-{0}-#####-###-#' if \
            fmt == 'isbn-13' else '{0}-#####-###-#'

        if self.locale in groups:
            mask = mask.format(groups[self.locale])
        else:
            mask = mask.format(groups['default'])

        return custom_code(mask=mask)

    @staticmethod
    def ean(fmt: str = 'ean-13') -> str:
        """Generate EAN (European Article Number) code. Default is
        EAN-13, but you also can use EAN-8.

        :param str fmt: Format of EAN.
        :return: EAN.

        :Example:
            3953753179567.
        """

        # TODO: here too
        mask = '########' if fmt == 'ean-8' \
            else '#############'
        return custom_code(mask=mask)

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
