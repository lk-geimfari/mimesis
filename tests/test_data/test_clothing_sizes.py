# -*- coding: utf-8 -*-
import pytest

from mimesis import ClothingSizes


@pytest.fixture
def sizes():
    return ClothingSizes()


def test_international_size(sizes):
    size_names = (
        'L', 'M', 'S',
        'XL', 'XS', 'XXL',
        'XXS', 'XXXL',
    )
    result = sizes.international_size()
    assert result in size_names


def test_european_size(sizes):
    result = sizes.european_size()
    assert result >= 38
    assert result <= 62


def test_custom_size(sizes):
    result = sizes.custom_size(minimum=10, maximum=16)
    assert result >= 10
    assert result <= 16
