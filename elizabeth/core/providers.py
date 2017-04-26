# providers.py
# -*- coding: utf-8 -*-

import array
import datetime
import inspect
import json
import os
import re
import sys
from calendar import monthrange
from hashlib import sha1, sha256, sha512, md5
from random import (
    choice,
    sample,
    randint,
    uniform,
    random
)
from string import (
    digits,
    punctuation,
    ascii_letters,
    ascii_uppercase
)
# The data which common for all locales.
from elizabeth.data.int.address import *
from elizabeth.data.int.business import *
from elizabeth.data.int.code import *
from elizabeth.data.int.development import *
from elizabeth.data.int.file import *
from elizabeth.data.int.hardware import *
from elizabeth.data.int.network import *
from elizabeth.data.int.personal import *
from elizabeth.data.int.scientific import *
from elizabeth.data.int.transport import *
from elizabeth.data.int.datetime import *

from elizabeth.exceptions import WrongArgument

from elizabeth.utils import pull, luhn_checksum, \
    locale_info

__all__ = [
    'Address',
    'Business',
    'ClothingSizes',
    'Code',
    'Datetime',
    'Development',
    'File',
    'Food',
    'Hardware',
    'Internet',
    'Numbers',
    'Path',
    'Personal',
    'Science',
    'Structured',
    'Text',
    'Transport',
    'UnitSystem',
    'Generic'
]


class Address(object):
    """Class for generate fake address data."""

    def __init__(self, locale='en'):
        """
        :param locale: Current locale.
        """
        self.locale = locale
        self.data = pull('address.json', self.locale)

    def __str__(self):
        return '{}:{}:{}'.format(
            self.__class__.__name__,
            self.locale,
            locale_info(self.locale)
        )

    @staticmethod
    def street_number(maximum=1400):
        """Generate a random street number.

        :return: Street number.
        :Example:
            134.
        """
        number = randint(1, int(maximum))
        return '%s' % number

    def street_name(self):
        """Get a random street name.

        :return: Street name.
        :Example:
           Candlewood.
        """
        names = self.data['street']['name']
        return choice(names)

    def street_suffix(self):
        """Get a random street suffix.

        :return: Street suffix.
        :Example:
            Alley.
        """
        suffix = choice(self.data['street']['suffix'])
        return suffix

    def address(self):
        """Get a random full address (include Street number, suffix and name).

        :return: Full address.
        :Example:
            5 Central Sideline.
        """
        fmt = self.data['address_fmt']

        if self.locale in SHORTENED_ADDRESS_FMT:
            # Because fmt for ko is {st_name}{st_sfx} {st_num},
            # i.e not shortened address format
            if self.locale != 'ko':
                return fmt.format(
                    st_num=self.street_number(),
                    st_name=self.street_name(),
                )

        if self.locale == 'ja':
            cities = self.data['city']
            return fmt.format(
                city=choice(cities),
                n=randint(1, 100),
                nn=randint(1, 100),
                nnn=randint(1, 100)
            )

        return fmt.format(
            st_num=self.street_number(),
            st_name=self.street_name(),
            st_sfx=self.street_suffix()

        )

    def state(self, abbr=False):
        """Get a random states or subject of country.

        :param abbr: If True then return ISO (ISO 3166-2)
        code of state/region/province/subject.
        :return: State of current country.
        :Example:
            Alabama (for locale `en`).
        """
        key = 'abbr' if abbr else 'name'
        states = self.data['state'][key]
        return choice(states)

    def postal_code(self):
        """Generate a postal code for current locale.

        :return: Postal code.
        :Example:
            389213
        """
        mask = self.data['postal_code_fmt']
        return Code.custom_code(mask)

    @staticmethod
    def country_iso(fmt='iso2'):
        """Get a random ISO code of country.

        :param fmt: Format of code (iso2, iso3, numeric).
        :return: ISO Code.
        :Example:
            DE
        """
        sup = ''.join(list(COUNTRIES_ISO.keys()))

        if fmt not in COUNTRIES_ISO:
            raise KeyError('Unsupported format. Use: {}'.format(sup))

        countries = COUNTRIES_ISO[fmt]
        return choice(countries)

    def country(self):
        """Get a random country.

        :return: The Country.
        :Example:
            Russia.
        """
        countries = self.data['country']['name']
        return choice(countries)

    def city(self):
        """Get a random city for current locale.

        :return: City name.
        :Example:
            Saint Petersburg.
        """
        cities = self.data['city']
        return choice(cities)

    @staticmethod
    def latitude():
        """Generate a random value of latitude (-90 to +90).

        :return: Value of longitude.
        :Example:
            -66.4214188124611
        """
        return uniform(-90, 90)

    @staticmethod
    def longitude():
        """
        Generate a random value of longitude (-180 to +180).

        :return: Value of longitude.
        :Example:
            112.18440260511943
        """
        return uniform(-180, 180)

    def coordinates(self):
        """Generate random geo coordinates.

        :return: Dict with coordinates.
        :rtype: dict
        :Example:
            {'latitude': 8.003968712834975, 'longitude': 36.02811153405548}
        """
        coord = {
            'longitude': self.longitude(),
            'latitude': self.latitude()
        }
        return coord

    def continent(self, code=False):
        """Get a random continent name or continent
        code (code in international format)

        :return: Continent name.
        :Example:
            Africa (en)
        """
        if code:
            codes = CONTINENT_CODES
            return choice(codes)

        continent = choice(self.data['continent'])
        return continent


class Numbers(object):
    """Class for generating numbers"""

    @staticmethod
    def floats(n=2, type_code='f', to_list=False):
        """Generate an array of random float number of 10**n.

        +-----------+----------------+--------------+----------------------+
        | Type Code | C Type         | Storage size | Value range          |
        +===========+================+==============+======================+
        | 'f'       | floating point | 4 byte       | 1.2E-38 to 3.4E+38   |
        +-----------+----------------+--------------+----------------------+
        | 'd'       | floating point | 8 byte       | 2.3E-308 to 1.7E+308 |
        +-----------+----------------+--------------+----------------------+

        :param n: Raise 10 to the 'n' power.
        :param type_code: A code of type.
        :param to_list: Convert array to list.

        .. note:: When you work with large numbers, it is better not to use
            this option, because type 'array' much faster than 'list'.

        :return: An array of floating-point numbers.
        """
        nums = array.array(type_code, (random() for _ in range(10 ** int(n))))
        return nums.tolist() if to_list else nums

    @staticmethod
    def primes(start=1, end=999, to_list=False):
        """Generate an array of prime numbers of 10 ** n.

        +------------+-----------------+--------------+--------------------+
        | Type Code | C Type           | Storage size | Value range        |
        +===========+==================+==============+====================+
        | 'L'       | unsigned integer | 4 byte       | 0 to 4,294,967,295 |
        +-----------+------------------+--------------+--------------------+

        :param start: First value of range.
        :param end: Last value of range.
        :param to_list: Convert array to list.
        :return: An array of floating-point numbers.
        """
        nums = array.array('L', (i for i in range(start, end) if i % 2))
        return nums.tolist() if to_list else nums

    @staticmethod
    def digit(to_bin=False):
        """Get a random digit.

        :param to_bin: If True then convert to binary.
        :return: Digit.
        :Example:
            4.
        """
        digit = randint(0, 9)

        if to_bin:
            return bin(digit)

        return digit

    @staticmethod
    def between(minimum=1, maximum=1000):
        """Generate a random number between minimum and maximum.

        :param minimum: Minimum of range.
        :param maximum: Maximum of range
        :return: Number
        """
        num = randint(int(minimum), int(maximum))
        return num

    @staticmethod
    def rating(maximum=5.0):
        """Generate random rating for something.

        :param maximum: Minimum value (default is 5.0).
        :return: Rating.
        :rtype: float
        :Example:
            4.7
        """
        res = '{0:0.1f}'.format(uniform(0, float(maximum)))
        return float(res)


