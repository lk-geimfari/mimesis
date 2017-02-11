# -*- coding: utf-8 -*-
import re
from unittest import TestCase

from elizabeth import Text
from tests.test_data import DummyCase

from ._patterns import STR_REGEX


class TextBaseTest(TestCase):
    def setUp(self):
        self.text = Text('en')

    def tearDown(self):
        del self.text

    def test_str(self):
        self.assertTrue(re.match(STR_REGEX, self.text.__str__()))

    def test_hex_color(self):
        result = self.text.hex_color()
        self.assertIn('#', result)

    def test_weather(self):
        result = self.text.weather(scale='c').split(' ')
        temp, scale = float(result[0]), result[1]
        self.assertEqual(scale, '°C')
        self.assertTrue((temp >= -30) and (temp <= 40))

        result = self.text.weather(
            scale='f', minimum=0, maximum=10).split(' ')

        temp, scale = float(result[0]), result[1]
        self.assertEqual(scale, '°F')
        self.assertTrue((temp >= 0) and (temp <= (10 * 1.8) + 32))


class TextTestCase(DummyCase):
    def test_alphabet(self):
        result = self.generic.text.alphabet()
        self.assertIsInstance(result, list)
        self.assertIsNotNone(result)

    def test_sentence(self):
        result = self.generic.text.sentence()
        self.assertIn(result.strip(), self.generic.text.data['text'])

    def test_title(self):
        result = self.generic.text.title()
        self.assertIsNotNone(result)
        self.assertIn(result.strip(), self.generic.text.data['text'])

    def test_text(self):
        result = self.generic.text.text(quantity=4)
        self.assertTrue(len(result) >= 4)
        self.assertIsInstance(result, str)

    def test_words(self):
        result = self.generic.text.words(quantity=5)
        self.assertEqual(len(result), 5)

        result = self.generic.text.words(quantity=1)
        self.assertEqual(len(result), 1)

    def test_word(self):
        result = self.generic.text.word()
        self.assertIn(result, self.generic.text.data['words']['normal'])

    def test_swear_word(self):
        result = self.generic.text.swear_word()
        self.assertIn(result, self.generic.text.data['words']['bad'])

    def test_quote(self):
        result = self.generic.text.quote()
        self.assertIn(result, self.generic.text.data['quotes'])

    def test_color(self):
        result = self.generic.text.color()
        self.assertIn(result, self.generic.text.data['color'])

    def test_level(self):
        result = self.generic.text.level()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
