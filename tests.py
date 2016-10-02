import re
import unittest

from church.church import (
    Address, Text, Personal,
    Datetime, Network, File, Science,
    Development, Food, Hardware
)
from church.utils import pull

LANG = 'en_us'


# LANG = 'ru_ru'
# LANG = 'de_de'
# LANG = 'fr_fr'


class AddressTestCase(unittest.TestCase):
    def setUp(self):
        self.address = Address(LANG)

    def tearDown(self):
        del self.address

    def test_street_number(self):
        result = self.address.street_number()
        self.assertTrue(re.match(r'[0-9]{1,5}$', result))

    def test_street_name(self):
        result = self.address.street_name() + '\n'
        self.assertIn(result, pull('street', self.address.lang))

    def test_street_suffix(self):
        result = self.address.street_suffix() + '\n'
        self.assertIn(result, pull('street_suffix', self.address.lang))

    def test_address(self):
        result = self.address.address()
        self.assertTrue(len(result) > 6)

    def test_state(self):
        result = self.address.state() + '\n'
        self.assertIn(result, pull('states', self.address.lang))

    def test_postal_code(self):
        result = self.address.postal_code()
        if self.address.lang == 'ru_ru':
            self.assertIsNotNone(re.match(r'[0-9]{6}$', result))
        else:
            self.assertTrue(re.match(r'[0-9]{5}$', result))

    def test_country(self):
        result = self.address.country() + '\n'
        self.assertTrue(len(result) > 3)

        result2 = self.address.country(only_iso_code=True) + '\n'
        self.assertTrue(len(result2) < 4)

    def test_city(self):
        result = self.address.city() + '\n'
        self.assertIn(result, pull('cities', self.address.lang))


class TextTestCase(unittest.TestCase):
    def setUp(self):
        self.data = Text(LANG)

    def tearDown(self):
        del self.data

    def test_sentence(self):
        result = self.data.sentence() + '\n'
        self.assertIn(result, pull('text', self.data.lang))

    def test_title(self):
        result = self.data.title() + '\n'
        self.assertIn(result, pull('text', self.data.lang))

    def test_words(self):
        result = self.data.words()
        self.assertEqual(len(result), 5)

        result = self.data.words(quantity=1)
        self.assertEqual(len(result), 1)

    def test_word(self):
        result = self.data.word() + '\n'
        self.assertIn(result, pull('words', self.data.lang))

    def test_swear_word(self):
        result = self.data.swear_word() + '\n'
        self.assertIn(result, pull('swear_words', self.data.lang))

    def test_naughty_strings(self):
        result = self.data.naughty_strings()
        self.assertTrue(len(result) > 10)

    def test_quote_from_movie(self):
        result = self.data.quote_from_movie() + '\n'
        self.assertIn(result, pull('quotes', self.data.lang))

    def test_currency_sio(self):
        result = self.data.currency_iso() + '\n'
        self.assertIn(result, pull('currency', 'en_us'))

    def test_color(self):
        result = self.data.color() + '\n'
        self.assertIn(result, pull('colors', self.data.lang))

    def test_hex_color(self):
        result = self.data.hex_color()
        self.assertIn('#', result)

    def test_company_type(self):
        result = self.data.company_type(abbreviated=True)
        self.assertTrue(len(result) < 7)

    def test_company(self):
        result = self.data.company() + '\n'
        self.assertIn(result, pull('company', self.data.lang))

    def test_copyright(self):
        result = self.data.copyright()
        copyright_symbol = '©'
        self.assertIn(copyright_symbol, result)

        result = self.data.copyright(without_date=True)
        self.assertFalse(any(char.isdigit() for char in result))

    def test_emoji(self):
        result = self.data.emoji() + '\n'
        self.assertIn(result, pull('emoji'))