class Structured(object):
    """Provider for structured text data such as CSS, Delimited, HTML, etc."""

    def __init__(self, locale='en'):
        """
        :param locale: Current locale.
        """
        self.locale = locale
        self.internet = Internet()
        self.text = Text(self.locale)

    def __str__(self):
        return '{}:{}:{}'.format(
            self.__class__.__name__,
            self.locale,
            locale_info(self.locale)
        )

    def css(self):
        """Generates a random snippet of CSS.

        :return: CSS.
        :rtype: str
        :Example:
            'strong {
                pointer: crosshair;
                padding-right: 46pt;
                margin-left: 38em;
                padding-right: 65em
            }'
        """
        selector = choice(CSS_SELECTORS)
        css_sel = '{}{}'.format(selector, self.text.word())

        cont_tag = choice(list(HTML_CONTAINER_TAGS.keys()))
        mrk_tag = choice(HTML_MARKUP_TAGS)

        base = "{}".format(choice([cont_tag, mrk_tag, css_sel]))
        props = "; ".join(
            [self.css_property() for _ in range(randint(1, 6))])
        return "{} {{{}}}".format(base, props)

    def css_property(self):
        """Generates a random snippet of CSS that assigns value to a property.

        :return: CSS property.
        :rtype: str
        :Examples:
            'background-color: #f4d3a1'
        """
        prop = choice(list(CSS_PROPERTIES.keys()))
        val = CSS_PROPERTIES[prop]

        if isinstance(val, list):
            val = choice(val)
        elif val == "color":
            val = self.text.hex_color()
        elif val == "size":
            val = "{}{}".format(randint(1, 99), choice(CSS_SIZE_UNITS))

        return "{}: {}".format(prop, val)

    def html(self):
        """Generate a random HTML tag with text inside and some attrs set.

        :return: HTML.
        :rtype: str
        :Examples:
            '<span class="select" id="careers">
                Ports are created with the built-in function open_port.
            </span>'
        """
        tag_name = choice(list(HTML_CONTAINER_TAGS))
        tag_attributes = list(HTML_CONTAINER_TAGS[tag_name])
        k = randint(1, len(tag_attributes))

        selected_attrs = sample(tag_attributes, k=k)

        attrs = []
        for attr in selected_attrs:
            attrs.append("{}=\"{}\"".format(
                attr, self.html_attribute_value(tag_name, attr)))

        html_result = "<{tag} {attrs}>{content}</{tag}>"
        return html_result.format(
            tag=tag_name,
            attrs=" ".join(attrs),
            content=self.text.sentence()
        )

    def html_attribute_value(self, tag, attribute):
        """Random value for specified HTML tag attribute.

        :param tag: An HTML tag.
        :param attribute: An attribute of the specified tag.
        :type tag: str
        :type attribute: str
        :return: An attribute.
        :rtype: str
        """
        try:
            value = HTML_CONTAINER_TAGS[tag][attribute]
        except KeyError:
            raise NotImplementedError(
                "Tag {} or attribute {} is not supported".format(
                    tag, attribute))

        if isinstance(value, list):
            value = choice(value)
        elif value == "css":
            value = self.css_property()
        elif value == "word":
            value = self.text.word()
        elif value == "url":
            value = self.internet.home_page()
        else:
            raise NotImplementedError(
                "Attribute type {} is not implemented".format(value))
        return value

    def json(self, provider_name, items=5):
        """Generate a random snippet of JSON

        :param provider_name: Name of provider to generate JSON data for.
        :type provider_name: str
        :param items: Number of top-level items to include.
        :type items: int
        :return: JSON.
        :rtype: str
        """
        providers = {
            'hardware': {
                'provider': Hardware,
                'root_element': 'computers',
            },
            'personal': {
                'provider': Personal,
                'root_element': 'users'
            }
        }

        try:
            provider_data = providers[provider_name.lower()]
        except KeyError:
            raise NotImplementedError(
                "Provider {} is not supported".format(provider_name)
            )

        try:
            provider = provider_data['provider'](self.locale)
        except TypeError:  # handle providers that do not accept locale
            provider = provider_data['provider']()

        root_element = provider_data['root_element']

        data = {root_element: []}

        for _ in range(items):
            element = dict()
            for attribute_name in dir(provider):
                attribute = getattr(provider, attribute_name)
                if attribute_name[:1] != "_" and callable(attribute):
                    element[attribute_name] = attribute()
            data[root_element].append(element)

        return json.dumps(data, indent=4)


class Text(object):
    """Class for generate text data, i.e text, lorem ipsum and another."""

    def __init__(self, locale='en'):
        """
        :param locale: Current locale.
        """
        self.locale = locale
        self.data = pull('text.json', self.locale)

    def __str__(self):
        return '{}:{}:{}'.format(
            self.__class__.__name__,
            self.locale,
            locale_info(self.locale)
        )

    def alphabet(self, letter_case=None):
        """Get an alphabet for current locale.

        :param letter_case: Letter case.
        :return: Alphabet.
        :rtype: list
        """
        letter_case = 'uppercase' if \
            not letter_case else letter_case

        alpha = self.data['alphabet'][letter_case]
        return alpha

    def level(self):
        """Generate a random level of danger or something else.

        :return: Level.
        :Example:
            critical.
        """
        levels = self.data['level']
        return choice(levels)

    def text(self, quantity=5):
        """Generate the text.

        :param quantity: Quantity of sentences.
        :return: Text.
        :Example:
            Haskell is a standardized, general-purpose purely
            functional programming language, with non-strict semantics
            and strong static typing.
        """
        text = ''
        for _ in range(int(quantity)):
            text += ' ' + choice(self.data['text'])
        return text.strip()

    def sentence(self):
        """Get a random sentence from text.

        :return: Sentence.
        :Example:
            Any element of a tuple can be accessed in constant time.
        """
        return self.text(quantity=1)

    def title(self):
        """Get a random title.

        :return: The title.
        :Example:
            Erlang - is a general-purpose, concurrent,
            functional programming language.
        """
        return self.text(quantity=1)

    def words(self, quantity=5):
        """Get the random words.

        :param quantity: Quantity of words. Default is 5.
        :return: Word list.
        :Example:
            science, network, god, octopus, love.
        """
        words = self.data['words']['normal']
        words_list = [choice(words) for _ in range(int(quantity))]
        return words_list

    def word(self):
        """Get a random word.

        :return: Single word.
        :Example:
            Science.
        """
        return self.words(quantity=1)[0]

    def swear_word(self):
        """Get a random swear word.

        :return: Swear word.
        :Example:
            Damn.
        """
        bad_words = self.data['words']['bad']
        return choice(bad_words)

    def quote(self):
        """Get a random quote.

        :return: Quote from movie.
        :Example:
            "Bond... James Bond."
        """
        quotes = self.data['quotes']
        return choice(quotes)

    def color(self):
        """Get a random name of color.

        :return: Color name.
        :Example:
            Red.
        """
        colors = self.data['color']
        return choice(colors)

    @staticmethod
    def hex_color():
        """Generate a hex color.

        :return: Hex color code.
        :Example:
            #D8346B
        """
        letters = '0123456789ABCDEF'
        color_code = '#' + ''.join(sample(letters, 6))
        return color_code

    def answer(self):
        """Get a random answer in current language.

        :return: An answer.
        :rtype: str
        :Example:
            No
        """
        answers = self.data['answers']
        return choice(answers)


