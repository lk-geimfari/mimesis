# -*- coding: utf-8 -*-
import pytest

from mimesis import ClothingSizes

from ..conftest import seed


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
    TIMES = 5

    @pytest.fixture
    def _clothing_sizes(self):
        return ClothingSizes(seed=seed), ClothingSizes(seed=seed)

    def test_international_size(self, _clothing_sizes):
        cs1, cs2 = _clothing_sizes
        for _ in range(self.TIMES):
            assert cs1.international_size() == cs2.international_size()

    def test_european_size(self, _clothing_sizes):
        cs1, cs2 = _clothing_sizes
        for _ in range(self.TIMES):
            assert cs1.european_size() == cs2.european_size()

    def test_custom_size(self, _clothing_sizes):
        cs1, cs2 = _clothing_sizes
        for _ in range(self.TIMES):
            assert cs1.custom_size() == cs2.custom_size()
            assert cs1.custom_size(minimum=11, maximum=22) == \
                cs2.custom_size(minimum=11, maximum=22)
