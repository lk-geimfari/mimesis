import pytest

from mimesis.enums import Gender
from mimesis.random import get_random_item
from mimesis.random import random as _random


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
    'str_seq, length', [
        ('U', 10),
        ('A', 20),
    ],
)
def test_generate_string(random, str_seq, length):
    result = random.generate_string(str_seq, length)
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


@pytest.mark.parametrize(
    'mask, digit, char', [
        ('##-FA-@@', '#', '@'),
        ('**-AF-$$', '*', '$'),
        ('**-š好-$$', '*', '$'),
    ],
)
def test_custom_code(random, mask, digit, char):
    result = random.custom_code(mask=mask, char=char, digit=digit)
    digit, middle, char = result.split('-')
    _, middle_mask, _ = mask.split('-')
    assert char.isalpha()
    assert digit.isdigit()
    assert middle == middle_mask


@pytest.mark.parametrize(
    'mask, digit, char', [
        ('??-FF-??', '?', '?'),
        ('@@-FF-@@', '@', '@'),
    ],
)
def test_custom_code_with_same_placeholders(random, mask, digit, char):
    with pytest.raises(ValueError):
        random.custom_code(mask=mask, char=char, digit=digit)


@pytest.mark.parametrize(
    'seed, expected', [
        (32, 'C239'),
        (0xff, 'B670'),
        ('👽', 'B806'),
    ],
)
def test_custom_code_with_seed(random, seed, expected):
    random.seed(seed)
    assert random.custom_code() == expected


def test_get_random_item(random):
    result = get_random_item(Gender)
    assert result in Gender

    random.seed(0xf)
    result_1 = get_random_item(Gender, rnd=random)
    result_2 = get_random_item(Gender, rnd=random)
    assert result_1 == result_2


@pytest.mark.parametrize(
    'length', [
        64,
        128,
        256,
    ],
)
def test_randstr(random, length):
    result = random.randstr(length=length)
    assert len(result) == length


@pytest.mark.parametrize(
    'count', [
        1000,
        10000,
        100000,
    ],
)
def test_randstr_unique(random, count):
    results = [random.randstr(unique=True) for _ in range(count)]
    assert len(results) == len(set(results))
