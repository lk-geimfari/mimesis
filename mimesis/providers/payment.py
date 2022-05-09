"""Provides data related to payment."""

import re
import string
import typing as t

from mimesis.data import CREDIT_CARD_NETWORKS
from mimesis.enums import CardType, Gender
from mimesis.exceptions import NonEnumerableError
from mimesis.locales import Locale
from mimesis.providers.base import BaseProvider
from mimesis.providers.person import Person
from mimesis.random import get_random_item
from mimesis.shortcuts import luhn_checksum

__all__ = ["Payment"]


class Payment(BaseProvider):
    """Class that provides data related to payments."""

    def __init__(self, *args: t.Any, **kwargs: t.Any) -> None:
        """Initialize attributes.

        :param args: Arguments.
        :param kwargs: Keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self._person = Person(Locale.EN, seed=self.seed)

    class Meta:
        """Class for metadata."""

        name: t.Final[str] = "payment"

    def cid(self) -> str:
        """Generate a random CID.

        :return: CID code.

        :Example:
            7452
        """
        return f"{self.random.randint(1, 9999):04d}"

    def paypal(self) -> str:
        """Generate a random PayPal account.

        :return: Email of PapPal user.

        :Example:
            wolf235@gmail.com
        """
        return self._person.email()

    def bitcoin_address(self) -> str:
        """Generate a random bitcoin address.

        Keep in mind that although it generates **valid-looking** addresses,
        it does not mean that they are actually valid.

        :return: Bitcoin address.

        :Example:
            3EktnHQD7RiAE6uzMj2ZifT9YgRrkSgzQX
        """
        type_ = self.random.choice(["1", "3"])
        characters = string.ascii_letters + string.digits
        return type_ + "".join(self.random.choices(characters, k=33))

    def ethereum_address(self) -> str:
        """Generate a random Ethereum address.

        ..note: The address will look like Ethereum address,
        but keep in mind that it is not the valid address.

        :return: Ethereum address.

        :Example:
            0xe8ece9e6ff7dba52d4c07d37418036a89af9698d
        """
        bits = self.random.getrandbits(160)
        address = bits.to_bytes(20, byteorder="big")
        return "0x" + address.hex()

    def credit_card_network(self) -> str:
        """Generate a random credit card network.

        :return: Credit card network

        :Example:
            MasterCard
        """
        return self.random.choice(CREDIT_CARD_NETWORKS)

    def credit_card_number(self, card_type: t.Optional[CardType] = None) -> str:
        """Generate a random credit card number.

        :param card_type: Issuing Network. Default is Visa.
        :return: Credit card number.
        :raises NotImplementedError: if card_type not supported.

        :Example:
            4455 5299 1152 2450
        """
        length = 16
        regex = re.compile(r"(\d{4})(\d{4})(\d{4})(\d{4})")

        if card_type is None:
            card_type = get_random_item(CardType, rnd=self.random)

        if card_type == CardType.VISA:
            number = self.random.randint(4000, 4999)
        elif card_type == CardType.MASTER_CARD:
            number = self.random.choice(
                [
                    self.random.randint(2221, 2720),
                    self.random.randint(5100, 5599),
                ]
            )
        elif card_type == CardType.AMERICAN_EXPRESS:
            number = self.random.choice([34, 37])
            length = 15
            regex = re.compile(r"(\d{4})(\d{6})(\d{5})")
        else:
            raise NonEnumerableError(CardType)

        str_num = str(number)
        while len(str_num) < length - 1:
            str_num += self.random.choice(string.digits)

        groups = regex.search(  # type: ignore
            str_num + luhn_checksum(str_num),
        ).groups()
        card = " ".join(groups)
        return card

    def credit_card_expiration_date(self, minimum: int = 16, maximum: int = 25) -> str:
        """Generate a random expiration date for credit card.

        :param minimum: Date of issue.
        :param maximum: Maximum of expiration_date.
        :return: Expiration date of credit card.

        :Example:
            03/19.
        """
        month = self.random.randint(1, 12)
        year = self.random.randint(minimum, maximum)
        return f"{month:02d}/{year}"

    def cvv(self) -> str:
        """Generate a random CVV.

        :return: CVV code.

        :Example:
            069
        """
        return f"{self.random.randint(1, 999):03d}"

    def credit_card_owner(
        self,
        gender: t.Optional[Gender] = None,
    ) -> t.Dict[str, str]:
        """Generate credit card owner.

        :param gender: Gender of credit card owner.
        :type gender: Gender's enum object.
        :return:
        """
        owner = {
            "credit_card": self.credit_card_number(),
            "expiration_date": self.credit_card_expiration_date(),
            "owner": self._person.full_name(gender=gender).upper(),
        }
        return owner
