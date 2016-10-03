# -*- coding: utf-8 -*-
"""
:copyright: (c) 2016 by Lk Geimfari.
:software_license: MIT, see LICENSES for more details.
"""

from datetime import date
from random import choice, sample, randint, uniform
from string import digits, ascii_letters

import church._common as common
from .utils import pull

# pull - is internal function,
# please do not use this function outside the module 'church'.

__all__ = ['Address', 'Personal',
           'Text', 'Network',
           'Datetime', 'File',
           'Science', 'Development',
           'Food', 'Hardware'
           ]


class Address(object):
    """
    Class for generate fake address data.
    """

    def __init__(self, lang='en_us'):
        self.lang = lang.lower()

    @staticmethod
    def street_number():
        """
        Generate a random street number.
        :return: Street number.
        """
        number = sample(digits, int(choice(digits[1:4])))
        return ''.join(number)

    def street_name(self):
        """
        Get a random street name.
        :return: Street name.
        """
        return choice(pull('street', self.lang)).strip()

    def street_suffix(self):
        """
        Get a random street suffix.
        :return: Street suffix. Example: Street.
        """
        return choice(pull('street_suffix', self.lang)).strip()

    def address(self):
        """
        Get a random full address.
        :return: Full address (include Street number, suffix and name).
        """
        if self.lang == 'ru_ru':
            return '{} {} {}'.format(
                self.street_suffix(),
                self.street_name(),
                self.street_number()
            )
        else:
            return '{} {} {}'.format(
                self.street_number(),
                self.street_name(),
                self.street_suffix()
            )

    def state(self):
        """
        Get a random states or subject of country.
        For locale 'ru_ru' always will be getting subject of Russia.
        :return: State of current country. Example (en_us): Alabama
        """
        return choice(pull('states', self.lang)).strip()

    def postal_code(self):
        """
        Get a random postal code.
        :return: postal code. Example: 389213
        """
        if self.lang == 'ru_ru':
            return randint(100000, 999999)
        return randint(10000, 99999)

    def country(self, only_iso_code=False):
        """
        Get a random country.
        :param only_iso_code: Return only ISO code of country.
        :return: Country. Example: Russia
        """
        country_name = choice(pull('countries', self.lang)).split('|')
        if only_iso_code:
            return country_name[0].strip()
        return country_name[1].strip()

    def city(self):
        """
        Get a random name of city.
        :return: City name. Example (for ru_ru): Saint Petersburg
        """
        return choice(pull('cities', self.lang)).strip()


