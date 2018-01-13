# -*- coding: utf-8 -*-
import re

import pytest

from mimesis import Text

from ..conftest import seed
from ._patterns import HEX_COLOR, STR_REGEX


class TestText(object):
    @pytest.fixture
    def _text(self):
        return Text()

    def test_str(self, text):
        assert re.match(STR_REGEX, str(text))

    def test_hex_color(self, _text):
        result = _text.hex_color()
        assert re.match(HEX_COLOR, result)

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
    TIMES = 5

    @pytest.fixture
    def _texts(self):
        return Text(seed=seed), Text(seed=seed)

    def test_hex_color(self, _texts):
        t1, t2 = _texts
        for _ in range(self.TIMES):
            assert t1.hex_color() == t2.hex_color()

    def test_alphabet(self, _texts):
        t1, t2 = _texts
        for _ in range(self.TIMES):
            assert t1.alphabet() == t2.alphabet()
            assert t1.alphabet(lower_case=True) == t2.alphabet(lower_case=True)

    def test_sentence(self, _texts):
        t1, t2 = _texts
        for _ in range(self.TIMES):
            assert t1.sentence() == t2.sentence()

    def test_title(self, _texts):
        t1, t2 = _texts
        for _ in range(self.TIMES):
            assert t1.title() == t2.title()

    def test_text(self, _texts):
        t1, t2 = _texts
        for _ in range(self.TIMES):
            assert t1.text() == t2.text()
            assert t1.text(quantity=1) == t2.text(quantity=1)

    def test_words(self, _texts):
        t1, t2 = _texts
        for _ in range(self.TIMES):
            assert t1.words() == t2.words()
            assert t1.words(quantity=1) == t2.words(quantity=1)

    def test_word(self, _texts):
        t1, t2 = _texts
        for _ in range(self.TIMES):
            assert t1.word() == t2.word()

    def test_swear_word(self, _texts):
        t1, t2 = _texts
        for _ in range(self.TIMES):
            assert t1.swear_word() == t2.swear_word()

    def test_quote(self, _texts):
        t1, t2 = _texts
        for _ in range(self.TIMES):
            assert t1.quote() == t2.quote()

    def test_color(self, _texts):
        t1, t2 = _texts
        for _ in range(self.TIMES):
            assert t1.color() == t2.color()

    def test_level(self, _texts):
        t1, t2 = _texts
        for _ in range(self.TIMES):
            assert t1.level() == t2.level()

    def test_answer(self, _texts):
        t1, t2 = _texts
        for _ in range(self.TIMES):
            assert t1.answer() == t2.answer()
