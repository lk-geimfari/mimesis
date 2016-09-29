# -*- coding: utf-8 -*-
"""
:copyright: (c) 2016 by Lk Geimfari.
:software_license: MIT, see LICENSE for more details.
"""

from datetime import date
from random import choice, sample, randint
from string import digits, ascii_letters

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
        :return: street number
        """
        return ''.join(sample(digits, int(choice(digits[1:4]))))

    def street_name(self):
        """
        Get a random street name.
        :return: street name
        """
        return choice(pull('street', self.lang)).strip()

    def street_suffix(self):
        """
        Get a random street suffix.
        :return: street suffix. Example: Street.
        """
        return choice(pull('street_suffix', self.lang)).strip()

    def street_address(self):
        """
        Get a random full address.
        :return: full address.
        """
        if self.lang == 'ru_ru':
            return '{} {} {}'.format(
                self.street_suffix(),
                self.street_name(),
                Address.street_number()
            )
        else:
            return '{} {} {}'.format(
                Address.street_number(),
                self.street_name(),
                self.street_suffix()
            )

    def state(self):
        """
        Get a random states or subject of country.
        For locale 'ru_ru' always will be getting subject of RF.
        :return: state. Example: Alabama
        """
        return choice(pull('states', self.lang)).strip()

    def postal_code(self):
        """
        Get a random (real) postal code.
        :return: postal code. Example: 389213
        """
        return choice(pull('postal_codes', self.lang)).strip()

    def country(self, only_iso_code=False):
        """
        Get a random country.
        :param only_iso_code: Return only ISO code of country.
        :return: country. Example: Russia
        """
        country_name = choice(pull('countries', self.lang)).split('|')
        if only_iso_code:
            return country_name[0].strip()
        return country_name[1].strip()

    def city(self):
        """
        Get a random name of city.
        :return: city name. Example: Saint Petersburg
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
        :param quantity: quantity of sentence
        :return: text
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
        :return: sentence.
        """
        return self.lorem_ipsum(quantity=1)

    def title(self):
        """
        Get a random title.
        :return: title Example: Erlang - is a general-purpose,
        concurrent, functional programming language.
        """
        return self.lorem_ipsum(quantity=1)

    def words(self, quantity=5):
        """
        Get the random words.
        :param quantity: quantity of words. Default is 5.
        :return: words. Example: science, network, god, octopus, love
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
        :return: single word. Example: science
        """
        return self.words(quantity=1)[0]

    def swear_word(self):
        """
        Get a random swear word.
        :return: swear word
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
        :return: The list of naughty strings
        """
        import os.path as op
        PATH = op.abspath(op.join(op.dirname(__file__), 'data'))

        with open(op.join(PATH + '/other', 'bad_input'), 'r') as f:
            result = f.readlines()
            strings = [x.strip(u'\n') for x in result]
            naughty_list = strings

        return naughty_list

    def quote_from_movie(self):
        """
        Get a random quotes from movie.
        :return: quotes. Example: "Bond... James Bond."
        """
        return choice(pull('quotes', self.lang)).strip()

    @staticmethod
    def currency_iso():
        """
        Get a currency code. ISO 4217 format.
        :return: currency code. Example: RUR
        """
        return choice(pull('currency', 'en_us')).strip()

    def color(self):
        """
        Get a random name of color.
        :return: color name. Example: Red
        """
        return choice(pull('colors', self.lang)).strip()

    def company_type(self, abbreviated=False):
        """
        Get a random company type.
        :param abbreviated: if True then abbreviated company type.
        :return: company type. Example: Inc.
        """
        _type = choice(pull('company_type', self.lang)).split('|')
        if abbreviated:
            return _type[1].strip()
        return _type[0].strip()

    def company(self):
        """
        Get a random company name.
        :return: company name. Example: Intel
        """
        company = choice(pull('company', self.lang))
        return company.strip()

    @staticmethod
    def emoji():
        """
        Get a random emoji shortcut code.
        :return: emoji. Example: :kissing:
        """
        _shortcut = choice(pull('emoji', 'en_us'))
        return _shortcut.strip()

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
        :return: random integer from minimum=16 to maximum=66
        """
        return randint(int(minimum), int(maximum))

    def name(self, gender='f'):
        """
        Get a random name.
        :param gender: if 'm' then will getting male name else female name.
        :return: name. Example (gender='m'): John Abbey
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
        :return: surname. Example: Wolf
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
        :return: full name. Example: Johann Wolfgang
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
        :return: username. For example: abby101
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
        :param gender:
        :return: URL to user. Example: https://facebook.com/some.user
        """
        url = 'https://facebook.com/{0}'
        _f = Personal.username(gender.lower())
        return url.format(_f)

    @staticmethod
    def password(length=8, algorithm=''):
        """
        Generate a password or hash password.
        :param length: length of password
        :param algorithm: hashing algorithm
        :return: password or password hash
        """
        import hashlib
        _punc = '!"#$%+:<?@^_'
        _pass = "".join([choice(ascii_letters + digits + _punc) for _ in range(length)])
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
    def email():
        """
        Generate a random email using usernames.
        :return: email address. Example: foretime10@live.com
        """
        name = Personal.username()
        email_adders = name + choice(pull('email', 'en_us'))
        return email_adders.strip()

    @staticmethod
    def home_page():
        """
        Generate a random home page using usernames.
        :return: random home page. Example: http://www.font6.info
        """
        url = 'http://www.' + Personal.username().replace(' ', '-')
        return url + choice(pull('domains', 'en_us')).strip()

    @staticmethod
    def subreddit(nsfw=False, full_url=False):
        """
        Get a random subreddit from list.
        :param nsfw: if True then will be returned NSFW subreddit.
        :param full_url: If true http://www.reddit.com/r/subreddit
        else /r/subreddit
        :return: subreddit or subreddit url.
        """
        url = 'http://www.reddit.com'
        if nsfw:
            if full_url:
                return url + choice(pull('nsfw_subreddits'))
            else:
                return choice(pull('nsfw_subreddits'))
        _subreddit = choice(pull('subreddits'))
        _result = url + _subreddit if full_url else _subreddit
        return _result

    @staticmethod
    def bitcoin(address_format='p2pkh'):
        """
        Get a random bitcoin address.
        Currently supported only two address formats that are most popular.
        It's 'P2PKH' and 'P2SH'
        :param address_format: bitcoin address format. Default is 'P2PKH'
        :return: address_format. Example: 3EktnHQD7RiAE6uzMj2ZifT9YgRrkSgzQX
        """
        _fmt = '1' if address_format.lower() == 'p2pkh' else '3'
        return _fmt + "".join([choice(ascii_letters + digits) for _ in range(33)])

    @staticmethod
    def cvv():
        """
        Generate a random card verification value (CVV)
        :return: CVV code
        """
        return randint(100, 999)

    @staticmethod
    def credit_card_number():
        """
        Generate a random credit card number for Visa or MasterCard
        :return: credit card. Example: 3519 2073 7960 3241
        """
        card = ' '.join([str(randint(1000, 9999)) for i in range(0, 4)])
        return card.strip()

    @staticmethod
    def cid():
        """
        Generate a random CID code.
        :return: CID code
        """
        return randint(1000, 9999)

    @staticmethod
    def wmid():
        """
        Generate a identifier of user WMID for WebMoney
        :return: Example: 834296404761
        """
        return "".join([choice(digits) for _ in range(12)])

    @staticmethod
    def paypal():
        """
        Generate a random PayPal account.
        :return: email. Example: wolf235@gmail.com
        """
        return Personal.email()

    @staticmethod
    def yandex_money():
        """
        Generate a random Yandex.Money account.
        :return: Y.Money account.
        """
        return "".join([choice(digits) for _ in range(14)])

    def gender(self, abbreviated=False):
        """
        Get a random gender.
        :param abbreviated: if True then will getting abbreviated gender title.
        For example: M or F
        :return: title of gender. Example: Male
        """
        if abbreviated:
            return choice(pull('gender', self.lang))[0:1]
        return choice(pull('gender', self.lang)).strip()

    def profession(self):
        """
        Get a random profession.
        :return: the name of profession. Example: Programmer
        """
        return choice(pull('professions', self.lang)).strip()

    def political_views(self):
        """
        Get a random political views.
        :return: political views. Example: Liberal
        """
        return choice(pull('political_views', self.lang)).strip()

    def worldview(self):
        """
        Get a random worldview.
        :return: worldview. Example: Pantheism
        """
        return choice(pull('worldview', self.lang)).strip()

    def views_on(self):
        """
        Get a random views on.
        :return: views on string. Example: Negative
        """
        return choice(pull('views_on', self.lang)).strip()

    def nationality(self, gender='f'):
        """
        Get a random nationality.
        :param gender: female or male
        :return: nationality. Example: Russian
        """
        try:
            # If you know Russian, then you will understand everything at once.
            if self.lang == 'ru_ru':
                index = 0 if gender.lower() == 'm' else 1
                return choice(pull('nation', self.lang)).split('|')[index].strip()
            else:
                return choice(pull('nation', self.lang)).strip()
        except Exception:
            raise TypeError('name takes only string type')

    def university(self):
        """
        Get a random university.
        :return: university name. Example: MIT
        """
        return choice(pull('university', self.lang)).strip()

    def qualification(self):
        """
        Get a random qualification.
        :return: degree. Example: Bachelor
        """
        return choice(pull('qualifications', self.lang)).strip()

    def language(self):
        """
        Get a random language.
        :return: random language. Example: Irish
        """
        return choice(pull('languages', self.lang)).strip()

    def favorite_movie(self):
        """
        Get a random movie.
        :return: name of the movie
        """
        return choice(pull('favorite_movie', self.lang)).strip()

    def telephone(self):
        """
        Generate a random phone number.
        :return: phone number. Example: +7-(963)409-11-22
        """
        phone_number = ''
        mask = '+7-($$$)$$$-$$-$$' if self.lang == 'ru_ru' \
            else '+$-($$$)$$$-$$-$$'
        for i in mask:
            if i == '$':
                phone_number += str(randint(1, 9))
            else:
                phone_number += i
        return phone_number.strip()

    @staticmethod
    def avatar():
        ava_path = 'https://raw.githubusercontent.com/lk-geimfari/' \
            'church/master/examples/avatars/{0}.png'.format(randint(1, 7))
        return ava_path


