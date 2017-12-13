# -*- coding: utf-8 -*-
import pytest

from mimesis import Transport
from mimesis.data import AIRPLANES, CARS, TRUCKS, VR_CODES, VRC_BY_LOCALES


@pytest.fixture
def _transport():
    return Transport()


def test_truck(_transport):
    result = _transport.truck().split('-')
    manufacturer, model = result[0], result[1]
    assert manufacturer in TRUCKS
    assert len(model) == 7

    result = _transport.truck(model_mask='###').split('-')
    manufacturer, model = result[0], result[1]
    assert manufacturer in TRUCKS
    assert len(model) == 3


def test_car(_transport):
    result = _transport.car()
    assert result in CARS


def test_airplane(_transport):
    mask = '@###'
    result = _transport.airplane(model_mask=mask).split()
    manufacturer, model = result[0], result[1]
    assert manufacturer in AIRPLANES
    assert len(model) == len(mask)


def test_vehicle_registration_code(transport):
    result = transport.vehicle_registration_code()
    assert result in VR_CODES

    result = transport.vehicle_registration_code(allow_random=False)
    assert result in VRC_BY_LOCALES[transport.get_current_locale()]
