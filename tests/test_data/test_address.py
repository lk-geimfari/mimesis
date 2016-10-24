# -*- coding: utf-8 -*-

import re
from unittest import TestCase

from church.church import Address
from church.utils import pull

from tests import LANG


class AddressTestCase(TestCase):
    def setUp(self):
        self.address = Address(LANG)

    def tearDown(self):
        del self.address

    def test_street_number(self):
        result = self.address.street_number()
        self.assertTrue(re.match(r'[0-9]{1,5}$', result))

    def test_street_name(self):
        result = self.address.street_name()
        parent_file = pull('streets', self.address.lang)
        self.assertIn(result + '\n', parent_file)

    def test_street_suffix(self):
        result = self.address.street_suffix()
        parent_file = pull('st_suffix', self.address.lang)
        self.assertIn(result + '\n', parent_file)

    def test_address(self):
        result = self.address.address()
        self.assertTrue(len(result) > 6)

    def test_state(self):
        result = self.address.state()
        parent_file = pull('states', self.address.lang)
        self.assertIn(result + '\n', parent_file)

    def test_postal_code(self):
        result = self.address.postal_code()
        if self.address.lang == 'ru':
            self.assertTrue(re.match(r'[0-9]{6}$', str(result)))
        else:
            self.assertTrue(re.match(r'[0-9]{5}$', str(result)))

    def test_country(self):
        result = self.address.country() + '\n'
        self.assertTrue(len(result) > 3)

        result2 = self.address.country(only_iso_code=True) + '\n'
        self.assertTrue(len(result2) < 4)

    def test_city(self):
        result = self.address.city()
        parent_file = pull('cities', self.address.lang)
        self.assertIn(result + '\n', parent_file)

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