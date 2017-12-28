# -*- coding: utf-8 -*-

import re

import pytest

from mimesis import Address
from mimesis.data import CALLING_CODES, CONTINENT_CODES, COUNTRIES_ISO
from mimesis.enums import CountryCode
from mimesis.exceptions import NonEnumerableError

from . import _patterns as p


@pytest.fixture
def _address():
    return Address()


def test_str(address):
    assert re.match(p.STR_REGEX, str(address))


def test_street_number(_address):
    result = _address.street_number()
    assert re.match(r'[0-9]{1,5}$', result)


def test_latitude(_address):
    result = _address.latitude()
    assert isinstance(result, float)
    assert result <= 90
    assert result >= -90


def test_longitude(_address):
    result = _address.longitude()
    assert isinstance(result, float)
    assert result <= 180
    assert result >= -180


def test_coordinates(_address):
    result = _address.coordinates()
    assert isinstance(result, dict)

    latitude = result['latitude']
    assert isinstance(latitude, float)
    assert latitude <= 90
    assert latitude >= -90

    longitude = result['longitude']
    assert isinstance(latitude, float)
    assert longitude <= 180
    assert longitude >= -180


def test_street_name(address):
    result = address.street_name()
    assert isinstance(result, str)
    assert result in address._data['street']['name']


def test_street_suffix(address):
    result = address.street_suffix()
    assert isinstance(result, str)
    assert result in address._data['street']['suffix']


def test_address(address):
    result = address.address()
    assert isinstance(result, str)
    assert result is not None


def test_state(address):
    result = address.state()
    assert result in address._data['state']['name']

    result_abbr = address.state(abbr=True)
    assert result_abbr in address._data['state']['abbr']


def test_state_aliases(address):
    province = address.province()
    region = address.region()
    federal_subject = address.federal_subject()

    states = address._data['state']['name']

    assert province in states
    assert region in states
    assert federal_subject in states

    province = address.province(abbr=True)
    region = address.region(abbr=True)
    federal_subject = address.federal_subject(abbr=True)

    abbreviations = address._data['state']['abbr']
    assert province in abbreviations
    assert region in abbreviations
    assert federal_subject in abbreviations


def test_postal_code(address):
    result = address.postal_code()
    current_locale = address.get_current_locale()

    if current_locale in p.POSTAL_CODE_REGEX:
        assert re.match(p.POSTAL_CODE_REGEX[current_locale], result)
    else:
        assert re.match(p.POSTAL_CODE_REGEX['default'], result)


def test_country(address):
    result = address.country()
    assert result in address._data['country']['name']


@pytest.mark.parametrize(
    'fmt, length', [
        (CountryCode.ISO2, 2),
        (CountryCode.ISO3, 3),
        (CountryCode.NUMERIC, 3),
        (None, [2, 3]),
    ],
)
def test_country_iso(_address, fmt, length):
    iso = _address.country_iso_code(fmt=fmt)

    if fmt is not None:
        assert iso in COUNTRIES_ISO[fmt.value]

    assert len(iso) == length or len(iso) in length

    with pytest.raises(NonEnumerableError):
        _address.country_iso_code(fmt='nil')


def test_city(address):
    result = address.city()
    assert result in address._data['city']


def test_continent(address):
    result = address.continent()
    assert result in address._data['continent']

    result = address.continent(code=True)
    assert result in CONTINENT_CODES


def test_calling_code(_address):
    result = _address.calling_code()
    assert result is not None
    assert result in CALLING_CODES
