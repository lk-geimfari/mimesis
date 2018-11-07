# -*- coding: utf-8 -*-
import re

import pytest

from mimesis import Text
from mimesis.data import SAFE_COLORS

from . import patterns


class TestText(object):

    @pytest.fixture
    def _text(self):
        return Text()

    def test_str(self, text):
        assert re.match(patterns.DATA_PROVIDER_STR_REGEX, str(text))

    def test_hex_to_rgb(self, _text):
        color = _text.hex_color()
        rgb = _text._hex_to_rgb(color)
        assert isinstance(rgb, tuple)

    @pytest.mark.parametrize(
        'safe', [
            True,
            False,
        ],
    )
    def test_hex_color(self, _text, safe):
        result = _text.hex_color(safe=safe)
        assert re.match(patterns.HEX_COLOR, result)
        assert result in SAFE_COLORS if safe else result

    @pytest.mark.parametrize(
        'safe', [
            True,
            False,
        ],
    )
    def test_rgb_color(self, _text, safe):
        result = _text.rgb_color(safe=safe)
        assert isinstance(result, tuple)

    @pytest.mark.parametrize(
        'case', [
            True,
            False,
        ],
    )
    def test_alphabet(self, text, case):
        result = text.alphabet(lower_case=case)
        assert result is not None
        assert isinstance(result, list)

    def test_sentence(self, text):
        result = text.sentence().strip()
        assert result in text._data['text']

    def test_title(self, text):
        result = text.title()
        assert result is not None
        assert result.strip() in text._data['text']

    def test_text(self, text):
        result = text.text(quantity=4)
        assert len(result) >= 4
        assert isinstance(result, str)

    def test_words(self, text):
        result = text.words(quantity=5)
        assert len(result) == 5

        result = text.words(quantity=1)
        assert len(result) == 1

    def test_word(self, text):
        result = text.word()
        assert result in text._data['words']['normal']

    def test_swear_word(self, text):
        result = text.swear_word()
        assert result in text._data['words']['bad']

    def test_quote(self, text):
        result = text.quote()
        assert result in text._data['quotes']

    def test_color(self, text):
        result = text.color()
        assert result in text._data['color']

    def test_level(self, text):
        result = text.level()
        assert result is not None
        assert isinstance(result, str)

    def test_answer(self, text):
        result = text.answer()
        assert result is not None
        assert isinstance(result, str)


class TestSeededText(object):

    @pytest.fixture
    def t1(self, seed):
        return Text(seed=seed)

    @pytest.fixture
    def t2(self, seed):
        return Text(seed=seed)

    def test_hex_color(self, t1, t2):
        assert t1.hex_color() == t2.hex_color()
        assert t1.hex_color(safe=True) == t2.hex_color(safe=True)

    def test_rgb_color(self, t1, t2):
        assert t1.rgb_color() == t2.rgb_color()
        assert t1.rgb_color(safe=True) == t2.rgb_color(safe=True)

    def test_alphabet(self, t1, t2):
        assert t1.alphabet() == t2.alphabet()
        assert t1.alphabet(lower_case=True) == t2.alphabet(lower_case=True)

    def test_sentence(self, t1, t2):
        assert t1.sentence() == t2.sentence()

    def test_title(self, t1, t2):
        assert t1.title() == t2.title()

    def test_text(self, t1, t2):
        assert t1.text() == t2.text()
        assert t1.text(quantity=1) == t2.text(quantity=1)

    def test_words(self, t1, t2):
        assert t1.words() == t2.words()
        assert t1.words(quantity=1) == t2.words(quantity=1)

    def test_word(self, t1, t2):
        assert t1.word() == t2.word()

    def test_swear_word(self, t1, t2):
        assert t1.swear_word() == t2.swear_word()

    def test_quote(self, t1, t2):
        assert t1.quote() == t2.quote()

    def test_color(self, t1, t2):
        assert t1.color() == t2.color()

    def test_level(self, t1, t2):
        assert t1.level() == t2.level()

    def test_answer(self, t1, t2):
        assert t1.answer() == t2.answer()
