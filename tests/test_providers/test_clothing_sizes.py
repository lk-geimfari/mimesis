# -*- coding: utf-8 -*-
import pytest

from mimesis import ClothingSizes


class TestClothingSizes(object):

    @pytest.fixture
    def sizes(self):
        return ClothingSizes()

    def test_international_size(self, sizes):
        size_names = (
            'L', 'M', 'S',
            'XL', 'XS', 'XXL',
            'XXS', 'XXXL',
        )
        result = sizes.international_size()
        assert result in size_names

    def test_european_size(self, sizes):
        result = sizes.european_size()
        assert result >= 38
        assert result <= 62

    def test_custom_size(self, sizes):
        result = sizes.custom_size(minimum=10, maximum=16)
        assert result >= 10
        assert result <= 16


class TestSeededClothingSizes(object):

    @pytest.fixture
    def cs1(self, seed):
        return ClothingSizes(seed=seed)

    @pytest.fixture
    def cs2(self, seed):
        return ClothingSizes(seed=seed)

    def test_international_size(self, cs1, cs2):
        assert cs1.international_size() == cs2.international_size()

    def test_european_size(self, cs1, cs2):
        assert cs1.european_size() == cs2.european_size()

    def test_custom_size(self, cs1, cs2):
        assert cs1.custom_size() == cs2.custom_size()
        assert cs1.custom_size(11, 22) == cs2.custom_size(11, 22)
