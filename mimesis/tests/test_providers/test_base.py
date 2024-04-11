import json
import re
import tempfile
from pathlib import Path

import pytest

from mimesis import random
from mimesis.enums import Gender
from mimesis.exceptions import LocaleError, NonEnumerableError
from mimesis.locales import Locale
from mimesis.providers import Code, Cryptographic, Internet, Person
from mimesis.providers.base import BaseDataProvider, BaseProvider
from mimesis.types import MissingSeed

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
            assert "Жен." in provider._dataset["gender"]
            assert Locale(provider.locale) == new_locale

        assert Locale(provider.locale) == locale
        assert "Жен." not in provider._dataset["gender"]

        del provider.locale
        with pytest.raises(ValueError):
            with provider.override_locale(new_locale):
                pass

    @pytest.mark.parametrize(
        "data, keys_count, values_count",
        [
            (
                {"test": "test"},
                1,
                1,
            ),
            (
                {"test": "test", "test2": ["a", "b", "c"]},
                2,
                2,
            ),
        ],
    )
    def test_update_dataset(self, base_data_provider, data, keys_count, values_count):
        base_data_provider.update_dataset(data=data)
        assert len(base_data_provider._dataset.keys()) == keys_count
        assert len(base_data_provider._dataset.values()) == values_count

        base_data_provider.update_dataset(data={"test3": "test3"})
        assert len(base_data_provider._dataset.keys()) == keys_count + 1
        assert len(base_data_provider._dataset.keys()) == values_count + 1

    @pytest.mark.parametrize("data", [set(), [], "", tuple()])
    def test_update_dataset_raises_error(self, base_data_provider, data):
        with pytest.raises(TypeError):
            base_data_provider.update_dataset(data=data)

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
    def test_load_datafile(self, locale, city):
        class MyProvider(BaseDataProvider):
            class Meta:
                name = "my_provider"
                datafile = "address.json"

        data_provider = MyProvider(locale)
        assert city in data_provider._dataset["city"]

    @pytest.mark.parametrize("locale", list(Locale))
    def test_load_datafile_raises(self, locale):
        class BadProvider(BaseDataProvider):
            class Meta:
                name = "bad"
                datafile = "bad.json"

        with pytest.raises(FileNotFoundError):
            BadProvider(locale=locale)

    def test_extract(self, base_data_provider):
        dictionary = {"names": {"female": "Ariel", "male": "John"}}

        base_data_provider._dataset = dictionary

        a = list(sorted(dictionary["names"].keys()))
        b = list(sorted(base_data_provider._extract(["names"]).keys()))

        assert base_data_provider._extract(["names", "male"]) == "John"
        assert base_data_provider._extract(["names", "female"]) == "Ariel"
        assert base_data_provider._extract(["names", "other"], default="Sam") == "Sam"
        assert a == b

        with pytest.raises(ValueError):
            assert base_data_provider._extract([])

    def test_extract_missing_positional_arguments(self, base_data_provider):
        with pytest.raises(TypeError):
            assert base_data_provider._extract(default=None)

        with pytest.raises(TypeError):
            assert base_data_provider._extract()

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

    def test_base_wrong_random_type(self):
        with pytest.raises(TypeError):
            BaseProvider(random="")

    def test_read_global_file(self, base_data_provider):
        result = base_data_provider._read_global_file("emojis.json")
        assert isinstance(result, dict)
        assert len(result.keys()) > 0

        with pytest.raises(FileNotFoundError):
            base_data_provider._read_global_file("nil.json")

    @pytest.mark.repeat(5)
    def test_custom_data_provider(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            datadir = Path(tmpdir).joinpath("en")
            datadir.mkdir(parents=True, exist_ok=True)
            file_data = {"key": ["value", "value2", "value3"]}

            with open(datadir / "data.json", "w") as f:
                json.dump(file_data, f)

            class CustomDataProvider(BaseDataProvider):
                class Meta:
                    name = "cdp"
                    datafile = "data.json"
                    datadir = Path(tmpdir)

                def val(self):
                    return self.random.choice(self._extract(["key"]))

            cdp = CustomDataProvider(Locale.EN)
            assert cdp.val() in file_data["key"]

            class CustomDataProvider(BaseDataProvider):
                class Meta:
                    name = "cdp"
                    datafile = "data.json"

            # Datadir is not set, so this should
            # raise an error
            with pytest.raises(FileNotFoundError):
                CustomDataProvider(Locale.EN)

            # We didn't create a ru folder,
            # so this should raise an error
            with pytest.raises(FileNotFoundError):
                CustomDataProvider(Locale.RU)


class TestSeededBase:
    @pytest.fixture
    def _bases(self, seed):
        return BaseDataProvider(seed=seed), BaseDataProvider(seed=seed)

    def test_base_random(self, _bases):
        b1, b2 = _bases
        assert b1.random.randints() == b2.random.randints()

    @pytest.mark.parametrize("seed", [None, 123, 0.5, "string", b"bytes", bytearray(1)])
    def test_per_instance_random(self, seed):
        b1 = BaseProvider(seed=seed)
        b2 = BaseProvider(seed=seed)

        assert b1.seed == b2.seed
        assert b1.random is not b2.random

    @pytest.mark.parametrize("seed", [123, 0.5, "string", b"bytes", bytearray(1)])
    @pytest.mark.parametrize("global_seed", [None, MissingSeed])
    def test_has_seed_no_global(self, monkeypatch, seed, global_seed):
        # We run this test with `pytest-randomly` enabled,
        # so we clean things up first.
        monkeypatch.setattr(random, "global_seed", global_seed)

        b1 = BaseProvider()
        assert b1._has_seed() is False

        b2 = BaseProvider(seed=None)
        assert b2._has_seed() is False

        b3 = BaseProvider(seed=seed)
        assert b3._has_seed() is True

    @pytest.mark.parametrize("seed", [123, 0.5, "string", b"bytes", bytearray(1)])
    def test_has_seed_global(self, monkeypatch, seed):
        monkeypatch.setattr(random, "global_seed", seed)

        b1 = BaseProvider()
        assert b1._has_seed() is True

        b2 = BaseProvider(seed=None)
        assert b2._has_seed() is True

        b3 = BaseProvider(seed=seed)
        assert b3._has_seed() is True