class Code(object):
    """Class that provides methods for generating codes (isbn, asin & etc.)"""

    def __init__(self, locale):
        """
        :param locale: Current locale.
        """
        self.locale = locale

    def __str__(self):
        return '{}:{}:{}'.format(
            self.__class__.__name__,
            self.locale,
            locale_info(self.locale)
        )

    @staticmethod
    def custom_code(mask="@###", char='@', digit='#'):
        """Generate custom code using ascii uppercase and random integers.

        :param mask: Mask of code.
        :param char: Placeholder for characters.
        :param digit: Placeholder for digits.
        :return: Custom code.
        :Example:
            5673-AGFR-SFSFF-1423-4/AD.
        """
        code = ''
        for p in mask:
            if p == char:
                code += choice(ascii_uppercase)
            elif p == digit:
                code += str(randint(0, 9))
            else:
                code += p

        return code

    @staticmethod
    def locale_code():
        """Get a random locale code (MS-LCID).
        See Windows Language Code Identifier Reference for more information.

        :return: Locale code.
        :rtype: str
        :Example:
            de-ch
        """
        locale = choice(LOCALE_CODES)
        return locale

    def issn(self, mask=None):
        """Generate a random International Standard Serial Number (ISSN).

        :param mask: Mask ISSN.
        :return: ISSN.
        """
        if not mask:
            mask = "####-####"
        return self.custom_code(mask=mask)

    def isbn(self, fmt='isbn-10'):
        """Generate ISBN for current locale. Default is ISBN 10,
        but you also can use ISBN-13.

        :param fmt: ISBN format.
        :return: ISBN.
        :Example:
            132-1-15411-375-8.
        """
        groups = ISBN_GROUPS

        mask = '###-{0}-#####-###-#' if \
            fmt == 'isbn-13' else '{0}-#####-###-#'

        if self.locale in groups:
            mask = mask.format(groups[self.locale])
        else:
            mask = mask.format(groups['default'])

        return self.custom_code(mask=mask)

    def ean(self, fmt='ean-13'):
        """Generate EAN (European Article Number) code. Default is
        EAN-13, but you also can use EAN-8.

        :param fmt: Format of EAN.
        :return: EAN.
        :Example:
            3953753179567.
        """
        mask = '########' if fmt == 'ean-8' \
            else '#############'
        return self.custom_code(mask=mask)

    def imei(self):
        """Generate a random IMEI (International Mobile Station Equipment Identity).

        :return: IMEI.

        :Example:
        353918052107063
        """
        num = choice(IMEI_TACS) + self.custom_code(mask='######')
        return num + luhn_checksum(num)

    def pin(self, mask='####'):
        """Generate a random PIN code.

        :return: PIN code.
        :Example:
            5241.
        """
        return self.custom_code(mask=mask)


class Business(object):
    """Class for generating data for business."""

    def __init__(self, locale='en'):
        """
        :param locale: Current locale.
        """
        self.locale = locale
        self.data = pull('business.json', self.locale)

    def __str__(self):
        return '{}:{}:{}'.format(
            self.__class__.__name__,
            self.locale,
            locale_info(self.locale)
        )

    def company_type(self, abbr=False):
        """Get a random type of business entity.

        :param abbr: If True then return abbreviated company type.
        :return: Types of business entity.
        :Example:
            Incorporated.
        """
        key = 'abbr' if abbr else 'title'
        company_type = self.data['company']['type'][key]
        return choice(company_type)

    def company(self):
        """Get a random company name.

        :return: Company name.
        :Example:
            Gamma Systems.
        """
        companies = self.data['company']['name']
        return choice(companies)

    def copyright(self):
        """Generate a random copyright.

        :return: Dummy copyright of company.
        :Example:
            © 1990-2016 Komercia, Inc.
        """
        company_type = self.company_type(abbr=True)
        return '© %s, %s' % (self.company(), company_type)

    @staticmethod
    def currency_iso():
        """Get a currency code. ISO 4217 format.

        :return: Currency code.
        :Example:
            RUR.
        """
        return choice(CURRENCIES)

    def price(self, minimum=10.00, maximum=1000.00):
        """Generate a random price.

        :param minimum:
        :param maximum:
        :return: Price.
        :Example:
            599.99 $.
        """
        currencies = CURRENCY_SYMBOLS

        price = uniform(float(minimum), float(maximum))

        fmt = '{0:.2f} {1}'

        if self.locale in currencies:
            return fmt.format(price, currencies[self.locale])

        return fmt.format(price, currencies['default'])


