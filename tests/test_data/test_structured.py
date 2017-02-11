# -*- coding: utf-8 -*-
import json
import re

from elizabeth.core.providers import Structured
from unittest import TestCase

from elizabeth.core.intd import HTML_CONTAINER_TAGS
from ._patterns import STR_REGEX


class StructuredBaseTest(TestCase):
    def setUp(self):
        self.structured = Structured('en')

    def tearDown(self):
        del self.structured

    def depth(self, x):
        """Calculates depth of object."""
        if isinstance(x, dict) and x:
            return 1 + max(self.depth(x[a]) for a in x)
        if isinstance(x, list) and x:
            return 1 + max(self.depth(a) for a in x)
        return 0

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
            HTML_CONTAINER_TAGS['div']['class'] = "bogus"
            from elizabeth.core.providers import Structured
            Structured('en').html_attribute_value("div", "class")

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
