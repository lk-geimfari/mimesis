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


@pytest.fixture
def _seeded_address():
    return Address(seed=42)


def test_str(address):
    assert re.match(p.STR_REGEX, str(address))


def test_street_number(_address):
    result = _address.street_number()
    assert re.match(r'[0-9]{1,5}$', result)


def test_seeded_street_number(_seeded_address):
    result = _seeded_address.street_number(maximum=42)
    assert result == '41'
    result = _seeded_address.street_number()
    assert result == '229'
    result = _seeded_address.street_number()
    assert result == '52'


def test_latitude(_address):
    result = _address.latitude()
    assert isinstance(result, float)
    assert result <= 90
    assert result >= -90


def test_seeded_latitude(_seeded_address):
    result = _seeded_address.latitude()
    assert result == 25.096823722419074
    result = _seeded_address.latitude()
    assert result == -85.49806405991995


def test_longitude(_address):
    result = _address.longitude()
    assert isinstance(result, float)
    assert result <= 180
    assert result >= -180


def test_seeded_longitude(_seeded_address):
    result = _seeded_address.longitude()
    assert result == 50.19364744483815
    result = _seeded_address.longitude()
    assert result == -170.9961281198399


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


def test_seeded_coordinates(_seeded_address):
    result = _seeded_address.coordinates()
    assert result == {
        'latitude': -85.49806405991995, 'longitude': 50.19364744483815,
    }
    result = _seeded_address.coordinates()
    assert result == {
        'latitude': -49.8220671332119, 'longitude': -80.98944538711707,
    }


def test_street_name(address):
    result = address.street_name()
    assert isinstance(result, str)
    assert result in address._data['street']['name']


def test_seeded_street_name(_seeded_address):
    result = _seeded_address.street_name()
    assert result == 'Collingwood'
    result = _seeded_address.street_name()
    assert result == 'Atalaya'


def test_street_suffix(address):
    result = address.street_suffix()
    assert isinstance(result, str)
    assert result in address._data['street']['suffix']


def test_seeded_street_suffix(_seeded_address):
    result = _seeded_address.street_suffix()
    assert result == 'Crescent'
    result = _seeded_address.street_suffix()
    assert result == 'Avenue'


def test_address(address):
    result = address.address()
    assert isinstance(result, str)
    assert result is not None


def test_seeded_address(_seeded_address):
    result = _seeded_address.address()
    assert result == '1310 Collingwood Avenue'
    result = _seeded_address.address()
    assert result == '564 Hillcrest Grove'


def test_state(address):
    result = address.state()
    assert result in address._data['state']['name']

    result_abbr = address.state(abbr=True)
    assert result_abbr in address._data['state']['abbr']


def test_seeded_state(_seeded_address):
    result = _seeded_address.state(abbr=True)
    assert result == 'SD'
    result = _seeded_address.state()
    assert result == 'Delaware'
    result = _seeded_address.state()
    assert result == 'Alaska'


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


def test_seeded_postal_code(_seeded_address):
    result = _seeded_address.postal_code()
    assert result == '10433'
    result = _seeded_address.postal_code()
    assert result == '21819'


def test_country(address):
    result = address.country()
    assert result in address._data['country']['name']


def test_seeded_country(_seeded_address):
    result = _seeded_address.country()
    assert result == 'Norfolk Island'
    result = _seeded_address.country()
    assert result == 'Botswana'


@pytest.mark.parametrize(
    'fmt, length', [
        (CountryCode.ISO2, 2),
        (CountryCode.ISO3, 3),
        (CountryCode.NUMERIC, 3),
    ],
)
def test_country_iso(_address, fmt, length):
    iso = _address.country_iso_code(fmt=fmt)

    assert iso in COUNTRIES_ISO[fmt.value]
    assert len(iso) == length

    with pytest.raises(NonEnumerableError):
        _address.country_iso_code(fmt='nil')


# TODO: https://github.com/lk-geimfari/mimesis/issues/325#issuecomment-352364359
def skip_test_seeded_country_iso(_seeded_address):
    result = _seeded_address.country_iso_code(fmt=CountryCode.NUMERIC)
    assert result == '558'
    result = _seeded_address.country_iso_code()
    assert result == 'AM'
    result = _seeded_address.country_iso_code()
    assert result == '238'


def test_city(address):
    result = address.city()
    assert result in address._data['city']


def test_seeded_city(_seeded_address):
    result = _seeded_address.city()
    assert result == 'Reno'
    result = _seeded_address.city()
    assert result == 'Carbondale'


def test_continent(address):
    result = address.continent()
    assert result in address._data['continent']

    result = address.continent(code=True)
    assert result in CONTINENT_CODES


def test_seeded_continent(_seeded_address):
    result = _seeded_address.continent(code=True)
    assert result == 'EU'
    result = _seeded_address.continent()
    assert result == 'Africa'
    result = _seeded_address.continent()
    assert result == 'Africa'
    result = _seeded_address.continent()
    assert result == 'North America'


def test_calling_code(_address):
    result = _address.calling_code()
    assert result is not None
    assert result in CALLING_CODES


def test_seeded_calling_code(_seeded_address):
    result = _seeded_address.calling_code()
    assert result == '+213'
    result = _seeded_address.calling_code()
    assert result == '+41'
