# -*- coding: utf-8 -*-
import re

import pytest

from mimesis import Transport
from mimesis.data import (
    AIRPLANES,
    CARS,
    MANUFACTURERS,
    TRUCKS,
    VR_CODES,
    VRC_BY_LOCALES,
)
from mimesis.locales import LIST_OF_LOCALES

from . import patterns


class TestTransport(object):

    @pytest.fixture
    def transport(self):
        return Transport()

    def test_str(self, transport):
        assert re.match(patterns.PROVIDER_STR_REGEX, str(transport))

    def test_truck(self, transport):
        result = transport.truck().split('-')
        manufacturer, model = result[0], result[1]
        assert manufacturer in TRUCKS
        assert len(model) == 7

        result = transport.truck(model_mask='###').split('-')
        manufacturer, model = result[0], result[1]
        assert manufacturer in TRUCKS
        assert len(model) == 3

    def test_car(self, transport):
        result = transport.car()
        assert result in CARS

    def test_manufacturer(self, transport):
        assert transport.manufacturer() in MANUFACTURERS

    def test_airplane(self, transport):
        mask = '@###'
        result = transport.airplane(model_mask=mask).split()
        manufacturer, model = result[0], result[1]
        assert manufacturer in AIRPLANES
        assert len(model) == len(mask)

    @pytest.mark.parametrize(
        'locale', LIST_OF_LOCALES,
    )
    def test_vehicle_registration_code(self, transport, locale):
        result = transport.vehicle_registration_code(locale=locale)
        if locale:
            assert result in VRC_BY_LOCALES[locale]
        else:
            assert result in VR_CODES


class TestSeededTransport(object):

    @pytest.fixture
    def t1(self, seed):
        return Transport(seed=seed)

    @pytest.fixture
    def t2(self, seed):
        return Transport(seed=seed)

    def test_truck(self, t1, t2):
        assert t1.truck() == t2.truck()
        assert t1.truck(model_mask='#@') == t2.truck(model_mask='#@')

    def test_car(self, t1, t2):
        assert t1.car() == t2.car()

    def test_manufacturer(self, t1, t2):
        assert t1.manufacturer() == t2.manufacturer()

    def test_airplane(self, t1, t2):
        assert t1.airplane() == t2.airplane()
        assert t1.airplane(model_mask='#_#_#') == \
               t2.airplane(model_mask='#_#_#')

    @pytest.mark.parametrize(
        'locale', LIST_OF_LOCALES,
    )
    def test_vehicle_registration_code(self, t1, t2, locale):
        a = t1.vehicle_registration_code(locale)
        b = t2.vehicle_registration_code(locale)
        assert a == b
