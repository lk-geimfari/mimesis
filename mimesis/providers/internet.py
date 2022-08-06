"""Provides data related to internet."""

import typing as t
import urllib.error
import urllib.parse
import urllib.request
from ipaddress import IPv4Address, IPv6Address

from mimesis.data import (
    EMOJI,
    HTTP_METHODS,
    HTTP_STATUS_CODES,
    HTTP_STATUS_MSGS,
    PUBLIC_DNS,
    TLD,
    USER_AGENTS,
    USERNAMES,
)
from mimesis.enums import MimeType, PortRange, TLDType, URLScheme
from mimesis.locales import Locale
from mimesis.providers.base import BaseProvider
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
        self._file = File(seed=self.seed)
        self._text = Text(locale=Locale.EN, seed=self.seed)
        self._datetime = Datetime(locale=Locale.EN)

    class Meta:
        """Class for metadata."""

        name: t.Final[str] = "internet"

    def content_type(self, mime_type: t.Optional[MimeType] = None) -> str:
        """Get a random HTTP content type.

        :return: Content type.

        :Example:
            Content-Type: application/json
        """
        fmt = self._file.mime_type(type_=mime_type)
        return f"Content-Type: {fmt}"

    def http_status_message(self) -> str:
        """Get a random HTTP status message.

        :return: HTTP status message.

        :Example:
            200 OK
        """
        return self.random.choice(HTTP_STATUS_MSGS)

    def http_status_code(self) -> int:
        """Get a random HTTP status code.

        :return: HTTP status.

        :Example:
            200
        """
        return self.random.choice(HTTP_STATUS_CODES)

    def http_method(self) -> str:
        """Get a random HTTP method.

        :return: HTTP method.

        :Example:
            POST
        """
        return self.random.choice(HTTP_METHODS)

    def ip_v4_object(self) -> IPv4Address:
        """Generate random :py:class:`ipaddress.IPv4Address` object.

        :return: :py:class:`ipaddress.IPv4Address` object.
        """
        return IPv4Address(
            self.random.randint(0, self._MAX_IPV4),
        )

    def ip_v4_with_port(self, port_range: PortRange = PortRange.ALL) -> str:
        """Generate a random IPv4 address as string.

        :param port_range: PortRange enum object.
        :return: IPv4 address as string.

        :Example:
            19.121.223.58:8000
        """
        addr = self.ip_v4()
        port = self.port(port_range)
        return f"{addr}:{port}"

    def ip_v4(self) -> str:
        """Generate a random IPv4 address as string.

        :Example:
            19.121.223.58
        """
        return str(self.ip_v4_object())

    def ip_v6_object(self) -> IPv6Address:
        """Generate random :py:class:`ipaddress.IPv6Address` object.

        :return: :py:class:`ipaddress.IPv6Address` object.
        """
        return IPv6Address(
            self.random.randint(
                0,
                self._MAX_IPV6,
            ),
        )

    def ip_v6(self) -> str:
        """Generate a random IPv6 address as string.

        :return: IPv6 address string.

        :Example:
            2001:c244:cf9d:1fb1:c56d:f52c:8a04:94f3
        """
        return str(self.ip_v6_object())

    def mac_address(self) -> str:
        """Generate a random MAC address.

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

    def emoji(self) -> str:
        """Get a random emoji shortcut code.

        :return: Emoji code.

        :Example:
            :kissing:
        """
        return self.random.choice(EMOJI)

    @staticmethod
    def stock_image(
        width: t.Union[int, str] = 1920,
        height: t.Union[int, str] = 1080,
        keywords: t.Optional[Keywords] = None,
        writable: bool = False,
    ) -> t.Union[str, bytes]:
        """Generate random stock image (JPG/JPEG) hosted on Unsplash.

        See «Random search term» on https://source.unsplash.com/
        for more details.

        .. note:: This method required an active HTTP connection
            if you want to get a writable object.

        :param width: Width of the image.
        :param height: Height of the image.
        :param keywords: List of search keywords.
        :param writable: Return image as sequence ob bytes.
        :return: Link to the image.
        """
        if keywords is not None:
            keywords_str = ",".join(keywords)
        else:
            keywords_str = ""

        url = f"https://source.unsplash.com/{width}x{height}?{keywords_str}"

        if writable:
            try:
                response = urllib.request.urlopen(url)
                content: bytes = response.read()
                return content
            except urllib.error.URLError:
                raise urllib.error.URLError("Required an active HTTP connection")
        return url

    def hashtags(self, quantity: int = 4) -> t.List[str]:
        """Generate a list of hashtags.

        :param quantity: The quantity of hashtags.
        :return: The list of hashtags.
        :raises NonEnumerableError: if category is not in Hashtag.

        :Example:
            ['#love', '#sky', '#nice']
        """

        if quantity < 1:
            raise ValueError("Quantity must be a positive integer.")

        return ["#" + self._text.word() for _ in range(quantity)]

    def hostname(
        self,
        tld_type: t.Optional[TLDType] = None,
        subdomains: t.Optional[t.List[str]] = None,
    ) -> str:
        """Generate a random hostname without scheme.

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
        scheme: t.Optional[URLScheme] = URLScheme.HTTPS,
        port_range: t.Optional[PortRange] = None,
        tld_type: t.Optional[TLDType] = None,
        subdomains: t.Optional[t.List[str]] = None,
    ) -> str:
        """Generate random URL.

        :param scheme: Scheme.
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
        scheme: t.Optional[URLScheme] = URLScheme.HTTPS,
        tld_type: t.Optional[TLDType] = None,
        subdomains: t.Optional[t.List[str]] = None,
        query_params_count: t.Optional[int] = None,
    ) -> str:
        """Generate a random URI.

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

    def query_string(self, length: t.Optional[int] = None) -> str:
        """Generate arbitrary query string of given length.

        :param length: Length of query string.
        :return: Query string.
        """
        return urllib.parse.urlencode(self.query_parameters(length))

    def query_parameters(self, length: t.Optional[int] = None) -> t.Dict[str, str]:
        """Generate arbitrary query parameters as a dict.

        :param length: Length of query parameters dictionary (maximum is 32).
        :return: Dict of query parameters.
        """

        def pick_unique_words(quantity: int = 5) -> t.List[str]:
            words: t.Set[str] = set()

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
        """Generates random top level domain.

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
        """Generate random port.

        :param port_range: PortRange enum object.
        :return: Port number.
        :raises NonEnumerableError: if port_range is not in PortRange.

        :Example:
            8080
        """

        rng = self.validate_enum(port_range, PortRange)
        return self.random.randint(*rng)

    def slug(self, parts_count: t.Optional[int] = None) -> str:
        """Generate a random slug of given parts count.

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
