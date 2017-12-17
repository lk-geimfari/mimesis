# -*- coding: utf-8 -*-
import re

import pytest

from mimesis.providers import Food

from ._patterns import STR_REGEX


@pytest.fixture
def _seeded_food():
    return Food(seed=42)


def test_str(food):
    assert re.match(STR_REGEX, str(food))


def test_vegetable(food):
    result = food.vegetable()
    assert result in food._data['vegetables']


def test_seeded_vegetable(_seeded_food):
    result = _seeded_food.vegetable()
    assert result == 'Celtuce'
    result = _seeded_food.vegetable()
    assert result == 'Beans'


def test_fruit(food):
    result = food.fruit()
    assert result in food._data['fruits']


def test_seeded_fruit(_seeded_food):
    result = _seeded_food.fruit()
    assert result == 'Blue tongue'
    result = _seeded_food.fruit()
    assert result == 'Banana'


def test_dish(food):
    result = food.dish()
    assert result in food._data['dishes']


def test_seeded_dish(_seeded_food):
    result = _seeded_food.dish()
    assert result == 'Sweet Potato Fries'
    result = _seeded_food.dish()
    assert result == 'Cheese fries'


def test_drink(food):
    result = food.drink()
    assert result in food._data['drinks']


def test_seeded_drink(_seeded_food):
    result = _seeded_food.drink()
    assert result == 'Caipirinha'
    result = _seeded_food.drink()
    assert result == 'Arrack'


def test_spices(food):
    result = food.spices()
    assert result in food._data['spices']


def test_seeded_spices(_seeded_food):
    result = _seeded_food.spices()
    assert result == 'Avocado leaf'
    result = _seeded_food.spices()
    assert result == 'Alkanet'
