# -*- coding: utf-8 -*-

from unittest import TestCase

from church import _common as common
from church.church import Text
from tests import LANG


class TextTestCase(TestCase):
    def setUp(self):
        self.text = Text(LANG)
        self.db = self.text.data

    def tearDown(self):
        del self.text

    def test_sentence(self):
        result = self.text.sentence()
        self.assertIn(result.strip(), self.db['text'])

    def test_title(self):
        result = self.text.title()
        self.assertIn(result.strip(), self.db['text'])

    def test_lorem_ipsum(self):
        result = self.text.lorem_ipsum(quantity=4)
        self.assertTrue(len(result) >= 4)
        self.assertIsInstance(result, str)

    def test_words(self):
        result = self.text.words(quantity=5)
        self.assertEqual(len(result), 5)

        result = self.text.words(quantity=1)
        self.assertEqual(len(result), 1)

    def test_word(self):
        result = self.text.word()
        self.assertIn(result, self.db['words']['normal'])

    def test_swear_word(self):
        result = self.text.swear_word()
        self.assertIn(result, self.db['words']['bad'])

    def test_naughty_strings(self):
        result = self.text.naughty_strings()
        self.assertTrue(len(result) > 10)
        self.assertIsInstance(result, list)

    def test_quote(self):
        result = self.text.quote()
        self.assertIn(result, self.db['quotes'])

    def test_color(self):
        result = self.text.color()
        self.assertIn(result, self.db['color'])

    def test_hex_color(self):
        result = self.text.hex_color()
        self.assertIn('#', result)

    def test_emoji(self):
        result = self.text.emoji()
        self.assertIn(result, common.EMOJI)

    def test_hashtags(self):
        result = self.text.hashtags(quantity=5)
        self.assertEqual(len(result), 5)

        result = self.text.hashtags(quantity=1, category='general')
        self.assertIn(result[0], common.HASHTAGS['general'])

    def test_weather(self):
        result = self.text.weather(scale='c').split(' ')
        temp, scale = float(result[0]), result[1]
        self.assertEqual(scale, '°C')
        self.assertTrue((temp >= -30) and (temp <= 40))

        result = self.text.weather(scale='f', a=0, b=10).split(' ')
        temp, scale = float(result[0]), result[1]
        self.assertEqual(scale, '°F')
        self.assertTrue((temp >= 0) and (temp <= (10 * 1.8) + 32))