class PersonalTestCase(unittest.TestCase):
    def setUp(self):
        self.person = Personal(LANG)

    def tearDown(self):
        del self.person

    def test_age(self):
        result = self.person.age(maximum=55)
        self.assertTrue(result <= 55)

    def test_name(self):
        result = self.person.name() + '\n'
        self.assertIn(result, pull('f_names', self.person.lang))

        result = self.person.name('m') + '\n'
        self.assertIn(result, pull('m_names', self.person.lang))

    def test_telephone(self):
        result = self.person.telephone()
        self.assertTrue(
            re.match(r'^((8|\+[1-9])[\- ]?)?'
                     r'(\(?\d{3}\)?[\- ]?)?'
                     r'[\d\- ]{7,10}$', result))

    def test_surname(self):
        if self.person.lang == 'ru_ru':
            result = self.person.surname('f') + '\n'
            self.assertIn(result, pull('f_surnames', self.person.lang))

            result = self.person.surname('m') + '\n'
            self.assertIn(result, pull('m_surnames', self.person.lang))
        else:
            result = self.person.surname() + '\n'
            self.assertIn(result, pull('surnames', self.person.lang))

    def test_full_name(self):
        result = self.person.full_name('f')
        _result = result.split(' ')
        self.assertEqual(len(_result), 2)

    def test_username(self):
        result = self.person.username()
        self.assertTrue(re.match(r'^[a-zA-Z0-9_.-]+$', result))

        result = self.person.username('f')
        self.assertTrue(re.match(r'^[a-zA-Z0-9_.-]+$', result))

    def test_twitter(self):
        result = self.person.twitter('f')
        self.assertIsNotNone(result)

        _result = self.person.twitter('m')
        self.assertIsNotNone(_result)

    def test_facebook(self):
        result = self.person.facebook('f')
        self.assertIsNotNone(result)

        _result = self.person.facebook('m')
        self.assertIsNotNone(_result)

    def test_wmid(self):
        result = self.person.wmid()
        self.assertEqual(len(result), 12)

    def test_paypal(self):
        result = self.person.paypal()
        self.assertIsNotNone(result)

    def test_yandex_money(self):
        result = self.person.yandex_money()
        self.assertEqual(len(result), 14)

    def test_password(self):
        _plain = self.person.password(length=15)
        self.assertEqual(len(_plain), 15)

        _md5 = self.person.password(algorithm='md5')
        self.assertEqual(len(_md5), 32)

        _sha1 = self.person.password(algorithm='sha1')
        self.assertEqual(len(_sha1), 40)

        _sha256 = self.person.password(algorithm='sha256')
        self.assertEqual(len(_sha256), 64)

        _sha512 = self.person.password(algorithm='sha512')
        self.assertEqual(len(_sha512), 128)

    def test_email(self):
        result = self.person.email()
        self.assertTrue(
            re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",
                     result))

    def test_home_page(self):
        result = self.person.home_page()
        self.assertTrue(re.match(r'http[s]?://(?:[a-zA-Z]|[0-9]|'
                                 r'[$-_@.&+]|[!*\(\),]|'
                                 r'(?:%[0-9a-fA-F][0-9a-fA-F]))+', result))

    def test_subreddit(self):
        result = self.person.subreddit()
        self.assertIn(result, pull('subreddits'))

        full_result = self.person.subreddit(full_url=True)
        self.assertTrue(len(full_result) > 20)

        result_nsfw = self.person.subreddit(nsfw=True)
        self.assertIn(result_nsfw, pull('nsfw_subreddits'))

        full_result = self.person.subreddit(nsfw=True, full_url=True)
        self.assertTrue(len(full_result) > 20)

    def test_bitcoin(self):
        result = self.person.bitcoin()
        self.assertEqual(len(result), 34)

        p2pkh = self.person.bitcoin(address_format='p2pkh')
        self.assertEqual(p2pkh[0], '1')

        p2sh = self.person.bitcoin(address_format='p2sh')
        self.assertEqual(p2sh[0], '3')

    def test_cvv(self):
        result = self.person.cvv()
        self.assertTrue((100 <= result) and (result <= 999))

    def test_credit_card_number(self):
        result = self.person.credit_card_number()
        self.assertTrue(re.match(r'[\d]+((-|\s)?[\d]+)+', result))

    def test_expiration_date(self):
        result = self.person.credit_card_expiration_date(from_=16, to_=25)
        year = result.split('/')[1]
        self.assertTrue((int(year) >= 16) and (int(year) <= 25))

    def test_cid(self):
        result = self.person.cid()
        self.assertTrue((1000 <= result) and (result <= 9999))

    def test_gender(self):
        result = self.person.gender() + '\n'
        self.assertIn(result, pull('gender', self.person.lang))

        result_abbr = self.person.gender(abbreviated=True) + '\n'
        self.assertEqual(len(result_abbr), 2)

    def test_height(self):
        result = self.person.height(from_=1.60, to_=1.90)
        self.assertTrue(result.startswith('1'))
        self.assertIsInstance(result, str)

    def test_weight(self):
        result = self.person.weight(from_=40, to_=60)
        self.assertTrue((result >= 40) and (result <= 60))

    def test_sexual_orientation(self):
        result = self.person.sexual_orientation()
        self.assertIn(
            result + '\n', pull('sexual_orientation', self.person.lang))

    def test_profession(self):
        result = self.person.profession() + '\n'
        self.assertIn(result, pull('professions', self.person.lang))

    def test_university(self):
        result = self.person.university() + '\n'
        self.assertIn(result, pull('university', self.person.lang))

    def test_qualification(self):
        result = self.person.qualification() + '\n'
        self.assertIn(result, pull('qualifications', self.person.lang))

    def test_language(self):
        result = self.person.language() + '\n'
        self.assertIn(result, pull('languages', self.person.lang))

    def test_favorite_movie(self):
        result = self.person.favorite_movie() + '\n'
        self.assertIn(result, pull('favorite_movie', self.person.lang))

    def test_worldview(self):
        result = self.person.worldview() + '\n'
        self.assertIn(result, pull('worldview', self.person.lang))

    def test_views_on(self):
        result = self.person.views_on() + '\n'
        self.assertIn(result, pull('views_on', self.person.lang))

    def test_political_views(self):
        result = self.person.political_views() + '\n'
        self.assertIn(result, pull('political_views', self.person.lang))

    def test_avatar(self):
        result = self.person.avatar()
        self.assertTrue(len(result) > 20)


