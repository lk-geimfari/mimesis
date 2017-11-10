# -*- coding: utf-8 -*-
import re

import pytest

import mimesis

from ._patterns import STR_REGEX


@pytest.fixture
def _text():
    return mimesis.Text()


def test_str(text):
    assert re.match(STR_REGEX, str(text))


def test_hex_color(_text):
    result = _text.hex_color()
    assert '#' in result


@pytest.mark.parametrize(
    'case', [
        True,
        False,
    ],
)
def test_alphabet(text, case):
    result = text.alphabet(lower_case=case)
    assert result is not None
    assert isinstance(result, list)


def test_sentence(text):
    result = text.sentence().strip()
    assert result in text.data['text']


def test_title(text):
    result = text.title()
    assert result is not None
    assert result.strip() in text.data['text']


def test_text(text):
    result = text.text(quantity=4)
    assert len(result) >= 4
    assert isinstance(result, str)


def test_words(text):
    result = text.words(quantity=5)
    assert len(result) == 5

    result = text.words(quantity=1)
    assert len(result) == 1


def test_word(text):
    result = text.word()
    assert result in text.data['words']['normal']


def test_swear_word(text):
    result = text.swear_word()
    assert result in text.data['words']['bad']


def test_quote(text):
    result = text.quote()
    assert result in text.data['quotes']


def test_color(text):
    result = text.color()
    assert result in text.data['color']


def test_level(text):
    result = text.level()
    assert result is not None
    assert isinstance(result, str)


def test_answer(text):
    result = text.answer()
    assert result is not None
    assert isinstance(result, str)