class Personal(object):
    """Class for generate personal data, i.e names, surnames,
    age and another."""

    def __init__(self, locale='en'):
        """
        :param locale: Current locale.
        """
        self.locale = locale
        self.data = pull('personal.json', self.locale)
        self._store = {
            'age': 0
        }

    def __str__(self):
        return '{}:{}:{}'.format(
            self.__class__.__name__,
            self.locale,
            locale_info(self.locale)
        )

    def age(self, minimum=16, maximum=66):
        """Get a random integer value.

        :param maximum: max age
        :param minimum: min age
        :return: Random integer (from minimum=16 to maximum=66)
        :Example:
            23.
        """
        a = randint(int(minimum), int(maximum))
        self._store['age'] = a
        return a

    def child_count(self, max_childs=5):
        """Get a count of child's.

        :param max_childs: Maximum count of child's.
        :return: Ints. Depend on previous generated age.
        """
        a = self._store['age']
        if a == 0:
            a = self.age()

        cc = 0 if a < 18 else randint(0, max_childs)
        return cc

    def work_experience(self, working_start_age=22):
        """Get a work experience.

        :param working_start_age: Age then person start to work.
        :return: Int. Depend on previous generated age.
        """
        a = self._store['age']
        if a == 0:
            a = self.age()

        return max(a - working_start_age, 0)

    def name(self, gender='female'):
        """Get a random name.

        :param gender: if 'male' then will getting male name else female name.
        :return: Name.
        :Example:
            John.
        """
        # TODO: Add function for checking gender.
        try:
            names = self.data['names'][gender]
        except KeyError:
            raise WrongArgument('gender must be "female" or "male"')

        return choice(names)

    def surname(self, gender='female'):
        """Get a random surname.

        :param gender: The gender of person.
        :return: Surname.
        :Example:
            Smith.
        """
        # Separated by gender.
        if self.locale in ('ru', 'is', 'uk'):
            try:
                return choice(self.data['surnames'][gender])
            except KeyError:
                raise WrongArgument('gender must be "female" or "male"')

        surname = choice(self.data['surnames'])
        return surname

    def title(self, gender='female', title_type='typical'):
        """Get a random title (prefix/suffix) for name.

        :param gender: The gender.
        :param title_type:  The type of title ('typical' and 'academic').
        :return: The title.
        :Example:
            PhD.
        """
        try:
            titles = self.data['title'][gender][title_type]
        except KeyError:
            raise WrongArgument('Wrong value of argument.')

        title = choice(titles)
        return title

    def full_name(self, gender='female', reverse=False):
        """Generate a random full name.

        :param reverse: if true: surname/name else name/surname
        :param gender: if gender='male' then will be returned male name else
            female name.
        :return: Full name.
        :Example:
            Johann Wolfgang.
        """
        gender = gender.lower()

        fmt = '{1} {0}' if reverse else '{0} {1}'
        return fmt.format(
            self.name(gender),
            self.surname(gender)
        )

    @staticmethod
    def username(gender='female'):
        """Get a random username with digits. Username generated
        from names (en) for all locales.

        :return: Username.
        :rtype: str
        :Example:
            abby1189.
        """
        try:
            names = pull('personal.json', 'en')['names'][gender]
            name = choice(names)
        except KeyError:
            raise WrongArgument('gender must be "female" or "male"')

        fmt = ['%s_%s', '%s%s', '%s-%s']

        username = choice(fmt) % (name, randint(2, 9999))
        return username.lower()

    @staticmethod
    def password(length=8, algorithm=None):
        """Generate a password or hash of password.

        :param length: Length of password.
        :param algorithm: Hashing algorithm.
        :return: Password or hash of password.
        :Example:
            k6dv2odff9#4h (without hashing).
        """
        password = "".join([choice(
            ascii_letters + digits + punctuation) for _ in range(int(length))])

        if algorithm is not None:
            algorithm = algorithm.lower()
            password = password.encode()
            if algorithm == 'sha1':
                return sha1(password).hexdigest()
            elif algorithm == 'sha256':
                return sha256(password).hexdigest()
            elif algorithm == 'sha512':
                return sha512(password).hexdigest()
            elif algorithm == 'md5':
                return md5(password).hexdigest()
            raise NotImplementedError(
                "The specified hashing algorithm is not available.")

        return password

    def email(self, gender='female', domains=None):
        """Generate a random email.

        :param gender: Gender of the user.
        :type gender: str
        :param domains: Custom domain for email.
        :type domains: list, tuple
        :return: Email address.
        :Example:
            foretime10@live.com
        """
        host = domains if domains \
            else EMAIL_DOMAINS

        email = self.username(gender) + choice(host)
        return email

    @staticmethod
    def bitcoin():
        """Generate a random bitcoin address. Currently supported only two
        address formats that are most popular: 'P2PKH' and 'P2SH'

        :return: Bitcoin address.
        :Example:
            3EktnHQD7RiAE6uzMj2ZifT9YgRrkSgzQX
        """
        fmt = choice(['1', '3'])
        fmt += "".join([choice(ascii_letters + digits) for _ in range(33)])
        return fmt

    @staticmethod
    def cvv():
        """Generate a random card verification value (CVV).

        :return: CVV code.
        :rtype: int
        :Example:
            324
        """
        return randint(100, 999)

    @staticmethod
    def credit_card_number(card_type='visa'):
        """Generate a random credit card number.

        :param card_type: Issuing Network. Default is Visa.
        :return: Credit card number.
        :Example:
            4455 5299 1152 2450
        """
        length = 16
        regex = re.compile("(\d{4})(\d{4})(\d{4})(\d{4})")

        if card_type in ('visa', 'vi', 'v'):
            number = randint(4000, 4999)
        elif card_type in ('master_card', 'mc', 'master', 'm'):
            number = choice([randint(2221, 2720), randint(5100, 5500)])
        elif card_type in ('american_express', 'amex', 'ax', 'a'):
            number = choice([34, 37])
            length = 15
            regex = re.compile("(\d{4})(\d{6})(\d{5})")
        else:
            raise NotImplementedError(
                "Card type {} is not supported.".format(card_type))

        number = str(number)
        while len(number) < length - 1:
            number += choice(digits)

        card = " ".join(regex.search(number + luhn_checksum(number)).groups())
        return card

    @staticmethod
    def credit_card_expiration_date(minimum=16, maximum=25):
        """Generate a random expiration date for credit card.

        :param minimum: Date of issue.
        :param maximum: Maximum of expiration_date.
        :return: Expiration date of credit card.
        :rtype: str
        :Example:
            03/19.
        """
        month, year = randint(1, 12), randint(minimum, maximum)
        month = '0' + str(month) if month < 10 else month
        return '{0}/{1}'.format(month, year)

    @staticmethod
    def cid():
        """Generate a random CID code.

        :return: CID code.
        :Example:
            7452
        """
        return randint(1000, 9999)

    def paypal(self):
        """Generate a random PayPal account.

        :return: Email of PapPal user.
        :Example:
            wolf235@gmail.com
        """
        return self.email()

    def social_media_profile(self, gender='female'):
        """Generate profile for random social network.

        :param gender: Gender of user.
        :return: Profile in some network.
        :Example:
            http://facebook.com/some_user
        """
        urls = [
            "facebook.com/{}",
            "twitter.com/{}",
            "medium.com/@{}"
        ]
        url = 'http://' + choice(urls)
        username = self.username(gender)

        return url.format(username)

    def gender(self, iso5218=False, symbol=False):
        """Get a random title of gender, code for the representation
        of human sexes is an international standard that defines a
        representation of human sexes through a language-neutral single-digit
        code or symbol of gender.

        :param iso5218: Codes for the representation of human sexes
        is an international standard.
        :param symbol: Symbol of gender.
        :return: Title of gender.
        :rtype: str
        :Example:
            Male
        """
        # The four codes specified in ISO/IEC 5218 are:
        #     0 = not known,
        #     1 = male,
        #     2 = female,
        #     9 = not applicable.
        codes = [0, 1, 2, 9]

        if iso5218:
            return choice(codes)

        if symbol:
            return choice(GENDER_SYMBOLS)

        gender = choice(self.data['gender'])
        return gender

    @staticmethod
    def height(minimum=1.5, maximum=2.0):
        """Generate a random height in M (Meter).

        :param minimum: Minimum value.
        :param maximum: Maximum value.
        :return: Height.
        :Example:
            1.85.
        """
        h = uniform(float(minimum), float(maximum))
        return '{:0.2f}'.format(h)

    @staticmethod
    def weight(minimum=38, maximum=90):
        """Generate a random weight in Kg.

        :param minimum: min value
        :param maximum: max value
        :return: Weight.
        :Example:
            48.
        """
        weight = randint(int(minimum), int(maximum))
        return weight

    @staticmethod
    def blood_type():
        """Get a random blood type.

        :return: Blood type (blood group).
        :Example:
            A+
        """
        return choice(BLOOD_GROUPS)

    def sexual_orientation(self, symbol=False):
        """Get a random (LOL) sexual orientation.

        :param symbol: Unicode symbol.
        :return: Sexual orientation.
        :Example:
            Heterosexuality.
        """
        if symbol:
            return choice(SEXUALITY_SYMBOLS)

        sexuality = self.data['sexuality']
        return choice(sexuality)

    def occupation(self):
        """Get a random job.

        :return: The name of job.
        :Example:
            Programmer.
        """
        jobs = self.data['occupation']
        return choice(jobs)

    def political_views(self):
        """Get a random political views.

        :return: Political views.
        :Example:
            Liberal.
        """
        views = self.data['political_views']
        return choice(views)

    def worldview(self):
        """Get a random worldview.

        :return: Worldview.
        :Example:
            Pantheism.
        """
        views = self.data['worldview']
        return choice(views)

    def views_on(self):
        """
        Get a random views on.

        :return: Views on.
        :Example:
            Negative.
        """
        views = self.data['views_on']
        return choice(views)

    def nationality(self, gender='female'):
        """Get a random nationality.

        :param gender: female or male
        :return: Nationality.
        :Example:
            Russian.
        """
        # Subtleties of the Russian and Ukrainian orthography.
        separated_locales = ['ru', 'uk']

        if self.locale in separated_locales:
            nations = self.data['nationality'][gender]
            return choice(nations)

        return choice(self.data['nationality'])

    def university(self):
        """
        Get a random university.

        :return: University name.
        :Example:
            MIT.
        """
        universities = self.data['university']
        return choice(universities)

    def academic_degree(self):
        """Get a random academic degree.

        :return: Degree.
        :Example:
            Bachelor.
        """
        degrees = self.data['academic_degree']
        return choice(degrees)

    def language(self):
        """Get a random language.

        :return: Random language.
        :Example:
            Irish.
        """
        languages = self.data['language']
        return choice(languages)

    def favorite_movie(self):
        """Get a random movie for current locale.

        :return: The name of the movie.
        :Example:
            Interstellar.
        """
        movies = self.data['favorite_movie']
        return choice(movies)

    @staticmethod
    def favorite_music_genre():
        """Get a random music genre.

        :return: A music genre.
        :Example:
            Ambient.
        """
        return choice(FAVORITE_MUSIC_GENRE)

    def telephone(self, mask=None, placeholder='#'):
        """Generate a random phone number.

        :param mask: Mask for formatting number.
        :param placeholder: A placeholder for a mask (default is #).
        :return: Phone number.
        :Example:
            +7-(963)-409-11-22.
        """
        # Default
        default = '+#-(###)-###-####'

        if not mask:
            masks = self.data.get('telephone_fmt', default)
            mask = choice(masks)

        _ = Code.custom_code
        return _(mask=mask, digit=placeholder)

    def avatar(self, size=256):
        """Generate a random avatar (link to avatar) using API of  Adorable.io.

        :return: Link to avatar.
        :Example:
            https://api.adorable.io/avatars/64/875ed3de1604812b3c2b592c05863f47.png
        """
        url = 'https://api.adorable.io/avatars/{0}/{1}.png'
        return url.format(size, self.password(algorithm='md5'))

    @staticmethod
    def identifier(mask='##-##/##'):
        """Generate a random identifier by mask. With this method you can generate
        any identifiers that you need. Simply select the mask that you need.

        :param mask: The mask. Here '@' is a placeholder for characters
        and '#' is placeholder for digits.
        :return: An identifier.
        :Example:
            07-97/04
        """
        _ = Code.custom_code
        return _(mask=mask)

    @staticmethod
    def level_of_english():
        """Get a random level of English.

        :return: Level of english.
        :Example:
            Intermediate.
        """
        return choice(ENGLISH_LEVEL)


