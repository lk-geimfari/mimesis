import re
from ipaddress import IPv4Address, IPv6Address

import pytest
import validators

from mimesis import Internet, data
from mimesis.enums import MimeType, PortRange, TLDType, URLScheme
from mimesis.exceptions import NonEnumerableError

from . import patterns


class TestInternet:
    @pytest.fixture
    def net(self):
        return Internet()

    def test_str(self, net):
        assert re.match(patterns.PROVIDER_STR_REGEX, str(net))

    def test_emoji(self, net):
        result = net.emoji()
        assert result in data.EMOJI

    def test_hashtags(self, net):
        result = net.hashtags(quantity=5)
        assert len(result) == 5

        with pytest.raises(ValueError):
            net.hashtags(quantity=0)

        with pytest.raises(ValueError):
            net.hashtags(quantity=-1)

    @pytest.mark.parametrize(
        "subdomains",
        [
            [],
            ["app", "core", "api"],
            ["dev", "prod", "test"],
            ["admin", "smtp", "pop3"],
        ],
    )
    def test_hostname(self, net, subdomains):
        hostname = net.hostname(subdomains=subdomains)
        subdomain, *_ = hostname.split(".", 1)

        if subdomains:
            assert subdomain in subdomains

    @pytest.mark.parametrize(
        "scheme",
        (
            URLScheme.HTTP,
            URLScheme.HTTPS,
            URLScheme.FTP,
            URLScheme.SFTP,
            URLScheme.WS,
            URLScheme.WSS,
        ),
    )
    def test_url(self, net, scheme):
        result = net.url(scheme=scheme)
        assert result.startswith(scheme.value)

    @pytest.mark.parametrize(
        "port",
        (
            PortRange.ALL,
            PortRange.WELL_KNOWN,
            PortRange.EPHEMERAL,
            PortRange.REGISTERED,
        ),
    )
    def test_url_with_port(self, net, port):
        url = net.url(port_range=port)
        port_val = int(url.split(":")[-1].replace("/", ""))
        port_start, port_end = port.value
        assert port_start <= port_val <= port_end

    def test_default(self, net):
        uri = net.uri()
        assert uri.startswith(URLScheme.HTTPS.value)

    @pytest.mark.repeat(10)
    @pytest.mark.parametrize(
        "scheme, tld_type, subdomains, query_params_count",
        [
            (
                URLScheme.HTTPS,
                TLDType.GTLD,
                ["core", "app", "test", "dev"],
                5,
            ),
        ],
    )
    def test_uri_with_parameters(
        self, net, scheme, tld_type, subdomains, query_params_count
    ):
        uri = net.uri(
            scheme=scheme,
            tld_type=tld_type,
            subdomains=subdomains,
            query_params_count=query_params_count,
        )
        assert uri.split(":")[0].strip() == scheme.value
        assert validators.url(uri)

    @pytest.mark.repeat(10)
    @pytest.mark.parametrize("length", [5, 10, 15])
    def test_query_string(self, net, length):
        assert len(net.query_string(length).split("&")) == length

    def test_query_string_raise_error_on_invalid_length(self, net):
        with pytest.raises(ValueError):
            net.query_string(33)

    def test_query_string_with_length_of_none(self, net):
        query_params_count = len(net.query_string().split("&"))
        assert 1 <= query_params_count <= 10

    @pytest.mark.repeat(10)
    @pytest.mark.parametrize("length", [5, 10, 15])
    def test_query_parameters(self, net, length):
        assert len(net.query_parameters(length)) == length

    def test_query_parameters_raise_error_on_invalid_length(self, net):
        with pytest.raises(ValueError):
            net.query_parameters(33)

    def test_query_parameters_with_length_of_none(self, net):
        query_params_count = len(net.query_parameters())
        assert 1 <= query_params_count <= 10

    def test_slug(self, net):
        with pytest.raises(ValueError):
            net.slug(parts_count=13)

        with pytest.raises(ValueError):
            net.slug(parts_count=1)

        parts_count = 5
        parts = net.slug(parts_count=parts_count).split("-")
        assert len(parts) == parts_count

    def test_path(self, net):
        with pytest.raises(ValueError):
            net.path(parts_count=13)

        with pytest.raises(ValueError):
            net.path(parts_count=1)

        parts_count = 5
        parts = net.path(parts_count=parts_count).split("/")
        assert len(parts) == parts_count

    def test_user_agent(self, net):
        result = net.user_agent()
        assert result in data.USER_AGENTS

    @pytest.mark.parametrize(
        "w, h, keywords",
        [
            (900, 900, ["octopus", "mimicry"]),
            (800, 800, {"octopus", "mimicry"}),
            (800, 800, None),
        ],
    )
    def test_stock_image_url(self, net, w, h, keywords):
        result = net.stock_image_url(
            width=w,
            height=h,
            keywords=keywords,
        )
        assert isinstance(result, str)
        assert re.match(patterns.STOCK_IMAGE, result)
        assert result.endswith("?" + ",".join(keywords or []))

    def test_ip_v4_object(self, net):
        ip = net.ip_v4_object()
        assert ip.version == 4
        assert ip.max_prefixlen == 32
        assert re.match(patterns.IP_V4_REGEX, ip.exploded)
        assert isinstance(ip, IPv4Address)

    def test_ip_v4(
        self,
        net,
    ):
        assert re.match(patterns.IP_V4_REGEX, net.ip_v4())

    @pytest.mark.parametrize(
        "port_range",
        [
            PortRange.ALL,
            PortRange.WELL_KNOWN,
            PortRange.EPHEMERAL,
            PortRange.REGISTERED,
        ],
    )
    def test_ip_v4_with_port(self, net, port_range):
        ip = net.ip_v4_with_port(port_range)
        port = int(ip.split(":")[-1])
        port_start, port_end = port_range.value
        assert port_start <= port <= port_end

    def test_ip_v6_object(self, net):
        ip = net.ip_v6_object()
        assert ip.version == 6
        assert ip.max_prefixlen == 128
        assert re.match(patterns.IP_V6_REGEX, ip.exploded)
        assert isinstance(ip, IPv6Address)

    def test_ip_v6(self, net):
        ip = net.ip_v6()
        assert re.match(patterns.IP_V6_REGEX, ip)

    def test_mac_address(self, net):
        mac = net.mac_address()
        assert re.match(patterns.MAC_ADDRESS_REGEX, mac)

    def test_http_method(self, net):
        result = net.http_method()
        assert result in data.HTTP_METHODS

    @pytest.mark.parametrize(
        "mime_type",
        [
            MimeType.APPLICATION,
            MimeType.AUDIO,
            MimeType.IMAGE,
            MimeType.MESSAGE,
            MimeType.TEXT,
            MimeType.VIDEO,
        ],
    )
    def test_content_type(self, net, mime_type):
        ct = net.content_type(mime_type=mime_type)
        assert ct in data.MIME_TYPES[mime_type.value]

    def test_content_type_wrong_arg(self, net):
        with pytest.raises(NonEnumerableError):
            net.content_type(mime_type="nil")

    def test_http_status_code(self, net):
        result = net.http_status_code()
        assert (int(result) >= 100) and (int(result) <= 511)

    def test_http_status_message(self, net):
        result = net.http_status_message()
        assert result in data.HTTP_STATUS_MSGS

    @pytest.mark.parametrize(
        "domain_type",
        [
            TLDType.CCTLD,
            TLDType.GTLD,
            TLDType.GEOTLD,
            TLDType.UTLD,
            TLDType.STLD,
        ],
    )
    def test_top_level_domain(self, net, domain_type):
        res_a = net.top_level_domain(tld_type=domain_type)
        res_b = net.tld(tld_type=domain_type)
        assert res_a in data.TLD[domain_type.value]
        assert res_b in data.TLD[domain_type.value]

    def test_top_level_domain_unsupported(self, net):
        with pytest.raises(NonEnumerableError):
            net.top_level_domain(tld_type="nil")

    @pytest.mark.parametrize(
        "port_range, excepted",
        [
            (PortRange.ALL, (1, 65535)),
            (PortRange.EPHEMERAL, (49152, 65535)),
            (PortRange.REGISTERED, (1024, 49151)),
        ],
    )
    def test_port(self, net, port_range, excepted):
        result = net.port(port_range=port_range)
        assert (result >= excepted[0]) and (result <= excepted[1])

        with pytest.raises(NonEnumerableError):
            net.port("nil")

    def test_public_dns(self, net):
        assert net.public_dns() in data.PUBLIC_DNS

    def test_http_response_headers(self, net):
        result = net.http_response_headers()
        assert isinstance(result, dict)
        assert result["Allow"] == "*"

    def test_http_request_headers(self, net):
        result = net.http_request_headers()
        assert isinstance(result, dict)
        assert result["Cookie"].startswith("csrftoken")


