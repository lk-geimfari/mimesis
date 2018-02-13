# -*- coding: utf-8 -*-
import re

import pytest

from mimesis import ClothingSize

from . import patterns


class TestClothingSize(object):

    @pytest.fixture
    def clothing_size(self):
        return ClothingSize()

    def test_str(self, clothing_size):
        assert re.match(patterns.STR_REGEX, str(clothing_size))

    def test_international_size(self, clothing_size):
        size_names = (
            'L', 'M', 'S',
            'XL', 'XS', 'XXL',
            'XXS', 'XXXL',
        )
        result = clothing_size.international_size()
        assert result in size_names

    def test_european_size(self, clothing_size):
        result = clothing_size.european_size()
        assert result >= 38
        assert result <= 62

    def test_custom_size(self, clothing_size):
        result = clothing_size.custom_size(minimum=10, maximum=16)
        assert result >= 10
        assert result <= 16


class TestSeededClothingSize(object):

    @pytest.fixture
    def cs1(self, seed):
        return ClothingSize(seed=seed)

    @pytest.fixture
    def cs2(self, seed):
        return ClothingSize(seed=seed)

    def test_international_size(self, cs1, cs2):
        assert cs1.international_size() == cs2.international_size()

    def test_european_size(self, cs1, cs2):
        assert cs1.european_size() == cs2.european_size()

    def test_custom_size(self, cs1, cs2):
        assert cs1.custom_size() == cs2.custom_size()
        assert cs1.custom_size(11, 22) == cs2.custom_size(11, 22)
