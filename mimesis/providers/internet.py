# -*- coding: utf-8 -*-

"""Provides data related to internet."""

import urllib.error
import urllib.request
from ipaddress import IPv4Address, IPv6Address
from typing import List, Optional, Union

from mimesis.data import (
    EMOJI,
    HASHTAGS,
    HTTP_METHODS,
    HTTP_STATUS_CODES,
    HTTP_STATUS_MSGS,
    NETWORK_PROTOCOLS,
    TLD,
    USER_AGENTS,
    USERNAMES,
)
from mimesis.enums import Layer, MimeType, PortRange, TLDType
from mimesis.exceptions import NonEnumerableError
from mimesis.providers.base import BaseProvider
from mimesis.providers.file import File

__all__ = ['Internet']


class Internet(BaseProvider):
    """Class for generating data related to the internet."""

    def __init__(self, *args, **kwargs):
        """Initialize attributes.

        :param args: Arguments.
        :param kwargs: Keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.__file = File(seed=self.seed)
        self._MAX_IPV4 = (2 ** 32) - 1
        self._MAX_IPV6 = (2 ** 128) - 1

    class Meta:
        """Class for metadata."""

        name = 'internet'

    def content_type(self, mime_type: Optional[MimeType] = None) -> str:
        """Get a random HTTP content type.

        :return: Content type.

        :Example:
            Content-Type: application/json
        """
        fmt = self.__file.mime_type(type_=mime_type)
        return 'Content-Type: {}'.format(fmt)

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
        """Generate random IPv4Address object.

        See documentation for module ipaddress:
        https://docs.python.org/3.7/library/ipaddress.html

        :return: IPv4Address object.
        """
        return IPv4Address(
            self.random.randint(0, self._MAX_IPV4),
        )

    def ip_v4(self, with_port: bool = False,
              port_range: PortRange = PortRange.ALL) -> str:
        """Generate a random IPv4 address as string.

        :param port_range: PortRange enum object.
        :param with_port: Add port from PortRange to IP.
        :return: IPv4 address as string.

        :Example:
            19.121.223.58 or 19.121.223.58:8000
        """
        ip = str(self.ip_v4_object())

        if with_port:
            port = self.port(port_range=port_range)
            return '{}:{}'.format(ip, port)

        return ip

    def ip_v6_object(self) -> IPv6Address:
        """Generate random IPv6Address object.

        See documentation for module ipaddress:
        https://docs.python.org/3.7/library/ipaddress.html

        :return: IPv6Address object.
        """
        return IPv6Address(
            self.random.randint(
                0, self._MAX_IPV6,
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
            00:16:3e:25:e7:b1
        """
        mac_hex = [
            0x00, 0x16, 0x3e,
            self.random.randint(0x00, 0x7f),
            self.random.randint(0x00, 0xff),
            self.random.randint(0x00, 0xff),
        ]
        mac = ['{:02x}'.format(x) for x in mac_hex]
        return ':'.join(mac)

    def emoji(self) -> str:
        """Get a random emoji shortcut code.

        :return: Emoji code.

        :Example:
            :kissing:
        """
        return self.random.choice(EMOJI)

    @staticmethod
    def image_placeholder(width: Union[int, str] = 1920,
                          height: Union[int, str] = 1080) -> str:
        """Generate a link to the image placeholder.

        :param width: Width of image.
        :param height: Height of image.
        :return: URL to image placeholder.
        """
        url = 'http://placehold.it/{width}x{height}'
        return url.format(width=width, height=height)

    @staticmethod
    def stock_image(width: Union[int, str] = 1920,
                    height: Union[int, str] = 1080,
                    keywords: Optional[List[str]] = None,
                    writable: bool = False) -> Union[str, bytes]:
        """Generate random stock image (JPG/JPEG) hosted on Unsplash.

        See «Random search term» on https://source.unsplash.com/
        for more details.

        .. note:: This method required an active HTTP connection
            if you want to get writable object

        :param width: Width of the image.
        :param height: Height of the image.
        :param keywords: List of search keywords.
        :param writable: Return image as sequence ob bytes.
        :return: Link to the image.
        """
        api_url = 'https://source.unsplash.com/{}x{}?{}'

        if keywords is not None:
            keywords_str = ','.join(keywords)
        else:
            keywords_str = ''

        url = api_url.format(width, height, keywords_str)

        if writable:
            try:
                response = urllib.request.urlopen(url)
                return response.read()
            except urllib.error.URLError:
                raise urllib.error.URLError(
                    'Required an active HTTP connection')
        return url

    def hashtags(self, quantity: int = 4) -> Union[str, list]:
        """Generate a list of hashtags.

        :param quantity: The quantity of hashtags.
        :return: The list of hashtags.
        :raises NonEnumerableError: if category is not in Hashtag.

        :Example:
            ['#love', '#sky', '#nice']
        """
        tags = ['#' + self.random.choice(HASHTAGS)
                for _ in range(quantity)]

        if int(quantity) == 1:
            return tags[0]

        return tags

    def home_page(self, tld_type: Optional[TLDType] = None) -> str:
        """Generate a random home page.

        :param tld_type: TLD type.
        :return: Random home page.

        :Example:
            https://fontir.info
        """
        resource = self.random.choice(USERNAMES)
        domain = self.top_level_domain(
            tld_type=tld_type,
        )

        return 'https://{}{}'.format(
            resource, domain)

    def top_level_domain(self, tld_type: Optional[TLDType] = None) -> str:
        """Return random top level domain.

        :param tld_type: Enum object DomainType
        :return: Top level domain.
        :raises NonEnumerableError: if tld_type not in DomainType.
        """
        key = self._validate_enum(item=tld_type, enum=TLDType)
        return self.random.choice(TLD[key])

    def user_agent(self) -> str:
        """Get a random user agent.

        :return: User agent.

        :Example:
            Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0)
            Gecko/20100101 Firefox/15.0.1
        """
        return self.random.choice(USER_AGENTS)

    def network_protocol(self, layer: Optional[Layer] = None) -> str:
        """Get a random network protocol form OSI model.

        :param layer: Enum object Layer.
        :return: Protocol name.

        :Example:
            AMQP
        """
        key = self._validate_enum(item=layer, enum=Layer)
        protocols = NETWORK_PROTOCOLS[key]
        return self.random.choice(protocols)

    def port(self, port_range: PortRange = PortRange.ALL) -> int:
        """Generate random port.

        :param port_range: PortRange enum object.
        :return: Port number.
        :raises NonEnumerableError: if port_range is not in PortRange.

        :Example:
            8080
        """
        if isinstance(port_range, PortRange):
            return self.random.randint(*port_range.value)

        raise NonEnumerableError(PortRange)
