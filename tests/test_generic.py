# -*- coding: utf-8 -*-

import re

import pytest

from .test_data import _patterns as p


def test_str(generic):
    assert re.match(p.STR_REGEX, str(generic))


def test_base_personal(generic):
    result = generic.personal.username()
    assert result is not None


def test_base_text(generic):
    result = generic.text.words()
    assert result is not None


def test_base_payment(generic):
    result = generic.payment.bitcoin_address()
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


def test_base_unit_system(generic):
    result = generic.unit_system.mass()
    assert result is not None


def test_base_code(generic):
    result = generic.code.isbn()
    assert result is not None


def test_bad_argument(generic):
    with pytest.raises(AttributeError):
        _ = generic.bad_argument  # noqa


def test_add_providers(generic):
    class Provider1(object):
        @staticmethod
        def one():
            return 1

    class Provider2(object):
        class Meta:
            name = 'custom_provider'

        @staticmethod
        def two():
            return 2

    class Provider3(object):
        @staticmethod
        def three():
            return 3

    generic.add_providers(Provider1, Provider2, Provider3)
    assert generic.provider1.one() == 1
    assert generic.custom_provider.two() == 2
    assert generic.provider3.three() == 3

    with pytest.raises(TypeError):
        generic.add_providers(True)

    class UnnamedProvider(object):
        @staticmethod
        def nothing():
            return None

    generic.add_provider(UnnamedProvider)
    assert generic.unnamedprovider.nothing() is None
