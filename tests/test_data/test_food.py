# -*- coding: utf-8 -*-
import re

from ._patterns import STR_REGEX


def test_str(food):
    assert re.match(STR_REGEX, str(food))


def test_vegetable(food):
    result = food.vegetable()
    assert result in food._data['vegetables']


def test_fruit(food):
    result = food.fruit()
    assert result in food._data['fruits']


def test_dish(food):
    result = food.dish()
    assert result in food._data['dishes']


def test_drink(food):
    result = food.drink()
    assert result in food._data['drinks']


def test_spices(food):
    result = food.spices()
    assert result in food._data['spices']