class Datetime(object):
    """Class for generate the fake data that you can use for
    working with date and time."""

    def __init__(self, locale='en'):
        """
        :param locale: Current locale.
        """
        self.locale = locale
        self.data = pull('datetime.json', self.locale)

    def __str__(self):
        return '{}:{}:{}'.format(
            self.__class__.__name__,
            self.locale,
            locale_info(self.locale)
        )

    def day_of_week(self, abbr=False):
        """Get a random day of week.

        :param abbr: Abbreviated name of the day.
        :return: Name of day of the week.
        :Example:
            Wednesday (Wed. when abbr=True).
        """
        key = 'abbr' if abbr else 'name'
        days = self.data['day'][key]
        return choice(days)

    def month(self, abbr=False):
        """Get a random month.

        :param abbr: if True then will be returned abbreviated month name.
        :return: Month name.
        :Example:
            January (Jan. when abbr=True).
        """
        key = 'abbr' if abbr else 'name'
        months = self.data['month'][key]
        return choice(months)

    @staticmethod
    def year(minimum=1990, maximum=2050):
        """Generate a random year.

        :param minimum: Minimum value.
        :param maximum: Maximum value
        :return: Year.
        :Example:
            2023.
        """
        return randint(int(minimum), int(maximum))

    @staticmethod
    def century():
        """Get a random value from list of centuries (roman format).

        :return: Century.
        :Example:
            XXI
        """
        return choice(ROMAN_NUMS)

    def periodicity(self):
        """Get a random periodicity string.

        :return: Periodicity.
        :Example:
            Never.
        """
        periodicity = self.data['periodicity']
        return choice(periodicity)

    def date(self, start=2000, end=2035, fmt=None):
        """Generate a string representing of random date formatted for
        the locale or as specified.

        :param start: Minimum value of year.
        :param end: Maximum value of year.
        :param fmt: Format string for date.
        :return: Formatted date.
        :Example:
            08/16/88 (en)
        """
        if not fmt:
            fmt = self.data['formats']['date']

        year = randint(start, end)
        month = randint(1, 12)
        d = datetime.date(
            year, month, randint(1, monthrange(year, month)[1]))
        return d.strftime(fmt)

    def time(self, fmt=None):
        """Generate a random time formatted for the locale or as specified.

        :return: Time.
        :Example:
            21:30:00 (en)
        """
        if not fmt:
            fmt = self.data['formats']['time']

        t = datetime.time(
            randint(0, 23),
            randint(0, 59),
            randint(0, 59),
            randint(0, 999999)
        )
        return t.strftime(fmt)

    @staticmethod
    def day_of_month():
        """Generate a random day of month, from 1 to 31.

        :return: Random value from 1 to 31.
        :Example:
            23
        """
        return randint(1, 31)


class File(object):
    """Class for generate fake data for files."""

    @staticmethod
    def extension(file_type='text'):
        """Get a random file extension from list.

        :param file_type: File type (source, text, data, audio, video, image,
        executable, compressed).
        :return: Extension of a file.
        :Example:
            .py (file_type='source').
        """
        k = file_type.lower()
        return choice(EXTENSIONS[k])

    @staticmethod
    def mime_type(type_t='application'):
        """Get a random mime type from list.

        :return: Mime type.
        :param type_t: Type of media: (application,
        image, video, audio, text, message).
        :rtype: str
        """
        supported = ' '.join(MIME_TYPES.keys())

        if type_t not in list(MIME_TYPES.keys()):
            raise ValueError(
                'Unsupported mime type! Use: {}'.format(supported))

        mime_type = choice(MIME_TYPES[type_t])
        return mime_type


class Science(object):
    """Class for getting scientific data"""

    def __init__(self, locale='en'):
        """
        :param locale: Current language.
        """
        self.locale = locale
        self._data = pull('science.json', self.locale)

    def __str__(self):
        return '{}:{}:{}'.format(
            self.__class__.__name__,
            self.locale,
            locale_info(self.locale)
        )

    @staticmethod
    def math_formula():
        """Get a random mathematical formula.

        :return: Math formula.
        :Example:
            A = (ab)/2.
        """
        formula = choice(MATH_FORMULAS)
        return formula

    def chemical_element(self, name_only=True):
        """Generate a random chemical element.

        :param name_only: If False then will be returned dict.
        :return: Name of chemical element or dict.
        :Example:
            {'Symbol': 'S', 'Name': 'Sulfur', 'Atomic number': '16'}
        """
        elements = self._data['chemical_element']
        nm, sm, an = choice(elements).split('|')

        if not name_only:
            return {
                'name': nm.strip(),
                'symbol': sm.strip(),
                'atomic_number': an.strip()
            }

        return nm.strip()

    def scientific_article(self):
        """Generate a random link to scientific article on Wikipedia.

        :return: Link to article on Wikipedia.
        :Example:
            https://en.wikipedia.org/wiki/Black_hole
        """
        articles = self._data['article']
        return choice(articles)


