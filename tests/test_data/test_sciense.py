# -*- coding: utf-8 -*-

from unittest import TestCase

import church._common as common
from church.church import Science
from church.utils import pull

from tests import LANG


class ScienceTestCase(TestCase):
    def setUp(self):
        self.science = Science(LANG)

    def tearDown(self):
        del self.science

    def test_math_formula(self):
        result = self.science.math_formula()
        self.assertIn(result, common.MATH_FORMULAS)

    def test_article_on_wiki(self):
        result = self.science.article_on_wiki()
        parent_file = pull('science_wiki', self.science.lang)
        self.assertIn(result + '\n', parent_file)

    def test_scientist(self):
        result = self.science.scientist()
        parent_file = pull('scientist', self.science.lang)
        self.assertIn(result + '\n', parent_file)

    def test_chemical_element(self):
        result = self.science.chemical_element(name_only=True)
        self.assertGreater(len(result), 2)

        _result = self.science.chemical_element(name_only=False)
        self.assertIsInstance(_result, dict)

