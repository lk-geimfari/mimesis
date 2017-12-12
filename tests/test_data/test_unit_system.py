# -*- coding: utf-8 -*-

import pytest

from mimesis import UnitSystem
from mimesis.data import SI_PREFIXES, SI_PREFIXES_SYM
from mimesis.enums import PrefixSign, UnitName
from mimesis.exceptions import NonEnumerableError


@pytest.fixture
def us():
    return UnitSystem()


# TODO: Fill seed test cases
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
def test_unit(us, name):
    result = us.unit(name)
    assert result in name.value

    symbol = us.unit(name, symbol=True)
    assert symbol in name.value


def test_seeded_unit(_seeded_us):
    result = _seeded_us.unit(name=UnitName.FORCE, symbol=True)
    # assert result ==
    result = _seeded_us.unit()
    # assert result ==
    result = _seeded_us.unit()
    # assert result ==
    pass


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


def test_seeded_prefix(_seeded_us):
    prefix = _seeded_us.prefix(sign=PrefixSign.NEGATIVE, symbol=True)
    # assert result ==
    prefix = _seeded_us.prefix()
    # assert result ==
    prefix = _seeded_us.prefix()
    # assert result ==
    pass
