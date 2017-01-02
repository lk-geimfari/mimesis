# -*- coding: utf-8 -*-

from elizabeth import Generic
from tests.test_data import DummyCase

from tests.test_data.test_address import AddressTestCase
from tests.test_data.test_business import BusinessTestCase
from tests.test_data.test_datetime import DatetimeTestCase
from tests.test_data.test_food import FoodTestCase
from tests.test_data.test_personal import PersonalTestCase
from tests.test_data.test_sciense import ScienceTestCase
from tests.test_data.test_text import TextTestCase
from tests.test_data.test_code import CodeIntTestCase


class GenericTest(DummyCase):
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

    def test_add_provider(self):
        class CustomProvider:
            class Meta:
                name = 'custom_provider'

            def say(self):
                return 'Custom'

            @staticmethod
            def number():
                return 1

        self.generic.add_provider(CustomProvider)
        self.assertIsNotNone(self.generic.custom_provider.say())
        self.assertEqual(self.generic.custom_provider.number(), 1)
        with self.assertRaises(TypeError):
            self.generic.add_provider(True)

        class UnnamedProvider():
            @staticmethod
            def nothing():
                return None

        self.generic.add_provider(UnnamedProvider)
        self.assertIs(self.generic.unnamedprovider.nothing(), None)

        self.assertTrue('unnamedprovider', UnnamedProvider.__name__.lower())


class LocaleBase(
    GenericTest, AddressTestCase, BusinessTestCase,
    DatetimeTestCase, FoodTestCase, PersonalTestCase,
    ScienceTestCase, TextTestCase, CodeIntTestCase):
    pass
