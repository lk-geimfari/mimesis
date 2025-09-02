import pytest

from mimesis.builtins import KazakhstanSpecProvider
from mimesis.enums import Gender
from mimesis.exceptions import NonEnumerableError


@pytest.fixture
def kazakhstan():
    return KazakhstanSpecProvider()


@pytest.mark.parametrize(
    "gender",
    [
        Gender.FEMALE,
        Gender.MALE,
    ],
)
def test_patronymic(kazakhstan, gender):
    result = kazakhstan.patronymic(gender=gender)

    assert result is not None
    assert result

    with pytest.raises(NonEnumerableError):
        kazakhstan.patronymic(gender="nil")


def test_iin(kazakhstan):
    result = kazakhstan.iin()
    assert isinstance(result, str)
    assert len(result) == 12
