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


@pytest.fixture
def _seeded_net():
    return Internet(seed=42)


def test_emoji(net):
    result = net.emoji()
    assert result in data.EMOJI


def test_seeded_emoji(_seeded_net):
    result = _seeded_net.emoji()
    assert result == ':hotsprings:'
    result = _seeded_net.emoji()
    assert result == ':clap:'


def test_hashtags(net):
    result = net.hashtags(quantity=5)
    assert len(result) == 5

    result = net.hashtags(quantity=1)
    assert result.replace('#', '') in data.HASHTAGS


def test_seeded_hashtags(_seeded_net):
    result = _seeded_net.hashtags(quantity=2)
    assert result == ['#familyfun', '#beautiful']
    result = _seeded_net.hashtags()
    assert result[0] == '#instagramanet'
    result = _seeded_net.hashtags()
    assert result[0] == '#family1st'


def test_home_page(net):
    result = net.home_page()
    assert re.match(p.HOME_PAGE, result)


def test_seeded_home_page(_seeded_net):
    result = _seeded_net.home_page(tld_type=TLDType.GEOTLD)
    assert result == 'http://www.imagining.bar'
    result = _seeded_net.home_page()
    assert result == 'http://www.afterfuture.catalonia'
    result = _seeded_net.home_page()
    assert result == 'http://www.boons.company'


def test_subreddit(net):
    result = net.subreddit()
    assert result in data.SUBREDDITS

    full_result = net.subreddit(full_url=True)
    assert len(full_result) > 20

    result_nsfw = net.subreddit(nsfw=True)
    assert result_nsfw in data.SUBREDDITS_NSFW

    full_result = net.subreddit(nsfw=True, full_url=True)
    assert len(full_result) > 20


def test_seeded_subreddit(_seeded_net):
    result = _seeded_net.subreddit(nsfw=True, full_url=True)
    assert result == 'http://www.reddit.com/r/distension'
    result = _seeded_net.subreddit()
    assert result == '/r/DoesAnybodyElse'
    result = _seeded_net.subreddit()
    assert result == '/r/4chan'


def test_user_agent(net):
    result = net.user_agent()
    assert result in data.USER_AGENTS


def test_seeded_user_agent(_seeded_net):
    result = _seeded_net.user_agent()
    assert result.startswith('Mozilla/5.0 (Windows')
    result = _seeded_net.user_agent()
    assert result.startswith('Mozilla/5.0 (Linux')


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


def test_seeded_stock_image(_seeded_net):
    result = _seeded_net.stock_image(category='space', width=800, height=600)
    assert result == 'https://source.unsplash.com/category/space/800x600'
    result = _seeded_net.stock_image()
    assert result.endswith('objects/1900x1080')
    result = _seeded_net.stock_image()
    assert result.endswith('buildings/1900x1080')


def test_image_by_keyword(net):
    result = net.image_by_keyword(keyword='word').split('/')[-1]
    assert 'word' == result.split('?')[1]

    default = net.image_by_keyword()
    assert isinstance(default, str)


def test_seeded_image_by_keyword(_seeded_net):
    result = _seeded_net.image_by_keyword(keyword='word')
    assert result == 'https://source.unsplash.com/weekly?word'
    result = _seeded_net.image_by_keyword()
    assert result == 'https://source.unsplash.com/weekly?girl'
    result = _seeded_net.image_by_keyword()
    assert result == 'https://source.unsplash.com/weekly?cat'


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


def test_seeded_network_protocol(_seeded_net):
    result = _seeded_net.network_protocol(layer=Layer.TRANSPORT)
    assert result == 'TCP'
    result = _seeded_net.network_protocol()
    assert result == 'AFP'
    result = _seeded_net.network_protocol()
    assert result == 'PPTP'


def test_network_protocol_exception(net):
    with pytest.raises(NonEnumerableError):
        net.network_protocol(layer='nil')


def test_ip_v4(net):
    ip = net.ip_v4()
    assert re.match(p.IP_V4_REGEX, ip)

    ip_with_port = net.ip_v4(with_port=True)
    port = int(ip_with_port.split(':')[1])

    assert (port >= 1) and (port <= 65535)


def test_seeded_ip_v4(_seeded_net):
    result = _seeded_net.ip_v4(with_port=True)
    assert result == '57.12.140.125:14629'
    result = _seeded_net.ip_v4()
    assert result == '71.52.44.216'
    result = _seeded_net.ip_v4()
    assert result == '16.15.47.111'


def test_ip_v6(net):
    ip = net.ip_v6()
    assert re.match(p.IP_V6_REGEX, ip)


def test_seeded_ip_v6(_seeded_net):
    result = _seeded_net.ip_v6()
    assert result == '2001:3900:cce:8cd0:7d62:7248:4771:347a'
    result = _seeded_net.ip_v6()
    assert result == '2001:2c83:d806:1045:f41:2ff8:6ff1:771f'


def test_mac_address(net):
    mac = net.mac_address()
    assert re.match(p.MAC_ADDRESS_REGEX, mac)


def test_seeded_mac_address(_seeded_net):
    result = _seeded_net.mac_address()
    assert result == '00:16:3e:1c:0c:8c'
    result = _seeded_net.mac_address()
    assert result == '00:16:3e:3e:72:47'


def test_http_method(net):
    result = net.http_method()
    assert result in data.HTTP_METHODS


def test_seeded_http_method(_seeded_net):
    result = _seeded_net.http_method()
    assert result == 'GET'
    result = _seeded_net.http_method()
    assert result == 'GET'
    result = _seeded_net.http_method()
    assert result == 'PUT'


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


def test_seeded_content_type(_seeded_net):
    result = _seeded_net.content_type(mime_type=MimeType.MESSAGE)
    assert result == 'Content-Type: message/vnd.wfa.wsc'
    result = _seeded_net.content_type()
    assert result == 'Content-Type: application/conference-info+xml'
    result = _seeded_net.content_type()
    assert result == 'Content-Type: video/raw'


def test_content_type_wrong_arg(net):
    with pytest.raises(NonEnumerableError):
        net.content_type(mime_type='nil')


def test_http_status_code(net):
    result = net.http_status_code(code_only=False)
    assert result in data.HTTP_STATUS_CODES

    result = net.http_status_code()
    assert (int(result) >= 100) and (int(result) <= 511)


def test_seeded_http_status_code(_seeded_net):
    result = _seeded_net.http_status_code(code_only=False)
    assert result == '429 Too Many Requests'
    result = _seeded_net.http_status_code()
    assert result == '205'
    result = _seeded_net.http_status_code()
    assert result == '101'


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


def test_seeded_top_level_domain(_seeded_net):
    result = _seeded_net.top_level_domain(tld_type=TLDType.CCTLD)
    assert result == '.cz'
    result = _seeded_net.top_level_domain()
    assert result == '.ly'
    result = _seeded_net.top_level_domain()
    assert result == '.gop'


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


def test_seeded_port(_seeded_net):
    result = _seeded_net.port(port_range=PortRange.REGISTERED)
    assert result == 42929
    result = _seeded_net.port()
    assert result == 7297
    result = _seeded_net.port()
    assert result == 1640


def test_torrent_portal_category(net):
    result = net.category_of_website()
    assert result in data.TORRENT_CATEGORIES


def test_seeded_category_of_website(_seeded_net):
    result = _seeded_net.category_of_website()
    assert result == 'Porn/Movies DVDR'
    result = _seeded_net.category_of_website()
    assert result == 'Applications/UNIX'
