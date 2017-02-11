# -*- coding: utf-8 -*-
import re

from tests.test_data import DummyCase
from ._patterns import STR_REGEX


class FoodTestCase(DummyCase):

    def test_str(self):
        self.assertTrue(re.match(STR_REGEX, self.generic.__str__()))

    def test_vegetable(self):
        result = self.generic.food.vegetable()
        self.assertIn(result, self.generic.food._data['vegetables'])

    def test_fruit(self):
        result = self.generic.food.fruit()
        self.assertIn(result, self.generic.food._data['fruits'])

    def test_dish(self):
        result = self.generic.food.dish()
        self.assertIn(result, self.generic.food._data['dishes'])

    def test_drink(self):
        result = self.generic.food.drink()
        self.assertIn(result, self.generic.food._data['drinks'])

    def test_spices(self):
        result = self.generic.food.spices()
        self.assertIn(result, self.generic.food._data['spices'])
