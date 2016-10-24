# -*- coding: utf-8 -*-

from unittest import TestCase

from church.church import Food
from church.utils import pull

from tests import LANG


class FoodTestCase(TestCase):
    def setUp(self):
        self.food = Food(LANG)

    def tearDown(self):
        del self.food

    def test_vegetable(self):
        result = self.food.vegetable()
        parent_file = pull('vegetables', self.food.lang)
        self.assertIn(result + '\n', parent_file)

    def test_fruit(self):
        result = self.food.fruit_or_berry()
        parent_file = pull('fruits_berries', self.food.lang)
        self.assertIn(result + '\n', parent_file)

    def test_dish(self):
        result = self.food.dish()
        parent_file = pull('dishes', self.food.lang)
        self.assertIn(result + '\n', parent_file)

    def test_drink(self):
        result = self.food.drink()
        parent_file = pull('drinks', self.food.lang)
        self.assertIn(result + '\n', parent_file)

    def test_spices(self):
        result = self.food.spices()
        parent_file = pull('spices', self.food.lang)
        self.assertIn(result + '\n', parent_file)
