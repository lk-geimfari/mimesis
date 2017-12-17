# -*- coding: utf-8 -*-

import re

import pytest

from mimesis import Science
from mimesis.data import MATH_FORMULAS

from ._patterns import STR_REGEX


@pytest.fixture
def default_science():
    return Science()


@pytest.fixture
def _seeded_science():
    return Science(seed=42)


def test_str(science):
    assert re.match(STR_REGEX, str(science))


def test_math_formula(default_science):
    result = default_science.math_formula()
    assert result in MATH_FORMULAS


def test_seeded_math_formula(_seeded_science):
    result = _seeded_science.math_formula()
    assert result == 'A = (h(a + b))/2'
    result = _seeded_science.math_formula()
    assert result == 'A = (ab)/2'


def test_scientific_article(science):
    result = science.scientific_article()
    assert result in science._data['article']


def test_seeded_scientific_article(_seeded_science):
    result = _seeded_science.scientific_article()
    assert result == 'https://en.wikipedia.org/wiki/Supernova'
    result = _seeded_science.scientific_article()
    assert result == 'https://en.wikipedia.org/wiki/Hypersurface'


def test_chemical_element(science):
    # Some issues with Farsi
    if science.get_current_locale() != 'fa':
        result = science.chemical_element(name_only=True)
        assert len(result) >= 1

        result = science.chemical_element(name_only=False)
        assert isinstance(result, dict)


def test_seeded_chemical_element(_seeded_science):
    result = _seeded_science.chemical_element(name_only=True)
    assert result == 'Roentgenium'
    result = _seeded_science.chemical_element()
    assert result == 'Cadmium'
    result = _seeded_science.chemical_element()
    assert result == 'Antimony'


def test_atomic_number(default_science):
    result = default_science.atomic_number()
    assert isinstance(result, int)
    assert result <= 119


def test_seeded_atomic_number(_seeded_science):
    result = _seeded_science.atomic_number()
    assert result == 82
    result = _seeded_science.atomic_number()
    assert result == 15


def test_rna(default_science):
    result = default_science.rna(length=10)
    assert isinstance(result, str)
    assert len(result) == 10


def test_seeded_rna(_seeded_science):
    result = _seeded_science.rna(length=5)
    assert result == 'UUGCC'
    result = _seeded_science.rna()
    assert result == 'CUUAUUUCCU'
    result = _seeded_science.rna()
    assert result == 'CACAGUCAGG'


def test_dna(default_science):
    result = default_science.dna(length=10)
    assert isinstance(result, str)
    assert len(result) == 10


def test_seeded_dna(_seeded_science):
    result = _seeded_science.dna(length=5)
    assert result == 'TTGCC'
    result = _seeded_science.dna()
    assert result == 'CTTATTTCCT'
    result = _seeded_science.dna()
    assert result == 'CACAGTCAGG'
