# -*- coding: utf-8 -*-

import pytest
import re

from .test_data._patterns import STR_REGEX


def test_str(generic):
    assert re.match(STR_REGEX, str(generic))


def test_base_personal(generic):
    result = generic.personal.username()
    assert result is not None


def test_base_text(generic):
    result = generic.text.words()
    assert result is not None


def test_base_address(generic):
    result = generic.address.address()
    assert result is not None


def test_base_food(generic):
    result = generic.food.fruit()
    assert result is not None


def test_base_science(generic):
    result = generic.science.scientific_article()
    assert result is not None


def test_base_business(generic):
    result = generic.business.copyright()
    assert result is not None


def test_base_code(generic):
    result = generic.code.isbn()
    assert result is not None


def test_add_provider(generic):
    class CustomProvider:
        class Meta:
            name = 'custom_provider'

        @staticmethod
        def say():
            return 'Custom'

        @staticmethod
        def number():
            return 1

    generic.add_provider(CustomProvider)
    assert generic.custom_provider.say() is not None
    assert generic.custom_provider.number() == 1
    with pytest.raises(TypeError):
        generic.add_provider(True)

    class UnnamedProvider():
        @staticmethod
        def nothing():
            return None

    generic.add_provider(UnnamedProvider)
    assert generic.unnamedprovider.nothing() is None

    assert 'unnamedprovider' == UnnamedProvider.__name__.lower()
