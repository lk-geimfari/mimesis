# -*- coding: utf-8 -*-

import re
from unittest import TestCase

from elizabeth import Address
import elizabeth.core.interdata as common

from tests.test_data import DummyCase
from ._patterns import POSTAL_CODE_REGEX, STR_REGEX


class AddressBaseTest(TestCase):
    def setUp(self):
        self.address = Address()

    def tearDown(self):
        del self.address

    def test_str(self):
        self.assertTrue(re.match(STR_REGEX, self.address.__str__()))

    def test_street_number(self):
        result = self.address.street_number()
        self.assertTrue(re.match(r'[0-9]{1,5}$', result))

    def test_latitude(self):
        result = self.address.latitude()
        self.assertLessEqual(result, 90)

    def test_longitude(self):
        result = self.address.longitude()
        self.assertLessEqual(result, 180)

    def test_coordinates(self):
        result = self.address.coordinates()
        self.assertIsInstance(result, dict)

        latitude = result['latitude']
        self.assertTrue(latitude <= 90)

        longitude = result['longitude']
        self.assertTrue(longitude <= 180)


class AddressTestCase(DummyCase):
    def test_street_name(self):
        result = self.generic.address.street_name()
        self.assertIn(result, self.generic.address.data['street']['name'])

    def test_street_suffix(self):
        result = self.generic.address.street_suffix()
        self.assertIn(result, self.generic.address.data['street']['suffix'])

    def test_address(self):
        result = self.generic.address.address()
        self.assertIsNotNone(result)

    def test_state(self):
        result = self.generic.address.state()
        self.assertIn(result, self.generic.address.data['state']['name'])

        result_ = self.generic.address.state(abbr=True)
        self.assertIn(result_, self.generic.address.data['state']['abbr'])

    def test_postal_code(self):
        result = self.generic.address.postal_code()
        current_locale = self.generic.address.locale

        if current_locale in POSTAL_CODE_REGEX:
            self.assertTrue(re.match(
                POSTAL_CODE_REGEX[current_locale], result)
            )
        else:
            self.assertTrue(re.match(
                POSTAL_CODE_REGEX['default'], result)
            )

    def test_country(self):
        result = self.generic.address.country()
        self.assertTrue(self.generic.address.data['country']['name'], result)

        result_iso = self.generic.address.country(iso_code=True)
        self.assertIn(result_iso, common.COUNTRIES_ISO)

    def test_city(self):
        result = self.generic.address.city()
        self.assertIn(result, self.generic.address.data['city'])
