# -*- coding: utf-8 -*-

import re

import pytest

from mimesis import Address
from mimesis.data import CALLING_CODES, CONTINENT_CODES, COUNTRIES_ISO
from mimesis.enums import CountryCode
from mimesis.exceptions import NonEnumerableError

from ._patterns import POSTAL_CODE_REGEX, STR_REGEX


class TestAddress(object):

    @pytest.fixture
    def _address(self):
        return Address()

    def test_str(self, address):
        assert re.match(STR_REGEX, str(address))

    def test_street_number(self, _address):
        result = _address.street_number()
        assert re.match(r'[0-9]{1,5}$', result)

    def test_latitude(self, _address):
        result = _address.latitude()
        assert isinstance(result, float)
        assert result <= 90
        assert result >= -90

    def test_longitude(self, _address):
        result = _address.longitude()
        assert isinstance(result, float)
        assert result <= 180
        assert result >= -180

    def test_coordinates(self, _address):
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

    def test_street_name(self, address):
        result = address.street_name()
        assert result in address._data['street']['name']

    def test_street_suffix(self, address):
        result = address.street_suffix()
        assert result in address._data['street']['suffix']

    def test_address(self, address):
        result = address.address()
        assert isinstance(result, str)
        assert result is not None

    @pytest.mark.parametrize(
        'abbr, key', [
            (False, 'name'),
            (True, 'abbr'),
        ],
    )
    def test_state(self, address, abbr, key):
        result = address.state(abbr=abbr)
        assert result in address._data['state'][key]

    @pytest.mark.parametrize(
        'alias, abbr', [
            ('province', True),
            ('region', True),
            ('federal_subject', True),
            ('prefecture', True),
        ],
    )
    def test_state_aliases_abbreviated(self, address, alias, abbr):
        method = getattr(address, alias)
        result = method(abbr=abbr)
        assert result in address._data['state']['abbr']

    @pytest.mark.parametrize(
        'alias', [
            'province',
            'region',
            'federal_subject',
            'prefecture',
        ],
    )
    def test_state_aliases(self, address, alias):
        result = getattr(address, alias)()
        assert result in address._data['state']['name']

    def test_postal_code(self, address):
        result = address.postal_code()
        current_locale = address.get_current_locale()

        if current_locale in POSTAL_CODE_REGEX:
            assert re.match(POSTAL_CODE_REGEX[current_locale], result)
        else:
            assert re.match(POSTAL_CODE_REGEX['default'], result)

    def test_country(self, address):
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
    def test_country_iso(self, _address, fmt, length):
        iso = _address.country_iso_code(fmt=fmt)

        if fmt is not None:
            assert iso in COUNTRIES_ISO[fmt.value]

        assert len(iso) == length or len(iso) in length

        with pytest.raises(NonEnumerableError):
            _address.country_iso_code(fmt='nil')

    def test_city(self, address):
        result = address.city()
        assert result in address._data['city']

    def test_continent(self, address):
        result = address.continent()
        assert result in address._data['continent']

        result = address.continent(code=True)
        assert result in CONTINENT_CODES

    def test_calling_code(self, _address):
        result = _address.calling_code()
        assert result is not None
        assert result in CALLING_CODES


class TestSeededAddress(object):
    TIMES = 5

    @pytest.fixture
    def _addresses(self, seed):
        return Address(seed=seed), Address(seed=seed)

    def test_street_number(self, _addresses):
        a1, a2 = _addresses
        for _ in range(self.TIMES):
            assert a1.street_number() == a2.street_number()

    def test_latitude(self, _addresses):
        a1, a2 = _addresses
        for _ in range(self.TIMES):
            assert a1.latitude() == a2.latitude()

    def test_longitude(self, _addresses):
        a1, a2 = _addresses
        for _ in range(self.TIMES):
            assert a1.longitude() == a2.longitude()

    def test_coordinates(self, _addresses):
        a1, a2 = _addresses
        for _ in range(self.TIMES):
            assert a1.coordinates() == a2.coordinates()

    def test_street_name(self, _addresses):
        a1, a2 = _addresses
        for _ in range(self.TIMES):
            assert a1.street_name() == a2.street_name()

    def test_street_suffix(self, _addresses):
        a1, a2 = _addresses
        for _ in range(self.TIMES):
            assert a1.street_suffix() == a2.street_suffix()

    def test_address(self, _addresses):
        a1, a2 = _addresses
        for _ in range(self.TIMES):
            assert a1.address() == a2.address()

    def test_state(self, _addresses):
        a1, a2 = _addresses
        for _ in range(self.TIMES):
            assert a1.state() == a2.state()
            assert a1.state(abbr=True) == a2.state(abbr=True)

    def test_postal_code(self, _addresses):
        a1, a2 = _addresses
        for _ in range(self.TIMES):
            assert a1.postal_code() == a2.postal_code()

    def test_country(self, _addresses):
        a1, a2 = _addresses
        for _ in range(self.TIMES):
            assert a1.country() == a2.country()

    def test_country_iso(self, _addresses):
        a1, a2 = _addresses
        for _ in range(self.TIMES):
            assert a1.country_iso_code() == a2.country_iso_code()

    def test_city(self, _addresses):
        a1, a2 = _addresses
        for _ in range(self.TIMES):
            assert a1.city() == a2.city()

    def test_continent(self, _addresses):
        a1, a2 = _addresses
        for _ in range(self.TIMES):
            assert a1.continent() == a2.continent()
            assert a1.continent(code=True) == a2.continent(code=True)

    def test_calling_code(self, _addresses):
        a1, a2 = _addresses
        for _ in range(self.TIMES):
            assert a1.calling_code() == a2.calling_code()
