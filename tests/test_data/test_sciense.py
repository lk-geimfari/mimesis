# -*- coding: utf-8 -*-

from unittest import TestCase

from elizabeth import Science
import elizabeth.core.interdata as common
from tests.test_data import DummyCase


class ScienceBaseTest(TestCase):
    def setUp(self):
        self.science = Science()

    def tearDown(self):
        del self.science

    def test_math_formula(self):
        result = self.science.math_formula()
        self.assertIn(result, common.MATH_FORMULAS)


class ScienceTestCase(DummyCase):
    def test_scientific_article(self):
        result = self.generic.science.scientific_article()
        self.assertIn(result, self.generic.science._data['article'])

    def test_scientist(self):
        result = self.generic.science.scientist()
        self.assertIn(result, self.generic.science._data['scientist'])

    def test_chemical_element(self):
        result = self.generic.science.chemical_element(name_only=True)
        self.assertTrue(len(result) >= 1)

        result = self.generic.science.chemical_element(name_only=False)
        self.assertIsInstance(result, dict)
