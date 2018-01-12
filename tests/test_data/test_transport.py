# -*- coding: utf-8 -*-
import pytest

from mimesis import Transport
from mimesis.data import AIRPLANES, CARS, TRUCKS, VR_CODES, VRC_BY_LOCALES

from ..conftest import seed


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
        assert result in VRC_BY_LOCALES[transport.get_current_locale()]


class TestSeededTransport(object):
    TIMES = 5

    @pytest.fixture
    def _transports(self):
        return Transport(seed=seed), Transport(seed=seed)

    def test_truck(self, _transports):
        t1, t2 = _transports
        for _ in range(self.TIMES):
            assert t1.truck() == t2.truck()
            assert t1.truck(model_mask='#_@_#_@') == \
                t2.truck(model_mask='#_@_#_@')

    def test_car(self, _transports):
        t1, t2 = _transports
        for _ in range(self.TIMES):
            assert t1.car() == t2.car()

    def test_airplane(self, _transports):
        t1, t2 = _transports
        for _ in range(self.TIMES):
            assert t1.airplane() == t2.airplane()
            assert t1.airplane(model_mask='#_#_#') == \
                t2.airplane(model_mask='#_#_#')

    def test_vehicle_registration_code(self, _transports):
        t1, t2 = _transports
        for _ in range(self.TIMES):
            assert t1.vehicle_registration_code() == \
                t2.vehicle_registration_code()
            assert t1.vehicle_registration_code(allow_random=False) == \
                t2.vehicle_registration_code(allow_random=False)
