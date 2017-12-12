import re

import pytest

from mimesis import Payment
from mimesis.data import CREDIT_CARD_NETWORKS
from mimesis.enums import CardType, Gender
from mimesis.exceptions import NonEnumerableError

from ._patterns import CREDIT_CARD_REGEX


@pytest.fixture
def payment():
    return Payment()


@pytest.fixture
def _seeded_payment():
    return Payment(seed=42)


def test_bitcoin(payment):
    result = payment.bitcoin_address()
    assert result[0] in ['1', '3']
    assert len(result) == 34


def test_seeded_bitcoin(_seeded_payment):
    result = _seeded_payment.bitcoin_address()
    # assert result ==
    result = _seeded_payment.bitcoin_address()
    # assert result ==
    pass


def test_ethereum_address(payment):
    pattern = r'^0x([a-zA-Z0-9]{40})$'
    address = payment.ethereum_address()
    assert re.match(pattern, address)


def test_seeded_ethereum_address(_seeded_payment):
    address = _seeded_payment.ethereum_address()
    # assert result ==
    address = _seeded_payment.ethereum_address()
    # assert result ==
    pass


def test_cvv(payment):
    result = payment.cvv()
    assert 100 <= result
    assert result <= 999


def test_seeded_cvv(_seeded_payment):
    result = _seeded_payment.cvv()
    # assert result ==
    result = _seeded_payment.cvv()
    # assert result ==
    pass


@pytest.mark.parametrize(
    'card_type', [
        CardType.VISA,
        CardType.MASTER_CARD,
        CardType.AMERICAN_EXPRESS,
    ],
)
def test_credit_card_number(payment, card_type):
    result = payment.credit_card_number(card_type=card_type)
    assert re.match(CREDIT_CARD_REGEX, result)

    with pytest.raises(NonEnumerableError):
        payment.credit_card_number(card_type='nil')


def test_seeded_credit_card_number(_seeded_payment):
    result = _seeded_payment.credit_card_number(card_type=CardType.VISA)
    # assert result ==
    result = _seeded_payment.credit_card_number()
    # assert result ==
    result = _seeded_payment.credit_card_number()
    # assert result ==
    pass


def test_expiration_date(payment):
    result = payment.credit_card_expiration_date(
        minimum=16, maximum=25)

    year = result.split('/')[1]
    assert int(year) >= 16
    assert int(year) <= 25


def test_seeded_expiration_date(_seeded_payment):
    result = _seeded_payment.credit_card_expiration_date(
        minimum=17, maximum=42)
    # assert result ==
    result = _seeded_payment.credit_card_expiration_date()
    # assert result ==
    result = _seeded_payment.credit_card_expiration_date()
    # assert result ==
    pass


def test_cid(payment):
    result = payment.cid()
    assert 1000 <= result
    assert result <= 9999


def test_seeded_cid(_seeded_payment):
    result = _seeded_payment.cid()
    # assert result ==
    result = _seeded_payment.cid()
    # assert result ==
    pass


def test_paypal(payment):
    result = payment.paypal()
    assert result is not None


def test_seeded_paypal(_seeded_payment):
    result = _seeded_payment.paypal()
    # assert result ==
    result = _seeded_payment.paypal()
    # assert result ==
    pass


@pytest.mark.parametrize(
    'gender', [
        Gender.MALE,
        Gender.FEMALE,
    ],
)
def test_credit_card_owner(payment, gender):
    result = payment.credit_card_owner(gender=gender)
    assert isinstance(result, dict)
    assert 'owner' in result
    assert 'credit_card' in result
    assert 'expiration_date' in result


def test_seeded_credit_card_owner(_seeded_payment):
    result = _seeded_payment.credit_card_owner(gender=Gender.FEMALE)
    # assert result ==
    result = _seeded_payment.credit_card_owner()
    # assert result ==
    result = _seeded_payment.credit_card_owner()
    # assert result ==
    pass


def credit_card_network(payment):
    result = payment.credit_card_network()
    assert result in CREDIT_CARD_NETWORKS


def credit_seeded_card_network(_seeded_payment):
    result = _seeded_payment.credit_card_network()
    # assert result ==
    result = _seeded_payment.credit_card_network()
    # assert result ==
    pass
