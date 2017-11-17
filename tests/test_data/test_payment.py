import re

import pytest

from mimesis import Payment
from mimesis.enums import CardType
from ._patterns import CREDIT_CARD_REGEX


@pytest.fixture
def payment():
    return Payment()


def test_bitcoin(payment):
    result = payment.bitcoin_address()
    assert result[0] in ['1', '3']
    assert len(result) == 34


def test_cvv(payment):
    result = payment.cvv()
    assert 100 <= result
    assert result <= 999


@pytest.mark.parametrize(
    'card_type', [
        CardType.RANDOM,
        CardType.VISA,
        CardType.MASTER_CARD,
        CardType.AMERICAN_EXPRESS,
    ],
)
def test_credit_card_number(payment, card_type):
    result = payment.credit_card_number(card_type=card_type)
    assert re.match(CREDIT_CARD_REGEX, result)

    with pytest.raises(ValueError):
        payment.credit_card_number(card_type=None)


def test_expiration_date(payment):
    result = payment.credit_card_expiration_date(
        minimum=16, maximum=25)

    year = result.split('/')[1]
    assert int(year) >= 16
    assert int(year) <= 25


def test_cid(payment):
    result = payment.cid()
    assert 1000 <= result
    assert result <= 9999


def test_paypal(payment):
    result = payment.paypal()
    assert result is not None
