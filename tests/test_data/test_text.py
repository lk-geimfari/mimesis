# -*- coding: utf-8 -*-

from unittest import TestCase

from church.church import Text
from church import _common as common
from church.utils import pull

from tests import LANG


class TextTestCase(TestCase):
    def setUp(self):
        self.data = Text(LANG)

    def tearDown(self):
        del self.data

    def test_sentence(self):
        result = self.data.sentence() + '\n'
        parent_file = pull('text', self.data.lang)
        self.assertIn(result, parent_file)

    def test_title(self):
        result = self.data.title() + '\n'
        parent_file = pull('text', self.data.lang)
        self.assertIn(result, parent_file)

    def test_lorem_ipsum(self):
        result = self.data.lorem_ipsum(quantity=2)
        self.assertIsNot(result, None)
        self.assertIsInstance(result, str)

    def test_words(self):
        result = self.data.words()
        self.assertEqual(len(result), 5)

        result = self.data.words(quantity=1)
        self.assertEqual(len(result), 1)

    def test_word(self):
        result = self.data.word()
        parent_file = pull('words', self.data.lang)
        self.assertIn(result + '\n', parent_file)

    def test_swear_word(self):
        result = self.data.swear_word()
        parent_file = pull('swear_words', self.data.lang)
        self.assertIn(result + '\n', parent_file)

    def test_naughty_strings(self):
        result = self.data.naughty_strings()
        self.assertTrue(len(result) > 10)
        self.assertIsInstance(result, list)

    def test_quote_from_movie(self):
        result = self.data.quote()
        parent_file = pull('quotes', self.data.lang)
        self.assertIn(result + '\n', parent_file)

    def test_color(self):
        result = self.data.color()
        parent_file = pull('colors', self.data.lang)
        self.assertIn(result + '\n', parent_file)

    def test_hex_color(self):
        result = self.data.hex_color()
        self.assertIn('#', result)

    def test_emoji(self):
        result = self.data.emoji()
        self.assertIn(result, common.EMOJI)

    def test_hashtags(self):
        result = self.data.hashtags(quantity=5)
        self.assertEqual(len(result), 5)

        result = self.data.hashtags(quantity=1, category='general')
        self.assertIn(result[0], common.HASHTAGS['general'])

    def test_weather(self):
        result = self.data.weather(scale='c').split(' ')
        temp, scale = float(result[0]), result[1]
        self.assertEqual(scale, '°C')
        self.assertTrue((temp >= -30) and (temp <= 40))

        result = self.data.weather(scale='f', a=0, b=10).split(' ')
        temp, scale = float(result[0]), result[1]
        self.assertEqual(scale, '°F')
        self.assertTrue((temp >= 0) and (temp <= (10 * 1.8) + 32))
