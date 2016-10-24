# -*- coding: utf-8 -*-

import array
from unittest import TestCase

from church.church import Numbers


class NumbersTestCase(TestCase):
    def setUp(self):
        self.numbers = Numbers()

    def tearDown(self):
        del self.numbers

    def test_floats(self):
        result = self.numbers.floats()
        self.assertEqual(len(result), 100)
        self.assertIsInstance(result, array.array)

        result = self.numbers.floats(n=3, to_list=True)
        self.assertEqual(len(result), 1000)
        self.assertIsInstance(result, list)

    def test_primes(self):
        result = self.numbers.primes()
        self.assertEqual(len(result), 50)
        self.assertIsInstance(result, array.array)

        result = self.numbers.primes(n=3, to_list=True)
        self.assertEqual(len(result), 500)
        self.assertIsInstance(result, list)
