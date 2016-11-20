# -*- coding: utf-8 -*-

import re

import elizabeth.data.common as common
from tests.test_data import DummyCase


class AddressTestCase(DummyCase):
    def test_street_number(self):
        result = self.generic.address.street_number()
        self.assertTrue(re.match(r'[0-9]{1,5}$', result))

    def test_street_name(self):
        result = self.generic.address.street_name()
        self.assertIn(result, self.generic.address.data['street']['name'])

    def test_street_suffix(self):
        result = self.generic.address.street_suffix()
        self.assertIn(result, self.generic.address.data['street']['suffix'])

    def test_address(self):
        result = self.generic.address.address()
        self.assertTrue(len(result) > 6)

    def test_state(self):
        result = self.generic.address.state()
        self.assertIn(result, self.generic.address.data['state']['name'])

    def test_postal_code(self):
        result = self.generic.address.postal_code()
        if self.generic.address.locale == 'ru':
            self.assertTrue(re.match(r'[0-9]{6}$', result))
        elif self.generic.address.locale == 'is':
            self.assertTrue(re.match(r'[0-9]{3}$', result))
        elif self.generic.address.locale == 'nl':
            nl_pattern = r'^[1-9][0-9]{3}\s?[a-zA-Z]{2}$'
            self.assertTrue(re.match(nl_pattern, result))
        elif self.generic.address.locale == 'pl':
            pl_pattern = r'\d{2}-\d{3}'
            self.assertTrue(re.match(pl_pattern, result))
        elif self.generic.address.locale in ('pt', 'no'):
            self.assertTrue(re.match(r'[0-9]{4}$', result))
        elif self.generic.address.locale == 'da':
            self.assertEqual(result.split('-')[0], 'DK')
            self.assertTrue(re.match(r'[0-9]{4}$', result.split('-')[1]))
        else:
            self.assertTrue(re.match(r'[0-9]{5}$', result))

    def test_country(self):
        result = self.generic.address.country()
        self.assertTrue(self.generic.address.data['country']['name'], result)

        result_iso = self.generic.address.country(iso_code=True)
        self.assertIn(result_iso, common.COUNTRY_ISO_CODE)

    def test_city(self):
        result = self.generic.address.city()
        self.assertIn(result, self.generic.address.data['city'])

    def test_latitude(self):
        result = self.generic.address.latitude()
        self.assertLessEqual(result, 90)

    def test_longitude(self):
        result = self.generic.address.longitude()
        self.assertLessEqual(result, 180)

    def test_coordinates(self):
        result = self.generic.address.coordinates()
        self.assertIsInstance(result, dict)

        latitude = result['latitude']
        self.assertTrue(latitude <= 90)

        longitude = result['longitude']
        self.assertTrue(longitude <= 180)
