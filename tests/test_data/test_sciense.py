# -*- coding: utf-8 -*-

import church._common as common

from tests.test_data import DummyCase


class ScienceTestCase(DummyCase):
    def test_math_formula(self):
        result = self.church.science.math_formula()
        self.assertIn(result, common.MATH_FORMULAS)

    def test_scientific_article(self):
        result = self.church.science.scientific_article()
        self.assertIn(result, self.church.science._data['article'])

    def test_scientist(self):
        result = self.church.science.scientist()
        self.assertIn(result, self.church.science._data['scientist'])

    def test_chemical_element(self):
        result = self.church.science.chemical_element(name_only=True)
        self.assertGreater(len(result), 2)

        _result = self.church.science.chemical_element(name_only=False)
        self.assertIsInstance(_result, dict)
