# -*- coding: utf-8 -*-
import re

import pytest

from mimesis import UnitSystem
from mimesis.data import SI_PREFIXES, SI_PREFIXES_SYM
from mimesis.enums import PrefixSign, UnitName
from mimesis.exceptions import NonEnumerableError

from . import patterns


class TestUnitSystem(object):

    @pytest.fixture
    def us(self):
        return UnitSystem()

    def test_str(self, us):
        assert re.match(patterns.PROVIDER_STR_REGEX, str(us))

    @pytest.mark.parametrize(
        'name', [
            UnitName.MASS,
            UnitName.INFORMATION,
            UnitName.THERMODYNAMIC_TEMPERATURE,
            UnitName.AMOUNT_OF_SUBSTANCE,
            UnitName.ANGLE,
            UnitName.SOLID_ANGLE,
            UnitName.FREQUENCY,
            UnitName.FORCE,
            UnitName.PRESSURE,
            UnitName.ENERGY,
            UnitName.POWER,
            UnitName.ELECTRIC_CHARGE,
            UnitName.VOLTAGE,
            UnitName.ELECTRIC_CAPACITANCE,
            UnitName.ELECTRIC_RESISTANCE,
            UnitName.ELECTRICAL_CONDUCTANCE,
            UnitName.MAGNETIC_FLUX,
            UnitName.MAGNETIC_FLUX_DENSITY,
            UnitName.INDUCTANCE,
            UnitName.TEMPERATURE,
            UnitName.RADIOACTIVITY,
        ],
    )
    def test_unit(self, us, name):
        result = us.unit(name)
        assert result in name.value
        symbol = us.unit(name, symbol=True)
        assert symbol in name.value

    @pytest.mark.parametrize(
        'sign, symbol', [
            (PrefixSign.POSITIVE, True),
            (PrefixSign.POSITIVE, False),
            (PrefixSign.NEGATIVE, True),
            (PrefixSign.NEGATIVE, False),
        ],
    )
    def test_prefix(self, us, sign, symbol):
        prefix = us.prefix(sign=sign, symbol=symbol)
        prefixes = SI_PREFIXES_SYM if symbol else SI_PREFIXES
        assert prefix in prefixes[sign.value]
        with pytest.raises(NonEnumerableError):
            us.prefix(sign='nil')


class TestSeededUnitSystem(object):

    @pytest.fixture
    def us1(self, seed):
        return UnitSystem(seed=seed)

    @pytest.fixture
    def us2(self, seed):
        return UnitSystem(seed=seed)

    def test_unit(self, us1, us2):
        assert us1.unit() == us2.unit()
        assert us1.unit(name=UnitName.ANGLE, symbol=True) == \
            us2.unit(name=UnitName.ANGLE, symbol=True)

    def test_prefix(self, us1, us2):
        assert us1.prefix() == us2.prefix()
        assert us1.prefix(sign=PrefixSign.POSITIVE, symbol=True) == \
            us2.prefix(sign=PrefixSign.POSITIVE, symbol=True)
