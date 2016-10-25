# -*- coding: utf-8 -*-

from unittest import TestCase

from church.church import Food
from church.utils import pull

from tests import LANG


class FoodTestCase(TestCase):
    def setUp(self):
        self.food = Food(LANG)
        self.db = self.food._data

    def tearDown(self):
        del self.food

    def test_vegetable(self):
        result = self.food.vegetable()
        self.assertIn(result, self.db['vegetables'])

    def test_fruit(self):
        result = self.food.fruit_or_berry()
        self.assertIn(result, self.db['fruits'])

    def test_dish(self):
        result = self.food.dish()
        self.assertIn(result, self.db['dishes'])

    def test_drink(self):
        result = self.food.drink()
        self.assertIn(result, self.db['drinks'])

    def test_spices(self):
        result = self.food.spices()
        self.assertIn(result, self.db['spices'])
