import array
import re
from unittest import TestCase

import church._common as common
from church.church import (
    Address, Text, Personal,
    Datetime, Network, File,
    Development, Food, Hardware,
    Science, Numbers, Business,
    Church
)
from church.exceptions import (
    UnsupportedLocale
)
from church.utils import pull

# en, es, de, fr, it, ru, pt,
# pt-br, da, no
LANG = 'en'


class AddressTestCase(TestCase):
    def setUp(self):
        self.address = Address(LANG)

    def tearDown(self):
        del self.address

    def test_street_number(self):
        result = self.address.street_number()
        self.assertTrue(re.match(r'[0-9]{1,5}$', result))

    def test_street_name(self):
        result = self.address.street_name()
        parent_file = pull('street', self.address.lang)
        self.assertIn(result + '\n', parent_file)

    def test_street_suffix(self):
        result = self.address.street_suffix()
        parent_file = pull('st_suffix', self.address.lang)
        self.assertIn(result + '\n', parent_file)

    def test_address(self):
        result = self.address.address()
        self.assertTrue(len(result) > 6)

    def test_state(self):
        result = self.address.state()
        parent_file = pull('states', self.address.lang)
        self.assertIn(result + '\n', parent_file)

    def test_postal_code(self):
        result = self.address.postal_code()
        if self.address.lang == 'ru':
            self.assertTrue(re.match(r'[0-9]{6}$', str(result)))
        else:
            self.assertTrue(re.match(r'[0-9]{5}$', str(result)))

    def test_country(self):
        result = self.address.country() + '\n'
        self.assertTrue(len(result) > 3)

        result2 = self.address.country(only_iso_code=True) + '\n'
        self.assertTrue(len(result2) < 4)

    def test_city(self):
        result = self.address.city()
        parent_file = pull('cities', self.address.lang)
        self.assertIn(result + '\n', parent_file)


class NumbersTestCase(TestCase):
    def setUp(self):
        self.numbers = Numbers()

    def tearDown(self):
        del self.numbers

    def test_floats(self):
        result = self.numbers.floats()
        self.assertEqual(len(result), 100)
        self.assertIsInstance(result, array.array)

        result = self.numbers.floats(n=3, to_list=True)
        self.assertEqual(len(result), 1000)
        self.assertIsInstance(result, list)

    def test_primes(self):
        result = self.numbers.primes()
        self.assertEqual(len(result), 50)
        self.assertIsInstance(result, array.array)

        result = self.numbers.primes(n=3, to_list=True)
        self.assertEqual(len(result), 500)
        self.assertIsInstance(result, list)


class TextTestCase(TestCase):
    def setUp(self):
        self.data = Text(LANG)

    def tearDown(self):
        del self.data

    def test_sentence(self):
        result = self.data.sentence() + '\n'
        parent_file = pull('text', self.data.lang)
        self.assertIn(result, parent_file)

    def test_title(self):
        result = self.data.title() + '\n'
        parent_file = pull('text', self.data.lang)
        self.assertIn(result, parent_file)

    def test_lorem_ipsum(self):
        result = self.data.lorem_ipsum(quantity=2)
        self.assertIsNot(result, None)
        self.assertIsInstance(result, str)

    def test_words(self):
        result = self.data.words()
        self.assertEqual(len(result), 5)

        result = self.data.words(quantity=1)
        self.assertEqual(len(result), 1)

    def test_word(self):
        result = self.data.word()
        parent_file = pull('words', self.data.lang)
        self.assertIn(result + '\n', parent_file)

    def test_swear_word(self):
        result = self.data.swear_word()
        parent_file = pull('swear_words', self.data.lang)
        self.assertIn(result + '\n', parent_file)

    def test_naughty_strings(self):
        result = self.data.naughty_strings()
        self.assertTrue(len(result) > 10)
        self.assertIsInstance(result, list)

    def test_quote_from_movie(self):
        result = self.data.quote_from_movie()
        parent_file = pull('quotes', self.data.lang)
        self.assertIn(result + '\n', parent_file)

    def test_color(self):
        result = self.data.color()
        parent_file = pull('colors', self.data.lang)
        self.assertIn(result + '\n', parent_file)

    def test_hex_color(self):
        result = self.data.hex_color()
        self.assertIn('#', result)

    def test_emoji(self):
        result = self.data.emoji()
        self.assertIn(result, common.EMOJI)

    def test_hashtags(self):
        result = self.data.hashtags(quantity=5)
        self.assertEqual(len(result), 5)

        result = self.data.hashtags(quantity=1, category='general')
        self.assertIn(result[0], common.HASHTAGS['general'])

    def test_weather(self):
        result = self.data.weather(scale='c').split(' ')
        temp, scale = float(result[0]), result[1]
        self.assertEqual(scale, '°C')
        self.assertTrue((temp >= -30) and (temp <= 40))

        result = self.data.weather(scale='f', a=0, b=10).split(' ')
        temp, scale = float(result[0]), result[1]
        self.assertEqual(scale, '°F')
        self.assertTrue((temp >= 0) and (temp <= (10 * 1.8) + 32))


