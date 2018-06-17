import pytest

from mimesis.enums import Gender
from mimesis.helpers import get_random_item
from mimesis.helpers import random as _random


@pytest.fixture
def random():
    return _random


def test_randints(random):
    result = random.randints()

    # Length of default list is 3
    assert len(result) == 3

    result = random.randints(25, 1, 1)

    assert len(result) == 25
    # All elements in result_custom equals to 1.
    assert result[0] == 1 and result[-1] == 1

    with pytest.raises(ValueError):
        random.randints(amount=0)


@pytest.mark.parametrize(
    'n', (8, 16, 32, 64),
)
def test_urandom(random, n):
    result = random.urandom(n)

    assert len(result) == n
    assert isinstance(result, bytes)


@pytest.mark.parametrize(
    'seq, length', [
        ('U', 10),
        ('A', 20),
    ],
)
def test_schoice(random, seq, length):
    result = random.schoice(seq, length)
    assert len(result) == length


@pytest.mark.parametrize(
    'precision', [
        4,
        6,
        8,
    ],
)
def test_uniform(random, precision):
    result = random.uniform(2.3, 10.5, precision)
    assert isinstance(result, float)

    result = str(result).split('.')[1]
    assert precision >= len(result)


def test_custom_code(random):
    result = random.custom_code(mask='AB@@@-###-@@@', char='@', digit='#')
    assert len(result) == 13

    a, b, c = result.split('-')
    assert a.isalpha()
    assert b.isdigit()
    assert c.isalpha()

    random.seed(50)
    result = random.custom_code()
    assert result == 'M262'


@pytest.mark.parametrize(
    'amount', [
        2,
        3,
        4,
    ],
)
def test_multiple_choice(random, amount):
    seq = [x for x in range(8)]
    result = random.multiple_choice(seq, amount)
    assert len(result) == amount


def test_get_random_item(random):
    result = get_random_item(Gender)
    assert result in Gender

    random.seed(0xf)
    result_1 = get_random_item(Gender, rnd=random)
    result_2 = get_random_item(Gender, rnd=random)
    assert result_1 == result_2
