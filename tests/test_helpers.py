import pytest

from mimesis.helpers import Random


@pytest.fixture
def random():
    return Random()


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
        (['U'], 10),
        (['A'], 20),
    ],
)
def test_schoice(random, seq, length):
    result = random.schoice(seq, length)
    assert len(result) == length


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
