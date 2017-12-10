# -*- coding: utf-8 -*-
import pytest

from mimesis import ClothingSizes


@pytest.fixture
def _sizes():
    return ClothingSizes()


@pytest.fixture
def _seeded_sizes():
    return ClothingSizes(seed=42)


def test_international(_sizes):
    size_names = (
        'L', 'M', 'S',
        'XL', 'XS', 'XXL',
        'XXS', 'XXXL',
    )
    result = _sizes.international()
    assert result in size_names


def test_seeded_international(_seeded_sizes):
    result = _seeded_sizes.international()
    assert result == 'M'
    result = _seeded_sizes.international()
    assert result == 'L'


def test_eur(_sizes):
    result = _sizes.european()
    assert result >= 40
    assert result <= 62


def test_seeded_eur(_seeded_sizes):
    result = _seeded_sizes.european()
    assert result == 60
    result = _seeded_sizes.european()
    assert result == 42


def test_custom(_sizes):
    result = _sizes.custom(minimum=40, maximum=62)
    assert result >= 40
    assert result <= 62


def test_seeded_custom(_seeded_sizes):
    result = _seeded_sizes.custom(minimum=42, maximum=142)
    assert result == 123
    result = _seeded_sizes.custom()
    assert result == 43
    result = _seeded_sizes.custom()
    assert result == 40