class Text(object):
    """
    Class for generate text data, i.e text, lorem ipsum and another.
    """

    def __init__(self, lang='en_us'):
        self.lang = lang.lower()

    def lorem_ipsum(self, quantity=5):
        """
        Get random strings. Not only lorem ipsum.
        :param quantity: Quantity of sentence.
        :return: Text.
        """
        if not isinstance(quantity, int):
            raise TypeError('lorem_ipsum takes only integer type')
        else:
            text = ''
            for _ in range(quantity):
                text += choice(pull('text', self.lang)).replace('\n', ' ')
            return text.strip()

    def sentence(self):
        """
        Get a random sentence from text.
        :return: Sentence.
        """
        return self.lorem_ipsum(quantity=1)

    def title(self):
        """
        Get a random title.
        :return: Title. Example: Erlang - is a general-purpose,
        concurrent, functional programming language.
        """
        return self.lorem_ipsum(quantity=1)

    def words(self, quantity=5):
        """
        Get the random words.
        :param quantity: Quantity of words. Default is 5.
        :return: Words. Example: science, network, god, octopus, love
        """
        if not isinstance(quantity, int):
            raise TypeError('words takes only integer type')
        else:
            words_list = []
            for _ in range(quantity):
                words_list.append(choice(pull('words', self.lang)).strip())
            return words_list

    def word(self):
        """
        Get a random word.
        :return: Single word. Example: science
        """
        return self.words(quantity=1)[0]

    def swear_word(self):
        """
        Get a random swear word.
        :return: Swear word.
        """
        _word = choice(pull('swear_words', self.lang))
        return _word.strip()

    @staticmethod
    def naughty_strings():
        """
        Get a random naughty string form file.
        Authors of big-list-of-naughty-strings is Max Woolf and contributors.
        Thank you to all who have contributed in big-list-of-naughty-strings.
        Repository: https://github.com/minimaxir/big-list-of-naughty-strings
        :return: The list of naughty strings.
        """
        import os.path as op
        path = op.abspath(op.join(op.dirname(__file__), 'data'))

        with open(op.join(path + '/other', 'naughty_strings'), 'r') as f:
            naughty_list = [x.strip(u'\n') for x in f.readlines()]

        return naughty_list

    def quote_from_movie(self):
        """
        Get a random quotes from movie.
        :return: Quote from movie. Example: "Bond... James Bond."
        """
        return choice(pull('quotes', self.lang)).strip()

    @staticmethod
    def currency_iso():
        """
        Get a currency code. ISO 4217 format.
        :return: Currency code. Example: RUR
        """
        return choice(common.CURRENCY)

    def color(self):
        """
        Get a random name of color.
        :return: Color name. Example: Red
        """
        return choice(pull('colors', self.lang)).strip()

    @staticmethod
    def hex_color():
        """
        Generate a hex color.
        :return: Hex color code. Example: #D8346B
        """
        letters = '0123456789ABCDEF'
        color_code = '#' + ''.join(sample(letters, 6))
        return color_code

    def company_type(self, abbreviated=False):
        """
        Get a random company type.
        :param abbreviated: if True then abbreviated company type.
        :return: Company type. Example: Inc.
        """
        _type = choice(pull('company_type', self.lang)).split('|')
        if abbreviated:
            return _type[1].strip()
        return _type[0].strip()

    def company(self):
        """
        Get a random company name.
        :return: Company name. Example: Gamma Systems
        """
        company = choice(pull('company', self.lang))
        return company.strip()

    def copyright(self, from_=1990, to_=2016, without_date=False):
        """
        Generate a random copyright.
        :param from_: foundation date
        :param to_: current date
        :param without_date: if True then will be returned
        copyright without date.
        :return: Copyright of company. Example: © 1990-2016 Komercia, Inc.
        """
        founded = randint(int(from_), int(to_))
        company = self.company()
        company_type = self.company_type(abbreviated=True)
        if without_date:
            return '© {}, {}'.format(company, company_type)
        return '© {0}-{1} {2}, {3}'.format(founded, to_, company, company_type)

    @staticmethod
    def emoji():
        """
        Get a random EMOJI shortcut code.
        :return: Emoji code. Example: :kissing:
        """
        return choice(common.EMOJI)

    @staticmethod
    def image_placeholder(width='400', height='300'):
        url = 'http://placehold.it/{0}x{1}'.format(width, height)
        return url


