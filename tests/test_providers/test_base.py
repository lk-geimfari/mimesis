import re

import pytest

from mimesis.enums import Gender
from mimesis.exceptions import NonEnumerableError, UnsupportedLocale
from mimesis.locales import LIST_OF_LOCALES
from mimesis.providers.base import BaseDataProvider

from . import patterns


class TestBase(object):

    @pytest.fixture
    def base_data_provider(self):
        return BaseDataProvider()

    @pytest.mark.parametrize(
        'inp, out', [
            ('EN', 'en'),
            ('DE', 'de'),
            ('RU', 'ru'),
        ],
    )
    def test_setup_locale(self, base_data_provider, inp, out):
        result = BaseDataProvider(locale=inp)
        assert result.locale == out

    def test_setup_locale_unsupported_locale(self):
        with pytest.raises(UnsupportedLocale):
            BaseDataProvider(locale='nil')

    def test_str(self, base_data_provider):
        assert re.match(
            patterns.DATA_PROVIDER_STR_REGEX,
            str(base_data_provider))

    @pytest.mark.parametrize(
        'gender, excepted', [
            (Gender.MALE, 'male'),
            (Gender.FEMALE, 'female'),
            (None, ['female', 'male']),
        ],
    )
    def test_validate_enum(self, base_data_provider, gender, excepted):
        result = base_data_provider._validate_enum(gender, Gender)

        assert (result == excepted) or (result in excepted)
        assert result in [item.value for item in Gender]

        with pytest.raises(NonEnumerableError):
            base_data_provider._validate_enum('', '')

    @pytest.mark.parametrize('locale', LIST_OF_LOCALES)
    def test_get_current_locale(self, locale):
        base = BaseDataProvider(locale=locale)
        assert locale == base.get_current_locale()


class TestSeededBase(object):

    @pytest.fixture
    def _bases(self, seed):
        return BaseDataProvider(seed=seed), BaseDataProvider(seed=seed)

    def test_base_random(self, _bases):
        b1, b2 = _bases
        assert b1.random.randints() == b2.random.randints()