class Datetime(object):
    """
    Class for generate the fake data that you can use for working with date and time.
    """

    def __init__(self, lang='en_us'):
        self.lang = lang.lower()

    def day_of_week(self, abbreviated=False):
        """
        Get a random day of week.
        :param abbreviated: if True then will be returned abbreviated name of day of the week.
        :return: name of day of the week
        """
        _day = choice(pull('days', self.lang)).split('|')
        if abbreviated:
            return _day[1].strip()
        return _day[0].strip()

    def month(self, abbreviated=False):
        """
        Get a random month.
        :param abbreviated: if True then will be returned abbreviated month name.
        :return: month name. Example: November
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
        :return: year. Example 2023
        """
        return randint(int(from_), int(to_))

    def periodicity(self):
        """
        Get a random periodicity string.
        :return: periodicity. Example: Never
        """
        return choice(pull('periodicity', self.lang)).strip()

    @staticmethod
    def date(sep='-', with_time=False):
        """
        Generate a random date formatted as a 11-05-2016
        :param sep: a separator for date. Default is '-'.
        :param with_time: if it's True then will be added random time.
        :return: formatted date and time: 20-03-2016 03:20
        """
        _d = date(randint(2000, 2035), randint(1, 12), randint(1, 28))
        pattern = '%d{0}%m{0}%Y %m:%d' if with_time else '%d{0}%m{0}%Y'
        return _d.strftime(pattern.format(sep))

    @staticmethod
    def day_of_month():
        """
        Static method for generate a random days of month, from 1 to 31.
        :return: random value from 1 to 31
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
        :return: random IPv4 address
        """
        ip = '.'.join([str(randint(0, 255)) for i in range(0, 4)])
        return ip.strip()

    @staticmethod
    def ip_v6():
        """
        Static method for generate a random IPv6 address.
        :return: random IPv6 address
        """
        return "2001:" + ":".join("%x" % randint(0, 16 ** 4) for _ in range(7))

    @staticmethod
    def mac_address():
        """
        Static method for generate a random MAC address.
        :return: random mac address
        """
        mac = [0x00, 0x16, 0x3e,
               randint(0x00, 0x7f),
               randint(0x00, 0xff),
               randint(0x00, 0xff)
               ]
        _mac = map(lambda x: "%02x" % x, mac)
        return ':'.join(_mac)

    @staticmethod
    def user_agent():
        """
        Get a random user agent.
        :return: user agent string
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
        :return:
        """
        _type = file_type.lower()

        source = [
            '.a', '.asm', '.asp', '.awk', '.c', '.class',
            '.cpp', '.pl', '.js', '.java', '.clj', '.py',
            '.rb', '.hs', '.erl', '.rs', '.swift', '.html',
            '.json', '.xml', '.css', '.php', '.jl', '.r',
            '.cs', 'd', '.lisp', '.cl', '.go', '.h', '.scala',
            '.sc', '.ts', '.sql'
        ]
        text = ['.doc', '.docx', '.log', '.rtf', '.md',
                '.pdf', '.odt', '.txt'
                ]

        data = ['.csv', '.dat', '.ged', '.pps', '.ppt', '.pptx']
        audio = ['.flac', '.mp3', '.m3u', '.m4a', '.wav', '.wma']
        video = ['.3gp', '.mp4', '.abi', '.m4v', '.mov', '.mpg', '.wmv']
        image = ['.bmp', '.jpg', '.jpeg', '.png', '.svg']
        executable = ['.apk', '.app', '.bat', '.jar', '.com', '.exe']
        compressed = ['.7z', '.war', '.zip', '.tar.gz', '.tar.xz', '.rar']

        if _type == 'source':
            return choice(source)
        elif _type == 'data':
            return choice(data)
        elif _type == 'audio':
            return choice(audio)
        elif _type == 'video':
            return choice(video)
        elif _type == 'image':
            return choice(image)
        elif _type == 'executable':
            return choice(executable)
        elif _type == 'compressed':
            return choice(compressed)
        else:
            return choice(text)


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
        :return: formula. For example: A = (ab)/2
        """
        formula = choice(pull('math_formula', 'en_us'))
        return formula.strip()

    def chemical_element(self, name_only=True):
        """
        Get a random chemical element from file.
        :param name_only: if False then will be returned dict.
        :return: name of chemical element or dict.
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
        :return: link. Example: https://en.wikipedia.org/wiki/Black_hole
        """
        article = choice(pull('science_wiki', self.lang))
        return article.strip()

    def scientist(self):
        """
        Get a random name of scientist.
        :return: name of scientist. Example: Konstantin Tsiolkovsky
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
        _license = [
            'Apache License, 2.0 (Apache-2.0)',
            'The BSD 3-Clause License',
            'The BSD 2-Clause License',
            'GNU General Public License (GPL)',
            'General Public License (LGPL),'
            'MIT software_license (MIT)',
            'Mozilla Public License 2.0 (MPL-2.0)',
            'Common Development and Distribution License (CDDL-1.0)',
            'Eclipse Public License (EPL-1.0)'
        ]
        return choice(_license)

    @staticmethod
    def database(nosql=False):
        """
        Get a random database name.
        :param nosql: only NoSQL databases
        :return: database name. Example: PostgreSQL
        """
        _nosql = ['MongoDB', 'RethinkDB', 'Couchbase', 'CouchDB',
                  'Aerospike', 'MemcacheDB', 'MUMPS,  Riak', 'Redis',
                  'AllegroGraph', 'Neo4J', 'InfiniteGraph']

        _sql = ['MariaDB', 'MySQL', 'PostgreSQL', 'Oracle DB', 'SQLite']
        if nosql:
            return choice(_nosql)
        return choice(_sql)

    @staticmethod
    def other():
        """
        Get a random value list.
        :return: some technology. Example: Nginx
        """
        _list = ['Docker', 'Rkt', 'LXC', 'Vagrant',
                 'Elasticsearch', 'Nginx', 'Git', 'Mercurial',
                 'Jira', 'REST', 'Apache Hadoop', 'Scrum', 'Redmine',
                 'Apache Kafka', 'Apache Spark']
        return choice(_list)

    @staticmethod
    def programming_language():
        """
        Get a random programming language from list.
        :return: programming language. Example: Erlang
        """
        return choice(pull('pro_lang', 'en_us')).strip()

    @staticmethod
    def framework(_type='back'):
        """
        Get a random framework from file.
        :param _type: If _type='front' then will be returned front-end framework,
        else will be returned back-end framework.
        :return: framework or list of used stack: Example:  Python/Django
        """
        _file = 'front_frmwk' if _type.lower() == 'front' else 'back_frmwk'
        _framework = choice(pull(_file))
        return _framework.strip()

    @staticmethod
    def stack_of_tech(nosql=False):
        """
        Get a random stack.
        :param nosql: if True the only NoSQL skills.
        :return: dict like in example.
        Example:      {'Back-end': 'Martini',
                      'DB': 'SQLite',
                      'Front-end': 'Webpack',
                      'Other': 'Martini'}
        """
        front = '{}'.format(Development.framework('front'))
        back = '{}'.format(Development.framework('back'))
        db = '{}'.format(Development.database(nosql))
        other = '{}'.format(Development.other())
        _stack = {
            'front-end': front,
            'back-end': back,
            'db': db,
            'other': other
        }

        return _stack

    @staticmethod
    def github_repo():
        """
        Get a random link to github repository.
        :return: link. Example: https://github.com/lk-geimfari/church
        """
        return choice(pull('github_repos')).strip()

    @staticmethod
    def os():
        """
        Get a random operating system or distributive name.
        :return: os name. Example: Gentoo
        """
        return choice(pull('os')).strip()