class Personal(object):
    """
    Class for generate personal data, i.e names, surnames, age and another.
    """

    def __init__(self, lang='en_us'):
        self.lang = lang.lower()

    @staticmethod
    def age(minimum=16, maximum=66):
        """
        Get a random integer value.
        :param maximum: max age
        :param minimum: min age
        :return: Random integer from minimum=16 to maximum=66
        """
        return randint(int(minimum), int(maximum))

    def name(self, gender='f'):
        """
        Get a random name.
        :param gender: if 'm' then will getting male name else female name.
        :return: Name. Example (gender='m'): John Abbey
        """
        if not isinstance(gender, str):
            raise TypeError('name takes only string type')

        _filename = 'f_names' if gender.lower() == 'f' else 'm_names'
        return choice(pull(_filename, self.lang)).strip()

    def surname(self, gender='f'):
        """
        Get a random surname.
        :param gender: if 'm' then will getting male surname else
        female surname.
        :return: Surname. Example: Smith
        """
        if not isinstance(gender, str):
            raise TypeError('surname takes only string type')

        if self.lang == 'ru_ru':
            _file = 'm_surnames' if gender == 'm' else 'f_surnames'
            return choice(pull(_file, self.lang)).strip()

        return choice(pull('surnames', self.lang)).strip()

    def full_name(self, gender='f', reverse=False):
        """
        Get a random full name.
        :param reverse: if true: surname/name else name/surname
        :param gender: if gender='m' then will be returned male name else
        female name.
        :return: Full name. Example: Johann Wolfgang
        """
        _sex = gender.lower()
        if reverse:
            return '{0} {1}'.format(self.surname(_sex), self.name(_sex))
        return '{0} {1}'.format(self.name(_sex), self.surname(_sex))

    @staticmethod
    def username(gender='m'):
        """
        Get a random username with digits.
        Username generated from en_us names for all locales.
        :return: Username. For example: abby101
        """

        _file_name = 'f_names' \
            if gender.lower() == 'f' else 'm_names'

        _u = choice(pull(_file_name)).replace(' ', '_')
        return _u.strip().lower() + str(randint(2, 9999))

    @staticmethod
    def twitter(gender='m'):
        """
        Get a random twitter user.
        :param gender:
        :return: URL to user. Example: http://twitter.com/someuser12
        """
        url = "http://twitter.com/{0}"
        _t = Personal.username(gender.lower())
        return url.format(_t)

    @staticmethod
    def facebook(gender='m'):
        """
        Generate a random facebook user.
        :param gender: gender of user.
        :return: URL to user.
        Example: https://facebook.com/some.user
        """
        url = 'https://facebook.com/{0}'
        _f = Personal.username(gender.lower())
        return url.format(_f)

    @staticmethod
    def password(length=8, algorithm=''):
        """
        Generate a password or hash of password.
        :param length: length of password.
        :param algorithm: hashing algorithm.
        :return: Password or hash of password.
        """
        import hashlib
        _punc = '!"#$%+:<?@^_'
        _str = [choice(ascii_letters + digits + _punc) for _ in range(length)]
        _pass = "".join(_str)
        if algorithm.lower() == 'sha1':
            return hashlib.sha1(_pass.encode()).hexdigest()
        elif algorithm.lower() == 'sha256':
            return hashlib.sha256(_pass.encode()).hexdigest()
        elif algorithm.lower() == 'sha512':
            return hashlib.sha512(_pass.encode()).hexdigest()
        elif algorithm.lower() == 'md5':
            return hashlib.md5(_pass.encode()).hexdigest()
        else:
            return _pass

    @staticmethod
    def email(gender='f'):
        """
        Generate a random email using usernames.
        :param gender: gender of user.
        :return: Email address. Example: foretime10@live.com
        """
        gender = 'm' if gender.lower() == 'm' else 'f'
        name = Personal.username(gender=gender)
        email_adders = name + choice(common.EMAIL_DOMAINS)
        return email_adders.strip()

    def home_page(self):
        """
        Generate a random home page using usernames.
        :return: Random home page. Example: http://www.font6.info
        """
        username = self.username().replace(' ', '-')
        url = 'http://www.' + username
        return url + choice(pull('domains', 'en_us')).strip()

    @staticmethod
    def subreddit(nsfw=False, full_url=False):
        """
        Get a random subreddit from list.
        :param nsfw: if True then will be returned NSFW subreddit.
        :param full_url: If true http://www.reddit.com/r/subreddit
        else /r/subreddit
        :return: Subreddit or URL to subreddit.
        """
        url = 'http://www.reddit.com'
        if nsfw:
            if full_url:
                return url + choice(common.SUBREDDITS_NSFW)
            else:
                return choice(common.SUBREDDITS_NSFW)
        _subreddit = choice(common.SUBREDDITS)
        _r = url + _subreddit if full_url else _subreddit
        return _r

    @staticmethod
    def bitcoin():
        """
        Get a random bitcoin address.
        Currently supported only two address formats that are most popular.
        It's 'P2PKH' and 'P2SH'
        :return: Bitcoin address. Example: 3EktnHQD7RiAE6uzMj2ZifT9YgRrkSgzQX
        """
        _fmt = choice(['1', '3'])
        _fmt += "".join([choice(ascii_letters + digits) for _ in range(33)])
        return _fmt

    @staticmethod
    def cvv():
        """
        Generate a random card verification value (CVV)
        :return: CVV code
        """
        return randint(100, 999)

    @staticmethod
    def credit_card_number(card_type='visa'):
        """
        Generate a random credit card number.
        :param card_type: Issuing Network. Default is Visa
        :return: Credit card number. Example: 4455 5299 1152 2450
        """
        visa = randint(4000, 4999)
        mc = choice([randint(2221, 2720), randint(5100, 5500)])

        # Issuer identification number.
        # Read more: http://bit.ly/2dBhNcX
        iin = mc if card_type.lower() == 'mastercard' or 'mc' else visa

        tail = ''.join([str(randint(0000, 9999)) for _ in range(0, 3)])
        return '{0} {1}'.format(str(iin), tail)

    @staticmethod
    def credit_card_expiration_date(from_=16, to_=25):
        """
        Generate a random expiration date for credit card.
        :param from_: date of issue.
        :param to_: maximum of expiration_date.
        :return: Expiration date of credit card. Example: 03/19.
        """
        month = randint(1, 12)
        year = randint(int(from_), int(to_))
        month = '0' + str(month) if month < 10 else month
        return '{0}/{1}'.format(month, year)

    @staticmethod
    def cid():
        """
        Generate a random CID code.
        :return: CID code.
        """
        return randint(1000, 9999)

    @staticmethod
    def wmid():
        """
        Generate a identifier of user WMID for WebMoney
        :return: WMID (WebMoney ID). Example: 834296404761
        """
        return "".join([choice(digits) for _ in range(12)])

    def paypal(self):
        """
        Generate a random PayPal account.
        :return: Email of PapPal user. Example: wolf235@gmail.com
        """
        return self.email()

    @staticmethod
    def yandex_money():
        """
        Generate a random Yandex.Money account.
        :return: Yandex.Money account.
        """
        return "".join([choice(digits) for _ in range(14)])

    def gender(self, abbreviated=False):
        """
        Get a random gender.
        :param abbreviated: if True then will getting abbreviated gender title.
        For example: M or F
        :return: Title of gender. Example: Male.
        """
        if abbreviated:
            return choice(pull('gender', self.lang))[0:1]
        return choice(pull('gender', self.lang)).strip()

    @staticmethod
    def height(from_=1.5, to_=2.0):
        """
        Generate a random height in M.
        :param from_: min value
        :param to_: max value
        :return: Height. Example: 1.85.
        """
        h = uniform(float(from_), float(to_))
        return '{:0.2f}'.format(h)

    @staticmethod
    def weight(from_=38, to_=90):
        """
        Generate a random weight in KG.
        :param from_: min value
        :param to_: max value
        :return: Weight. Example: 74.
        """
        w = randint(int(from_), int(to_))
        return w

    def sexual_orientation(self):
        """
        Get a random (LOL) sexual orientation.
        :return: Sexual orientation. Example: Heterosexuality.
        """
        so = choice(pull('sexual_orientation', self.lang))
        return so.strip()

    def profession(self):
        """
        Get a random profession.
        :return: The name of profession. Example: Programmer.
        """
        return choice(pull('professions', self.lang)).strip()

    def political_views(self):
        """
        Get a random political views.
        :return: Political views. Example: Liberal.
        """
        return choice(pull('political_views', self.lang)).strip()

    def worldview(self):
        """
        Get a random worldview.
        :return: Worldview. Example: Pantheism.
        """
        return choice(pull('worldview', self.lang)).strip()

    def views_on(self):
        """
        Get a random views on.
        :return: Views on string. Example: Negative.
        """
        return choice(pull('views_on', self.lang)).strip()

    def nationality(self, gender='f'):
        """
        Get a random nationality.
        :param gender: female or male
        :return: Nationality. Example: Russian.
        """
        try:
            # Subtleties of the Russian orthography.
            if self.lang == 'ru_ru':
                i = 0 if gender.lower() == 'm' else 1
                return choice(pull('nation', self.lang)).split('|')[i].strip()
            else:
                return choice(pull('nation', self.lang)).strip()
        except Exception:
            raise TypeError('name takes only string type')

    def university(self):
        """
        Get a random university.
        :return: University name. Example: MIT.
        """
        return choice(pull('university', self.lang)).strip()

    def qualification(self):
        """
        Get a random qualification.
        :return: Degree. Example: Bachelor.
        """
        return choice(pull('qualifications', self.lang)).strip()

    def language(self):
        """
        Get a random language.
        :return: Random language. Example: Irish
        """
        return choice(pull('languages', self.lang)).strip()

    def favorite_movie(self):
        """
        Get a random movie.
        :return: Name of the movie.
        """
        return choice(pull('favorite_movie', self.lang)).strip()

    def __telephone_mask(self):
        """
        It's internal method.
        Return a mask of telephone for current locale.
        :return: mask. Example (ru_ru): '+7-(###)-###-##-##'
        """
        mask = ''
        if self.lang == 'ru_ru':
            mask = '+7-(###)-###-##-##'
        elif self.lang == 'fr_fr':
            mask = '+33-#########'
        elif self.lang == 'de_de':
            mask = '+49-#########'
        elif self.lang == 'en_us':
            mask = '+1-(###)-###-####'
        return mask

    def telephone(self, mask=None, placeholder='#'):
        """
        Generate a random phone number.
        :param mask: Mask for formatting number.
        :param placeholder: A Placeholder for a mask.
        :return: Phone number. Example: +7-(963)-409-11-22.
        """
        if not mask:
            mask = self.__telephone_mask()
        phone_number = ''
        for i in mask:
            if i == placeholder:
                phone_number += str(randint(1, 9))
            else:
                phone_number += i
        return phone_number.strip()

    @staticmethod
    def avatar():
        url = 'https://raw.githubusercontent.com/lk-geimfari/' \
              'church/master/examples/avatars/{0}.png'.format(randint(1, 7))
        return url


