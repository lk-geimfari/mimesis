import pytest

from mimesis.enums import Gender
from mimesis.random import random as _random


@pytest.fixture
def random():
    return _random


@pytest.mark.parametrize(
    "n, a, b",
    [
        (3, 1, 20),
        (5, 1, 20),
        (10, 1, 20),
    ],
)
def test_randints(random, n, a, b):
    result = random.randints(n, a, b)
    assert len(result) == n
    assert all(a <= x <= b for x in result)


def test_randints_value_error(random):
    with pytest.raises(ValueError):
        random.randints(0, 1, 2)


@pytest.mark.parametrize(
    "str_seq, length",
    [
        ("U", 10),
        ("A", 20),
    ],
)
def test_generate_string(random, str_seq, length):
    result = random._generate_string(str_seq, length)
    assert len(result) == length


@pytest.mark.parametrize("precision", [4, 6, 8])
def test_uniform(random, precision):
    result = random.uniform(2.3, 10.5, precision)
    assert isinstance(result, float)

    result = str(result).split(".")[1]
    assert precision >= len(result)


@pytest.mark.parametrize(
    "mask, digit, char",
    [
        ("##-FA-@@", "#", "@"),
        ("**-AF-$$", "*", "$"),
        ("**-š好-$$", "*", "$"),
    ],
)
def test_custom_code(random, mask, digit, char):
    result = random.custom_code(mask=mask, char=char, digit=digit)
    digit, middle, char = result.split("-")
    _, middle_mask, _ = mask.split("-")
    assert char.isalpha()
    assert digit.isdigit()
    assert middle == middle_mask


@pytest.mark.parametrize(
    "mask, digit, char",
    [
        ("??-FF-??", "?", "?"),
        ("@@-FF-@@", "@", "@"),
    ],
)
def test_custom_code_with_same_placeholders(random, mask, digit, char):
    with pytest.raises(ValueError):
        random.custom_code(mask=mask, char=char, digit=digit)


@pytest.mark.parametrize(
    "seed, expected",
    [
        (32, "C239"),
        (0xFF, "B670"),
        ("👽", "B806"),
    ],
)
def test_custom_code_with_seed(random, seed, expected):
    random.seed(seed)
    assert random.custom_code() == expected


def test_get_random_item(random):
    result = random.choice_enum_item(Gender)
    assert result in Gender

    random.seed(0xF)
    result_1 = random.choice_enum_item(Gender)
    result_2 = random.choice_enum_item(Gender)
    assert result_1 == result_2


def test_weighted_choice(random):
    result = [
        random.weighted_choice(
            choices={
                Gender.MALE: 0.1,
                Gender.FEMALE: 0.9,
            },
        )
        for _ in range(100)
    ]

    assert result.count(Gender.MALE) < 20
    assert result.count(Gender.FEMALE) > 80


def test_weighted_choice_with_empty_dict(random):
    with pytest.raises(ValueError):
        random.weighted_choice(choices={})