class BusinessTestCase(TestCase):
    def setUp(self):
        self.business = Business(LANG)

    def test_company_type(self):
        result = self.business.company_type()
        self.assertTrue(len(result) > 8)

    def test_company(self):
        result = self.business.company()
        parent_file = pull('company', self.business.lang)
        self.assertIn(result + '\n', parent_file)

    def test_copyright(self):
        result = self.business.copyright()
        copyright_symbol = '©'
        self.assertIn(copyright_symbol, result)

        result = self.business.copyright(without_date=True)
        self.assertFalse(any(char.isdigit() for char in result))

    def test_currency_sio(self):
        result = self.business.currency_iso()
        self.assertIn(result, common.CURRENCY)


class PersonalTestCase(TestCase):
    def setUp(self):
        self.person = Personal(LANG)

    def tearDown(self):
        del self.person

    def test_age(self):
        result = self.person.age(maximum=55)
        self.assertTrue(result <= 55)

    def test_name(self):
        result = self.person.name()
        parent_file = pull('f_names', self.person.lang)
        self.assertIn(result + '\n', parent_file)

        result = self.person.name('m')
        parent_file = pull('m_names', self.person.lang)
        self.assertIn(result + '\n', parent_file)

    def test_telephone(self):
        result = self.person.telephone()
        self.assertTrue(len(result) >= 11)

        mask = '+5 (###)-###-##-##'
        result2 = self.person.telephone(mask=mask)
        head = result2.split(' ')[0]
        self.assertEqual(head, '+5')

    def test_surname(self):
        if self.person.lang == 'ru':
            result = self.person.surname('f')
            parent_file = pull('f_surnames', self.person.lang)
            self.assertIn(result + '\n', parent_file)

            result = self.person.surname('m')
            parent_file = pull('m_surnames', self.person.lang)
            self.assertIn(result + '\n', parent_file)
        else:
            result = self.person.surname()
            parent_file = pull('surnames', self.person.lang)
            self.assertIn(result + '\n', parent_file)

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
        plain = self.person.password(length=15)
        self.assertEqual(len(plain), 15)

        md5 = self.person.password(algorithm='md5')
        self.assertEqual(len(md5), 32)

        sha1 = self.person.password(algorithm='sha1')
        self.assertEqual(len(sha1), 40)

        sha256 = self.person.password(algorithm='sha256')
        self.assertEqual(len(sha256), 64)

        sha512 = self.person.password(algorithm='sha512')
        self.assertEqual(len(sha512), 128)

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
        self.assertIn(result, common.SUBREDDITS)

        full_result = self.person.subreddit(full_url=True)
        self.assertTrue(len(full_result) > 20)

        result_nsfw = self.person.subreddit(nsfw=True)
        self.assertIn(result_nsfw, common.SUBREDDITS_NSFW)

        full_result = self.person.subreddit(nsfw=True, full_url=True)
        self.assertTrue(len(full_result) > 20)

    def test_bitcoin(self):
        result = self.person.bitcoin()
        self.assertEqual(len(result), 34)

    def test_cvv(self):
        result = self.person.cvv()
        self.assertTrue((100 <= result) and (result <= 999))

    def test_credit_card_number(self):
        result = self.person.credit_card_number()
        self.assertTrue(re.match(r'[\d]+((-|\s)?[\d]+)+', result))

    def test_expiration_date(self):
        result = self.person.credit_card_expiration_date(mi=16, mx=25)
        year = result.split('/')[1]
        self.assertTrue((int(year) >= 16) and (int(year) <= 25))

    def test_cid(self):
        result = self.person.cid()
        self.assertTrue((1000 <= result) and (result <= 9999))

    def test_gender(self):
        result = self.person.gender() + '\n'
        self.assertIn(result, pull('gender', self.person.lang))

        result_abbr = self.person.gender(abbr=True) + '\n'
        self.assertEqual(len(result_abbr), 2)

    def test_height(self):
        result = self.person.height(from_=1.60, to_=1.90)
        self.assertTrue(result.startswith('1'))
        self.assertIsInstance(result, str)

    def test_weight(self):
        result = self.person.weight(from_=40, to_=60)
        self.assertTrue((result >= 40) and (result <= 60))

    def test_blood_type(self):
        result = self.person.blood_type()
        self.assertIn(result, common.BLOOD_GROUPS)

    def test_sexual_orientation(self):
        result = self.person.sexual_orientation()
        parent_file = pull('sexuality', self.person.lang)
        self.assertIn(result + '\n', parent_file)

    def test_profession(self):
        result = self.person.profession()
        parent_file = pull('professions', self.person.lang)
        self.assertIn(result + '\n', parent_file)

    def test_university(self):
        result = self.person.university()
        parent_file = pull('university', self.person.lang)
        self.assertIn(result + '\n', parent_file)

    def test_qualification(self):
        result = self.person.qualification()
        parent_file = pull('qualifications', self.person.lang)
        self.assertIn(result + '\n', parent_file)

    def test_language(self):
        result = self.person.language()
        parent_file = pull('languages', self.person.lang)
        self.assertIn(result + '\n', parent_file)

    def test_favorite_movie(self):
        result = self.person.favorite_movie()
        parent_file = pull('movies', self.person.lang)
        self.assertIn(result + '\n', parent_file)

    def test_favorite_music_genre(self):
        result = self.person.favorite_music_genre()
        self.assertIn(result, common.FAVORITE_MUSIC_GENRE)

    def test_worldview(self):
        result = self.person.worldview()
        parent_file = pull('worldview', self.person.lang)
        self.assertIn(result + '\n', parent_file)

    def test_views_on(self):
        result = self.person.views_on()
        parent_file = pull('views_on', self.person.lang)
        self.assertIn(result + '\n', parent_file)

    def test_political_views(self):
        result = self.person.political_views()
        parent_file = pull('political_views', self.person.lang)
        self.assertIn(result + '\n', parent_file)

    def test_avatar(self):
        result = self.person.avatar()
        self.assertTrue(len(result) > 20)

    def test_vehicle(self):
        result = self.person.vehicle()
        self.assertIn(result, common.THE_VEHICLES)


