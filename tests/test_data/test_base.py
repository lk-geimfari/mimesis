import pytest

from mimesis import config
from mimesis.enums import Gender
from mimesis.exceptions import NonEnumerableError
from mimesis.providers.base import BaseDataProvider


@pytest.fixture
def base_data_provider():
    return BaseDataProvider()


@pytest.mark.parametrize(
    'gender, excepted', [
        (Gender.MALE, 'male'),
        (Gender.FEMALE, 'female'),
        (None, ['female', 'male']),
    ],
)
def test_validate_enum(base_data_provider, gender, excepted):
    result = base_data_provider._validate_enum(gender, Gender)

    assert (result == excepted) or (result in excepted)
    assert result in [item.value for item in Gender]

    with pytest.raises(NonEnumerableError):
        base_data_provider._validate_enum('', '')


@pytest.mark.parametrize('locale', config.LIST_OF_LOCALES)
def test_get_current_locale(locale):
    base = BaseDataProvider(locale=locale)
    assert locale == base.get_current_locale()


@pytest.fixture
def seeded_base_data_provider():
    return BaseDataProvider(seed=42)


def test_base_with_seed(seeded_base_data_provider):
    result = seeded_base_data_provider.random.randint(1, 10)
    assert result == 2
