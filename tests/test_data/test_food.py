# -*- coding: utf-8 -*-

from tests.test_data import DummyCase


class FoodTestCase(DummyCase):
    def test_vegetable(self):
        result = self.generic.food.vegetable()
        self.assertIn(result, self.generic.food._data['vegetables'])

    def test_fruit(self):
        result = self.generic.food.fruit_or_berry()
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

    def test_measurement(self):
        result = self.generic.food.measurement()
        quantity, measure = result.split()
        self.assertIsNotNone(quantity)
        self.assertIn(measure, self.generic.food._data['measurement'])
