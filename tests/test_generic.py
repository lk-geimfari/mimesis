# -*- coding: utf-8 -*-

from unittest import TestCase

from elizabeth import Generic
from tests.test_data import DummyCase

# A ll locale dependent cases

from .test_data.test_address import AddressTestCase
from .test_data.test_business import BusinessTestCase
from .test_data.test_datetime import DatetimeTestCase
from .test_data.test_food import FoodTestCase
from .test_data.test_personal import PersonalTestCase
from .test_data.test_sciense import ScienceTestCase
from .test_data.test_text import TextTestCase
from .test_data.test_code import CodeTestCase


class GenericTestCase(DummyCase):
    def setUp(self):
        self.generic = Generic(self.LANG)

    def test_base_personal(self):
        result = self.generic.personal.username()
        self.assertIsNotNone(result)

    def test_base_text(self):
        result = self.generic.text.words()
        self.assertIsNotNone(result)

    def test_base_address(self):
        result = self.generic.address.address()
        self.assertIsNotNone(result)

    def test_base_food(self):
        result = self.generic.food.fruit()
        self.assertIsNotNone(result)

    def test_base_science(self):
        result = self.generic.science.scientist()
        self.assertIsNotNone(result)

    def test_base_business(self):
        result = self.generic.business.copyright()
        self.assertIsNotNone(result)

    def test_base_code(self):
        result = self.generic.code.isbn()
        self.assertIsNotNone(result)


class LocaleBase(
    GenericTestCase, AddressTestCase, BusinessTestCase,
    DatetimeTestCase, FoodTestCase, PersonalTestCase,
    ScienceTestCase, TextTestCase, CodeTestCase):
    pass


class EnglishTestCase(LocaleBase, TestCase):
    LANG = 'en'


class GermanTestCase(LocaleBase, TestCase):
    LANG = 'de'


class RussianTestCase(LocaleBase, TestCase):
    LANG = 'ru'


class DanishTestCase(LocaleBase, TestCase):
    LANG = 'da'


class FrenchTestCase(LocaleBase, TestCase):
    LANG = 'fr'


class SpanishTestCase(LocaleBase, TestCase):
    LANG = 'es'


class ItalianTestCase(LocaleBase, TestCase):
    LANG = 'it'


class BrazilianPortugueseTestCase(LocaleBase, TestCase):
    LANG = 'pt-br'


class NorwegianTestCase(LocaleBase, TestCase):
    LANG = 'no'


class SwedishTestCase(LocaleBase, TestCase):
    LANG = 'sv'


class FinnishTestCase(LocaleBase, TestCase):
    LANG = 'fi'


class DutchTestCase(LocaleBase, TestCase):
    LANG = 'nl'


class IcelandicTestCase(LocaleBase, TestCase):
    LANG = 'is'


class PortugueseTestCase(LocaleBase, TestCase):
    LANG = 'pt'


class PolishTestCase(LocaleBase, TestCase):
    LANG = 'pl'


class FarsiTestCase(LocaleBase, TestCase):
    LANG = 'fa'
