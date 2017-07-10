from elizabeth.data.int.network import (
    HTTP_METHODS,
    HTTP_STATUS_CODES,
    EMOJI,
    SUBREDDITS,
    SUBREDDITS_NSFW,
    USER_AGENTS,
    HASHTAGS,
    DOMAINS,
    NETWORK_PROTOCOLS,
)
from elizabeth.exceptions import WrongArgument

from .base import BaseProvider
from .file import File
from .personal import Personal


class Internet(BaseProvider):
    """Class for generate the internet data."""

    @staticmethod
    def content_type(mime_type='application'):
        """Get a random HTTP content type.

        :return: Content type.
        :Example:
            Content-Type: application/json
        """
        fmt = File().mime_type(type_t=mime_type)
        return 'Content-Type: {}'.format(fmt)

    def http_status_code(self, code_only=True):
        """Get a random HTTP status.

        :param code_only: Return only http status code.
        :return: HTTP status.
        :Example:
            200 OK
        """
        status = self.random.choice(HTTP_STATUS_CODES)

        if code_only:
            return status.split()[0]
        return status

    def http_method(self):
        """Get a random HTTP method.

        :return: HTTP method.
        :Example:
            POST
        """
        return self.random.choice(HTTP_METHODS)

    def ip_v4(self):
        """Generate a random IPv4 address.

        :return: Random IPv4 address.
        :Example:
            19.121.223.58
        """
        ip = '.'.join([str(self.random.randint(0, 255)) for _ in range(4)])
        return ip

    def ip_v6(self):
        """Generate a random IPv6 address.

        :return: Random IPv6 address.
        :Example:
            2001:c244:cf9d:1fb1:c56d:f52c:8a04:94f3
        """
        ip = "2001:" + ":".join("%x" % self.random.randint(0, 16 ** 4) for _ in range(7))
        return ip

    def mac_address(self):
        """Generate a random MAC address.

        :return: Random MAC address.
        :Example:
            00:16:3e:25:e7:b1
        """
        mac_hex = [
            0x00, 0x16, 0x3e,
            self.random.randint(0x00, 0x7f),
            self.random.randint(0x00, 0xff),
            self.random.randint(0x00, 0xff)
        ]
        mac = map(lambda x: "%02x" % x, mac_hex)
        return ':'.join(mac)

    def emoji(self):
        """Get a random emoji shortcut code.

        :return: Emoji code.
        :Example:
            :kissing:
        """
        return self.random.choice(EMOJI)

    @staticmethod
    def image_placeholder(width='400', height='300'):
        """Generate a link to the image placeholder.

        :param width: Width of image.
        :param height: Height of image.
        :return: URL to image placeholder.
        """
        url = 'http://placehold.it/%sx%s'
        return url % (width, height)

    def stock_image(self, category=None, width=1900, height=1080):
        """Get a random beautiful stock image that hosted on Unsplash.com

        :param category: Category of image. Available: 'buildings', 'food',
        'nature', 'people', 'technology', 'objects'.
        :param width: Width of the image.
        :param height: Height of the image.
        :return: An image (Link to image).
        """
        url = 'https://source.unsplash.com/category/' \
              '{category}/{width}x{height}'

        categories = (
            'buildings', 'food', 'nature',
            'people', 'technology', 'objects'
        )

        if not category or category not in categories:
            category = self.random.choice(categories)

        return url.format(category=category, width=width, height=height)

    def image_by_keyword(self, keyword=None):
        url = 'https://source.unsplash.com/weekly?{keyword}'

        keywords = [
            'cat', 'girl', 'boy', 'beauty',
            'nature', 'woman', 'man', 'tech',
            'space'
        ]

        if not keyword:
            keyword = self.random.choice(keywords)

        return url.format(keyword=keyword)

    def hashtags(self, quantity=4, category='general'):
        """Create a list of hashtags (for Instagram, Twitter etc.)

        :param quantity: The quantity of hashtags.
        :type quantity: int
        :param category: Available categories: general, girls, love,
        boys, friends, family, nature, travel, cars, sport, tumblr.
        :return: The list of hashtags.
        :rtype: list

        :Example:
            ['#love', '#sky', '#nice'].
        """
        category = category.lower()
        supported = ''.join(list(HASHTAGS.keys()))

        try:
            hashtags = HASHTAGS[category]
        except KeyError:
            raise KeyError('Unsupported category. Use: {}'.format(supported))

        if int(quantity) == 1:
            return self.random.choice(hashtags)

        tags = [self.random.choice(hashtags) for _ in range(int(quantity))]
        return tags

    def home_page(self, gender='female'):
        """Generate a random home page.

        :param gender: Gender of author of site.
        :return: Random home page.
        :Example:
            http://www.font6.info
        """
        url = 'http://www.' + Personal().username(gender)
        domain = self.random.choice(DOMAINS)
        return '{}{}'.format(url, domain)

    def subreddit(self, nsfw=False, full_url=False):
        """Get a random subreddit from the list.

        :param nsfw: NSFW subreddit.
        :param full_url: Full URL address.
        :return: Subreddit or URL to subreddit.
        :Example:
            https://www.reddit.com/r/flask/
        """
        url = 'http://www.reddit.com'
        if not nsfw:
            if not full_url:
                return self.random.choice(SUBREDDITS)
            else:
                return url + self.random.choice(SUBREDDITS)

        nsfw_sr = self.random.choice(SUBREDDITS_NSFW)
        result = url + nsfw_sr if full_url else nsfw_sr
        return result

    def user_agent(self):
        """Get a random user agent.

        :return: User agent.
        :Example:
            Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0)
            Gecko/20100101 Firefox/15.0.1
        """
        return self.random.choice(USER_AGENTS)

    def network_protocol(self, layer='application'):
        """Get a random network protocol form OSI model.

        :param layer: Layer of protocol: application, data_link,
        network, physical, presentation, session and transport.
        :return: Protocol name.
        :Example:
            AMQP
        """
        # TODO: Refactoring.
        layer = layer.lower()
        try:
            protocol = self.random.choice(NETWORK_PROTOCOLS[layer])
            return protocol
        except KeyError:
            raise WrongArgument(
                'Unsupported layer, use: {}'.format(list(NETWORK_PROTOCOLS.keys())))
