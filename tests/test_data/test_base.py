import pytest

from mimesis import config
from mimesis.enums import Gender
from mimesis.exceptions import NonEnumerableError
from mimesis.providers.base import BaseProvider, ValidateEnumMixin


@pytest.fixture
def validate_enum_mixin():
    return ValidateEnumMixin()


@pytest.mark.parametrize(
    'gender, excepted', [
        (Gender.MALE, 'male'),
        (Gender.FEMALE, 'female'),
        (None, ['female', 'male']),
    ],
)
def test_validate_enum(validate_enum_mixin, gender, excepted):
    result = validate_enum_mixin._validate_enum(gender, Gender)

    assert (result == excepted) or (result in excepted)
    assert result in [item.value for item in Gender]

    with pytest.raises(NonEnumerableError):
        validate_enum_mixin._validate_enum('', '')


@pytest.mark.parametrize('locale', config.LIST_OF_LOCALES)
def test_get_current_locale(locale):
    base = BaseProvider(locale=locale)
    assert locale == base.get_current_locale()
