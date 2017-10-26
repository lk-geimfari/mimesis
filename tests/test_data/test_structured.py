# -*- coding: utf-8 -*-
import json
import re

import pytest

from ._patterns import STR_REGEX


def test_str(structured):
    assert re.match(STR_REGEX, str(structured))


def depth(x):
    """Calculates depth of object."""
    if isinstance(x, dict) and x:
        return 1 + max(depth(x[a]) for a in x)
    if isinstance(x, list) and x:
        return 1 + max(depth(a) for a in x)
    return 0


def test_css(structured):
    result = structured.css()
    assert isinstance(result, str)  # returns string
    assert ':' in result  # contains property assignments
    assert result[-1] == '}'  # closed at end
    assert result.split(' ')[1][0] == '{'  # opened after selector


def test_css_property(structured):
    result = structured.css_property()
    assert len(result.split(' ')) == 2  # contains one property assignment
    assert ':' in result  # contains any property assignments


def test_html_attribute_value(structured):
    result = structured.html_attribute_value('a', 'href')
    assert result[0:4] == 'http'
    with pytest.raises(NotImplementedError):
        structured.html_attribute_value('a', 'bogus')


def test_html(structured):
    result = structured.html()
    assert result[0] == '<'  # tag is enclosed
    assert result[-1] == '>'  # tag is enclosed


def test_json(structured):
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
    assert depth(result) <= 4
