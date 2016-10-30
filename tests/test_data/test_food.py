# -*- coding: utf-8 -*-

from tests.test_data import DummyCase


class FoodTestCase(DummyCase):
    def test_vegetable(self):
        result = self.church.food.vegetable()
        self.assertIn(result, self.church.food._data['vegetables'])

    def test_fruit(self):
        result = self.church.food.fruit_or_berry()
        self.assertIn(result, self.church.food._data['fruits'])

    def test_dish(self):
        result = self.church.food.dish()
        self.assertIn(result, self.church.food._data['dishes'])

    def test_drink(self):
        result = self.church.food.drink()
        self.assertIn(result, self.church.food._data['drinks'])

    def test_spices(self):
        result = self.church.food.spices()
        self.assertIn(result, self.church.food._data['spices'])

    def test_measurement(self):
        result = self.church.food.measurement()
        quantity, measure = result.split()
        self.assertIsNotNone(quantity)
        self.assertIn(measure, self.church.food._data['measurement'])
