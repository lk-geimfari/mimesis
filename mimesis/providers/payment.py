import re
import string
from typing import Optional

from mimesis.data import CREDIT_CARD_NETWORKS
from mimesis.enums import CardType, Gender
from mimesis.exceptions import NonEnumerableError
from mimesis.providers.base import BaseProvider
from mimesis.providers.personal import Personal
from mimesis.utils import luhn_checksum


class Payment(BaseProvider):
    """Data related to payments"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__personal = Personal('en')

    def cid(self) -> int:
        """Generate a random CID code.

        :return: CID code.

        :Example:
            7452
        """
        return self.random.randint(1000, 9999)

    def paypal(self) -> str:
        """Generate a random PayPal account.

        :return: Email of PapPal user.

        :Example:
            wolf235@gmail.com
        """
        return self.__personal.email()

    def bitcoin_address(self) -> str:
        """Generate a random bitcoin address.

        :return: Bitcoin address.

        :Example:
            3EktnHQD7RiAE6uzMj2ZifT9YgRrkSgzQX
        """
        type_ = self.random.choice(['1', '3'])
        letters = string.ascii_letters + string.digits
        address = [self.random.choice(letters) for _ in range(33)]
        return type_ + ''.join(address)

    def credit_card_network(self) -> str:
        """Get random credit card network

        :return: Credit card network

        :Example:
            MasterCard
        """
        return self.random.choice(CREDIT_CARD_NETWORKS)

    def credit_card_number(self, card_type: Optional[CardType] = None) -> str:
        """Generate a random credit card number.

        :param str card_type: Issuing Network. Default is Visa.
        :return: Credit card number.
        :raises NotImplementedError: if cart_type is not supported.

        :Example:
            4455 5299 1152 2450
        """
        length = 16
        regex = re.compile('(\d{4})(\d{4})(\d{4})(\d{4})')

        if card_type is None:
            card_type = CardType.get_random_item()

        if card_type == CardType.VISA:
            number = self.random.randint(4000, 4999)
        elif card_type == CardType.MASTER_CARD:
            number = self.random.choice([
                self.random.randint(2221, 2720),
                self.random.randint(5100, 5500),
            ])
        elif card_type == CardType.AMERICAN_EXPRESS:
            number = self.random.choice([34, 37])
            length = 15
            regex = re.compile('(\d{4})(\d{6})(\d{5})')
        else:
            raise NonEnumerableError(CardType)

        str_num = str(number)
        while len(str_num) < length - 1:
            str_num += self.random.choice(string.digits)

        groups = regex.search(str_num + luhn_checksum(str_num))
        card = ' '.join(groups.groups())
        return card

    def credit_card_expiration_date(self, minimum: int = 16,
                                    maximum: int = 25) -> str:
        """Generate a random expiration date for credit card.

        :param int minimum: Date of issue.
        :param int maximum: Maximum of expiration_date.
        :return: Expiration date of credit card.

        :Example:
            03/19.
        """
        month = self.random.randint(1, 12)
        year = self.random.randint(minimum, maximum)
        return '{0:02d}/{1}'.format(month, year)

    def cvv(self) -> int:
        """Generate a random card verification value (CVV).

        :return: CVV code.

        :Example:
            324
        """
        return self.random.randint(100, 999)

    def credit_card_owner(self, gender: Optional[Gender] = None) -> dict:
        owner = {
            'credit_card': self.credit_card_number(),
            'expiration_date': self.credit_card_expiration_date(),
            'owner': self.__personal.full_name(gender=gender).upper(),
        }
        return owner
