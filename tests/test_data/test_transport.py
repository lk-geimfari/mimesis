# -*- coding: utf-8 -*-
import pytest

from mimesis import Transport
from mimesis.data import AIRPLANES, CARS, TRUCKS, VR_CODES, VRC_BY_LOCALES


@pytest.fixture
def _transport():
    return Transport()


# TODO: Fill seed test cases
@pytest.fixture
def _seeded_transport():
    return Transport(seed=42)


def test_truck(_transport):
    result = _transport.truck().split('-')
    manufacturer, model = result[0], result[1]
    assert manufacturer in TRUCKS
    assert len(model) == 7

    result = _transport.truck(model_mask='###').split('-')
    manufacturer, model = result[0], result[1]
    assert manufacturer in TRUCKS
    assert len(model) == 3


def test_seeded_truck(_seeded_transport):
    result = _seeded_transport.truck(model_mask='@@##@@_##')
    # assert result ==
    result = _seeded_transport.truck()
    # assert result ==
    result = _seeded_transport.truck()
    # assert result ==
    pass


def test_car(_transport):
    result = _transport.car()
    assert result in CARS


def test_seeded_car(_seeded_transport):
    result = _seeded_transport.car()
    # assert result ==
    result = _seeded_transport.car()
    # assert result ==
    pass


def test_airplane(_transport):
    mask = '@###'
    result = _transport.airplane(model_mask=mask).split()
    manufacturer, model = result[0], result[1]
    assert manufacturer in AIRPLANES
    assert len(model) == len(mask)


def test_seeded_airplane(_seeded_transport):
    result = _seeded_transport.airplane(model_mask='@@##@@_@')
    # assert result ==
    result = _seeded_transport.airplane()
    # assert result ==
    result = _seeded_transport.airplane()
    # assert result ==
    pass


def test_vehicle_registration_code(transport):
    result = transport.vehicle_registration_code()
    assert result in VR_CODES

    result = transport.vehicle_registration_code(allow_random=False)
    assert result in VRC_BY_LOCALES[transport.locale]


def test_seeded_vehicle_registration_code(_seeded_transport):
    result = _seeded_transport.vehicle_registration_code(allow_random=True)
    # assert result ==
    result = _seeded_transport.vehicle_registration_code()
    # assert result ==
    result = _seeded_transport.vehicle_registration_code()
    # assert result ==
    pass
