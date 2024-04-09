"""Provides data related to internet."""

import typing as t
import urllib.error
import urllib.parse
import urllib.request
from base64 import b64encode
from ipaddress import IPv4Address, IPv6Address

from mimesis.datasets import (
    CONTENT_ENCODING_DIRECTIVES,
    CORS_OPENER_POLICIES,
    CORS_RESOURCE_POLICIES,
    HTTP_METHODS,
    HTTP_SERVERS,
    HTTP_STATUS_CODES,
    HTTP_STATUS_MSGS,
    PUBLIC_DNS,
    TLD,
    USER_AGENTS,
    USERNAMES,
)
from mimesis.enums import (
    DSNType,
    Locale,
    MimeType,
    PortRange,
    TLDType,
    URLScheme,
)
from mimesis.providers.base import BaseProvider
from mimesis.providers.code import Code
from mimesis.providers.date import Datetime
from mimesis.providers.file import File
from mimesis.providers.text import Text
from mimesis.types import Keywords

__all__ = ["Internet"]


class Internet(BaseProvider):
    """Class for generating data related to the internet."""

    _MAX_IPV4: t.Final[int] = (2**32) - 1
    _MAX_IPV6: t.Final[int] = (2**128) - 1

    def __init__(self, *args: t.Any, **kwargs: t.Any) -> None:
        """Initialize attributes.

        :param args: Arguments.
        :param kwargs: Keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self._file = File(
            seed=self.seed,
            random=self.random,
        )
        self._code = Code(
            seed=self.seed,
            random=self.random,
        )
        self._text = Text(
            locale=Locale.EN,
            seed=self.seed,
            random=self.random,
        )
        self._datetime = Datetime(
            locale=Locale.EN,
            seed=self.seed,
            random=self.random,
        )

    class Meta:
        name = "internet"

    def content_type(self, mime_type: MimeType | None = None) -> str:
        """Generates a random HTTP content type.

        :return: Content type.

        :Example:
            application/json
        """
        return self._file.mime_type(type_=mime_type)

    def dsn(self, dsn_type: DSNType | None = None, **kwargs: t.Any) -> str:
        """Generates a random DSN (Data Source Name).

        :param dsn_type: DSN type.
        :param kwargs: Additional keyword-arguments for hostname method.
        """
        hostname = self.hostname(**kwargs)
        scheme, port = self.validate_enum(dsn_type, DSNType)
        return f"{scheme}://{hostname}:{port}"

    def http_status_message(self) -> str:
        """Generates a random HTTP status message.

        :return: HTTP status message.

        :Example:
            200 OK
        """
        return self.random.choice(HTTP_STATUS_MSGS)

    def http_status_code(self) -> int:
        """Generates a random HTTP status code.

        :return: HTTP status.

        :Example:
            200
        """
        return self.random.choice(HTTP_STATUS_CODES)

    def http_method(self) -> str:
        """Generates a random HTTP method.

        :return: HTTP method.

        :Example:
            POST
        """
        return self.random.choice(HTTP_METHODS)

    def ip_v4_object(self) -> IPv4Address:
        """Generates a random :py:class:`ipaddress.IPv4Address` object.

        :return: :py:class:`ipaddress.IPv4Address` object.
        """
        return IPv4Address(
            self.random.randint(0, self._MAX_IPV4),
        )

    def ip_v4_with_port(self, port_range: PortRange = PortRange.ALL) -> str:
        """Generates a random IPv4 address as string.

        :param port_range: PortRange enum object.
        :return: IPv4 address as string.

        :Example:
            19.121.223.58:8000
        """
        addr = self.ip_v4()
        port = self.port(port_range)
        return f"{addr}:{port}"

    def ip_v4(self) -> str:
        """Generates a random IPv4 address as string.

        :Example:
            19.121.223.58
        """
        return str(self.ip_v4_object())

    def ip_v6_object(self) -> IPv6Address:
        """Generates random :py:class:`ipaddress.IPv6Address` object.

        :return: :py:class:`ipaddress.IPv6Address` object.
        """
        return IPv6Address(
            self.random.randint(
                0,
                self._MAX_IPV6,
            ),
        )

    def ip_v6(self) -> str:
        """Generates a random IPv6 address as string.

        :return: IPv6 address string.

        :Example:
            2001:c244:cf9d:1fb1:c56d:f52c:8a04:94f3
        """
        return str(self.ip_v6_object())

    def mac_address(self) -> str:
        """Generates a random MAC address.

        :return: Random MAC address.

        :Example:
            00:16:3e:25:e7:f1
        """
        mac_hex = [
            0x00,
            0x16,
            0x3E,
            self.random.randint(0x00, 0x7F),
            self.random.randint(0x00, 0xFF),
            self.random.randint(0x00, 0xFF),
        ]
        mac = [f"{x:02x}" for x in mac_hex]
        return ":".join(mac)

    @staticmethod
    def stock_image_url(
        width: int | str = 1920,
        height: int | str = 1080,
        keywords: Keywords | None = None,
    ) -> str:
        """Generates a random stock image URL hosted on Unsplash.

        See «Random search term» on https://source.unsplash.com/
        for more details.

        :param width: Width of the image.
        :param height: Height of the image.
        :param keywords: Sequence of search keywords.
        :return: URL of the image.
        """
        if keywords is not None:
            keywords_str = ",".join(keywords)
        else:
            keywords_str = ""

        return f"https://source.unsplash.com/{width}x{height}?{keywords_str}"

    def hostname(
        self,
        tld_type: TLDType | None = None,
        subdomains: list[str] | None = None,
    ) -> str:
        """Generates a random hostname without a scheme.

        :param tld_type: TLDType.
        :param subdomains: List of subdomains (make sure they are valid).
        :return: Hostname.
        """
        tld = self.tld(tld_type=tld_type)
        host = self.random.choice(USERNAMES)

        if subdomains:
            subdomain = self.random.choice(subdomains)
            host = f"{subdomain}.{host}"

        return f"{host}{tld}"

    def url(
        self,
        scheme: URLScheme | None = URLScheme.HTTPS,
        port_range: PortRange | None = None,
        tld_type: TLDType | None = None,
        subdomains: list[str] | None = None,
    ) -> str:
        """Generates a random URL.

        :param scheme: The scheme.
        :param port_range: PortRange enum object.
        :param tld_type: TLDType.
        :param subdomains: List of subdomains (make sure they are valid).
        :return: URL.
        """
        host = self.hostname(tld_type, subdomains)
        url_scheme = self.validate_enum(scheme, URLScheme)

        url = f"{url_scheme}://{host}"

        if port_range is not None:
            url = f"{url}:{self.port(port_range)}"

        return f"{url}/"

    def uri(
        self,
        scheme: URLScheme | None = URLScheme.HTTPS,
        tld_type: TLDType | None = None,
        subdomains: list[str] | None = None,
        query_params_count: int | None = None,
    ) -> str:
        """Generates a random URI.

        :param scheme: Scheme.
        :param tld_type: TLDType.
        :param subdomains: List of subdomains (make sure they are valid).
        :param query_params_count: Query params.
        :return: URI.
        """
        directory = (
            self._datetime.date(start=2010, end=self._datetime._CURRENT_YEAR)
            .strftime("%Y-%m-%d")
            .replace("-", "/")
        )
        url = self.url(scheme, None, tld_type, subdomains)
        uri = f"{url}{directory}/{self.slug()}"

        if query_params_count:
            uri += f"?{self.query_string(query_params_count)}"

        return uri

    def query_string(self, length: int | None = None) -> str:
        """Generates an arbitrary query string of given length.

        :param length: Length of query string.
        :return: Query string.
        """
        return urllib.parse.urlencode(self.query_parameters(length))

    def query_parameters(self, length: int | None = None) -> dict[str, str]:
        """Generates an arbitrary query parameters as a dict.

        :param length: Length of query parameters dictionary (maximum is 32).
        :return: Dict of query parameters.
        """

        def pick_unique_words(quantity: int = 5) -> list[str]:
            words: set[str] = set()

            while len(words) != quantity:
                words.add(self._text.word())

            return list(words)

        if not length:
            length = self.random.randint(1, 10)

        if length > 32:
            raise ValueError("Maximum allowed length of query parameters is 32.")

        return dict(zip(pick_unique_words(length), self._text.words(length)))

    def top_level_domain(self, tld_type: TLDType = TLDType.CCTLD) -> str:
        """Generates random top level domain.

        :param tld_type: Enum object :class:`enums.TLDType`
        :return: Top level domain.
        :raises NonEnumerableError: if tld_type not in :class:`enums.TLDType`.
        """
        key = self.validate_enum(item=tld_type, enum=TLDType)
        return self.random.choice(TLD[key])

    def tld(self, *args: t.Any, **kwargs: t.Any) -> str:
        """Generates a random TLD.

        An alias for :meth:`top_level_domain`
        """
        return self.top_level_domain(*args, **kwargs)

    def user_agent(self) -> str:
        """Get a random user agent.

        :return: User agent.

        :Example:
            Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0)
            Gecko/20100101 Firefox/15.0.1
        """
        return self.random.choice(USER_AGENTS)

    def port(self, port_range: PortRange = PortRange.ALL) -> int:
        """Generates a random port.

        :param port_range: PortRange enum object.
        :return: Port number.
        :raises NonEnumerableError: if port_range is not in PortRange.

        :Example:
            8080
        """

        rng = self.validate_enum(port_range, PortRange)
        return self.random.randint(*rng)

    def path(self, *args: t.Any, **kwargs: t.Any) -> str:
        """Generates a random path.

        :param args: Arguments to pass to :meth:`slug`.
        :param kwargs: Keyword arguments to pass to :meth:`slug`.
        :return: Path.
        """
        return self.slug(*args, **kwargs).replace("-", "/")

    def slug(self, parts_count: int | None = None) -> str:
        """Generates a random slug of given parts count.

        :param parts_count: Slug's parts count.
        :return: Slug.
        """

        if not parts_count:
            parts_count = self.random.randint(2, 12)

        if parts_count > 12:
            raise ValueError("Slug's parts count must be <= 12")

        if parts_count < 2:
            raise ValueError("Slug must contain more than 2 parts")

        return "-".join(self._text.words(parts_count))

    def public_dns(self) -> str:
        """Generates a random public DNS.

        :Example:
            1.1.1.1
        """
        return self.random.choice(PUBLIC_DNS)

    def http_response_headers(self) -> dict[str, t.Any]:
        """Generates a random HTTP response headers.

        The following headers are included:

        - Allow
        - Age
        - Server
        - Content-Type
        - X-Request-ID
        - Content-Language
        - Content-Location
        - Set-Cookie
        - Upgrade-Insecure-Requests
        - X-Content-Type-Options
        - X-XSS-Protection
        - Connection
        - X-Frame-Options
        - Content-Encoding
        - Cross-Origin-Opener-Policy
        - Cross-Origin-Resource-Policy
        - Strict-Transport-Security

        :return: Response headers as dict.
        """
        max_age = self.random.randint(0, 60 * 60 * 15)
        cookie_attributes = [
            "Secure",
            "HttpOnly",
            "SameSite=Lax",
            "SameSite=Strict",
            f"Max-Age={max_age}",
            f"Domain={self.hostname()}",
        ]
        k, v = self._text.words(quantity=2)
        cookie_attr = self.random.choice(cookie_attributes)
        csrf_token = b64encode(self.random.randbytes(n=32)).decode()
        cookie_value = f"csrftoken={csrf_token}; {k}={v}; {cookie_attr}"

        headers = {
            "Allow": "*",
            "Age": max_age,
            "Server": self.random.choice(HTTP_SERVERS),
            "Content-Type": self._file.mime_type(),
            "X-Request-ID": self.random.randbytes(16).hex(),
            "Content-Language": self._code.locale_code(),
            "Content-Location": self.path(parts_count=4),
            "Set-Cookie": cookie_value,
            "Upgrade-Insecure-Requests": 1,
            "X-Content-Type-Options": "nosniff",
            "X-XSS-Protection": 1,
            "Connection": self.random.choice(["close", "keep-alive"]),
            "X-Frame-Options": self.random.choice(["DENY", "SAMEORIGIN"]),
            "Content-Encoding": self.random.choice(CONTENT_ENCODING_DIRECTIVES),
            "Cross-Origin-Opener-Policy": self.random.choice(CORS_OPENER_POLICIES),
            "Cross-Origin-Resource-Policy": self.random.choice(CORS_RESOURCE_POLICIES),
            "Strict-Transport-Security": f"max-age={max_age}",
        }
        return headers

    def http_request_headers(self) -> dict[str, t.Any]:
        """Generates a random HTTP request headers.

        The following headers are included:

        - Referer
        - Authorization
        - Cookie
        - User-Agent
        - X-CSRF-Token
        - Content-Type
        - Content-Length
        - Connection
        - Cache-Control
        - Accept
        - Host
        - Accept-Language

        :return: Request headers as dict.
        """
        k, v = self._text.words(quantity=2)
        max_age = self.random.randint(0, 60 * 60 * 15)
        token = b64encode(self.random.randbytes(64)).hex()
        csrf_token = b64encode(self.random.randbytes(n=32)).decode()
        headers = {
            "Referer": self.uri(),
            "Authorization": f"Bearer {token}",
            "Cookie": f"csrftoken={csrf_token}; {k}={v}",
            "User-Agent": self.user_agent(),
            "X-CSRF-Token": b64encode(self.random.randbytes(32)).hex(),
            "Content-Type": self._file.mime_type(),
            "Content-Length": self.random.randint(0, 10000),
            "Connection": self.random.choice(["close", "keep-alive"]),
            "Cache-Control": self.random.choice(
                [
                    "no-cache",
                    "no-store",
                    "must-revalidate",
                    "public",
                    "private",
                    f"max-age={max_age}",
                ]
            ),
            "Accept": self.random.choice(
                [
                    "*/*",
                    self._file.mime_type(),
                ]
            ),
            "Host": self.hostname(),
            "Accept-Language": self.random.choice(
                [
                    "*",
                    self._code.locale_code(),
                ]
            ),
        }
        return headers
