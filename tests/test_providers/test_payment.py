import re

import pytest

from mimesis import Payment
from mimesis.data import CREDIT_CARD_NETWORKS
from mimesis.enums import CardType, Gender
from mimesis.exceptions import NonEnumerableError

from . import patterns


class TestPayment(object):

    @pytest.fixture
    def payment(self):
        return Payment()

    def test_str(self, payment):
        assert re.match(patterns.PROVIDER_STR_REGEX, str(payment))

    def test_bitcoin(self, payment):
        result = payment.bitcoin_address()
        assert result[0] in ['1', '3']
        assert len(result) == 34

    def test_ethereum_address(self, payment):
        pattern = r'^0x([a-zA-Z0-9]{40})$'
        address = payment.ethereum_address()
        assert re.match(pattern, address)

    def test_cvv(self, payment):
        result = payment.cvv()
        assert 100 <= result
        assert result <= 999

    @pytest.mark.parametrize(
        'card_type', [
            CardType.VISA,
            CardType.MASTER_CARD,
            CardType.AMERICAN_EXPRESS,
        ],
    )
    def test_credit_card_number(self, payment, card_type):
        result = payment.credit_card_number(card_type=card_type)
        assert re.match(patterns.CREDIT_CARD_REGEX, result)

        with pytest.raises(NonEnumerableError):
            payment.credit_card_number(card_type='nil')

    def test_expiration_date(self, payment):
        result = payment.credit_card_expiration_date(
            minimum=16, maximum=25)

        year = result.split('/')[1]
        assert int(year) >= 16
        assert int(year) <= 25

    def test_cid(self, payment):
        result = payment.cid()
        assert 1000 <= result
        assert result <= 9999

    def test_paypal(self, payment):
        result = payment.paypal()
        assert result is not None

    @pytest.mark.parametrize(
        'gender', [
            Gender.MALE,
            Gender.FEMALE,
        ],
    )
    def test_credit_card_owner(self, payment, gender):
        result = payment.credit_card_owner(gender=gender)
        assert isinstance(result, dict)
        assert 'owner' in result
        assert 'credit_card' in result
        assert 'expiration_date' in result

    def test_credit_card_network(self, payment):
        result = payment.credit_card_network()
        assert result in CREDIT_CARD_NETWORKS


class TestSeededPayment(object):

    @pytest.fixture
    def p1(self, seed):
        return Payment(seed=seed)

    @pytest.fixture
    def p2(self, seed):
        return Payment(seed=seed)

    def test_bitcoin_address(self, p1, p2):
        assert p1.bitcoin_address() == p2.bitcoin_address()

    def test_ethereum_address(self, p1, p2):
        assert p1.ethereum_address() == p2.ethereum_address()

    def test_cvv(self, p1, p2):
        assert p1.cvv() == p2.cvv()

    def test_credit_card_number(self, p1, p2):
        assert p1.credit_card_number() == p2.credit_card_number()
        assert p1.credit_card_number(card_type=CardType.VISA) == \
            p2.credit_card_number(card_type=CardType.VISA)

    def test_credit_card_expiration_date(self, p1, p2):
        assert p1.credit_card_expiration_date() == \
            p2.credit_card_expiration_date()
        assert p1.credit_card_expiration_date(minimum=18, maximum=24) == \
            p2.credit_card_expiration_date(minimum=18, maximum=24)

    def test_cid(self, p1, p2):
        assert p1.cid() == p2.cid()

    def test_paypal(self, p1, p2):
        assert p1.paypal() == p2.paypal()

    def test_credit_card_owner(self, p1, p2):
        assert p1.credit_card_owner() == p2.credit_card_owner()
        assert p1.credit_card_owner(gender=Gender.FEMALE) == \
            p2.credit_card_owner(gender=Gender.FEMALE)

    def test_credit_card_network(self, p1, p2):
        assert p1.credit_card_network() == p2.credit_card_network()
