# -*- coding: utf-8 -*-

from unittest import TestCase

from elizabeth import Generic
from tests.test_data import DummyCase

# all locale dependent cases
from tests.test_data.test_address import AddressTestCase
from tests.test_data.test_business import BusinessTestCase
from tests.test_data.test_datetime import DatetimeTestCase
from tests.test_data.test_food import FoodTestCase
from tests.test_data.test_personal import PersonalTestCase
from tests.test_data.test_sciense import ScienceTestCase
from tests.test_data.test_text import TextTestCase


class ElizabethBase(DummyCase):
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
        result = self.generic.food.fruit_or_berry()
        self.assertIsNotNone(result)

    def test_base_science(self):
        result = self.generic.science.scientist()
        self.assertIsNotNone(result)

    def test_base_business(self):
        result = self.generic.business.copyright()
        self.assertIsNotNone(result)


class ElizabethLocaleBase(ElizabethBase, AddressTestCase, BusinessTestCase,
                          DatetimeTestCase, FoodTestCase, PersonalTestCase,
                          ScienceTestCase, TextTestCase):
    pass


class EnglishTestCase(ElizabethLocaleBase, TestCase):
    LANG = 'en'


class GermanTestCase(ElizabethLocaleBase, TestCase):
    LANG = 'de'


class RussianTestCase(ElizabethLocaleBase, TestCase):
    LANG = 'ru'


class DanishTestCase(ElizabethLocaleBase, TestCase):
    LANG = 'da'


class FrenchTestCase(ElizabethLocaleBase, TestCase):
    LANG = 'fr'


class SpanishTestCase(ElizabethLocaleBase, TestCase):
    LANG = 'es'


class ItalianTestCase(ElizabethLocaleBase, TestCase):
    LANG = 'it'


class BrazilianPortugueseTestCase(ElizabethLocaleBase, TestCase):
    LANG = 'pt-br'


class NorwegianTestCase(ElizabethLocaleBase, TestCase):
    LANG = 'no'


class SwedishTestCase(ElizabethLocaleBase, TestCase):
    LANG = 'sv'


class FinnishTestCase(ElizabethLocaleBase, TestCase):
    LANG = 'fi'


class DutchTestCase(ElizabethLocaleBase, TestCase):
    LANG = 'nl'


class IcelandicTestCase(ElizabethLocaleBase, TestCase):
    LANG = 'is'


class PortugueseTestCase(ElizabethLocaleBase, TestCase):
    LANG = 'pt'
