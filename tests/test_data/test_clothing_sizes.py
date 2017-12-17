# -*- coding: utf-8 -*-
import pytest

from mimesis import ClothingSizes


@pytest.fixture
def _sizes():
    return ClothingSizes()


@pytest.fixture
def _seeded_sizes():
    return ClothingSizes(seed=42)


def test_international_size(_sizes):
    size_names = (
        'L', 'M', 'S',
        'XL', 'XS', 'XXL',
        'XXS', 'XXXL',
    )
    result = _sizes.international_size()
    assert result in size_names


def test_seeded_international_size(_seeded_sizes):
    result = _seeded_sizes.international_size()
    assert result == 'M'
    result = _seeded_sizes.international_size()
    assert result == 'L'


def test_european_size(_sizes):
    result = _sizes.european_size()
    assert result >= 40
    assert result <= 62


def test_seeded_european_size(_seeded_sizes):
    result = _seeded_sizes.european_size()
    assert result == 60
    result = _seeded_sizes.european_size()
    assert result == 42


def test_custom_size(_sizes):
    result = _sizes.custom_size(minimum=40, maximum=62)
    assert result >= 40
    assert result <= 62


def test_seeded_custom_size(_seeded_sizes):
    result = _seeded_sizes.custom_size(minimum=42, maximum=142)
    assert result == 123
    result = _seeded_sizes.custom_size()
    assert result == 43
    result = _seeded_sizes.custom_size()
    assert result == 40
