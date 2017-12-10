# -*- coding: utf-8 -*-
import re

import pytest

from mimesis import Text

from ._patterns import STR_REGEX


@pytest.fixture
def _text():
    return Text()


@pytest.fixture
def _seeded_text():
    return Text(seed=42)


def test_str(text):
    assert re.match(STR_REGEX, str(text))


def test_hex_color(_text):
    result = _text.hex_color()
    assert '#' in result


def test_seeded_hex_color(_seeded_text):
    result = _seeded_text.hex_color()
    assert result == '#30B4FD'
    result = _seeded_text.hex_color()
    assert result == '#4B1AE8'


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


# def test_seeded_alphabet(_seeded_text):
#     result = _seeded_text.alphabet(lower_case=True)
#     # assert result ==
#     result = _seeded_text.alphabet()
#     # assert result ==
#     result = _seeded_text.alphabet()
#     # assert result ==
#     pass


def test_sentence(text):
    result = text.sentence().strip()
    assert result in text.data['text']


def test_seeded_sentence(_seeded_text):
    result = _seeded_text.sentence()
    assert result == 'Where are my pants?'
    result = _seeded_text.sentence()
    assert result == 'Its main implementation is the Glasgow Haskell Compiler.'


def test_title(text):
    result = text.title()
    assert result is not None
    assert result.strip() in text.data['text']


def test_seeded_title(_seeded_text):
    result = _seeded_text.title()
    assert result == 'Where are my pants?'
    result = _seeded_text.title()
    assert result == 'Its main implementation is the Glasgow Haskell Compiler.'


def test_text(text):
    result = text.text(quantity=4)
    assert len(result) >= 4
    assert isinstance(result, str)


def test_seeded_text(_seeded_text):
    result = _seeded_text.text(quantity=4)
    assert result.endswith('sandwich.')
    result = _seeded_text.text()
    assert result.startswith('Atoms')
    result = _seeded_text.text()
    assert result.startswith('Its main')


def test_words(text):
    result = text.words(quantity=5)
    assert len(result) == 5

    result = text.words(quantity=1)
    assert len(result) == 1


def test_seeded_words(_seeded_text):
    result = _seeded_text.words(quantity=5)
    assert result[0] == 'superior'
    result = _seeded_text.words()
    assert result[1] == 'confirmation'
    result = _seeded_text.words()
    assert result[2] == 'modify'


def test_word(text):
    result = text.word()
    assert result in text.data['words']['normal']


def test_seeded_word(_seeded_text):
    result = _seeded_text.word()
    assert result == 'superior'
    result = _seeded_text.word()
    assert result == 'checking'


def test_swear_word(text):
    result = text.swear_word()
    assert result in text.data['words']['bad']


def test_seeded_swear_word(_seeded_text):
    result = _seeded_text.swear_word()
    assert result == 'Pencil dick'
    result = _seeded_text.swear_word()
    assert result == 'Brain-fart'


def test_quote(text):
    result = text.quote()
    assert result in text.data['quotes']


def test_seeded_quote(_seeded_text):
    result = _seeded_text.quote()
    assert result == 'Here\'s looking at you, kid.'
    result = _seeded_text.quote()
    assert result.endswith('Punk!')


def test_color(text):
    result = text.color()
    assert result in text.data['color']


def test_seeded_color(_seeded_text):
    result = _seeded_text.color()
    assert result == 'Red'
    result = _seeded_text.color()
    assert result == 'Black'


def test_level(text):
    result = text.level()
    assert result is not None
    assert isinstance(result, str)


def test_seeded_level(_seeded_text):
    result = _seeded_text.level()
    assert result == 'critical'
    result = _seeded_text.level()
    assert result == 'low'


def test_answer(text):
    result = text.answer()
    assert result is not None
    assert isinstance(result, str)


def test_seeded_answer(_seeded_text):
    result = _seeded_text.answer()
    assert result == 'Maybe'
    result = _seeded_text.answer()
    assert result == 'Yes'
