# -*- coding: utf-8 -*-

import re
from unittest import TestCase

from church.church import Address
from tests import LANG


class AddressTestCase(TestCase):
    def setUp(self):
        self.address = Address(LANG)
        self.db = self.address.data

    def tearDown(self):
        del self.address

    def test_street_number(self):
        result = self.address.street_number()
        self.assertTrue(re.match(r'[0-9]{1,5}$', result))

    def test_street_name(self):
        result = self.address.street_name()
        self.assertIn(result, self.db['street']['name'])

    def test_street_suffix(self):
        result = self.address.street_suffix()
        self.assertIn(result, self.db['street']['suffix'])

    def test_address(self):
        result = self.address.address()
        self.assertTrue(len(result) > 6)

    def test_state(self):
        result = self.address.state()
        self.assertIn(result, self.db['state']['name'])

    def test_postal_code(self):
        result = self.address.postal_code()
        if self.address.lang == 'ru':
            self.assertTrue(re.match(r'[0-9]{6}$', str(result)))
        else:
            self.assertTrue(re.match(r'[0-9]{5}$', str(result)))

    def test_country(self):
        result = self.address.country()
        self.assertTrue(self.db['country']['name'], result)

        result2 = self.address.country(iso_code=True)
        self.assertTrue(self.db['country']['iso_code'], result2)

    def test_city(self):
        result = self.address.city()
        self.assertIn(result, self.db['city'])

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