class DatetimeTestCase(unittest.TestCase):
    def setUp(self):
        self.datetime = Datetime(LANG)

    def tearDown(self):
        del self.datetime

    def test_day_of_week(self):
        result = self.datetime.day_of_week() + '\n'
        self.assertGreater(len(result), 4)

        result_abbr = self.datetime.day_of_week(abbreviated=True)
        self.assertTrue(len(result_abbr) < 6 or '.' in result_abbr)

    def test_month(self):
        result = self.datetime.month() + '\n'
        self.assertGreater(len(result), 3)

        result_abbr = self.datetime.month(abbreviated=True)
        self.assertLess(len(result_abbr), 6)

    def test_year(self):
        result = self.datetime.year(from_=2000, to_=2016)
        self.assertTrue((result >= 2000) and (result <= 2016))

    def test_periodicity(self):
        result = self.datetime.periodicity() + '\n'
        self.assertIn(result, pull('periodicity', self.datetime.lang))

    def test_day_of_month(self):
        result = self.datetime.day_of_month()
        self.assertTrue((result >= 1) or (result <= 31))


class NetworkTestCase(unittest.TestCase):
    def setUp(self):
        self.net = Network()

    def test_ip_v4(self):
        result = self.net.ip_v4()
        ip_v4_pattern = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"
        self.assertTrue(re.match(ip_v4_pattern, result))

    def test_ip_v6(self):
        result = self.net.ip_v6()
        ip_v6_pattern = \
            r'(([0-9a-fA-F]{1,4}:)' \
            '{7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:)' \
            '{1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]' \
            '{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4})' \
            '{1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}' \
            '|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|' \
            '([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|' \
            '[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|' \
            ':((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]' \
            '{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:)' \
            '{0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.)' \
            '{3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|' \
            '([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|' \
            '1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|' \
            '(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))'

        self.assertTrue(re.match(ip_v6_pattern, result))

    def test_mac_address(self):
        result = self.net.mac_address()
        mac_pattern = r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'
        self.assertTrue(re.match(mac_pattern, result))

    def test_user_agent(self):
        result = self.net.user_agent() + '\n'
        self.assertIn(result, pull('useragents', 'en_us'))


