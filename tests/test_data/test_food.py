# -*- coding: utf-8 -*-
import re

import pytest

from mimesis import Food

from ..conftest import seed
from ._patterns import STR_REGEX


class TestFood(object):
    def test_str(self, food):
        assert re.match(STR_REGEX, str(food))

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
    TIMES = 5

    @pytest.fixture
    def _foods(self):
        return Food(seed=seed), Food(seed=seed)

    def test_vegetable(self, _foods):
        f1, f2 = _foods
        for _ in range(self.TIMES):
            assert f1.vegetable() == f2.vegetable()

    def test_fruit(self, _foods):
        f1, f2 = _foods
        for _ in range(self.TIMES):
            assert f1.fruit() == f2.fruit()

    def test_dish(self, _foods):
        f1, f2 = _foods
        for _ in range(self.TIMES):
            assert f1.dish() == f2.dish()

    def test_drink(self, _foods):
        f1, f2 = _foods
        for _ in range(self.TIMES):
            assert f1.drink() == f2.drink()

    def test_spices(self, _foods):
        f1, f2 = _foods
        for _ in range(self.TIMES):
            assert f1.spices() == f2.spices()
