# -*- coding: utf-8 -*-
import re

from ._patterns import STR_REGEX


def test_str(text):
    assert re.match(STR_REGEX, str(text))


def test_hex_color(text):
    result = text.hex_color()
    assert '#' in result


def test_alphabet(generic):
    result = generic.text.alphabet()
    assert isinstance(result, list)
    assert result is not None


def test_sentence(generic):
    result = generic.text.sentence()
    assert result.strip() in generic.text.data['text']


def test_title(generic):
    result = generic.text.title()
    assert result is not None
    assert result.strip() in generic.text.data['text']


def test_text(generic):
    result = generic.text.text(quantity=4)
    assert len(result) >= 4
    assert isinstance(result, str)


def test_words(generic):
    result = generic.text.words(quantity=5)
    assert len(result) == 5

    result = generic.text.words(quantity=1)
    assert len(result) == 1


def test_word(generic):
    result = generic.text.word()
    assert result in generic.text.data['words']['normal']


def test_swear_word(generic):
    result = generic.text.swear_word()
    assert result in generic.text.data['words']['bad']


def test_quote(generic):
    result = generic.text.quote()
    assert result in generic.text.data['quotes']


def test_color(generic):
    result = generic.text.color()
    assert result in generic.text.data['color']


def test_level(generic):
    result = generic.text.level()
    assert result is not None
    assert isinstance(result, str)


def test_answer(generic):
    result = generic.text.answer()
    assert result is not None
    assert isinstance(result, str)
