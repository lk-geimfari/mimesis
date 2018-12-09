# -*- coding: utf-8 -*-
import re

import pytest

from mimesis import Clothing

from . import patterns


class TestClothing(object):

    @pytest.fixture
    def clothing(self):
        return Clothing()

    def test_str(self, clothing):
        assert re.match(patterns.PROVIDER_STR_REGEX, str(clothing))

    def test_international_size(self, clothing):
        size_names = (
            'L', 'M', 'S',
            'XL', 'XS', 'XXL',
            'XXS', 'XXXL',
        )
        result = clothing.international_size()
        assert result in size_names

    def test_european_size(self, clothing):
        result = clothing.european_size()
        assert result >= 38
        assert result <= 62

    def test_custom_size(self, clothing):
        result = clothing.custom_size(minimum=10, maximum=16)
        assert result >= 10
        assert result <= 16


class TestSeededClothing(object):

    @pytest.fixture
    def cs1(self, seed):
        return Clothing(seed=seed)

    @pytest.fixture
    def cs2(self, seed):
        return Clothing(seed=seed)

    def test_international_size(self, cs1, cs2):
        assert cs1.international_size() == cs2.international_size()

    def test_european_size(self, cs1, cs2):
        assert cs1.european_size() == cs2.european_size()

    def test_custom_size(self, cs1, cs2):
        assert cs1.custom_size() == cs2.custom_size()
        assert cs1.custom_size(11, 22) == cs2.custom_size(11, 22)
