# -*- coding: utf-8 -*-

import re

import pytest

from mimesis import Science
from mimesis.data import MATH_FORMULAS

from . import patterns


class TestScience(object):

    @pytest.fixture
    def default_science(self):
        return Science()

    def test_str(self, science):
        assert re.match(patterns.DATA_PROVIDER_STR_REGEX, str(science))

    def test_math_formula(self, default_science):
        result = default_science.math_formula()
        assert result in MATH_FORMULAS

    def test_chemical_element(self, science):
        # Some issues with Farsi
        if science.get_current_locale() != 'fa':
            result = science.chemical_element(name_only=True)
            assert len(result) >= 1

            result = science.chemical_element(name_only=False)
            assert isinstance(result, dict)

    def test_atomic_number(self, default_science):
        result = default_science.atomic_number()
        assert isinstance(result, int)
        assert result <= 119

    def test_rna_sequence(self, default_science):
        result = default_science.rna_sequence(length=10)
        assert isinstance(result, str)
        assert len(result) == 10

    def test_dna_sequence(self, default_science):
        result = default_science.dna_sequence(length=10)
        assert isinstance(result, str)
        assert len(result) == 10


class TestSeededScience(object):

    @pytest.fixture
    def s1(self, seed):
        return Science(seed=seed)

    @pytest.fixture
    def s2(self, seed):
        return Science(seed=seed)

    def test_math_formula(self, s1, s2):
        assert s1.math_formula() == s2.math_formula()

    def test_chemical_element(self, s1, s2):
        assert s1.chemical_element() == s2.chemical_element()
        assert s1.chemical_element(name_only=True) == \
               s2.chemical_element(name_only=True)

    def test_atomic_number(self, s1, s2):
        assert s1.atomic_number() == s2.atomic_number()

    def test_rna_sequence(self, s1, s2):
        assert s1.rna_sequence() == s2.rna_sequence()
        assert s1.rna_sequence(length=22) == s2.rna_sequence(length=22)

    def test_dna_sequence(self, s1, s2):
        assert s1.dna_sequence() == s2.dna_sequence()
        assert s1.dna_sequence(length=10) == s2.dna_sequence(length=10)
