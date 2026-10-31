import json
from enum import Enum

import pytest

from mimesis.constants import DATADIR
from mimesis.exceptions import LocaleError
from mimesis.locales import Locale, validate_locale


SUPPORTED_LOCALES_COUNT = 48


def test_locale_enum():
    assert len(list(Locale)) == SUPPORTED_LOCALES_COUNT
    assert issubclass(Locale, Enum)


def test_validate_locale_missing_locale():
    with pytest.raises(TypeError):
        validate_locale()


def test_validate_locale_invalid_locale():
    with pytest.raises(LocaleError):
        validate_locale(locale=None)

    with pytest.raises(LocaleError):
        validate_locale(locale="nil")


def test_validate_locale():
    validated_locale = validate_locale("en")

    assert validated_locale == Locale.EN
    assert issubclass(validated_locale.__class__, Enum)
    assert isinstance(validate_locale(Locale.EN), Locale)


def _iter_strings(data):
    if isinstance(data, dict):
        for value in data.values():
            yield from _iter_strings(value)
    elif isinstance(data, list):
        for value in data:
            yield from _iter_strings(value)
    elif isinstance(data, str):
        yield data


@pytest.mark.parametrize(
    "dataset",
    sorted(DATADIR.glob("*/*.json")),
    ids=lambda path: f"{path.parent.name}/{path.name}",
)
def test_dataset_values_have_no_surrounding_whitespace(dataset):
    data = json.loads(dataset.read_text(encoding="utf-8"))
    bad = [value for value in _iter_strings(data) if value != value.strip()]
    assert not bad
