# -*- coding: utf-8 -*-

import pytest

from mimesis import UnitSystem
from mimesis.data import SI_PREFIXES, SI_PREFIXES_SYM
from mimesis.exceptions import WrongArgument


@pytest.fixture
def us():
    return UnitSystem()


def test_mass(us):
    result = us.mass(symbol=False)
    assert result == 'gram'

    result_sym = us.mass(symbol=True)
    assert result_sym == 'gr'


def test_thermodynamic_temperature(us):
    result = us.thermodynamic_temperature(symbol=False)
    assert result == 'kelvin'

    result_sym = us.thermodynamic_temperature(symbol=True)
    assert result_sym == 'K'


def test_amount_of_substance(us):
    result = us.amount_of_substance(symbol=False)
    assert result == 'mole'

    result_sym = us.amount_of_substance(symbol=True)
    assert result_sym == 'mol'


def test_angle(us):
    result = us.angle(symbol=False)
    assert result == 'radian'

    result_sym = us.angle(symbol=True)
    assert result_sym == 'r'


def test_solid_angle(us):
    result = us.solid_angle(symbol=False)
    assert result == 'steradian'

    result_sym = us.solid_angle(symbol=True)
    assert result_sym == '㏛'


def test_frequency(us):
    result = us.frequency(symbol=False)
    assert result == 'hertz'

    result_sym = us.frequency(symbol=True)
    assert result_sym == 'Hz'


def test_pressure(us):
    result = us.pressure(symbol=True)
    assert result == 'P'

    result_sym = us.pressure(symbol=False)
    assert result_sym == 'pascal'


def test_energy(us):
    result = us.energy(symbol=True)
    assert result == 'J'

    result_sym = us.energy(symbol=False)
    assert result_sym == 'joule'


def test_power(us):
    result_sym = us.power(symbol=True)
    assert result_sym == 'W'

    result = us.power(symbol=False)
    assert result == 'watt'


def test_flux(us):
    result_sym = us.flux(symbol=True)
    assert result_sym == 'W'

    result = us.flux(symbol=False)
    assert result == 'watt'


def test_electric_charge(us):
    result_sym = us.electric_charge(symbol=True)
    assert result_sym == 'C'

    result = us.electric_charge(symbol=False)
    assert result == 'coulomb'


def test_voltage(us):
    result_sym = us.voltage(symbol=True)
    assert result_sym == 'V'

    result = us.voltage(symbol=False)
    assert result == 'volt'


def test_electric_capacitance(us):
    result_sym = us.electric_capacitance(symbol=True)
    assert result_sym == 'F'

    result = us.electric_capacitance(symbol=False)
    assert result == 'farad'


def test_electric_resistance(us):
    result_sym = us.electric_resistance(symbol=True)
    assert result_sym == 'Ω'

    result = us.electric_resistance(symbol=False)
    assert result == 'ohm'


def test_impedance(us):
    result_sym = us.impedance(symbol=True)
    assert result_sym == 'Ω'

    result = us.impedance(symbol=False)
    assert result == 'ohm'


def test_reactance(us):
    result_sym = us.reactance(symbol=True)
    assert result_sym == 'Ω'

    result = us.reactance(symbol=False)
    assert result == 'ohm'


def test_electrical_conductance(us):
    result_sym = us.electrical_conductance(symbol=True)
    assert result_sym == 'S'

    result = us.electrical_conductance(symbol=False)
    assert result == 'siemens'


def test_magnetic_flux(us):
    result_sym = us.magnetic_flux(symbol=True)
    assert result_sym == 'Wb'

    result = us.magnetic_flux(symbol=False)
    assert result == 'weber'


def test_magnetic_flux_density(us):
    result_sym = us.magnetic_flux_density(symbol=True)
    assert result_sym == 'T'

    result = us.magnetic_flux_density(symbol=False)
    assert result == 'tesla'


def test_inductance(us):
    result_sym = us.inductance(symbol=True)
    assert result_sym == 'H'

    result = us.inductance(symbol=False)
    assert result == 'henry'


def test_temperature(us):
    result_sym = us.temperature(symbol=True)
    assert result_sym == '°C'

    result = us.temperature(symbol=False)
    assert result == 'Celsius'


def test_radioactivity(us):
    result_sym = us.radioactivity(symbol=True)
    assert result_sym == 'Bq'

    result = us.radioactivity(symbol=False)
    assert result == 'becquerel'


@pytest.mark.parametrize(
    'sign, symbol', [
        ('positive', True),
        ('positive', False),
        ('negative', True),
        ('negative', False),
    ],
)
def test_prefix(us, sign, symbol):
    prefix = us.prefix(sign=sign, symbol=symbol)
    assert prefix in SI_PREFIXES[sign] or prefix in SI_PREFIXES_SYM[sign]

    with pytest.raises(WrongArgument):
        us.prefix(sign='nil')


def test_information(us):
    result_sym = us.information(symbol=True)
    assert result_sym == 'b'

    result = us.information(symbol=False)
    assert result == 'byte'


def test_force(us):
    result_sym = us.force(symbol=True)
    assert result_sym == 'N'

    result = us.force(symbol=False)
    assert result == 'newton'
