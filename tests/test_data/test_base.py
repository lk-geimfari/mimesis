import pytest

from mimesis.enums import Gender
from mimesis.exceptions import NonEnumerableError
from mimesis.providers.base import ValidateEnumMixin


@pytest.fixture
def boilerplate():
    return ValidateEnumMixin()


@pytest.mark.parametrize(
    'gender, excepted', [
        (Gender.MALE, 'male'),
        (Gender.FEMALE, 'female'),
        (None, ['female', 'male']),
    ],
)
def test_validate_enum(boilerplate, gender, excepted):
    result = boilerplate._validate_enum(gender, Gender)

    assert (result == excepted) or (result in excepted)
    assert result in [item.value for item in Gender]

    with pytest.raises(NonEnumerableError):
        boilerplate._validate_enum('', '')