class Development(object):
    """Class for getting fake data for Developers."""

    @staticmethod
    def software_license():
        """Get a random software license from list.

        :return: License name.
        :rtype: str
        :Example:
            The BSD 3-Clause License.
        """
        return choice(LICENSES)

    @staticmethod
    def version():
        """Generate a random version information.

        :return: The version of software.
        :Example:
            0.11.3.
        """
        n = (randint(0, 11) for _ in range(3))
        return '{}.{}.{}'.format(*n)

    @staticmethod
    def database(nosql=False):
        """Get a random database name.

        :param nosql: only NoSQL databases.
        :return: Database name.
        :Example:
            PostgreSQL.
        """
        if nosql:
            return choice(NOSQL)
        return choice(SQL)

    @staticmethod
    def container():
        """Get a random containerization system.

        :return: Containerization system.
        :Example:
            Docker.
        """
        return choice(CONTAINER)

    @staticmethod
    def version_control_system():
        """Get a random version control system.

        :return: Version control system
        :Example:
            Git
        """
        return choice(["Git", "Subversion"])

    @staticmethod
    def programming_language():
        """Get a random programming language from the list.

        :return: Programming language.
        :Example:
            Erlang.
        """
        return choice(PROGRAMMING_LANGS)

    @staticmethod
    def backend():
        """Get a random backend stack.

        :return: Stack.
        :Example:
            Elixir/Phoenix
        """
        return choice(BACKEND)

    @staticmethod
    def frontend():
        """Get a random front-end stack.

        :return: Stack.
        :Example:
            JS/React.
        """
        return choice(FRONTEND)

    @staticmethod
    def os():
        """Get a random operating system or distributive name.

        :return: The name of OS.
        :Example:
            Gentoo
        """
        return choice(OS)

    @staticmethod
    def stackoverflow_question():
        """Generate a random question id for StackOverFlow
        and return url to a question.

        :return: URL to a question.
        :Example:
            http://stackoverflow.com/questions/1726403

        """
        post_id = randint(1000000, 9999999)
        url = 'http://stackoverflow.com/questions/{0}'
        return url.format(post_id)


class Food(object):
    """Class for Food, i.e fruits, vegetables, berries and other."""

    def __init__(self, locale='en'):
        """
        :param locale: Current locale.
        """
        self.lang = locale
        self._data = pull('food.json', self.lang)

    def __str__(self):
        return '{}:{}:{}'.format(
            self.__class__.__name__,
            self.lang,
            locale_info(self.lang)
        )

    def vegetable(self):
        """Get a random vegetable.

        :return: Vegetable.
        :Example:
            Tomato.
        """
        vegetables = self._data['vegetables']
        return choice(vegetables)

    def fruit(self):
        """Get a random name of fruit or berry .

        :return: Fruit.
        :Example:
            Banana.
        """
        fruits = self._data['fruits']
        return choice(fruits)

    def dish(self):
        """Get a random dish for current locale.

        :return: Dish name.
        :Example:
            Ratatouille.
        """
        dishes = self._data['dishes']
        return choice(dishes)

    def spices(self):
        """Get a random spices or herbs.

        :return: Spices or herbs.
        :Example:
            Anise.
        """
        spices = self._data['spices']
        return choice(spices)

    def drink(self):
        """Get a random drink.

        :return: Alcoholic drink.
        :Example:
            Vodka.
        """
        drinks = self._data['drinks']
        return choice(drinks)


class Hardware(object):
    """Class for generate data about hardware."""

    @staticmethod
    def resolution():
        """Get a random screen resolution.

        :return: Resolution of screen.
        :Example:
            1280x720.
        """
        return choice(RESOLUTIONS)

    @staticmethod
    def screen_size():
        """Get a random size of screen in inch.

        :return: Screen size.
        :Example:
            13″.
        """
        return choice(SCREEN_SIZES)

    @staticmethod
    def cpu():
        """Get a random CPU name.

        :return: CPU name.
        :Example:
            Intel® Core i7.
        """
        return choice(CPU)

    @staticmethod
    def cpu_frequency():
        """Get a random frequency of CPU.

        :return: Frequency of CPU.
        :Example:
            4.0 GHz.
        """
        cf = uniform(1.5, 4.3)
        return "{0:.1f}GHz".format(cf)

    @staticmethod
    def generation(abbr=False):
        """Get a random generation.

        :return: Generation of something.
        :Example:
             6th Generation.
        """
        if not abbr:
            return choice(GENERATION)

        return choice(GENERATION_ABBR)

    @staticmethod
    def cpu_codename():
        """Get a random CPU code name.

        :return: CPU code name.
        :Example:
            Cannonlake.
        """
        return choice(CPU_CODENAMES)

    @staticmethod
    def ram_type():
        """Get a random RAM type.

        :return: Type of RAM.
        :Example:
            DDR3.
        """
        ram_types = ('DDR2', 'DDR3', 'DDR4')
        return choice(ram_types)

    @staticmethod
    def ram_size():
        """Get a random size of RAM.

        :return: RAM size.
        :Example:
            16GB.
        """
        sizes = ('4', '6', '8', '16', '32', '64')
        return choice(sizes) + 'GB'

    @staticmethod
    def ssd_or_hdd():
        """Get a random value from list.

        :return: HDD or SSD.
        :Example:
            512GB SSD.
        """
        return choice(HDD_SSD)

    @staticmethod
    def graphics():
        """Get a random graphics.

        :return: Graphics.
        :Example:
            Intel® Iris™ Pro Graphics 6200.
        """
        return choice(GRAPHICS)

    @staticmethod
    def manufacturer():
        """Get a random manufacturer.

        :return: Manufacturer.
        :Example:
            Dell.
        """
        return choice(MANUFACTURERS)

    @staticmethod
    def phone_model():
        """Get a random phone model.

        :return: Phone model.
        :Example:
            Nokia Lumia 920.
        """
        return choice(PHONE_MODELS)


class ClothingSizes(object):
    """Class for generate clothing sizes data"""

    @staticmethod
    def international():
        """Get a random size in international format.

        :return: Clothing size.
        :Example:
            XXL.
        """
        sizes = (
            "L", "M", "S",
            "XL", "XS", "XXL",
            "XXS", "XXXL"
        )

        return choice(sizes)

    @staticmethod
    def european():
        """Generate a random clothing size in European format.

        :return: Clothing size.
        :Example:
            42
        """
        size = choice([i for i in range(40, 62) if i % 2 == 0])
        return size

    @staticmethod
    def custom(minimum=40, maximum=62):
        """Generate clothing size using custom format.

        :param minimum: Min value.
        :param maximum: Max value
        :return: Clothing size.
        :Example:
            44
        """
        return randint(int(minimum), int(maximum))


