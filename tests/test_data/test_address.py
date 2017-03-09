# -*- coding: utf-8 -*-

import re

from elizabeth.intd import COUNTRIES_ISO, CONTINENT_CODES
from ._patterns import POSTAL_CODE_REGEX, STR_REGEX


def test_str(address):
    assert re.match(STR_REGEX, str(address))


def test_continent_code(address):
    result = address.continent_code()
    assert result in CONTINENT_CODES


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

    if current_locale in POSTAL_CODE_REGEX:
        assert re.match(POSTAL_CODE_REGEX[current_locale], result)
    else:
        assert re.match(POSTAL_CODE_REGEX['default'], result)


def test_country(generic):
    result = generic.address.country()
    assert result in generic.address.data['country']['name']


def test_country_iso(generic):
    default = generic.address.country_iso()
    assert isinstance(default, str)
    assert default in COUNTRIES_ISO['iso2']

    iso2 = generic.address.country_iso(fmt='iso2')
    assert iso2 in COUNTRIES_ISO['iso2']
    assert len(iso2) == 2

    iso3 = generic.address.country_iso(fmt='iso3')
    assert iso3 in COUNTRIES_ISO['iso3']
    assert len(iso3) == 3

    numeric = generic.address.country_iso(fmt='numeric')
    assert numeric in COUNTRIES_ISO['numeric']
    assert len(numeric) == 3
    assert numeric.isdigit()


def test_city(generic):
    result = generic.address.city()
    assert result in generic.address.data['city']
