# -*- coding: utf-8 -*-
import re

import pytest

from mimesis import Food

from . import patterns


class TestFood(object):

    def test_str(self, food):
        assert re.match(patterns.DATA_PROVIDER_STR_REGEX, str(food))

    def test_vegetable(self, food):
        result = food.vegetable()
        assert result in food._data['vegetables']

    def test_fruit(self, food):
        result = food.fruit()
        assert result in food._data['fruits']

    def test_dish(self, food):
        result = food.dish()
        assert result in food._data['dishes']

    def test_drink(self, food):
        result = food.drink()
        assert result in food._data['drinks']

    def test_spices(self, food):
        result = food.spices()
        assert result in food._data['spices']


class TestSeededFood(object):

    @pytest.fixture
    def fd1(self, seed):
        return Food(seed=seed)

    @pytest.fixture
    def fd2(self, seed):
        return Food(seed=seed)

    def test_vegetable(self, fd1, fd2):
        assert fd1.vegetable() == fd2.vegetable()

    def test_fruit(self, fd1, fd2):
        assert fd1.fruit() == fd2.fruit()

    def test_dish(self, fd1, fd2):
        assert fd1.dish() == fd2.dish()

    def test_drink(self, fd1, fd2):
        assert fd1.drink() == fd2.drink()

    def test_spices(self, fd1, fd2):
        assert fd1.spices() == fd2.spices()
