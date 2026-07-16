import re

import pytest

from mimesis import Science

from .. import patterns


class TestScience:
    @pytest.fixture
    def science(self):
        return Science()

    def test_str(self, science):
        assert re.match(patterns.PROVIDER_STR_REGEX, str(science))

    def test_rna_sequence(self, science):
        result = science.rna_sequence(length=10)
        assert isinstance(result, str)
        assert len(result) == 10

    def test_dna_sequence(self, science):
        result = science.dna_sequence(length=10)
        assert isinstance(result, str)
        assert len(result) == 10


class TestSeededScience:
    @pytest.fixture
    def s1(self, seed):
        return Science(seed=seed)

    @pytest.fixture
    def s2(self, seed):
        return Science(seed=seed)

    def test_rna_sequence(self, s1, s2):
        assert s1.rna_sequence() == s2.rna_sequence()
        assert s1.rna_sequence(length=22) == s2.rna_sequence(length=22)

    def test_dna_sequence(self, s1, s2):
        assert s1.dna_sequence() == s2.dna_sequence()
        assert s1.dna_sequence(length=10) == s2.dna_sequence(length=10)
