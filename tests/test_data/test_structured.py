# -*- coding: utf-8 -*-
import re
import csv

from elizabeth.core.providers import Structured
from unittest import TestCase

from elizabeth.core import interdata as common
from ._patterns import STR_REGEX


class StructuredBaseTest(TestCase):
    def setUp(self):
        self.structured = Structured('en')

    def tearDown(self):
        del self.structured

    def test_str(self):
        self.assertTrue(re.match(STR_REGEX, self.structured.__str__()))

    def test_css(self):
        result = self.structured.css()
        self.assertIsInstance(result, str)  # returns string
        self.assertIn(":", result)  # contains property assignments
        self.assertEqual(result[-1], "}")  # closed at end
        self.assertEqual(result.split(" ")[1][0], "{")  # opened after selector

    def test_css_property(self):
        result = self.structured.css_property()
        self.assertEqual(len(result.split(" ")), 2)  # contains one property assignment
        self.assertIn(":", result)  # contains any property assignments

    def test_html_attribute_value(self):
        result = self.structured.html_attribute_value("a", "href")
        self.assertEqual(result[0:4], "http")
        with self.assertRaises(NotImplementedError):
            self.structured.html_attribute_value("a", "bogus")
        with self.assertRaises(NotImplementedError):
            common.HTML_CONTAINER_TAGS['div']['class'] = "bogus"
            from elizabeth.core.providers import Structured
            Structured('en').html_attribute_value("div", "class")

    def test_html(self):
        result = self.structured.html()
        self.assertEqual(result[0], "<")  # tag is enclosed
        self.assertEqual(result[-1], ">")  # tag is enclosed
