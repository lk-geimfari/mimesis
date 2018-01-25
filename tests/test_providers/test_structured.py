# -*- coding: utf-8 -*-
import json
import re

import pytest

from mimesis import Structured

from ._patterns import STR_REGEX


class TestStructured(object):

    @pytest.fixture
    def structured(self):
        return Structured()

    def test_str(self, structured):
        assert re.match(STR_REGEX, str(structured))

    def depth(self, x):
        """Calculates depth of object."""
        if isinstance(x, dict) and x:
            return 1 + max(self.depth(x[a]) for a in x)
        if isinstance(x, list) and x:
            return 1 + max(self.depth(a) for a in x)
        return 0

    def test_css(self, structured):
        result = structured.css()
        assert isinstance(result, str)  # returns string
        assert ':' in result  # contains property assignments
        assert result[-1] == '}'  # closed at end
        assert result.split(' ')[1][0] == '{'  # opened after selector

    def test_css_property(self, structured):
        result = structured.css_property()
        assert len(result.split(' ')) == 2  # contains one property assignment
        assert ':' in result  # contains any property assignments

    def test_html_attribute_value(self, structured):
        result = structured.html_attribute_value('a', 'href')
        assert result[0:4] == 'http'
        with pytest.raises(NotImplementedError):
            structured.html_attribute_value('a', 'bogus')

    def test_html(self, structured):
        result = structured.html()
        assert result[0] == '<'  # tag is enclosed
        assert result[-1] == '>'  # tag is enclosed

    def test_json(self, structured):
        result = structured.json(items=3, max_depth=4)
        assert isinstance(result, str)

        # Is valid json and root element is container with three items
        data = json.loads(result)
        assert isinstance(data, (dict, list))
        assert len(data) == 3

        # Recursive returns python object, not JSON and
        # maximum depth of three elements
        result = structured.json(items=3, max_depth=4, recursive=True)
        assert isinstance(result, (dict, list))
        assert self.depth(result) <= 4


class TestSeededStructured(object):

    @pytest.fixture
    def s1(self, seed):
        return Structured(seed=seed)

    @pytest.fixture
    def s2(self, seed):
        return Structured(seed=seed)

    def test_css(self, s1, s2):
        assert s1.css() == s2.css()

    def test_css_property(self, s1, s2):
        assert s1.css_property() == s2.css_property()

    def test_html_attribute_value(self, s1, s2):
        assert s1.html_attribute_value() == s2.html_attribute_value()
        assert s1.html_attribute_value(tag='p', attribute='class') == \
            s2.html_attribute_value(tag='p', attribute='class')

    def test_html(self, s1, s2):
        assert s1.html() == s2.html()

    def test_json(self, s1, s2):
        assert s1.json() == s2.json()
        assert s1.json(items=2, max_depth=4, recursive=True) == \
            s2.json(items=2, max_depth=4, recursive=True)
