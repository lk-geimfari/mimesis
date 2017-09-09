# -*- coding: utf-8 -*-

import re

import pytest

from mimesis.data import CONTINENT_CODES, COUNTRIES_ISO

from . import _patterns as p


def test_str(address):
    assert re.match(p.STR_REGEX, str(address))


def test_street_number(address):
    result = address.street_number()
    assert re.match(r'[0-9]{1,5}$', result)


def test_latitude(address):
    result = address.latitude()
    assert isinstance(result, float)
    assert result <= 90
    assert result >= -90


def test_longitude(address):
    result = address.longitude()
    assert isinstance(result, float)
    assert result <= 180
    assert result >= -180


def test_coordinates(address):
    result = address.coordinates()
    assert isinstance(result, dict)

    latitude = result['latitude']
    assert isinstance(latitude, float)
    assert latitude <= 90
    assert latitude >= -90

    longitude = result['longitude']
    assert isinstance(latitude, float)
    assert longitude <= 180
    assert longitude >= -180


def test_street_name(generic):
    result = generic.address.street_name()
    assert isinstance(result, str)
    assert result in generic.address.data['street']['name']


def test_street_suffix(generic):
    result = generic.address.street_suffix()
    assert isinstance(result, str)
    assert result in generic.address.data['street']['suffix']


def test_address(generic):
    result = generic.address.address()
    assert isinstance(result, str)
    assert result is not None


def test_state(generic):
    result = generic.address.state()
    assert result in generic.address.data['state']['name']

    result_ = generic.address.state(abbr=True)
    assert result_ in generic.address.data['state']['abbr']


def test_postal_code(generic):
    result = generic.address.postal_code()
    current_locale = generic.address.locale

    if current_locale in p.POSTAL_CODE_REGEX:
        assert re.match(p.POSTAL_CODE_REGEX[current_locale], result)
    else:
        assert re.match(p.POSTAL_CODE_REGEX['default'], result)


def test_country(generic):
    result = generic.address.country()
    assert result in generic.address.data['country']['name']


@pytest.mark.parametrize(
    'fmt, length', [
        ('iso2', 2),
        ('iso3', 3),
        ('numeric', 3),
    ],
)
def test_country_iso(generic, fmt, length):
    iso = generic.address.country_iso(fmt=fmt)
    assert iso in COUNTRIES_ISO[fmt]
    assert len(iso) == length

    with pytest.raises(KeyError):
        generic.address.country_iso(fmt='none')


def test_city(generic):
    result = generic.address.city()
    assert result in generic.address.data['city']


def test_continent(generic):
    result = generic.address.continent()
    assert result in generic.address.data['continent']

    result = generic.address.continent(code=True)
    assert result in CONTINENT_CODES
