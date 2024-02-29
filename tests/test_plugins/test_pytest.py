import string

import pytest

from mimesis.locales import Locale


def test_locale(mimesis_locale, mimesis):
    assert mimesis_locale == Locale.DEFAULT
    assert mimesis._generic.locale == Locale.DEFAULT


@pytest.mark.parametrize("mimesis_locale", [Locale.DE])
def test_locale_override(mimesis_locale, mimesis):
    assert mimesis_locale == Locale.DE
    assert mimesis._generic.locale == Locale.DE


def test_mimesis_fixture(mimesis):
    assert mimesis("birthdate", min_year=2023, max_year=2023).year == 2023
    assert len(mimesis("full_name").split(" ")) > 1


@pytest.mark.parametrize("mimesis_locale", [Locale.RU])
def test_mimesis_fixture_with_overridden_locale(mimesis, mimesis_locale):
    assert mimesis._generic.locale == Locale.RU

    name = mimesis("full_name")
    for letter in name:  # russian letters are not in ASCII:
        assert letter not in string.ascii_letters