class Food(object):
    """
    Class for Food, i.e fruits, vegetables, berries and other.
    """

    def __init__(self, lang):
        self.lang = lang

    def berry(self):
        """
        Get random berry.
        :return: berry. Example: Blackberry
        """
        _berry = choice(pull('berries', self.lang))
        return _berry.strip()

    def vegetable(self):
        """
        Get a random vegetable.
        :return: vegetable. Example: Tomato
        """
        _vegetable = choice(pull('vegetables', self.lang))
        return _vegetable.strip()

    def fruit(self):
        """
        Get a random fruit name.
        :return: fruit. Example: Banana
        """
        _fruit = choice(pull('fruits', self.lang))
        return _fruit.strip()

    def dish(self):
        """
        Get a random dish for current locale.
        :return: dish name. Example (ru_ru): Борщ
        """
        _dishes = choice(pull('dishes', self.lang))
        return _dishes.strip()

    def spices(self):
        """
        Get a random spices or herbs.
        :return: spices or herbs.
        """
        result = choice(pull('spices', self.lang))
        return result.strip()

    def mushroom(self):
        """
        Get a random mushroom's name
        :return: mushroom's name. Example: Marasmius oreades
        """
        result = choice(pull('mushrooms', self.lang))
        return result.strip()

    def alcoholic_drink(self):
        """
        Get a random alcoholic drink.
        :return: alcoholic_drink. Example: Vodka
        """
        _ad = choice(pull('alcoholic_drinks', self.lang))
        return _ad.strip()

    def cocktail(self):
        """
        Get a random cocktail.
        :return: cocktail name.
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
        :return: resolution. Example: 1280x720
        """
        _res = ['1152x768', '1280x854', '1440x960',
                '2880x1920', '1024x768', '1152x864',
                '1280x960', '1400x1050', '1600x1200',
                '2048x1536', '3200x2400', '1280x768',
                '1280x1024', '2560x2048', '1280x720',
                '1365x768', '1600x900', '1920x1080',
                '1280x800', '1440x900', '1680x1050',
                '1920x1200', '2560x1600'
                ]

        return choice(_res)

    @staticmethod
    def screen_size():
        """
        Get a random size of screen in inch
        :return: screen size. Example: 13″
        """
        _size = ['14″', '12.1″', '12″', '14.4″',
                 '15″', ' 15.7″', '13.3″', '13″',
                 '17″', '15.4″', ' 14.1″']
        return choice(_size)

    @staticmethod
    def cpu():
        """
        Get a random CPU name.
        :return: CPU name. Example: Intel® Core i7
        """
        _cpu = ['Intel® Core i3',
                'Intel® Core i5',
                'Intel® Core i7']
        return choice(_cpu)

    @staticmethod
    def cpu_frequency():
        """
        Get a random frequency of CPU.
        :return: frequency. Example: 4.0 GHz
        """
        _c = ['3.50', '3.67', '2.2', '1.6',
              '2.7', '2.8', '3.2', '3.0',
              '2.5', '2.9', '2.4', '4.0',
              '3.8', '3.7', '3.9', '4.2',
              '2.3', '2.9', '3.3', '3.1']
        return choice(_c) + ' GHz'

    @staticmethod
    def generation():
        """
        Get a random generation.
        :return: generation.
        """
        _gn = ['2nd Generation',
               '3rd Generation',
               '4th Generation',
               '5th Generation',
               '6th Generation',
               '7th Generation',
               ]
        return choice(_gn)

    @staticmethod
    def cpu_codename():
        """
        Get a random CPU code name.
        :return: cpu code name. Example: Haswell
        """
        _cn = ['Ivytown', 'Haswell', 'Fortville',
               'Devil\'s Canyon', 'Valley Island',
               'Broadwell', 'Bay Trail', 'Skylake',
               'Orchid Island', 'Bear Ridge',
               'Cannonlake'
               ]
        return choice(_cn)

    @staticmethod
    def ram_type():
        """
        Get a random RAM type.
        :return: type of ram. Example: DDR3
        """
        return choice(['DDR2', 'DDR3', 'DDR4'])

    @staticmethod
    def ram_size():
        """
        Get a random size of RAM.
        :return: RAM size. Example: 16GB
        """
        return choice(['4', '6', '8', '16', '32']) + 'GB'

    @staticmethod
    def ssd_or_hdd():
        """
        Get a random value from list.
        :return: HDD or SSD. Example: 512GB HDD
        """
        _hard = [
            '64GB SSD', '128GB SSD',
            '256GB SDD', '512GB SSD', '1024GB SSD',
            '256GB HDD', '256GB HDD(7200 RPM)',
            '256GB HDD(5400 RPM)', '512GB HDD',
            '512GB HDD(7200 RPM)', '1TB HDD',
            '1TB HDD(7200 RPM)', '1TB HDD + 64GB SSD',
            '2TB HDD(7200 RPM)', '512 GB HDD + 32GB SSD',
            '1TB HDD(7200 RPM) + 32GB SSD'
        ]
        return choice(_hard)

    @staticmethod
    def graphics():
        """
        Get a random graphics.
        :return: graphics. Example: Intel® Iris™ Pro Graphics 6200
        """
        _g = ['Intel® HD Graphics 620',
              'Intel® HD Graphics 615',
              'Intel® Iris™ Pro Graphics 580',
              'Intel® Iris™ Graphics 550'
              'Intel® HD Graphics 520',
              'Intel® Iris™ Pro Graphics 6200',
              'Intel® Iris™ Graphics 6100',
              'Intel® HD Graphics 6000',
              'Intel® HD Graphics 5300 ',
              'Intel® Iris™ Pro Graphics 5200',
              'Intel® Iris™ Graphics 5100',
              'Intel® HD Graphics 5500',
              'Intel® HD Graphics 5000',
              'Intel® HD Graphics 4600',
              'Intel® HD Graphics 4400',
              'Intel® HD Graphics 4000',
              'Intel® HD Graphics 3000',
              'NVIDIA GeForce GTX 1080',
              'NVIDIA GeForce GTX 1070',
              'NVIDIA GeForce GTX 1080',
              'NVIDIA GeForce GTX 980',
              'NVIDIA GeForce GTX 1070',
              'NVIDIA GeForce GTX 980M',
              'NVIDIA GeForce GTX 980',
              'NVIDIA GeForce GTX 970M',
              'NVIDIA GeForce GTX 880M',
              'AMD Radeon R9 M395X',
              'AMD Radeon R9 M485X',
              'AMD Radeon R9 M395'
              ]
        return choice(_g)

    @staticmethod
    def manufacturer():
        """
        Get a random manufacturer.
        :return: manufacturer. Example: Dell
        """
        _m = ['Acer', 'Dell', 'ASUS',
              'VAIO', 'Lenovo', 'HP',
              'Toshiba', 'Sony', 'Samsung',
              'Fujitsu', 'Apple']
        return choice(_m)

    @staticmethod
    def hardware_full_info():
        """
        Get a random full information about device (laptop).
        :return: full information. Example:
        ASUS Intel® Core i3 3rd Generation 3.50 GHz/1920x1200/12″/
        512GB HDD(7200 RPM)/DDR2-4GB/Intel® Iris™ Pro Graphics 6200
        """
        _c = '{}'.format(Hardware.cpu())
        _r = '{}'.format(Hardware.resolution())
        _ss = '{}'.format(Hardware.screen_size())
        _cl = '{}'.format(Hardware.cpu_frequency())
        _gn = '{}'.format(Hardware.generation())
        _rt = '{}'.format(Hardware.ram_type())
        _rs = '{}'.format(Hardware.ram_size())
        _mem = '{}'.format(Hardware.ssd_or_hdd())
        _gr = '{}'.format(Hardware.graphics())
        _mnf = '{}'.format(Hardware.manufacturer())
        _full = '{0} {1} {2} {3}/{4}/{5}/{6}/{7}-{8}/{9}'.format(
            _mnf, _c, _gn, _cl, _r, _ss, _mem, _rt, _rs, _gr)
        return _full

    @staticmethod
    def phone_model():
        """
        Get a random phone model.
        :return: phone model. Example: Nokia Lumia 920
        """
        _model = choice(pull('phone_models', 'en_us'))
        return _model.strip()
