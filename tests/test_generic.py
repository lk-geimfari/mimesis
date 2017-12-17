# -*- coding: utf-8 -*-

import re

import pytest

from mimesis.providers import Generic

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
    result = generic.unit_system.unit()
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


def test_seeded_generic():
    ceogen = Generic(seed=42)
    generators = [Generic(seed=42) for _ in range(42)]
    for _ in range(42):
        ceo_address = ceogen.address.address()
        ceo_business = ceogen.business.copyright()
        ceo_clothing = ceogen.clothing_sizes.custom_size()
        ceo_code = ceogen.code.isbn()
        ceo_crypto = ceogen.cryptographic.uuid()
        ceo_datetime = ceogen.datetime.week_date()
        ceo_dev = ceogen.development.version()
        ceo_file = ceogen.file.extension()
        ceo_food = ceogen.food.fruit()
        ceo_games = ceogen.games.gaming_platform()
        ceo_hrdw = ceogen.hardware.cpu()
        ceo_internet = ceogen.internet.mac_address()
        ceo_numbers = ceogen.numbers.rating()
        ceo_path = ceogen.path.user()
        ceo_payment = ceogen.payment.bitcoin_address()
        ceo_personal = ceogen.personal.username()
        ceo_science = ceogen.science.scientific_article()
        ceo_structured = ceogen.structured.html()
        ceo_text = ceogen.text.words()
        ceo_transport = ceogen.transport.car()
        ceo_unit = ceogen.unit_system.unit()

        for gen in generators:
            assert gen.address.address() == ceo_address
            assert gen.business.copyright() == ceo_business
            assert gen.clothing_sizes.custom_size() == ceo_clothing
            assert gen.code.isbn() == ceo_code
            assert gen.cryptographic.uuid() == ceo_crypto
            assert gen.datetime.week_date() == ceo_datetime
            assert gen.development.version() == ceo_dev
            assert gen.file.extension() == ceo_file
            assert gen.food.fruit() == ceo_food
            assert gen.games.gaming_platform() == ceo_games
            assert gen.hardware.cpu() == ceo_hrdw
            assert gen.internet.mac_address() == ceo_internet
            assert gen.numbers.rating() == ceo_numbers
            assert gen.path.user() == ceo_path
            assert gen.payment.bitcoin_address() == ceo_payment
            assert gen.personal.username() == ceo_personal
            assert gen.science.scientific_article() == ceo_science
            assert gen.structured.html() == ceo_structured
            assert gen.text.words() == ceo_text
            assert gen.transport.car() == ceo_transport
            assert gen.unit_system.unit() == ceo_unit