class FileTestCase(unittest.TestCase):
    def setUp(self):
        self.file = File()

    def tearDown(self):
        del self.file

    def test_extension(self):
        source = self.file.extension('source')
        self.assertLess(len(source), 10)

        _text = self.file.extension()
        text = ['.doc', '.docx', '.log',
                '.rtf', '.md', '.pdf',
                '.odt', '.txt'
                ]
        self.assertIn(_text, text)


class ScienceTestCase(unittest.TestCase):
    def setUp(self):
        self.science = Science(LANG)

    def tearDown(self):
        del self.science

    def test_math_formula(self):
        result = self.science.math_formula() + '\n'
        self.assertIn(result, pull('math_formula', 'en_us'))

    def test_article_on_wiki(self):
        result = self.science.article_on_wiki() + '\n'
        self.assertIn(result, pull('science_wiki', self.science.lang))

    def test_scientist(self):
        result = self.science.scientist() + '\n'
        self.assertIn(result, pull('scientist', self.science.lang))

    def test_chemical_element(self):
        result = self.science.chemical_element(name_only=True)
        self.assertGreater(len(result), 2)

        _result = self.science.chemical_element(name_only=False)
        self.assertIsInstance(_result, dict)


class DevelopmentTestCase(unittest.TestCase):
    def setUp(self):
        self.dev = Development()

    def tearDown(self):
        del self.dev

    def test_license(self):
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

        result = self.dev.software_license()
        self.assertIn(result, _license)

    def test_programming_language(self):
        result = self.dev.programming_language() + '\n'
        self.assertIn(result, pull('pro_lang', 'en_us'))

    def test_database(self):
        _sql = ['MariaDB', 'MySQL', 'PostgreSQL',
                'Oracle DB', 'SQLite'
                ]

        result = self.dev.database()
        self.assertIn(result, _sql)

        _nosql = ['MongoDB', 'RethinkDB',
                  'Couchbase', 'CouchDB',
                  'Aerospike', 'MemcacheDB',
                  'MUMPS,  Riak', 'Redis',
                  'AllegroGraph', 'Neo4J',
                  'InfiniteGraph'
                  ]
        _result = self.dev.database(nosql=True)
        self.assertIn(_result, _nosql)

    def test_other(self):
        _list = ['Docker', 'Rkt',
                 'LXC', 'Vagrant',
                 'Elasticsearch',
                 'Nginx', 'Git',
                 'Mercurial', 'Jira',
                 'REST', 'Apache Hadoop',
                 'Scrum', 'Redmine',
                 'Apache Spark', 'Apache Kafka'
                 ]
        result = self.dev.other()
        self.assertIn(result, _list)

    def test_framework(self):
        result = self.dev.framework(_type='front') + '\n'
        self.assertIn(result, pull('frontend'))

        _result = self.dev.framework(_type='back') + '\n'
        self.assertIn(_result, pull('backend'))

    def test_stack_of_tech(self):
        result = self.dev.stack_of_tech(nosql=True)
        self.assertIsInstance(result, dict)

    def test_github_repo(self):
        url = self.dev.github_repo() + '\n'
        self.assertIn(url, pull('github_repos'))

    def test_os(self):
        result = self.dev.os() + '\n'
        self.assertIn(result, pull('os'))


class FoodTestCase(unittest.TestCase):
    def setUp(self):
        self.food = Food(LANG)

    def tearDown(self):
        del self.food

    def test_berry(self):
        result = self.food.berry() + '\n'
        self.assertIn(result, pull('berries', self.food.lang))

    def test_vegetable(self):
        result = self.food.vegetable() + '\n'
        self.assertIn(result, pull('vegetables', self.food.lang))

    def test_fruit(self):
        result = self.food.fruit() + '\n'
        self.assertIn(result, pull('fruits', self.food.lang))

    def test_dish(self):
        result = self.food.dish() + '\n'
        self.assertIn(result, pull('dishes', self.food.lang))

    def test_alcoholic_drink(self):
        result = self.food.alcoholic_drink() + '\n'
        self.assertIn(result, pull('alcoholic_drinks', self.food.lang))

    def test_spices(self):
        result = self.food.spices() + '\n'
        self.assertIn(result, pull('spices', self.food.lang))

    def test_mushroom(self):
        result = self.food.mushroom() + '\n'
        self.assertIn(result, pull('mushrooms', self.food.lang))