class Datetime(object):
    """
    Class for generate the fake data that you can use for
    working with date and time.
    """

    def __init__(self, lang='en_us'):
        self.lang = lang.lower()

    def day_of_week(self, abbreviated=False):
        """
        Get a random day of week.
        :param abbreviated: if True then will be returned abbreviated name
        of day of the week.
        :return: Name of day of the week.
        """
        _day = choice(pull('days', self.lang)).split('|')
        if abbreviated:
            return _day[1].strip()
        return _day[0].strip()

    def month(self, abbreviated=False):
        """
        Get a random month.
        :param abbreviated: if True then will be returned
        abbreviated month name.
        :return: Month name. Example: November.
        """
        _month = choice(pull('months', self.lang)).split('|')
        if abbreviated:
            return _month[1].strip()
        return _month[0].strip()

    @staticmethod
    def year(from_=1990, to_=2050):
        """
        Generate a random year.
        :param from_:
        :param to_:
        :return: Year. Example 2023.
        """
        return randint(int(from_), int(to_))

    def periodicity(self):
        """
        Get a random periodicity string.
        :return: Periodicity. Example: Never.
        """
        return choice(pull('periodicity', self.lang)).strip()

    @staticmethod
    def date(sep='-', with_time=False):
        """
        Generate a random date formatted as a 11-05-2016
        :param sep: a separator for date. Default is '-'.
        :param with_time: if it's True then will be added random time.
        :return: Formatted date and time: 20-03-2016 03:20.
        """
        _d = date(randint(2000, 2035), randint(1, 12), randint(1, 28))
        pattern = '%d{0}%m{0}%Y %m:%d' if with_time else '%d{0}%m{0}%Y'
        return _d.strftime(pattern.format(sep))

    @staticmethod
    def day_of_month():
        """
        Static method for generate a random days of month, from 1 to 31.
        :return: Random value from 1 to 31.
        """
        return randint(1, 31)


