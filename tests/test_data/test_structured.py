# -*- coding: utf-8 -*-
import csv

from elizabeth.core.elizabeth import Structured
from unittest import TestCase


class StructuredBaseTest(TestCase):
    def setUp(self):
        self.structured = Structured()

    def tearDown(self):
        del self.structured

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

    def test_delimited(self):
        result = self.structured.delimited(lines=5, cols=3, delimiter="\x14", quotechar="\xfe")[:-1]
        self.assertIn("\x14", result)  # contains delimiter
        self.assertIn("\xfe", result)  # contains quotechar
        rows = 0
        reader = csv.reader(result.split("\n"), delimiter="\x14", quotechar="\xfe")
        for row in reader:
            rows += 1
            self.assertEqual(len(row), 3)  # row contains three columns
        self.assertEqual(rows, 6)  # 5 lines plus header

    def test_html_attribute_value(self):
        result = self.structured.html_attribute_value("a", "href")
        self.assertEqual(result[0:4], "http")
        with self.assertRaises(NotImplementedError):
            self.structured.html_attribute_value("a", "bogus")

    def test_html(self):
        result = self.structured.html()
        self.assertEqual(result[0], "<")  # tag is enclosed
        self.assertEqual(result[-1], ">") # tag is enclosed
