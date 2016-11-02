# -*- coding: utf-8 -*-

from unittest import TestCase

from church import Church
from tests.test_data import DummyCase

# all locale dependent cases
from tests.test_data.test_address import AddressTestCase
from tests.test_data.test_business import BusinessTestCase
from tests.test_data.test_datetime import DatetimeTestCase
from tests.test_data.test_food import FoodTestCase
from tests.test_data.test_personal import PersonalTestCase
from tests.test_data.test_sciense import ScienceTestCase
from tests.test_data.test_text import TextTestCase


class ChurchBase(DummyCase):
    def setUp(self):
        self.church = Church(self.LANG)

    def test_base_personal(self):
        result = self.church.personal.username()
        self.assertIsNotNone(result)

    def test_base_text(self):
        result = self.church.text.words()
        self.assertIsNotNone(result)

    def test_base_address(self):
        result = self.church.address.address()
        self.assertIsNotNone(result)

    def test_base_food(self):
        result = self.church.food.fruit_or_berry()
        self.assertIsNotNone(result)

    def test_base_science(self):
        result = self.church.science.scientist()
        self.assertIsNotNone(result)

    def test_base_business(self):
        result = self.church.business.copyright()
        self.assertIsNotNone(result)


class ChurchLocaleBase(ChurchBase, AddressTestCase, BusinessTestCase,
                       DatetimeTestCase, FoodTestCase, PersonalTestCase,
                       ScienceTestCase, TextTestCase):
    pass


class ChurchEnglishTestCase(ChurchLocaleBase, TestCase):
    LANG = 'en'


class ChurchGermanTestCase(ChurchLocaleBase, TestCase):
    LANG = 'de'


class ChurchRussianTestCase(ChurchLocaleBase, TestCase):
    LANG = 'ru'


class ChurchDanishTestCase(ChurchLocaleBase, TestCase):
    LANG = 'da'


class ChurchFrenchTestCase(ChurchLocaleBase, TestCase):
    LANG = 'fr'


class ChurchSpanishTestCase(ChurchLocaleBase, TestCase):
    LANG = 'es'


class ChurchItalianTestCase(ChurchLocaleBase, TestCase):
    LANG = 'it'


class ChurchPortugueseTestCase(ChurchLocaleBase, TestCase):
    LANG = 'pt-br'


class ChurchNorwegianTestCase(ChurchLocaleBase, TestCase):
    LANG = 'no'


class ChurchSwedishTestCase(ChurchLocaleBase, TestCase):
    LANG = 'sv'


class ChurchFinnishTestCase(ChurchLocaleBase, TestCase):
    LANG = 'fi'


class ChurchDutchTestCase(ChurchLocaleBase, TestCase):
    LANG = 'nl'


class ChurchIcelandicTestCase(ChurchLocaleBase, TestCase):
    LANG = 'is'