class DatetimeTestCase(TestCase):
    def setUp(self):
        self.datetime = Datetime(LANG)

    def tearDown(self):
        del self.datetime

    def test_day_of_week(self):
        result = self.datetime.day_of_week() + '\n'
        self.assertGreater(len(result), 4)

        result_abbr = self.datetime.day_of_week(abbr=True)
        self.assertTrue(len(result_abbr) < 6 or '.' in result_abbr)

    def test_month(self):
        result = self.datetime.month() + '\n'
        self.assertGreater(len(result), 3)

        result_abbr = self.datetime.month(abbr=True)
        self.assertIsInstance(result_abbr, str)

    def test_year(self):
        result = self.datetime.year(from_=2000, to_=2016)
        self.assertTrue((result >= 2000) and (result <= 2016))

    def test_periodicity(self):
        result = self.datetime.periodicity()
        parent_file = pull('periodicity', self.datetime.lang)
        self.assertIn(result + '\n', parent_file)

    def test_day_of_month(self):
        result = self.datetime.day_of_month()
        self.assertTrue((result >= 1) or (result <= 31))

    def test_birthday(self):
        result = self.datetime.birthday()
        self.assertIsInstance(result, str)


class NetworkTestCase(TestCase):
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
        result = self.net.user_agent()
        parent_file = pull('useragents', 'en')
        self.assertIn(result + '\n', parent_file)


class FileTestCase(TestCase):
    def setUp(self):
        self.file = File()

    def tearDown(self):
        del self.file

    def test_extension(self):
        text = self.file.extension()
        self.assertIn(text, common.EXTENSIONS['text'])


class ScienceTestCase(TestCase):
    def setUp(self):
        self.science = Science(LANG)

    def tearDown(self):
        del self.science

    def test_math_formula(self):
        result = self.science.math_formula()
        self.assertIn(result, common.MATH_FORMULAS)

    def test_article_on_wiki(self):
        result = self.science.article_on_wiki()
        parent_file = pull('science_wiki', self.science.lang)
        self.assertIn(result + '\n', parent_file)

    def test_scientist(self):
        result = self.science.scientist()
        parent_file = pull('scientist', self.science.lang)
        self.assertIn(result + '\n', parent_file)

    def test_chemical_element(self):
        result = self.science.chemical_element(name_only=True)
        self.assertGreater(len(result), 2)

        _result = self.science.chemical_element(name_only=False)
        self.assertIsInstance(_result, dict)


