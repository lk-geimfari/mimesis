# -*- coding: utf-8 -*-

import re

from tests.test_data import DummyCase


class AddressTestCase(DummyCase):
    def test_street_number(self):
        result = self.church.address.street_number()
        self.assertTrue(re.match(r'[0-9]{1,5}$', result))

    def test_street_name(self):
        result = self.church.address.street_name()
        self.assertIn(result, self.church.address.data['street']['name'])

    def test_street_suffix(self):
        result = self.church.address.street_suffix()
        self.assertIn(result, self.church.address.data['street']['suffix'])

    def test_address(self):
        result = self.church.address.address()
        self.assertTrue(len(result) > 6)

    def test_state(self):
        result = self.church.address.state()
        self.assertIn(result, self.church.address.data['state']['name'])

    def test_postal_code(self):
        result = self.church.address.postal_code()
        if self.church.address.lang == 'ru':
            self.assertTrue(re.match(r'[0-9]{6}$', str(result)))
        else:
            self.assertTrue(re.match(r'[0-9]{5}$', str(result)))

    def test_country(self):
        result = self.church.address.country()
        self.assertTrue(self.church.address.data['country']['name'], result)

        result2 = self.church.address.country(iso_code=True)
        self.assertTrue(self.church.address.data['country']['iso_code'],
                        result2)

    def test_city(self):
        result = self.church.address.city()
        self.assertIn(result, self.church.address.data['city'])

    def test_latitude(self):
        result = self.church.address.latitude()
        self.assertLessEqual(result, 90)

    def test_longitude(self):
        result = self.church.address.longitude()
        self.assertLessEqual(result, 180)

    def test_coordinates(self):
        result = self.church.address.coordinates()
        self.assertIsInstance(result, dict)

        latitude = result['latitude']
        self.assertTrue(latitude <= 90)

        longitude = result['longitude']
        self.assertTrue(longitude <= 180)
