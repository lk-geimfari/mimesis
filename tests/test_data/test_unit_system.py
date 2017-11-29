# -*- coding: utf-8 -*-

import pytest

from mimesis import UnitSystem
from mimesis.data import SI_PREFIXES, SI_PREFIXES_SYM
from mimesis.enums import PrefixSign, UnitName
from mimesis.exceptions import NonEnumerableError


@pytest.fixture
def us():
    return UnitSystem()


@pytest.mark.parametrize(
    'name', [
        UnitName.MASS,
        UnitName.INFORMATION,
        UnitName.THERMODYNAMIC_TEMPERATURE,
        UnitName.AMOUNT_OF_SUBSTANCE,
        UnitName.ANGLE, UnitName.SOLID_ANGLE,
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
def test_unit(us, name):
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
def test_prefix(us, sign, symbol):
    prefix = us.prefix(sign=sign, symbol=symbol)
    prefixes = SI_PREFIXES_SYM if symbol else SI_PREFIXES

    assert prefix in prefixes[sign.value]

    with pytest.raises(NonEnumerableError):
        us.prefix(sign='nil')