class Network(object):
    """
    Class for generate data for working with network,
    i.e IPv4, IPv6 and another
    """

    @staticmethod
    def ip_v4():
        """
        Static method for generate a random IPv4 address.
        :return: Random IPv4 address.
        """
        ip = '.'.join([str(randint(0, 255)) for _ in range(0, 4)])
        return ip.strip()

    @staticmethod
    def ip_v6():
        """
        Static method for generate a random IPv6 address.
        :return: Random IPv6 address.
        Example: 2001:c244:cf9d:1fb1:c56d:f52c:8a04:94f3
        """
        n = 16 ** 4
        ip = "2001:" + ":".join("%x" % randint(0, n) for _ in range(7))
        return ip

    @staticmethod
    def mac_address():
        """
        Static method for generate a random MAC address.
        :return: Random MAC address.
        Example: 00:16:3e:25:e7:b1
        """
        mac = [0x00, 0x16, 0x3e,
               randint(0x00, 0x7f),
               randint(0x00, 0xff),
               randint(0x00, 0xff)
               ]
        _mac = map(lambda x: "{:02x}".format(x), mac)
        return ':'.join(_mac)

    @staticmethod
    def user_agent():
        """
        Get a random user agent.
        :return: User agent.
        """
        u_agent = choice(pull('useragents', 'en_us'))
        return u_agent.strip()


class File(object):
    """
    Class for generate fake data for files.
     """

    @staticmethod
    def extension(file_type='text'):
        """
        Get a random extension from list.
        :param file_type: The type of extension. Default is text.
        All supported types:
            1. source - '.py', '.rb', '.cpp' and other.
            2. text = '.doc', '.log', '.rtf' and other.
            3. data = '.csv', '.dat', '.pps' and other.
            4. audio = '.mp3', '.flac', '.m4a' and other.
            5. video = '.mp4', '.m4v', '.avi' and other.
            6. image = '.jpeg', '.jpg', '.png' and other.
            7. executable = '.exe', '.apk', '.bat' and other.
            8. compressed = '.zip', '.7z', '.tar.xz' and other.
        :return: Extension of a file. Example (file_type='source'): .py
        """
        _type = file_type.upper()

        return choice(common.EXTENSIONS[_type])


