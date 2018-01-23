# -*- coding: utf-8 -*-
import pytest

from mimesis import Transport
from mimesis.data import AIRPLANES, CARS, TRUCKS, VR_CODES, VRC_BY_LOCALES


class TestTransport(object):

    @pytest.fixture
    def _transport(self):
        return Transport()

    def test_truck(self, _transport):
        result = _transport.truck().split('-')
        manufacturer, model = result[0], result[1]
        assert manufacturer in TRUCKS
        assert len(model) == 7

        result = _transport.truck(model_mask='###').split('-')
        manufacturer, model = result[0], result[1]
        assert manufacturer in TRUCKS
        assert len(model) == 3

    def test_car(self, _transport):
        result = _transport.car()
        assert result in CARS

    def test_airplane(self, _transport):
        mask = '@###'
        result = _transport.airplane(model_mask=mask).split()
        manufacturer, model = result[0], result[1]
        assert manufacturer in AIRPLANES
        assert len(model) == len(mask)

    def test_vehicle_registration_code(self, transport):
        result = transport.vehicle_registration_code()
        assert result in VR_CODES

        result = transport.vehicle_registration_code(allow_random=False)
        assert result in VRC_BY_LOCALES[transport.locale]


class TestSeededTransport(object):

    @pytest.fixture
    def t1(self, seed):
        return Transport(seed=seed)

    @pytest.fixture
    def t2(self, seed):
        return Transport(seed=seed)

    def test_truck(self, t1, t2):
        assert t1.truck() == t2.truck()

    def test_car(self, t1, t2):
        assert t1.car() == t2.car()

    def test_airplane(self, t1, t2):
        assert t1.airplane() == t2.airplane()

    def test_vehicle_registration_code(self, t1, t2):
        assert t1.vehicle_registration_code() == t2.vehicle_registration_code()
