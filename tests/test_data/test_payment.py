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
    assert result == '1bVrpoiVgRV5IfLBcbfnoGMbJmTPSIAoCL'
    result = _seeded_payment.bitcoin_address()
    assert result == '3Z3aWZkSBvrjn9Wvgfygw2wMqZcUDIh7yf'


def test_ethereum_address(payment):
    pattern = r'^0x([a-zA-Z0-9]{40})$'
    for _ in range(42):
        address = payment.ethereum_address()
        assert re.match(pattern, address)


def test_seeded_ethereum_address(_seeded_payment):
    result = _seeded_payment.ethereum_address()
    assert result == '0x46685257bdd640fb06671ad11c80317fa3b1799d'
    result = _seeded_payment.ethereum_address()
    assert result == '0x1a3d1fa7bc8960a923b8c1e9392456de3eb13b90'


def test_cvv(payment):
    result = payment.cvv()
    assert 100 <= result
    assert result <= 999


def test_seeded_cvv(_seeded_payment):
    result = _seeded_payment.cvv()
    assert result == 754
    result = _seeded_payment.cvv()
    assert result == 214


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


# TODO: https://github.com/lk-geimfari/mimesis/issues/325#issuecomment-352364359
def skip_test_seeded_credit_card_number(_seeded_payment):
    result = _seeded_payment.credit_card_number(card_type=CardType.VISA)
    assert result == '4654 1043 3218 1966'
    result = _seeded_payment.credit_card_number()
    assert result == '2236 3890 8386 3794'
    result = _seeded_payment.credit_card_number()
    assert result == '4828 0265 4235 1165'


def test_expiration_date(payment):
    result = payment.credit_card_expiration_date(
        minimum=16, maximum=25)

    year = result.split('/')[1]
    assert int(year) >= 16
    assert int(year) <= 25


def test_seeded_expiration_date(_seeded_payment):
    result = _seeded_payment.credit_card_expiration_date(
        minimum=17, maximum=42)
    assert result == '11/20'
    result = _seeded_payment.credit_card_expiration_date()
    assert result == '01/20'
    result = _seeded_payment.credit_card_expiration_date()
    assert result == '04/19'


def test_cid(payment):
    result = payment.cid()
    assert 1000 <= result
    assert result <= 9999


def test_seeded_cid(_seeded_payment):
    result = _seeded_payment.cid()
    assert result == 2824
    result = _seeded_payment.cid()
    assert result == 1409


def test_paypal(payment):
    result = payment.paypal()
    assert result is not None


def test_seeded_paypal(_seeded_payment):
    result = _seeded_payment.paypal()
    assert result == 'afterfuture1940@gmail.com'
    result = _seeded_payment.paypal()
    assert result == 'boons1871@yandex.com'


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


# TODO: https://github.com/lk-geimfari/mimesis/issues/325#issuecomment-352364359
def skip_test_seeded_credit_card_owner(_seeded_payment):
    result = _seeded_payment.credit_card_owner(gender=Gender.FEMALE)
    assert result == {
        'owner': 'DARLENA AVILA',
        'credit_card': '3404 332181 96006',
        'expiration_date': '02/19',
    }
    result = _seeded_payment.credit_card_owner()
    assert result == {
        'owner': 'HANK DAY',
        'credit_card': '2479 8386 3794 0264',
        'expiration_date': '06/20',
    }
    result = _seeded_payment.credit_card_owner()
    assert result == {
        'owner': 'CRYSTLE OSBORN',
        'credit_card': '5490 1161 5594 0786',
        'expiration_date': '02/22',
    }


def test_credit_card_network(payment):
    result = payment.credit_card_network()
    assert result in CREDIT_CARD_NETWORKS


def test_credit_seeded_card_network(_seeded_payment):
    result = _seeded_payment.credit_card_network()
    assert result == 'Visa'
    result = _seeded_payment.credit_card_network()
    assert result == 'Visa'
    result = _seeded_payment.credit_card_network()
    assert result == 'Chase'
