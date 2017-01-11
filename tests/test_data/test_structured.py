# -*- coding: utf-8 -*-
import csv
import json

from elizabeth.core.elizabeth import Structured
from unittest import TestCase

from elizabeth.core import interdata as common

class StructuredBaseTest(TestCase):
    def setUp(self):
        self.structured = Structured()

    def tearDown(self):
        del self.structured

    def depth(self, x):
        """Calculates depth of object."""
        if isinstance(x, dict) and x:
            return 1 + max(self.depth(x[a]) for a in x)
        if isinstance(x, list) and x:
            return 1 + max(self.depth(a) for a in x)
        return 0

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
        with self.assertRaises(NotImplementedError):
            common.HTML_CONTAINER_TAGS['div']['class'] = "bogus"
            from elizabeth.core.elizabeth import Structured
            Structured().html_attribute_value("div", "class")

    def test_html(self):
        result = self.structured.html()
        self.assertEqual(result[0], "<")  # tag is enclosed
        self.assertEqual(result[-1], ">") # tag is enclosed

    def test_json(self):
        result = self.structured.json(items=3, max_depth=4)
        self.assertIsInstance(result, str)  # returns str
        data = json.loads(result)  # is valid JSON
        self.assertIsInstance(data, (dict, list))  # root element is container
        self.assertEqual(len(data), 3)  # root container has three items
        r = self.structured.json(items=3, max_depth=4, _recursive=True)
        self.assertIsInstance(r, (dict, list))  # recursive returns python object, not JSON
        self.assertLessEqual(self.depth(r), 4)  # maximum depth of three elements


