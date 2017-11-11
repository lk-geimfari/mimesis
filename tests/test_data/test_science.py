# -*- coding: utf-8 -*-

import re

import pytest

import mimesis
from mimesis.data import MATH_FORMULAS

from ._patterns import STR_REGEX


@pytest.fixture
def default_science():
    return mimesis.Science()


def test_str(science):
    assert re.match(STR_REGEX, str(science))


def test_math_formula(default_science):
    result = default_science.math_formula()
    assert result in MATH_FORMULAS


def test_scientific_article(science):
    result = science.scientific_article()
    assert result in science._data['article']


def test_chemical_element(science):
    # Some issues with Farsi
    if science.locale != 'fa':
        result = science.chemical_element(name_only=True)
        assert len(result) >= 1

        result = science.chemical_element(name_only=False)
        assert isinstance(result, dict)
