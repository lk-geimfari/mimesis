# -*- coding: utf-8 -*-

import pytest

from elizabeth.providers.clothing import ClothingSizes


@pytest.fixture
def sizes():
    return ClothingSizes()


def test_international(sizes):
    size_names = (
        "L", "M", "S",
        "XL", "XS", "XXL",
        "XXS", "XXXL"
    )
    result = sizes.international()
    assert result in size_names


def test_eur(sizes):
    result = sizes.european()
    assert result >= 40
    assert result <= 62


def test_custom(sizes):
    result = sizes.custom(minimum=40, maximum=62)
    assert result >= 40
    assert result <= 62
