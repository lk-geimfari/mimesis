# -*- coding: utf-8 -*-

import re

import pytest

from elizabeth.core.providers import Internet
from elizabeth.intd import (
    SUBREDDITS, EMOJI, USER_AGENTS,
    SUBREDDITS_NSFW, HASHTAGS,
    HTTP_METHODS, MIME_TYPES,
    HTTP_STATUS_CODES
)
from ._patterns import (
    HOME_PAGE,
    IP_V6_REGEX,
    IP_V4_REGEX,
    MAC_ADDRESS_REGEX
)


@pytest.fixture
def net():
    return Internet()


def test_emoji(net):
    result = net.emoji()
    assert result in EMOJI


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


def test_ip_v4(net):
    ip = net.ip_v4()
    assert re.match(IP_V4_REGEX, ip)


def test_ip_v6(net):
    ip = net.ip_v6()
    assert re.match(IP_V6_REGEX, ip)


def test_mac_address(net):
    mac = net.mac_address()
    assert re.match(MAC_ADDRESS_REGEX, mac)


def test_http_method(net):
    result = net.http_method()
    assert result in HTTP_METHODS


def test_content_type(net):
    result = net.content_type().split(':')
    result = result[1].strip()
    assert result in MIME_TYPES


def test_http_status_code(net):
    result = net.http_status_code()
    assert result in HTTP_STATUS_CODES
