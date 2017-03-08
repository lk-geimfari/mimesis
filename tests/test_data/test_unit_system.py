# -*- coding: utf-8 -*-

import pytest

from elizabeth.core.providers import UnitSystem
from elizabeth.core.intd import SI_PREFIXES


@pytest.fixture
def us():
    return UnitSystem()


def test_mass(us):
    assert us.mass(symbol=False) == 'gram'
    assert us.mass(symbol=True) == 'gr'


def test_thermodynamic_temperature(us):
    assert us.thermodynamic_temperature(symbol=False) == 'kelvin'
    assert us.thermodynamic_temperature(symbol=True) == 'K'


def test_amount_of_substance(us):
    assert us.amount_of_substance(symbol=False) == 'mole'
    assert us.amount_of_substance(symbol=True) == 'mol'


def test_angle(us):
    assert us.angle(symbol=False) == 'radian'
    assert us.angle(symbol=True) == 'r'


def test_solid_angle(us):
    assert us.solid_angle(symbol=False) == 'steradian'
    assert us.solid_angle(symbol=True) == '㏛'


def test_frequency(us):
    assert us.frequency(symbol=False) == 'hertz'
    assert us.frequency(symbol=True) == 'Hz'


def test_pressure(us):
    assert us.pressure(symbol=True) == 'P'
    assert us.pressure(symbol=False) == 'pascal'


def test_energy(us):
    assert us.energy(symbol=True) == 'J'
    assert us.energy(symbol=False) == 'joule'


def test_power(us):
    assert us.power(symbol=True) == 'W'
    assert us.power(symbol=False) == 'watt'


def test_flux(us):
    assert us.flux(symbol=True) == 'W'
    assert us.flux(symbol=False) == 'watt'


def test_electric_charge(us):
    assert us.electric_charge(symbol=True) == 'C'
    assert us.electric_charge(symbol=False) == 'coulomb'


def test_voltage(us):
    assert us.voltage(symbol=True) == 'V'
    assert us.voltage(symbol=False) == 'volt'


def test_electric_capacitance(us):
    assert us.electric_capacitance(symbol=True) == 'F'
    assert us.electric_capacitance(symbol=False) == 'farad'


def test_electric_resistance(us):
    assert us.electric_resistance(symbol=True) == 'Ω'
    assert us.electric_resistance(symbol=False) == 'ohm'


def test_impedance(us):
    assert us.impedance(symbol=True) == 'Ω'
    assert us.impedance(symbol=False) == 'ohm'


def test_reactance(us):
    assert us.reactance(symbol=True) == 'Ω'
    assert us.reactance(symbol=False) == 'ohm'


def test_electrical_conductance(us):
    assert us.electrical_conductance(symbol=True) == 'S'
    assert us.electrical_conductance(symbol=False) == 'siemens'


def test_magnetic_flux(us):
    assert us.magnetic_flux(symbol=True) == 'Wb'
    assert us.magnetic_flux(symbol=False) == 'weber'


def test_magnetic_flux_density(us):
    assert us.magnetic_flux_density(symbol=True) == 'T'
    assert us.magnetic_flux_density(symbol=False) == 'tesla'


def test_inductance(us):
    assert us.inductance(symbol=True) == 'H'
    assert us.inductance(symbol=False) == 'henry'


def test_temperature(us):
    assert us.temperature(symbol=True) == '°C'
    assert us.temperature(symbol=False) == 'Celsius'


def test_radioactivity(us):
    assert us.radioactivity(symbol=True) == 'Bq'
    assert us.radioactivity(symbol=False) == 'becquerel'


def test_prefix(us):
    assert us.prefix(sign='positive', symbol=False) in SI_PREFIXES['positive']
    assert us.prefix(sign='negative', symbol=False) in SI_PREFIXES['negative']

    assert us.prefix(sign='positive', symbol=True) in SI_PREFIXES['_sym_']['positive']
    assert us.prefix(sign='negative', symbol=True) in SI_PREFIXES['_sym_']['negative']


def test_information(us):
    assert us.information(symbol=True) == 'b'
    assert us.information(symbol=False) == 'byte'
