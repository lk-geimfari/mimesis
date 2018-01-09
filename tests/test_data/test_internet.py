# -*- coding: utf-8 -*-

import re

import pytest

from mimesis import Internet, data
from mimesis.enums import Layer, MimeType, PortRange, TLDType
from mimesis.exceptions import NonEnumerableError

from . import _patterns as p


@pytest.fixture
def net():
    return Internet()


def test_emoji(net):
    result = net.emoji()
    assert result in data.EMOJI


def test_hashtags(net):
    result = net.hashtags(quantity=5)
    assert len(result) == 5

    result = net.hashtags(quantity=1)
    assert result.replace('#', '') in data.HASHTAGS


def test_home_page(net):
    result = net.home_page()
    assert re.match(p.HOME_PAGE, result)


def test_subreddit(net):
    result = net.subreddit()
    assert result in data.SUBREDDITS

    full_result = net.subreddit(full_url=True)
    assert len(full_result) > 20

    result_nsfw = net.subreddit(nsfw=True)
    assert result_nsfw in data.SUBREDDITS_NSFW

    full_result = net.subreddit(nsfw=True, full_url=True)
    assert len(full_result) > 20


def test_user_agent(net):
    result = net.user_agent()
    assert result in data.USER_AGENTS


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
        Layer.APPLICATION,
        Layer.DATA_LINK,
        Layer.NETWORK,
        Layer.PHYSICAL,
        Layer.PRESENTATION,
        Layer.SESSION,
        Layer.TRANSPORT,
    ],
)
def test_network_protocol(net, layer):
    result = net.network_protocol(layer=layer)
    assert result in data.NETWORK_PROTOCOLS[layer.value]


def test_network_protocol_exception(net):
    with pytest.raises(NonEnumerableError):
        net.network_protocol(layer='nil')


def test_ip_v4(net):
    ip = net.ip_v4()
    assert re.match(p.IP_V4_REGEX, ip)

    ip_with_port = net.ip_v4(with_port=True)
    port = int(ip_with_port.split(':')[1])

    assert (port >= 1) and (port <= 65535)


def test_ip_v6(net):
    ip = net.ip_v6()
    assert re.match(p.IP_V6_REGEX, ip)


def test_mac_address(net):
    mac = net.mac_address()
    assert re.match(p.MAC_ADDRESS_REGEX, mac)


def test_http_method(net):
    result = net.http_method()
    assert result in data.HTTP_METHODS


@pytest.mark.parametrize(
    'mime_type', [
        MimeType.APPLICATION,
        MimeType.AUDIO,
        MimeType.IMAGE,
        MimeType.MESSAGE,
        MimeType.TEXT,
        MimeType.VIDEO,
    ],
)
def test_content_type(net, mime_type):
    ct = net.content_type(mime_type=mime_type)
    ct = ct.split(':')[1].strip()
    assert ct in data.MIME_TYPES[mime_type.value]


def test_content_type_wrong_arg(net):
    with pytest.raises(NonEnumerableError):
        net.content_type(mime_type='nil')


def test_http_status_code(net):
    result = net.http_status_code()
    assert (int(result) >= 100) and (int(result) <= 511)


def test_http_status_message(net):
    result = net.http_status_message()
    assert result in data.HTTP_STATUS_MSGS


@pytest.mark.parametrize(
    'domain_type', [
        TLDType.CCTLD,
        TLDType.GTLD,
        TLDType.GEOTLD,
        TLDType.UTLD,
        TLDType.STLD,
    ],
)
def test_top_level_domain(net, domain_type):
    result = net.top_level_domain(tld_type=domain_type)
    assert result is not None
    assert result in data.TLD[domain_type.value]


def test_top_level_domain_unsupported(net):
    with pytest.raises(NonEnumerableError):
        net.top_level_domain(tld_type='nil')


@pytest.mark.parametrize(
    'range_, excepted', [
        (PortRange.ALL, (1, 65535)),
        (PortRange.EPHEMERAL, (49152, 65535)),
        (PortRange.REGISTERED, (1024, 49151)),
    ],
)
def test_port(net, range_, excepted):
    result = net.port(port_range=range_)
    assert (result >= excepted[0]) and (result <= excepted[1])

    with pytest.raises(NonEnumerableError):
        net.port('nill')


def test_torrent_portal_category(net):
    result = net.category_of_website()
    assert result in data.TORRENT_CATEGORIES
