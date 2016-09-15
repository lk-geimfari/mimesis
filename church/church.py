from datetime import date
from random import choice, sample, randint
from string import digits, ascii_letters

from .utils import pull

__all__ = ['Address', 'Personal',
           'BasicData', 'Network',
           'Datetime', 'File', 'Science'
           ]


class Address(object):
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
        :return: street suffix. For example: Street.
        """
        return choice(pull('street_suffix', self.lang)).strip()

    def street_address(self):
        """
        Get a random address.
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

    def state_or_subject(self):
        """
        Get a random states or subject of country. For 'ru_ru' always will
        be getting subject of Russian Federation. For other localization will be getting state.
        :return:
        """
        if self.lang == 'ru_ru':
            return choice(pull('subjects', self.lang)).strip()
        else:
            return choice(pull('states', self.lang)).strip()

    def postal_code(self):
        """
        Get a random postal code.
        :return: postal code. For example: 389213
        """
        return choice(pull('postal_codes', self.lang)).strip()

    def country(self):
        """
        Get a random country.
        :return: country. For example: Russia
        """
        return choice(pull('countries', self.lang)).strip()

    def city(self):
        """
        Get a random name of city.
        :return: city name. For example: Saint Petersburg
        """
        return choice(pull('cities', self.lang)).strip()