class Science(object):
    """
    Class for getting facts science.
    """

    def __init__(self, lang='en_us'):
        self.lang = lang.lower()

    @staticmethod
    def math_formula():
        """
        Get a random mathematical formula.
        :return: Math formula. For example: A = (ab)/2
        """
        formula = choice(common.MATH_FORMULAS)
        return formula.strip()

    def chemical_element(self, name_only=True):
        """
        Get a random chemical element from file.
        :param name_only: if False then will be returned dict.
        :return: Name of chemical element or dict.
        Example: {'Symbol': 'S',
                  'Name': 'Sulfur',
                  'Atomic number': '16'
                }
           or name of chemical element: 'Helium'
        """
        _e = choice(pull('chemical_elements', self.lang)).split('|')
        if not name_only:
            return {'name': _e[0].strip(),
                    'symbol': _e[1].strip(),
                    'atomic_number': _e[2].strip()
                    }
        else:
            return _e[0]

    def article_on_wiki(self):
        """
        Get a random link to scientific article on Wikipedia.
        :return: Link to article on Wikipedia.
        Example: https://en.wikipedia.org/wiki/Black_hole
        """
        article = choice(pull('science_wiki', self.lang))
        return article.strip()

    def scientist(self):
        """
        Get a random name of scientist.
        :return: Name of scientist. Example: Konstantin Tsiolkovsky
        """
        scientist_name = choice(pull('scientist', self.lang))
        return scientist_name.strip()


class Development(object):
    """
    Class for getting fake data for Developers.
    """

    @staticmethod
    def software_license():
        """
        Get a random software license from list.
        :return:
        """
        return choice(common.LICENSES)

    @staticmethod
    def database(nosql=False):
        """
        Get a random database name.
        :param nosql: only NoSQL databases.
        :return: Database name. Example: PostgreSQL.
        """
        if nosql:
            return choice(common.NOSQL)
        return choice(common.SQL)

    @staticmethod
    def other():
        """
        Get a random value list.
        :return: Some other technology. Example: Nginx
        """
        return choice(common.OTHER_TECH)

    @staticmethod
    def programming_language():
        """
        Get a random programming language from list.
        :return: Programming language. Example: Erlang
        """
        return choice(common.PROGRAMMING_LANGS)

    @staticmethod
    def framework(_type='back'):
        """
        Get a random framework from file.
        :param _type: If _type='front' then will be returned
        front-end framework, else will be returned back-end framework.
        :return: Framework or dict of used stack: Example:  Python/Django.
        """
        if _type == 'front':
            return choice(common.FRONTEND)
        else:
            return choice(common.BACKEND)

    def stack_of_tech(self, nosql=False):
        """
        Get a random stack.
        :param nosql: if True the only NoSQL skills.
        :return: Dict of technologies.
        Example:      {'Back-end': 'Martini',
                      'DB': 'SQLite',
                      'Front-end': 'Webpack',
                      'Other': 'Martini'}
        """
        _stack = {
            'front-end': self.framework('front'),
            'back-end': self.framework('back'),
            'db': self.database(nosql),
            'other': self.other()
        }

        return _stack

    @staticmethod
    def os():
        """
        Get a random operating system or distributive name.
        :return: The name of OS. Example: Gentoo
        """
        return choice(common.OS)


