# -*- coding: utf-8 -*-

import array
from unittest import TestCase

from elizabeth.core.providers import Numbers


class NumbersTest(TestCase):
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
        self.assertEqual(len(result), 499)
        self.assertIsInstance(result, array.array)

        result = self.numbers.primes(to_list=True)
        self.assertEqual(len(result), 499)
        self.assertIsInstance(result, list)

    def test_digit(self):
        digits = (
            0, 1, 2,
            3, 4, 5,
            6, 7, 8,
            9
        )
        result = self.numbers.digit()
        self.assertIn(result, digits)

        result = self.numbers.digit(to_bin=True)
        self.assertIsInstance(result, str)

    def test_between(self):
        result = self.numbers.between(90, 100)
        self.assertTrue((result >= 90) and (result <= 100))
