# -*- coding: utf-8 -*-
import json
import re

import pytest

from mimesis import Structured

from ._patterns import STR_REGEX


@pytest.fixture
def _structured():
    return Structured()


@pytest.fixture
def _seeded_structured():
    return Structured(seed=42)


def test_str(_structured):
    assert re.match(STR_REGEX, str(_structured))


def depth(x):
    """Calculates depth of object."""
    if isinstance(x, dict) and x:
        return 1 + max(depth(x[a]) for a in x)
    if isinstance(x, list) and x:
        return 1 + max(depth(a) for a in x)
    return 0


def test_css(_structured):
    result = _structured.css()
    assert isinstance(result, str)  # returns string
    assert ':' in result  # contains property assignments
    assert result[-1] == '}'  # closed at end
    assert result.split(' ')[1][0] == '{'  # opened after selector


def test_seeded_css(_seeded_structured):
    result = _seeded_structured.css()
    assert result == 'a {color: #30B4FD; position: absolute}'
    result = _seeded_structured.css()
    assert result == 'span {display: block}'


def test_css_property(_structured):
    result = _structured.css_property()
    assert len(result.split(' ')) == 2  # contains one property assignment
    assert ':' in result  # contains any property assignments


def test_seeded_css_property(_seeded_structured):
    result = _seeded_structured.css_property()
    assert result == 'pointer: crosshair'
    result = _seeded_structured.css_property()
    assert result == 'background-color: #30B4FD'


def test_html_attribute_value(_structured):
    result = _structured.html_attribute_value('a', 'href')
    assert result[0:4] == 'http'
    with pytest.raises(NotImplementedError):
        _structured.html_attribute_value('a', 'bogus')


# TODO: https://github.com/lk-geimfari/mimesis/issues/325#issuecomment-352364359
def skip_test_seeded_html_attribute_value(_seeded_structured):
    result = _seeded_structured.html_attribute_value('a', 'href')
    assert result == 'http://www.imagining.as'
    result = _seeded_structured.html_attribute_value('div', 'class')
    assert result == 'superior'


def test_html(_structured):
    result = _structured.html()
    assert result[0] == '<'  # tag is enclosed
    assert result[-1] == '>'  # tag is enclosed


def test_seeded_html(_seeded_structured):
    result = _seeded_structured.html()
    assert result.startswith('<a id="superior">')
    result = _seeded_structured.html()
    assert result == '<div class="amd">Make me a sandwich.</div>'


def test_json(_structured):
    result = _structured.json(items=3, max_depth=4)
    assert isinstance(result, str)

    # Is valid json and root element is container with three items
    data = json.loads(result)
    assert isinstance(data, (dict, list))
    assert len(data) == 3

    # Recursive returns python object, not JSON and
    # maximum depth of three elements
    result = _structured.json(items=3, max_depth=4, recursive=True)
    assert isinstance(result, (dict, list))
    assert depth(result) <= 4


def test_seeded_json(_seeded_structured):
    result = _seeded_structured.json(items=3, max_depth=2, recursive=True)
    assert 0.7415504997598329 in result
    result = _seeded_structured.json()
    assert json.loads(result)['prove'] == 'Where are my pants?'
    result = _seeded_structured.json()
    assert json.loads(result)['guinea'] == 'Make me a sandwich.'
