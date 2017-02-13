# -*- coding: utf-8 -*-

import re
from unittest import TestCase

from elizabeth.core.providers import Internet
from elizabeth.core.intd import (
    SUBREDDITS, EMOJI, USER_AGENTS,
    SUBREDDITS_NSFW, HASHTAGS
)


class InternetTest(TestCase):
    def setUp(self):
        self.net = Internet()

    def tearDown(self):
        del self.net

    def test_emoji(self):
        result = self.net.emoji()
        self.assertIn(result, EMOJI)

    def test_facebook(self):
        result = self.net.facebook(gender='female')
        self.assertIsNotNone(result)

        _result = self.net.facebook(gender='female')
        self.assertIsNotNone(_result)

    def test_hashtags(self):
        result = self.net.hashtags(quantity=5)
        self.assertEqual(len(result), 5)

        result = self.net.hashtags(quantity=1, category='general')
        self.assertIn(result[0], HASHTAGS['general'])

    def test_home_page(self):
        result = self.net.home_page()
        self.assertTrue(re.match(r'http[s]?://(?:[a-zA-Z]|[0-9]|'
                                 r'[$_@.&+-]|[!*\(\),]|'
                                 r'(?:%[0-9a-fA-F][0-9a-fA-F]))+', result))

    def test_subreddit(self):
        result = self.net.subreddit()
        self.assertIn(result, SUBREDDITS)

        full_result = self.net.subreddit(full_url=True)
        self.assertTrue(len(full_result) > 20)

        result_nsfw = self.net.subreddit(nsfw=True)
        self.assertIn(result_nsfw, SUBREDDITS_NSFW)

        full_result = self.net.subreddit(nsfw=True, full_url=True)
        self.assertTrue(len(full_result) > 20)

    def test_twitter(self):
        result = self.net.twitter(gender='female')
        self.assertIsNotNone(result)

        _result = self.net.twitter(gender='male')
        self.assertIsNotNone(_result)

    def test_user_agent(self):
        result = self.net.user_agent()
        self.assertIn(result, USER_AGENTS)

    def test_image_placeholder(self):
        result = self.net.image_placeholder(width=400, height=300)
        self.assertIsNotNone(result)

    def test_stock_image(self):
        result = self.net.stock_image()
        self.assertIsNotNone(result)

        result_2 = self.net.stock_image(category='nature').split('/')[-2]
        self.assertEqual(result_2, 'nature')

        result_3 = self.net.stock_image(width=1900, height=1080).split('/')[-1]
        self.assertEqual(result_3, '1900x1080')

    def test_image_by_keyword(self):
        result = self.net.image_by_keyword(keyword='word').split('/')[-1]
        self.assertEqual('word', result.split('?')[1])
