# -*- coding: utf-8 -*-

import elizabeth._common as common

from tests.test_data import DummyCase


class ScienceTestCase(DummyCase):
    def test_math_formula(self):
        result = self.generic.science.math_formula()
        self.assertIn(result, common.MATH_FORMULAS)

    def test_scientific_article(self):
        result = self.generic.science.scientific_article()
        self.assertIn(result, self.generic.science._data['article'])

    def test_scientist(self):
        result = self.generic.science.scientist()
        self.assertIn(result, self.generic.science._data['scientist'])

    def test_chemical_element(self):
        result = self.generic.science.chemical_element(name_only=True)
        self.assertGreater(len(result), 2)

        _result = self.generic.science.chemical_element(name_only=False)
        self.assertIsInstance(_result, dict)
