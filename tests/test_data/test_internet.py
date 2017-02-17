# -*- coding: utf-8 -*-

import pytest
import re

from elizabeth.core.providers import Internet
from elizabeth.core.intd import (
    SUBREDDITS, EMOJI, USER_AGENTS,
    SUBREDDITS_NSFW, HASHTAGS
)

from ._patterns import HOME_PAGE


@pytest.fixture
def net():
    return Internet()


def test_emoji(net):
    result = net.emoji()
    assert result in EMOJI


def test_facebook(net):
    result = net.facebook(gender='female')
    assert result is not None

    _result = net.facebook(gender='female')
    assert _result is not None


def test_hashtags(net):
    result = net.hashtags(quantity=5)
    assert len(result) == 5

    result = net.hashtags(quantity=1, category='general')
    assert result[0] in HASHTAGS['general']


def test_home_page(net):
    result = net.home_page()
    assert re.match(HOME_PAGE, result)


def test_subreddit(net):
    result = net.subreddit()
    assert result in SUBREDDITS

    full_result = net.subreddit(full_url=True)
    assert len(full_result) > 20

    result_nsfw = net.subreddit(nsfw=True)
    assert result_nsfw in SUBREDDITS_NSFW

    full_result = net.subreddit(nsfw=True, full_url=True)
    assert len(full_result) > 20


def test_twitter(net):
    result = net.twitter(gender='female')
    assert result is not None

    _result = net.twitter(gender='male')
    assert _result is not None


def test_user_agent(net):
    result = net.user_agent()
    assert result in USER_AGENTS


def test_image_placeholder(net):
    result = net.image_placeholder(width=400, height=300)
    assert result is not None


def test_stock_image(net):
    result = net.stock_image()
    assert result is not None

    result_2 = net.stock_image(category='nature').split('/')[-2]
    assert result_2 == 'nature'

    result_3 = net.stock_image(width=1900, height=1080).split('/')[-1]
    assert result_3 == '1900x1080'


def test_image_by_keyword(net):
    result = net.image_by_keyword(keyword='word').split('/')[-1]
    assert 'word' == result.split('?')[1]

    default = net.image_by_keyword()
    assert isinstance(default, str)


def test_protocol(net):
    result = net.protocol()
    assert result is not None
    assert result in ['http', 'https']