class Internet(object):
    """Class for generate the internet data."""

    @staticmethod
    def content_type(mime_type='application'):
        """Get a random HTTP content type.

        :return: Content type.
        :Example:
            Content-Type: application/json
        """
        fmt = File.mime_type(type_t=mime_type)
        return 'Content-Type: {}'.format(fmt)

    @staticmethod
    def http_status_code(code_only=True):
        """Get a random HTTP status.

        :param code_only: Return only http status code.
        :return: HTTP status.
        :Example:
            200 OK
        """
        status = choice(HTTP_STATUS_CODES)

        if code_only:
            return status.split()[0]
        return status

    @staticmethod
    def http_method():
        """Get a random HTTP method.

        :return: HTTP method.
        :Example:
            POST
        """
        return choice(HTTP_METHODS)

    @staticmethod
    def ip_v4():
        """Generate a random IPv4 address.

        :return: Random IPv4 address.
        :Example:
            19.121.223.58
        """
        ip = '.'.join([str(randint(0, 255)) for _ in range(4)])
        return ip

    @staticmethod
    def ip_v6():
        """Generate a random IPv6 address.

        :return: Random IPv6 address.
        :Example:
            2001:c244:cf9d:1fb1:c56d:f52c:8a04:94f3
        """
        ip = "2001:" + ":".join("%x" % randint(0, 16 ** 4) for _ in range(7))
        return ip

    @staticmethod
    def mac_address():
        """Generate a random MAC address.

        :return: Random MAC address.
        :Example:
            00:16:3e:25:e7:b1
        """
        mac_hex = [0x00, 0x16, 0x3e,
                   randint(0x00, 0x7f),
                   randint(0x00, 0xff),
                   randint(0x00, 0xff)
                   ]
        mac = map(lambda x: "%02x" % x, mac_hex)
        return ':'.join(mac)

    @staticmethod
    def emoji():
        """Get a random emoji shortcut code.

        :return: Emoji code.
        :Example:
            :kissing:
        """
        return choice(EMOJI)

    @staticmethod
    def image_placeholder(width='400', height='300'):
        """Generate a link to the image placeholder.

        :param width: Width of image.
        :param height: Height of image.
        :return: URL to image placeholder.
        """
        url = 'http://placehold.it/%sx%s'
        return url % (width, height)

    @staticmethod
    def stock_image(category=None, width=1900, height=1080):
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
            category = choice(categories)

        return url.format(category=category, width=width, height=height)

    @staticmethod
    def image_by_keyword(keyword=None):
        url = 'https://source.unsplash.com/weekly?{keyword}'

        keywords = [
            'cat', 'girl', 'boy', 'beauty',
            'nature', 'woman', 'man', 'tech',
            'space'
        ]

        if not keyword:
            keyword = choice(keywords)

        return url.format(keyword=keyword)

    @staticmethod
    def hashtags(quantity=4, category='general'):
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
            return choice(hashtags)

        tags = [choice(hashtags) for _ in range(int(quantity))]
        return tags

    @staticmethod
    def home_page(gender='female'):
        """Generate a random home page.

        :param gender: Gender of author of site.
        :return: Random home page.
        :Example:
            http://www.font6.info
        """
        url = 'http://www.' + Personal.username(gender)
        domain = choice(DOMAINS)
        return '{}{}'.format(url, domain)

    @staticmethod
    def subreddit(nsfw=False, full_url=False):
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
                return choice(SUBREDDITS)
            else:
                return url + choice(SUBREDDITS)

        nsfw_sr = choice(SUBREDDITS_NSFW)
        result = url + nsfw_sr if full_url else nsfw_sr
        return result

    @staticmethod
    def user_agent():
        """Get a random user agent.

        :return: User agent.
        :Example:
            Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0)
            Gecko/20100101 Firefox/15.0.1
        """
        return choice(USER_AGENTS)

    @staticmethod
    def network_protocol(layer='application'):
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
            protocol = choice(NETWORK_PROTOCOLS[layer])
            return protocol
        except KeyError:
            raise WrongArgument(
                'Unsupported layer, use: {}'.format(list(NETWORK_PROTOCOLS.keys())))


class Transport(object):
    """Class that provides dummy data about transport."""

    def __init__(self):
        self._model = Code.custom_code

    def truck(self, model_mask='#### @@'):
        """Generate a truck model.

        :param model_mask: Mask of truck model. Here '@' is a \
        placeholder of characters and '#' is a placeholder of digits.
        :return: Dummy truck model.
        :Example:
            Caledon-966O.
        """
        model = self._model(mask=model_mask)
        truck = choice(TRUCKS)
        return '%s-%s' % (truck, model)

    @staticmethod
    def car():
        """Get a random vehicle.

        :return: A vehicle.
        :Example:
            Tesla Model S.
        """
        return choice(CARS)

    def airplane(self, model_mask='###'):
        """Generate a dummy airplane model.

        :param model_mask: Mask of truck model. Here '@' is a \
        placeholder of characters and '#' is a placeholder of digits.
        :return:
        :Example:
            Boeing 727.
        """
        model = self._model(mask=model_mask)
        plane = choice(AIRPLANES)
        return '%s %s' % (plane, model)


class Path(object):
    """Class that provides methods and property for generate paths."""

    def __init__(self):
        self.__p = Personal('en')

    @property
    def root(self):
        """Generate a root dir path.

        :return: Root dir.
        :Example:
            /
        """
        if sys.platform == 'win32':
            return 'С:\\'
        else:
            return '/'

    @property
    def home(self):
        """Generate a home path.

        :return: Home path.
        :Example:
            /home/
        """
        if sys.platform == 'win32':
            return self.root + 'Users\\'
        else:
            return self.root + 'home/'

    def user(self, gender='female'):
        """Generate a random user.

        :param gender: Gender of user.
        :return: Path to user.
        :Example:
            /home/oretha
        """
        user = self.__p.name(gender)
        user = user.capitalize() if \
            sys.platform == 'win32' else user.lower()
        return self.home + user

    def users_folder(self, user_gender='female'):
        """Generate a random path to user's folders.

        :return: Path.
        :Example:
            /home/taneka/Pictures
        """
        folder = choice(FOLDERS)
        user = self.user(user_gender)
        return os.path.join(user, folder)

    def dev_dir(self, user_gender='female'):
        """Generate a random path to development directory.

        :param user_gender: Path to dev directory.
        :return: Path.
        :Example:
            /home/sherrell/Development/Python/mercenary
        """
        dev_folder = choice(['Development', 'Dev'])
        stack = choice(PROGRAMMING_LANGS)
        user = self.user(user_gender)

        return os.path.join(user, dev_folder, stack)

    def project_dir(self, user_gender='female'):
        """Generate a random path to project directory.

        :param user_gender: Gender of user.
        :return: Path to project.
        :Example:
            /home/sherika/Development/Falcon/mercenary
        """
        project = choice(PROJECT_NAMES)
        return os.path.join(
            self.dev_dir(user_gender), project)


