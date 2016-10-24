# -*- coding: utf-8 -*-

from unittest import TestCase

from church import Church


class ChurchTestCase(TestCase):
    def setUp(self):
        self.church = Church('en')

    def test_personal(self):
        result = self.church.personal.username()
        self.assertIsNotNone(result)

    def test_text(self):
        result = self.church.text.words()
        self.assertIsNotNone(result)

    def test_address(self):
        result = self.church.address.address()
        self.assertIsNotNone(result)

    def test_food(self):
        result = self.church.food.fruit_or_berry()
        self.assertIsNotNone(result)

    def test_science(self):
        result = self.church.science.scientist()
        self.assertIsNotNone(result)

    def test_business(self):
        result = self.church.business.copyright()
        self.assertIsNotNone(result)
