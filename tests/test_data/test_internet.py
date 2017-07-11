# -*- coding: utf-8 -*-

import re

import pytest

from elizabeth.data.int import (
    SUBREDDITS, EMOJI, USER_AGENTS,
    SUBREDDITS_NSFW, HASHTAGS,
    HTTP_METHODS, MIME_TYPES,
    HTTP_STATUS_CODES,
    NETWORK_PROTOCOLS,
)
from elizabeth.exceptions import WrongArgument
from elizabeth.providers.internet import Internet
from tests.test_data._patterns import (
    HOME_PAGE,
    IP_V6_REGEX,
    IP_V4_REGEX,
    MAC_ADDRESS_REGEX,
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

    tags = list(HASHTAGS.keys())

    for category in tags:
        result = net.hashtags(quantity=1, category=category)
        assert result in HASHTAGS[category]

    with pytest.raises(KeyError):
        net.hashtags(category='religious')


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


def test_network_protocol(net):
    # Default layer 'is application'

    layers = list(NETWORK_PROTOCOLS.keys())

    for layer in layers:
        result = net.network_protocol(layer=layer)
        assert result in NETWORK_PROTOCOLS[layer]

    with pytest.raises(WrongArgument):
        net.network_protocol(layer='super')


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
    types = list(MIME_TYPES.keys())

    for typ in types:
        ct = net.content_type(mime_type=typ)
        ct = ct.split(':')[1].strip()
        assert ct in MIME_TYPES[typ]

    with pytest.raises(ValueError):
        net.content_type(mime_type='blablabla')


def test_http_status_code(net):
    result = net.http_status_code(code_only=False)
    assert result in HTTP_STATUS_CODES

    result = net.http_status_code()
    assert (int(result) >= 100) and (int(result) <= 511)
