# -*- coding: utf-8 -*-

import re
from unittest import TestCase

import elizabeth.core.interdata as common
from elizabeth.core.elizabeth import Internet


class InternetSizesTestCase(TestCase):
    def setUp(self):
        self.net = Internet()

    def tearDown(self):
        del self.net

    def test_emoji(self):
        result = self.net.emoji()
        self.assertIn(result, common.EMOJI)

    def test_facebook(self):
        result = self.net.facebook(gender='female')
        self.assertIsNotNone(result)

        _result = self.net.facebook(gender='female')
        self.assertIsNotNone(_result)

    def test_hashtags(self):
        result = self.net.hashtags(quantity=5)
        self.assertEqual(len(result), 5)

        result = self.net.hashtags(quantity=1, category='general')
        self.assertIn(result[0], common.HASHTAGS['general'])

    def test_home_page(self):
        result = self.net.home_page()
        self.assertTrue(re.match(r'http[s]?://(?:[a-zA-Z]|[0-9]|'
                                 r'[$-_@.&+]|[!*\(\),]|'
                                 r'(?:%[0-9a-fA-F][0-9a-fA-F]))+', result))

    def test_subreddit(self):
        result = self.net.subreddit()
        self.assertIn(result, common.SUBREDDITS)

        full_result = self.net.subreddit(full_url=True)
        self.assertTrue(len(full_result) > 20)

        result_nsfw = self.net.subreddit(nsfw=True)
        self.assertIn(result_nsfw, common.SUBREDDITS_NSFW)

        full_result = self.net.subreddit(nsfw=True, full_url=True)
        self.assertTrue(len(full_result) > 20)

    def test_twitter(self):
        result = self.net.twitter(gender='female')
        self.assertIsNotNone(result)

        _result = self.net.twitter(gender='male')
        self.assertIsNotNone(_result)

    def test_user_agent(self):
        result = self.net.user_agent()
        self.assertIn(result, common.USER_AGENTS)
