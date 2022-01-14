import re

import pytest
from mimesis.enums import Gender
from mimesis.exceptions import LocaleError, NonEnumerableError
from mimesis.locales import Locale
from mimesis.providers import Code, Cryptographic, Internet, Person
from mimesis.providers.base import BaseDataProvider

from . import patterns


class TestBase:
    @pytest.fixture
    def base_data_provider(self):
        return BaseDataProvider()

    @pytest.mark.parametrize(
        "locale, new_locale",
        [
            (Locale.EN, Locale.RU),
        ],
    )
    def test_override_locale(self, locale, new_locale):
        provider = Person(locale)
        assert Locale(provider.locale) == locale

        with provider.override_locale(new_locale):
            assert "Жен." in provider._data["gender"]
            assert Locale(provider.locale) == new_locale

        assert Locale(provider.locale) == locale
        assert "Жен." not in provider._data["gender"]

        del provider.locale
        with pytest.raises(ValueError):
            with provider.override_locale(new_locale):
                pass

    def test_override_missing_locale_argument(self):
        provider = Person(Locale.EN)
        with pytest.raises(TypeError):
            with provider.override_locale():
                pass

    @pytest.mark.parametrize(
        "provider",
        [
            Code,
            Cryptographic,
            Internet,
        ],
    )
    def test_override_locale_independent(self, provider):
        with pytest.raises(AttributeError):
            with provider.override_locale():
                pass

    @pytest.mark.parametrize(
        "locale, city",
        [
            (Locale.EN, "New York"),
            (Locale.EN_GB, "Aberystwyth"),
            (Locale.RU, "Москва"),
        ],
    )
    def test_pull(self, locale, city):
        data_provider = BaseDataProvider(locale)
        data_provider._load_datafile("address.json")
        assert city in data_provider._data["city"]

    @pytest.mark.parametrize("locale", list(Locale))
    def test_pull_raises(self, locale):
        data_provider = BaseDataProvider(locale=locale)
        with pytest.raises(FileNotFoundError):
            data_provider._load_datafile("something.json")

    def test_extract(self, base_data_provider):
        dictionary = {"names": {"female": "Ariel", "male": "John"}}

        base_data_provider._data = dictionary

        a = list(sorted(dictionary["names"].keys()))
        b = list(sorted(base_data_provider.extract(["names"]).keys()))

        assert base_data_provider.extract(["names", "male"]) == "John"
        assert base_data_provider.extract(["names", "female"]) == "Ariel"
        assert base_data_provider.extract(["names", "other"], default="Sam") == "Sam"
        assert a == b

        with pytest.raises(ValueError):
            assert base_data_provider.extract([])

    def test_extract_missing_positional_arguments(self, base_data_provider):
        with pytest.raises(TypeError):
            assert base_data_provider.extract(default=None)

        with pytest.raises(TypeError):
            assert base_data_provider.extract()

    def test_update_dict(self, base_data_provider):
        first = {
            "animals": {
                "dogs": [
                    "spaniel",
                ],
            },
        }
        second = {
            "animals": {
                "cats": [
                    "maine coon",
                ],
            },
        }

        result = base_data_provider._update_dict(first, second)

        assert "cats" in result["animals"]
        assert "dogs" in result["animals"]

        third = {
            "animals": {
                "dogs": [
                    "golden retriever",
                ],
            },
        }

        result = base_data_provider._update_dict(first, third)
        assert "spaniel" not in result["animals"]["dogs"]

    @pytest.mark.parametrize(
        "inp, out",
        [
            (Locale.EN, "en"),
            (Locale.DE, "de"),
            (Locale.RU, "ru"),
        ],
    )
    def test_setup_locale(self, base_data_provider, inp, out):
        result = BaseDataProvider(locale=inp)
        assert result.locale == out

    def test_setup_locale_unsupported_locale(self):
        with pytest.raises(LocaleError):
            BaseDataProvider(locale="nil")

    def test_str(self, base_data_provider):
        assert re.match(patterns.DATA_PROVIDER_STR_REGEX, str(base_data_provider))

    @pytest.mark.parametrize(
        "gender, excepted",
        [
            (Gender.MALE, "male"),
            (Gender.FEMALE, "female"),
            (None, ["female", "male"]),
        ],
    )
    def test_validate_enum(self, base_data_provider, gender, excepted):
        result = base_data_provider.validate_enum(gender, Gender)

        assert (result == excepted) or (result in excepted)
        assert result in [item.value for item in Gender]

        with pytest.raises(NonEnumerableError):
            base_data_provider.validate_enum("", "")

    @pytest.mark.parametrize("locale", Locale)
    def test_get_current_locale(self, locale):
        base = BaseDataProvider(locale=locale)
        assert locale.value == base.get_current_locale()


class TestSeededBase:
    @pytest.fixture
    def _bases(self, seed):
        return BaseDataProvider(seed=seed), BaseDataProvider(seed=seed)

    def test_base_random(self, _bases):
        b1, b2 = _bases
        assert b1.random.randints() == b2.random.randints()
