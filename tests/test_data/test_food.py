# -*- coding: utf-8 -*-
import pytest
import re

from tests.test_data import generic
from ._patterns import STR_REGEX


def test_str(generic):
    assert re.match(STR_REGEX, str(generic))


def test_vegetable(generic):
    result = generic.food.vegetable()
    assert result in generic.food._data['vegetables']


def test_fruit(generic):
    result = generic.food.fruit()
    assert result in generic.food._data['fruits']


def test_dish(generic):
    result = generic.food.dish()
    assert result in generic.food._data['dishes']


def test_drink(generic):
    result = generic.food.drink()
    assert result in generic.food._data['drinks']


def test_spices(generic):
    result = generic.food.spices()
    assert result in generic.food._data['spices']