class BasicData(object):
    """
    Class for generate text data, i.e text, lorem ipsum and another.
    """

    def __init__(self, lang='en_us'):
        self.lang = lang.lower()

    def lorem_ipsum(self, quantity=5):
        """
        Get random strings.
        :param quantity: quantity of strings.
        :return: random text
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
        Get random title.
        :return: title. For example: Erlang - is a general-purpose,
        concurrent, functional programming language.
        """
        return self.lorem_ipsum(quantity=1)

    def words(self, quantity=5):
        """
        Get the random words.
        :param quantity: quantity of words. Default is 5.
        :return: words. For example: science, network, god, octopus, love
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
        :return: single word. For example: science
        """
        return self.words(quantity=1)[0]

    def quote_from_movie(self):
        """
        Get a random quotes from movie.
        :return: quotes. For example: Bond... James Bond.
        """
        return choice(pull('quotes', self.lang)).strip()

    @staticmethod
    def currency_iso():
        """
        Get currency code. ISO 4217
        :return: currency code. For example: RUR
        """
        return choice(pull('currency', 'en_us')).strip()

    def color(self):
        """
        Get random name of color.
        :return: color name. For example: Red
        """
        return choice(pull('colors', self.lang)).strip()

    def company_type(self, abbreviated=False):
        """
        Get a random company type.
        :param abbreviated: if True then abbreviated company type.
        :return: company type. For example: Inc.
        """
        _type = choice(pull('company_type', self.lang)).split('|')
        if abbreviated:
            return _type[1].strip()
        return _type[0].strip()

    def company(self):
        """
        Get a random company name.
        :return: company name. For example: Intel
        """
        company = choice(pull('company', self.lang))
        return company.strip()

    @staticmethod
    def programming_language():
        """
        Get a random programming language from list with 82 values.
        :return: programming language. For example: Erlang
        """
        return choice(pull('pro_lang', 'en_us')).strip()


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
        :return: name
        """
        if not isinstance(gender, str):
            raise TypeError('name takes only string type')
        if gender.lower() == 'f':
            return choice(pull('f_names', self.lang)).strip()
        elif gender.lower() == 'm':
            return choice(pull('m_names', self.lang)).strip()

    def surname(self, gender='f'):
        """
        Get a random surname.
        :param gender: if 'm' then will getting male surname else
        female surname.
        :return: surname. For example: Wolf
        """
        if not isinstance(gender, str):
            raise TypeError('surname takes only string type')
        if self.lang == 'en_us':
            return choice(pull('surnames', self.lang)).strip()

        elif self.lang == 'ru_ru':
            if gender.lower() == 'f':
                return choice(pull('f_surnames', self.lang)).strip()
            elif gender.lower() == 'm':
                return choice(pull('m_surnames', self.lang)).strip()

    def full_name(self, gender='f'):
        """
        Get a random full name
        :param gender: if gender='m' then will be returned male name else
        female name.
        :return: full name. For example: Johann Wolfgang
        """
        if self.lang == 'ru_ru':
            if gender.lower() == 'f':
                return '{0} {1}'.format(self.surname(), self.name())
            elif gender.lower() == 'm':
                return '{0} {1}'.format(self.surname('m'), self.name('m'))
        else:
            if gender.lower() == 'f':
                return '{0} {1}'.format(self.name(), self.surname())
            elif gender.lower() == 'm':
                return '{0} {1}'.format(self.name('m'), self.surname('m'))

    def username(self):
        """
        Get a random username with digits.
        :return: username. For example: foretime10
        """
        user_name = choice(pull('usernames', 'en_us')) \
            .replace(' ', '_').strip()
        user_name += str(randint(3, 94))
        return user_name.lower()

    @staticmethod
    def password(length=8):
        """
        Generate a random password.
        :param length: length of password
        :return: random password
        """
        _punc = '!"#$%+:<?@^_'
        return "".join([choice(ascii_letters + digits + _punc) for _ in range(length)])

    def email(self):
        """
        Generate a random email using usernames.
        :return: email address. For example: foretime10@live.com
        """
        name = self.username()
        email_adders = name + choice(pull('email', 'en_us'))
        return email_adders.strip()

    def home_page(self):
        """
        Generate a random home page using usernames.
        :return: random home page. For example: http://www.font6.info
        """
        domain_name = 'http://www.' + self.username().replace(' ', '-')
        return domain_name + choice(pull('domains', 'en_us')).strip()

    @staticmethod
    def bitcoin(address_format='p2pkh'):
        """
        Get a random bitcoin address.
        Currently supported only two address formats that are most popular.
        It's 'P2PKH' and 'P2SH'
        :param address_format: bitcoin address format. Default is 'P2PKH'
        :return: address_format. For example: 3EktnHQD7RiAE6uzMj2ZifT9YgRrkSgzQX
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
        :return: credit card. For example: 3519 2073 7960 3241
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

    def gender(self, abbreviated=False):
        """
        Get a random gender.
        :param abbreviated: if True then will getting abbreviated gender title.
        For example: M or F
        :return: title of gender. For example: Male
        """
        if abbreviated:
            return choice(pull('gender', self.lang))[0:1]
        return choice(pull('gender', self.lang)).strip()

    def profession(self):
        """
        Get a random profession.
        :return: the name of profession. For example: Programmer
        """
        return choice(pull('professions', self.lang)).strip()

    def political_views(self):
        """
        Get a random political views.
        :return: political views. For example: Liberal
        """
        return choice(pull('political_views', self.lang)).strip()

    def worldview(self):
        """
        Get a random worldview.
        :return: worldview. For example: Pantheism
        """
        return choice(pull('worldview', self.lang)).strip()

    def views_on(self):
        """
        Get a random views on.
        :return: views on string. For example: Negative
        """
        return choice(pull('views_on', self.lang)).strip()

    def nationality(self, gender='f'):
        """
        Get a random nationality.
        :param gender: female or male
        :return: nationality. For example: Russian
        """
        try:
            # If you know Russian, then you will understand everything at once.
            if self.lang == 'ru_ru':
                if gender.lower() == 'm':
                    return choice(pull('nation', self.lang)).split('|')[0].strip()
                else:
                    return choice(pull('nation', self.lang)).split('|')[1].strip()
            else:
                return choice(pull('nation', self.lang)).strip()
        except Exception:
            raise TypeError('name takes only string type')

    def university(self):
        """
        Get a random university.
        :return: university name. For example: MIT
        """
        return choice(pull('university', self.lang)).strip()

    def qualification(self):
        """
        Get a random qualification.
        :return: degree. For example: Bachelor
        """
        return choice(pull('qualifications', self.lang)).strip()

    def language(self):
        """
        Get a random language.
        :return: random language. For example: Irish
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
        :return: phone number. For example: +7-(963)409-11-22
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
        if abbreviated:
            return choice(pull('days_abbr', self.lang)).strip()
        return choice(pull('days', self.lang)).strip()

    def month(self, abbreviated=False):
        """
        Get a random month.
        :param abbreviated: if True then will be returned abbreviated month name.
        :return: month name. For example: November
        """
        if abbreviated:
            return choice(pull('month_abbr', self.lang)).strip()
        return choice(pull('months', self.lang)).strip()

    def periodicity(self):
        """
        Get a random periodicity string.
        :return: periodicity. For example: Never
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
        :param type: The type of extension. Default is text.
        All supported types:
            1. source - '.py', '.rb', '.cpp' and other.
            2. text = '.doc', '.log', '.rtf' and other.
            3. data_file = '.csv', '.dat', '.pps' and other.
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

    def physical_law(self):
        """
        Get the wording of the law of physics.
        :return: law of physics
        """
        law = choice(pull('physical_law', self.lang))
        return law.strip()

    def article_on_wiki(self):
        """
        Get a random link to article in Wikipedia.
        :return: link. For example: https://en.wikipedia.org/wiki/Black_hole
        """
        article = choice(pull('science_wiki', self.lang))
        return article.strip()

    def scientist(self):
        """
        Get a random name of scientist.
        :return: name of scientist. For example: Konstantin Tsiolkovsky
        """
        scientist_name = choice(pull('scientist', self.lang))
        return scientist_name.strip()