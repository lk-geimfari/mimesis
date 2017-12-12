# -*- coding: utf-8 -*-

import pytest

from mimesis import UnitSystem
from mimesis.data import SI_PREFIXES, SI_PREFIXES_SYM
from mimesis.enums import PrefixSign, UnitName
from mimesis.exceptions import NonEnumerableError


@pytest.fixture
def _us():
    return UnitSystem()


@pytest.fixture
def _seeded_us():
    return UnitSystem(seed=42)


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
def test_unit(_us, name):
    result = _us.unit(name)
    assert result in name.value

    symbol = _us.unit(name, symbol=True)
    assert symbol in name.value


def test_seeded_unit(_seeded_us):
    result = _seeded_us.unit(name=UnitName.FORCE, symbol=True)
    assert result == 'N'
    result = _seeded_us.unit()
    assert result == 'becquerel'
    result = _seeded_us.unit()
    assert result == 'mole'


@pytest.mark.parametrize(
    'sign, symbol', [
        (PrefixSign.POSITIVE, True),
        (PrefixSign.POSITIVE, False),
        (PrefixSign.NEGATIVE, True),
        (PrefixSign.NEGATIVE, False),
    ],
)
def test_prefix(_us, sign, symbol):
    prefix = _us.prefix(sign=sign, symbol=symbol)
    prefixes = SI_PREFIXES_SYM if symbol else SI_PREFIXES

    assert prefix in prefixes[sign.value]

    with pytest.raises(NonEnumerableError):
        _us.prefix(sign='nil')


def test_seeded_prefix(_seeded_us):
    result = _seeded_us.prefix(sign=PrefixSign.NEGATIVE, symbol=True)
    assert result == 'c'
    result = _seeded_us.prefix()
    assert result == 'tera'
    result = _seeded_us.prefix()
    assert result == 'peta'
