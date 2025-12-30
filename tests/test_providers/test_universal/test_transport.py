import re

import pytest

from mimesis import Transport
from mimesis.datasets import (
    AIRPLANES,
    AUTO_MANUFACTURERS,
    CARS,
    VR_CODES,
    VRC_BY_LOCALES,
)
from mimesis.locales import Locale

from .. import patterns


class TestTransport:
    @pytest.fixture
    def transport(self):
        return Transport()

    def test_str(self, transport):
        assert re.match(patterns.PROVIDER_STR_REGEX, str(transport))

    def test_car(self, transport):
        result = transport.car()
        assert result in CARS

    def test_manufacturer(self, transport):
        assert transport.manufacturer() in AUTO_MANUFACTURERS

    def test_airplane(self, transport):
        result = transport.airplane()
        assert result in AIRPLANES

    @pytest.mark.parametrize("locale", Locale)
    def test_vehicle_registration_code(self, transport, locale):
        result = transport.vehicle_registration_code(locale=locale)
        assert result in VRC_BY_LOCALES[locale.value]

    def test_random_vehicle_registration_code(self, transport):
        result = transport.vehicle_registration_code(locale=None)
        assert result in VR_CODES


class TestSeededTransport:
    @pytest.fixture
    def t1(self, seed):
        return Transport(seed=seed)

    @pytest.fixture
    def t2(self, seed):
        return Transport(seed=seed)

    def test_car(self, t1, t2):
        assert t1.car() == t2.car()

    def test_manufacturer(self, t1, t2):
        assert t1.manufacturer() == t2.manufacturer()

    def test_airplane(self, t1, t2):
        assert t1.airplane() == t2.airplane()

    @pytest.mark.parametrize(
        "locale",
        list(Locale) + [None],
    )
    def test_vehicle_registration_code(self, t1, t2, locale):
        a = t1.vehicle_registration_code(locale)
        b = t2.vehicle_registration_code(locale)
        assert a == b
