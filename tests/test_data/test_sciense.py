# -*- coding: utf-8 -*-

from unittest import TestCase

import church._common as common
from church.church import Science
from church.utils import pull

from tests import LANG


class ScienceTestCase(TestCase):
    def setUp(self):
        self.science = Science(LANG)
        self.db = self.science._data

    def tearDown(self):
        del self.science

    def test_math_formula(self):
        result = self.science.math_formula()
        self.assertIn(result, common.MATH_FORMULAS)

    def test_scientific_article(self):
        result = self.science.scientific_article()
        self.assertIn(result, self.db['article'])

    def test_scientist(self):
        result = self.science.scientist()
        self.assertIn(result, self.db['scientist'])

    def test_chemical_element(self):
        result = self.science.chemical_element(name_only=True)
        self.assertGreater(len(result), 2)

        _result = self.science.chemical_element(name_only=False)
        self.assertIsInstance(_result, dict)

