import pytest

from mimesis.builtins import UkraineSpecProvider
from mimesis.enums import Gender
from mimesis.exceptions import NonEnumerableError


@pytest.fixture
def ukraine():
    return UkraineSpecProvider()


@pytest.mark.parametrize(
    'gender', [
        Gender.FEMALE,
        Gender.MALE,
    ],
)
def test_patronymic(ukraine, gender):
    result = ukraine.patronymic(gender=gender)

    assert result is not None
    assert len(result) >= 4

    with pytest.raises(NonEnumerableError):
        ukraine.patronymic(gender='nil')