class HardwareTestCase(unittest.TestCase):
    def setUp(self):
        self.hard = Hardware()

    def tearDown(self):
        del self.hard

    def test_resolution(self):
        resolution = ['1152x768', '1280x854', '1440x960',
                      '2880x1920', '1024x768', '1152x864',
                      '1280x960', '1400x1050', '1600x1200',
                      '2048x1536', '3200x2400', '1280x768',
                      '1280x1024', '2560x2048', '1280x720',
                      '1365x768', '1600x900', '1920x1080',
                      '1280x800', '1440x900', '1680x1050',
                      '1920x1200', '2560x1600'
                      ]
        _result = self.hard.resolution()
        self.assertIn(_result, resolution)

    def test_screen_size(self):
        sizes = ['14″', '12.1″', '12″', '14.4″',
                 '15″', ' 15.7″', '13.3″', '13″',
                 '17″', '15.4″', ' 14.1″']
        result = self.hard.screen_size()
        self.assertIn(result, sizes)

    def test_generation(self):
        gn = ['2nd Generation',
              '3rd Generation',
              '4th Generation',
              '5th Generation',
              '6th Generation',
              '7th Generation',
              ]
        result = self.hard.generation()
        self.assertIn(result, gn)

    def test_cpu_frequency(self):
        f = ['3.50', '3.67', '2.2', '1.6',
             '2.7', '2.8', '3.2', '3.0',
             '2.5', '2.9', '2.4', '4.0',
             '3.8', '3.7', '3.9', '4.2',
             '2.3', '2.9', '3.3', '3.1']
        result = self.hard.cpu_frequency().split(' ')[0]
        self.assertIn(result, f)

    def test_cpu(self):
        cpu = ['Intel® Core i3',
               'Intel® Core i5',
               'Intel® Core i7']
        result = self.hard.cpu()
        self.assertIn(result, cpu)

    def test_cpu_codename(self):
        code_name = ['Ivytown', 'Haswell', 'Fortville',
                     'Devil\'s Canyon', 'Valley Island',
                     'Broadwell', 'Bay Trail', 'Skylake',
                     'Orchid Island', 'Bear Ridge',
                     'Cannonlake'
                     ]
        result = self.hard.cpu_codename()
        self.assertIn(result, code_name)

    def test_ram_type(self):
        result = self.hard.ram_type()
        self.assertIn(result, ['DDR2', 'DDR3', 'DDR4'])

    def test_ram_size(self):
        result = self.hard.ram_size().split(' ')
        self.assertGreater(len(result), 0)

    def test_ssd_or_hdd(self):
        _hard = [
            '64GB SSD', '128GB SSD',
            '256GB SDD', '512GB SSD', '1024GB SSD',
            '256GB HDD', '256GB HDD(7200 RPM)',
            '256GB HDD(5400 RPM)', '512GB HDD',
            '512GB HDD(7200 RPM)', '1TB HDD',
            '1TB HDD(7200 RPM)', '1TB HDD + 64GB SSD',
            '2TB HDD(7200 RPM)', '512 GB HDD + 32GB SSD',
            '1TB HDD(7200 RPM) + 32GB SSD']
        result = self.hard.ssd_or_hdd()
        self.assertIn(result, _hard)

    def test_graphics(self):
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
        result = self.hard.graphics()
        self.assertIn(result, _g)

    def test_manufacturer(self):
        _m = ['Acer', 'Dell', 'ASUS',
              'VAIO', 'Lenovo', 'HP',
              'Toshiba', 'Sony', 'Samsung',
              'Fujitsu', 'Apple']
        result = self.hard.manufacturer()
        self.assertIn(result, _m)

    def test_hardware_full(self):
        result = self.hard.hardware_full_info()
        self.assertGreater(len(result), 15)

    def test_phone_model(self):
        result = self.hard.phone_model() + '\n'
        self.assertIn(result, pull('phone_models', 'en_us'))
