import string

import factory
from pytest_factoryboy import register

from mimesis.locales import Locale
from mimesis.plugins.factory import MimesisField


class Person(object):
    def __init__(self, full_name_en: str, full_name_ru: str) -> None:
        self._full_name_en = full_name_en
        self._full_name_ru = full_name_ru

    @property
    def full_name_en(self) -> str:
        """Some names have special symbols in them."""
        return self._full_name_en.replace(" ", "").replace("'", "")

    @property
    def full_name_ru(self) -> str:
        """Some names have special symbols in them."""
        return self._full_name_ru.replace(" ", "").replace("'", "")


@register
class PersonFactory(factory.Factory):
    class Meta(object):
        model = Person

    full_name_en = MimesisField("full_name")
    full_name_ru = MimesisField("full_name", locale=Locale.RU)


def test_data_with_different_locales(person):
    for letter in person.full_name_en:
        assert letter in string.ascii_letters

    for russian_letter in person.full_name_ru:
        assert russian_letter not in string.ascii_letters


def test_data_with_override_locale(person_factory):
    with MimesisField.override_locale(Locale.RU):
        person = person_factory()

    for letter in person.full_name_en:
        # Default locale will be changed to overridden:
        assert letter not in string.ascii_letters

    for russian_letter in person.full_name_ru:
        assert russian_letter not in string.ascii_letters


def test_data_with_override_defined_locale(person_factory):
    with MimesisField.override_locale(Locale.EN):
        person = person_factory()

    for letter in person.full_name_en:
        assert letter in string.ascii_letters

    for russian_letter in person.full_name_ru:
        # Keyword locale has a priority over override:
        assert russian_letter not in string.ascii_letters
