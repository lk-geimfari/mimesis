# -*- coding: utf-8 -*-

import re

import pytest

from mimesis.data import (EMOJI, HASHTAGS, HTTP_METHODS, HTTP_STATUS_CODES,
                          MIME_TYPES, NETWORK_PROTOCOLS, SUBREDDITS,
                          SUBREDDITS_NSFW, USER_AGENTS)
from mimesis.exceptions import WrongArgument

from . import _patterns as p


def test_emoji(net):
    result = net.emoji()
    assert result in EMOJI


@pytest.mark.parametrize(
    'category', [
        'boys',
        'cars',
        'family',
        'friends',
        'general',
        'girls',
        'love',
        'nature',
        'sport',
        'travel',
        'tumblr',
    ],
)
def test_hashtags(net, category):
    result = net.hashtags(quantity=5)
    assert len(result) == 5

    result = net.hashtags(quantity=1, category=category)
    assert result in HASHTAGS[category]

    with pytest.raises(KeyError):
        net.hashtags(category='religious')


def test_home_page(net):
    result = net.home_page()
    assert re.match(p.HOME_PAGE, result)


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


@pytest.mark.parametrize(
    'layer', [
        'application',
        'data_link',
        'network',
        'physical',
        'presentation',
        'session',
        'transport',
    ],
)
def test_network_protocol(net, layer):
    result = net.network_protocol(layer=layer)
    assert result in NETWORK_PROTOCOLS[layer]


def test_network_protocol_wrong(net):
    with pytest.raises(WrongArgument):
        net.network_protocol(layer='super')


def test_ip_v4(net):
    ip = net.ip_v4()
    assert re.match(p.IP_V4_REGEX, ip)


def test_ip_v6(net):
    ip = net.ip_v6()
    assert re.match(p.IP_V6_REGEX, ip)


def test_mac_address(net):
    mac = net.mac_address()
    assert re.match(p.MAC_ADDRESS_REGEX, mac)


def test_http_method(net):
    result = net.http_method()
    assert result in HTTP_METHODS


@pytest.mark.parametrize(
    'mime_type', [
        'application',
        'audio',
        'image',
        'message',
        'text',
        'video',
    ],
)
def test_content_type(net, mime_type):
    ct = net.content_type(mime_type=mime_type)
    ct = ct.split(':')[1].strip()
    assert ct in MIME_TYPES[mime_type]


def test_content_type_wrong_arg(net):
    with pytest.raises(ValueError):
        net.content_type(mime_type='blablabla')


def test_http_status_code(net):
    result = net.http_status_code(code_only=False)
    assert result in HTTP_STATUS_CODES

    result = net.http_status_code()
    assert (int(result) >= 100) and (int(result) <= 511)