class Food(object):
    """
    Class for Food, i.e fruits, vegetables, berries and other.
    """

    def __init__(self, lang):
        self.lang = lang.lower()

    def berry(self):
        """
        Get random berry.
        :return: Berry. Example: Blackberry
        """
        _berry = choice(pull('berries', self.lang))
        return _berry.strip()

    def vegetable(self):
        """
        Get a random vegetable.
        :return: Vegetable. Example: Tomato
        """
        _vegetable = choice(pull('vegetables', self.lang))
        return _vegetable.strip()

    def fruit(self):
        """
        Get a random fruit name.
        :return: Fruit. Example: Banana
        """
        _fruit = choice(pull('fruits', self.lang))
        return _fruit.strip()

    def dish(self):
        """
        Get a random dish for current locale.
        :return: Dish name. Example (ru_ru): Борщ
        """
        _dishes = choice(pull('dishes', self.lang))
        return _dishes.strip()

    def spices(self):
        """
        Get a random spices or herbs.
        :return: Spices or herbs.
        """
        result = choice(pull('spices', self.lang))
        return result.strip()

    def mushroom(self):
        """
        Get a random mushroom's name
        :return: Mushroom's name. Example: Marasmius oreades
        """
        result = choice(pull('mushrooms', self.lang))
        return result.strip()

    def alcoholic_drink(self):
        """
        Get a random alcoholic drink.
        :return: Alcoholic drink. Example: Vodka
        """
        _ad = choice(pull('alcoholic_drinks', self.lang))
        return _ad.strip()

    def cocktail(self):
        """
        Get a random cocktail.
        :return: Cocktail name.
        """
        _list = choice(pull('cocktails', self.lang))
        return _list.strip()


class Hardware(object):
    """
    Class for generate data about hardware.
    All available methods:
      1. resolution - resolution of screen
      2. screen_size - screen size in inch.
      3. cpu_frequency - cpu frequency.
      4. generation - generation of something.
      5. cpu_codename - codename of CPU.
      6. ram_type - type of RAM.
      7. ram_size - size of RAM in GB.
      8. ssd_or_hdd - get HDD or SSD.
      9. graphics - graphics.
      10. cpu - cpu name.
    """

    @staticmethod
    def resolution():
        """
        Get a random screen resolution.
        :return: Resolution of screen. Example: 1280x720.
        """
        return choice(common.RESOLUTIONS)

    @staticmethod
    def screen_size():
        """
        Get a random size of screen in inch.
        :return: Screen size. Example: 13″.
        """
        return choice(common.SCREEN_SIZES)

    @staticmethod
    def cpu():
        """
        Get a random CPU name.
        :return: CPU name. Example: Intel® Core i7
        """
        return choice(common.CPU)

    @staticmethod
    def cpu_frequency():
        """
        Get a random frequency of CPU.
        :return: frequency. Example: 4.0 GHz
        """
        _c = common.CPU_FREQUENCY
        return choice(_c) + ' GHz'

    @staticmethod
    def generation():
        """
        Get a random generation.
        :return: Generation of something.
        """
        _gn = common.GENERATION
        return choice(_gn)

    @staticmethod
    def cpu_codename():
        """
        Get a random CPU code name.
        :return: CPU code name. Example: .
        """
        _cn = common.CPU_CODENAMES
        return choice(_cn)

    @staticmethod
    def ram_type():
        """
        Get a random RAM type.
        :return: Type of RAM. Example: DDR3.
        """
        return choice(['DDR2', 'DDR3', 'DDR4'])

    @staticmethod
    def ram_size():
        """
        Get a random size of RAM.
        :return: RAM size. Example: 16GB.
        """
        return choice(['4', '6', '8', '16', '32']) + 'GB'

    @staticmethod
    def ssd_or_hdd():
        """
        Get a random value from list.
        :return: HDD or SSD. Example: 512GB HDD.
        """
        return choice(common.MEMORY)

    @staticmethod
    def graphics():
        """
        Get a random graphics.
        :return: Graphics. Example: Intel® Iris™ Pro Graphics 6200
        """
        return choice(common.GRAPHICS)

    @staticmethod
    def manufacturer():
        """
        Get a random manufacturer.
        :return: Manufacturer. Example: Dell
        """
        return choice(common.MANUFACTURERS)

    def hardware_full_info(self):
        """
        Get a random full information about device (laptop).
        :return: Full information. Example:
        ASUS Intel® Core i3 3rd Generation 3.50 GHz/1920x1200/12″/
        512GB HDD(7200 RPM)/DDR2-4GB/Intel® Iris™ Pro Graphics 6200
        """
        _full = '{0} {1} {2} {3}/{4}/{5}/{6}/{7}-{8}/{9}'.format(
            self.manufacturer(), self.cpu(),
            self.generation(), self.cpu_frequency(),
            self.resolution(), self.screen_size(),
            self.ssd_or_hdd(), self.ram_type(),
            self.ram_size(), self.graphics()
        )
        return _full

    @staticmethod
    def phone_model():
        """
        Get a random phone model.
        :return: Phone model. Example: Nokia Lumia 920
        """
        return choice(common.PHONE_MODELS)