class DevelopmentTestCase(TestCase):
    def setUp(self):
        self.dev = Development()

    def tearDown(self):
        del self.dev

    def test_license(self):
        result = self.dev.software_license()
        self.assertIn(result, common.LICENSES)

    def test_version(self):
        result = self.dev.version().split('.')
        major = int(result[0])
        self.assertTrue((major >= 0) and (major <= 11))
        minor = int(result[1])
        self.assertTrue((minor >= 0) and (minor <= 11))
        micro = int(result[2])
        self.assertTrue((micro >= 0) and (micro <= 11))

    def test_programming_language(self):
        result = self.dev.programming_language()
        self.assertIn(result, common.PROGRAMMING_LANGS)

    def test_database(self):
        result = self.dev.database()
        self.assertIn(result, common.SQL)

        _result = self.dev.database(nosql=True)
        self.assertIn(_result, common.NOSQL)

    def test_other(self):
        result = self.dev.other()
        self.assertIn(result, common.OTHER_TECH)

    def test_framework(self):
        result = self.dev.framework(_type='front')
        self.assertIn(result, common.FRONTEND)

        _result = self.dev.framework(_type='back')
        self.assertIn(_result, common.BACKEND)

    def test_stack_of_tech(self):
        result = self.dev.stack_of_tech(nosql=True)
        self.assertIsInstance(result, dict)

    def test_os(self):
        result = self.dev.os()
        self.assertIn(result, common.OS)

    def test_stackoverflow_question(self):
        url = self.dev.stackoverflow_question()
        post_id = int(url.split('/')[-1])
        self.assertTrue((post_id >= 1000000) and
                        (post_id <= 9999999))


class FoodTestCase(TestCase):
    def setUp(self):
        self.food = Food(LANG)

    def tearDown(self):
        del self.food

    def test_berry(self):
        result = self.food.berry()
        parent_file = pull('berries', self.food.lang)
        self.assertIn(result + '\n', parent_file)

    def test_vegetable(self):
        result = self.food.vegetable()
        parent_file = pull('vegetables', self.food.lang)
        self.assertIn(result + '\n', parent_file)

    def test_fruit(self):
        result = self.food.fruit()
        parent_file = pull('fruits', self.food.lang)
        self.assertIn(result + '\n', parent_file)

    def test_dish(self):
        result = self.food.dish()
        parent_file = pull('dishes', self.food.lang)
        self.assertIn(result + '\n', parent_file)

    def test_drink(self):
        result = self.food.drink()
        parent_file = pull('drinks', self.food.lang)
        self.assertIn(result + '\n', parent_file)

    def test_spices(self):
        result = self.food.spices()
        parent_file = pull('spices', self.food.lang)
        self.assertIn(result + '\n', parent_file)

    def test_mushroom(self):
        result = self.food.mushroom()
        parent_file = pull('mushrooms', self.food.lang)
        self.assertIn(result + '\n', parent_file)


class HardwareTestCase(TestCase):
    def setUp(self):
        self.hard = Hardware()

    def tearDown(self):
        del self.hard

    def test_resolution(self):
        result = self.hard.resolution()
        self.assertIn(result, common.RESOLUTIONS)

    def test_screen_size(self):
        result = self.hard.screen_size()
        self.assertIn(result, common.SCREEN_SIZES)

    def test_generation(self):
        result = self.hard.generation()
        self.assertIn(result, common.GENERATION)

    def test_cpu_frequency(self):
        result = self.hard.cpu_frequency().split('G')[0]
        self.assertLess(float(result), 4.4)

    def test_cpu(self):
        result = self.hard.cpu()
        self.assertIn(result, common.CPU)

    def test_cpu_codename(self):
        result = self.hard.cpu_codename()
        self.assertIn(result, common.CPU_CODENAMES)

    def test_ram_type(self):
        result = self.hard.ram_type()
        self.assertIn(result, ['DDR2', 'DDR3', 'DDR4'])

    def test_ram_size(self):
        result = self.hard.ram_size().split(' ')
        self.assertGreater(len(result), 0)

    def test_ssd_or_hdd(self):
        result = self.hard.ssd_or_hdd()
        self.assertIn(result, common.MEMORY)

    def test_graphics(self):
        result = self.hard.graphics()
        self.assertIn(result, common.GRAPHICS)

    def test_manufacturer(self):
        result = self.hard.manufacturer()
        self.assertIn(result, common.MANUFACTURERS)

    def test_hardware_full(self):
        result = self.hard.hardware_full_info()
        self.assertGreater(len(result), 15)

    def test_phone_model(self):
        result = self.hard.phone_model()
        self.assertIn(result, common.PHONE_MODELS)


class PullTestCase(TestCase):
    def test_pull(self):
        result = pull('views_on', 'en')
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertRaises(
            UnsupportedLocale, lambda: pull('views_on', 'spoke'))
        self.assertRaises(
            FileNotFoundError, lambda: pull('something', 'en'))


class ChurchTestCase(TestCase):
    def setUp(self):
        self.church = Church('en')

    def test_personal(self):
        result = self.church.personal.username()
        self.assertIsNotNone(result)

    def test_text(self):
        result = self.church.text.words()
        self.assertIsNotNone(result)

    def test_address(self):
        result = self.church.address.address()
        self.assertIsNotNone(result)

    def test_food(self):
        result = self.church.food.fruit()
        self.assertIsNotNone(result)

    def test_science(self):
        result = self.church.science.scientist()
        self.assertIsNotNone(result)

    def test_business(self):
        result = self.church.business.copyright()
        self.assertIsNotNone(result)
