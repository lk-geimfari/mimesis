# -*- coding: utf-8 -*-

import pytest

from elizabeth.core.intd import CAR, TRUCKS, AIRPLANES
from tests.test_data import transport


def test_truck(transport):
    result = transport.truck().split('-')
    manufacturer, model = result[0], result[1]
    assert manufacturer in TRUCKS
    assert len(model) == 7

    result = transport.truck(model_mask='###').split('-')
    manufacturer, model = result[0], result[1]
    assert manufacturer in TRUCKS
    assert len(model) == 3


def test_car(transport):
    result = transport.car()
    assert result in CAR


def test_airplane(transport):
    mask = '@###'
    result = transport.airplane(model_mask=mask).split()
    manufacturer, model = result[0], result[1]
    assert manufacturer in AIRPLANES
    assert len(model) == len(mask)
