# -*- coding: utf-8 -*-

from unittest import TestCase

from elizabeth.core.elizabeth import ClothingSizes


class ClothingSizesTestCase(TestCase):
    def setUp(self):
        self.sizes = ClothingSizes()

    def tearDown(self):
        del self.sizes

    def test_international(self):
        sizes = ("L", "M", "S",
                 "XL", "XS", "XXL",
                 "XXS", "XXXL"
                 )
        result = self.sizes.international()
        self.assertIn(result, sizes)

    def test_eur(self):
        result = self.sizes.european()
        self.assertTrue((result >= 40) and (result <= 62))

    def test_custom(self):
        result = self.sizes.custom(minimum=40, maximum=62)
        self.assertTrue((result >= 40) and (result <= 62))

        result_even = self.sizes.custom(even=True)
        self.assertTrue(result_even % 2 == 0)