class UnitSystem(object):
    """Class for generating name of unit.
    """

    @staticmethod
    def mass(symbol=False):
        """Get a mass unit name.

        :param symbol: Symbol of unit.
        :return: Mass unit name.
        :Example:
            gr
        """
        if not symbol:
            return 'gram'
        return 'gr'

    @staticmethod
    def information(symbol=False):
        if not symbol:
            return 'byte'
        return 'b'

    @staticmethod
    def thermodynamic_temperature(symbol=False):
        """Get the thermodynamic temperature unit name.

        :param symbol: Symbol of unit.
        :return: Thermodynamic temperature unit name
        :Example:
            K
        """
        if not symbol:
            return 'kelvin'
        return 'K'

    @staticmethod
    def amount_of_substance(symbol=False):
        """Get unit name of amount of substance.

        :param symbol: Symbol of unit.
        :return: Unit name of amount of substance.
        :Example:
            mol
        """
        if not symbol:
            return 'mole'
        return 'mol'

    @staticmethod
    def angle(symbol=False):
        """Get unit name of angle.

        :param symbol: Symbol of unit.
        :return: Unit name of angle.
        :Example:
            radian
        """
        if not symbol:
            return 'radian'
        return 'r'

    @staticmethod
    def solid_angle(symbol=False):
        """Get unit name if solid angle

        :param symbol: Symbol of unit.
        :return: Unit name of solid angle
        :Example:
            ㏛
        """
        if not symbol:
            return 'steradian'
        return '㏛'

    @staticmethod
    def frequency(symbol=False):
        """Get unit name of frequency.

        :param symbol: Symbol of unit.
        :return: Unit name if frequency.
        :Example:
            Hz
        """
        if not symbol:
            return 'hertz'
        return 'Hz'

    @staticmethod
    def force(symbol=False):
        """Get unit name of fore.

        :param symbol:  Symbol of unit.
        :return:  Unit name of force.
        :Example:
            N
        """
        if not symbol:
            return 'newton'
        return 'N'

    @staticmethod
    def pressure(symbol=False):
        """Get unit name of pressure.

        :param symbol: Symbol of unit.
        :return: Unit name of pressure.
        :Example:
            pascal
        """
        if not symbol:
            return 'pascal'
        return 'P'

    @staticmethod
    def energy(symbol=False):
        """Get unit name of energy.

        :param symbol: Symbol of unit.
        :return: Unit name of energy.
        :Example:
            J
        """
        if not symbol:
            return 'joule'
        return 'J'

    @staticmethod
    def power(symbol=False):
        """Get unit name of power.

        :param symbol: Symbol of unit.
        :return: Unit name of power.
        :Example:
            watt
        """
        if not symbol:
            return 'watt'
        return 'W'

    def flux(self, symbol=True):
        return self.power(symbol)

    @staticmethod
    def electric_charge(symbol=False):
        """Get unit name of electric charge.

        :param symbol: Symbol of unit.
        :return: Unit name of electric charge.
        :Example:
            coulomb
        """
        if not symbol:
            return 'coulomb'
        return 'C'

    @staticmethod
    def voltage(symbol=False):
        """Get unit name of voltage.

        :param symbol: Symbol of unit.
        :return: Unit name of voltage.
        :Example:
            volt
        """
        if not symbol:
            return 'volt'
        return 'V'

    @staticmethod
    def electric_capacitance(symbol=False):
        """Get unit name of electric capacitance.

        :param symbol: Symbol of unit.
        :return: Unit name of electric capacitance.
        :Example:
            F
        """
        if not symbol:
            return 'farad'
        return 'F'

    @staticmethod
    def electric_resistance(symbol=False):
        """Get name of electric resistance.

        :param symbol: Symbol of unit.
        :return: Name of electric resistance.
        :Example:
            Ω
        """
        if not symbol:
            return 'ohm'
        return 'Ω'

    def impedance(self, symbol=False):
        return self.electric_resistance(symbol)

    def reactance(self, symbol=False):
        return self.electric_resistance(symbol)

    @staticmethod
    def electrical_conductance(symbol=False):
        """Get unit name of electrical conductance.

        :param symbol: Symbol of unit.
        :return: Unit name of electrical conductance.
        :Example:
            siemens
        """
        if not symbol:
            return 'siemens'
        return 'S'

    @staticmethod
    def magnetic_flux(symbol=False):
        """Get unit name of magnetic flux.

        :param symbol: Symbol of unit.
        :return: Unit name of magnetic flux.
        :Example:
            Wb
        """
        if not symbol:
            return 'weber'
        return 'Wb'

    @staticmethod
    def magnetic_flux_density(symbol=False):
        """Get unit name of magnetic flux density.

        :param symbol: Symbol of unit.
        :return: Unit name of magnetic flux density.
        :Example:
            tesla
        """
        if not symbol:
            return 'tesla'
        return 'T'

    @staticmethod
    def inductance(symbol=False):
        """Get unit name of inductance.

        :param symbol: Symbol of unit.
        :return: Unit name of inductance.
        :Example:
            H
        """
        if not symbol:
            return 'henry'
        return 'H'

    @staticmethod
    def temperature(symbol=False):
        """Get unit name of temperature.

        :param symbol:
        :return:
        """
        if not symbol:
            return 'Celsius'
        return '°C'

    @staticmethod
    def radioactivity(symbol=False):
        """Get unit name of radioactivity.

        :param symbol: Symbol of unit.
        :return: Unit name of radioactivity.
        :Example:
            Bq
        """
        if not symbol:
            return 'becquerel'
        return 'Bq'

    @staticmethod
    def prefix(sign='positive', symbol=False):
        """Get a random prefix for the International System of Units (SI)

        :param sign: Sing of number (positive, negative)
        :param symbol: Return symbol of prefix.
        :return: Prefix for SI.
        :rtype: str
        :Example:
            mega
        """
        sign = sign.lower()

        if symbol:
            prefixes = SI_PREFIXES['_sym_']
        else:
            prefixes = SI_PREFIXES

        try:
            return choice(prefixes[sign])
        except KeyError:
            raise WrongArgument(
                "Unsupported sign. Use: 'positive' or 'negative'")


class Generic(object):
    """A lazy initialization of locale for all classes that have locales."""

    # (Priority: high)
    # TODO: Update this class using __getattr__ or add the other
    # more acceptable mechanism.

    def __init__(self, locale):
        """
        :param locale: Current locale.
        """
        self.locale = locale
        self._personal = Personal
        self._address = Address
        self._datetime = Datetime
        self._business = Business
        self._text = Text
        self._food = Food
        self._science = Science
        self._code = Code
        self.unit_system = UnitSystem()
        self.file = File()
        self.numbers = Numbers()
        self.development = Development()
        self.hardware = Hardware()
        self.clothing_sizes = ClothingSizes()
        self.internet = Internet()
        self.transport = Transport()
        self.path = Path()

    def __str__(self):
        return '{}:{}:{}'.format(
            self.__class__.__name__,
            self.locale,
            locale_info(self.locale)
        )

    def add_provider(self, cls):
        if inspect.isclass(cls):
            name = ''
            if hasattr(cls, 'Meta'):
                if inspect.isclass(cls.Meta) and hasattr(cls.Meta, 'name'):
                    name = cls.Meta.name
            else:
                name = cls.__name__.lower()
            setattr(self, name, cls())
        else:
            raise TypeError("Provider must be a class")

    @property
    def personal(self):
        if callable(self._personal):
            self._personal = self._personal(self.locale)
        return self._personal

    @property
    def address(self):
        if callable(self._address):
            self._address = self._address(self.locale)
        return self._address

    @property
    def datetime(self):
        if callable(self._datetime):
            self._datetime = self._datetime(self.locale)
        return self._datetime

    @property
    def business(self):
        if callable(self._business):
            self._business = self._business(self.locale)
        return self._business

    @property
    def text(self):
        if callable(self._text):
            self._text = self._text(self.locale)
        return self._text

    @property
    def food(self):
        if callable(self._food):
            self._food = self._food(self.locale)
        return self._food

    @property
    def science(self):
        if callable(self._science):
            self._science = self._science(self.locale)
        return self._science

    @property
    def code(self):
        if callable(self._code):
            self._code = self._code(self.locale)
        return self._code