class TestSeededInternet:
    @pytest.fixture
    def i1(self, seed):
        return Internet(seed=seed)

    @pytest.fixture
    def i2(self, seed):
        return Internet(seed=seed)

    def test_http_request_headers(self, i1, i2):
        r1 = i1.http_request_headers()
        r2 = i2.http_request_headers()

        for key, val in r1.items():
            assert r2[key] == val

    def test_http_response_headers(self, i1, i2):
        r1 = i1.http_response_headers()
        r2 = i2.http_response_headers()

        for key, val in r1.items():
            assert r2[key] == val

    def test_emoji(self, i1, i2):
        assert i1.emoji() == i2.emoji()

    def test_hashtags(self, i1, i2):
        assert i1.hashtags() == i2.hashtags()
        assert i1.hashtags(quantity=7) == i2.hashtags(quantity=7)

    def test_hostname(self, i1, i2):
        assert i1.hostname() == i2.hostname()
        assert i1.hostname(subdomains=["app", "core", "api"]) == i2.hostname(
            subdomains=["app", "core", "api"]
        )

    def test_url(self, i1, i2):
        assert i1.url() == i2.url()
        assert i1.url(tld_type=TLDType.GEOTLD) == i2.url(tld_type=TLDType.GEOTLD)

    def test_user_agent(self, i1, i2):
        assert i1.user_agent() == i2.user_agent()

    def test_ip_v4(self, i1, i2):
        assert i1.ip_v4() == i2.ip_v4()

    def test_ip_v4_with_port(self, i1, i2):
        assert i1.ip_v4_with_port(port_range=PortRange.ALL) == i2.ip_v4_with_port(
            port_range=PortRange.ALL
        )

    def test_ip_v4_object(self, i1, i2):
        assert i1.ip_v4_object() == i2.ip_v4_object()

    def test_ip_v6(self, i1, i2):
        assert i1.ip_v6() == i2.ip_v6()

    def test_slug(self, i1, i2):
        assert i1.slug(parts_count=2) == i2.slug(parts_count=2)

    def test_path(self, i1, i2):
        assert i1.path(parts_count=2) == i2.path(parts_count=2)

    def test_query_string(self, i1, i2):
        assert i1.query_string(length=2) == i2.query_string(length=2)
        assert i1.query_string(length=None) == i2.query_string(length=None)

    def test_query_parameters(self, i1, i2):
        assert i1.query_parameters(length=2) == i2.query_parameters(length=2)
        assert i1.query_parameters(length=None) == i2.query_parameters(length=None)

    def test_ip_v6_object(self, i1, i2):
        assert i1.ip_v6_object() == i2.ip_v6_object()

    def test_mac_address(self, i1, i2):
        assert i1.mac_address() == i2.mac_address()

    def test_http_method(self, i1, i2):
        assert i1.http_method() == i2.http_method()

    def test_content_type(self, i1, i2):
        assert i1.content_type() == i2.content_type()
        assert i1.content_type(mime_type=MimeType.APPLICATION) == i2.content_type(
            mime_type=MimeType.APPLICATION
        )

    def test_http_status_code(self, i1, i2):
        assert i1.http_status_code() == i2.http_status_code()

    def test_http_status_message(self, i1, i2):
        assert i1.http_status_message() == i2.http_status_message()

    def test_top_level_domain(self, i1, i2):
        assert i1.top_level_domain() == i2.top_level_domain()
        assert i1.top_level_domain(tld_type=TLDType.UTLD) == i2.top_level_domain(
            tld_type=TLDType.UTLD
        )

    def test_port(self, i1, i2):
        assert i1.port() == i2.port()
        assert i1.port(port_range=PortRange.REGISTERED) == i2.port(
            port_range=PortRange.REGISTERED
        )

    def test_public_dns(self, i1, i2):
        assert i1.public_dns() == i2.public_dns()
