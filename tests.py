import re
from unittest import TestCase

from church.church import (
    Address, BasicData, Personal, Datetime, Network, File, Science, Development
)
from church.utils import pull

# LANG = 'ru_ru'
LANG = 'en_us'


# LANG = 'de_de'


class AddressTestCase(TestCase):
    address = Address(LANG)

    def test_street_number(self):
        result = self.address.street_number()
        assert re.match(r'[0-9]{1,5}$', result)

    def test_street_name(self):
        result = self.address.street_name() + '\n'
        assert result in pull('street', self.address.lang)

    def test_street_suffix(self):
        result = self.address.street_suffix() + '\n'
        assert result in pull('street_suffix', self.address.lang)

    def test_state_or_subject(self):
        result = self.address.state_or_subject() + '\n'
        if self.address.lang == 'en_us':
            assert result in pull('states', self.address.lang)
        elif self.address.lang == 'ru_ru':
            assert result in pull('subjects', self.address.lang)

    def test_postal_code(self):
        result = self.address.postal_code()
        if self.address.lang == 'en_us':
            assert re.match(r'[0-9]{5}$', result) is not None
        elif self.address.lang == 'ru_ru':
            assert re.match(r'[0-9]{6}$', result)

    def test_country(self):
        result = self.address.country() + '\n'
        assert len(result) > 3

        result2 = self.address.country(only_iso_code=True) + '\n'
        assert len(result2) < 4

    def test_city(self):
        result = self.address.city() + '\n'
        assert result in pull('cities', self.address.lang)


class BasicDataTestCase(TestCase):
    data = BasicData(LANG)

    def test_sentence(self):
        result = self.data.sentence() + '\n'
        assert result in pull('text', self.data.lang)

    def test_title(self):
        result = self.data.title() + '\n'
        assert result in pull('text', self.data.lang)

    def test_words(self):
        result = self.data.words()
        assert len(result) == 5

        result = self.data.words(quantity=1)
        assert len(result) == 1

    def test_word(self):
        result = self.data.word() + '\n'
        assert result in pull('words', self.data.lang)

    def test_quote_from_movie(self):
        result = self.data.quote_from_movie() + '\n'
        assert result in pull('quotes', self.data.lang)

    def test_currency_sio(self):
        result = self.data.currency_iso() + '\n'
        assert result in pull('currency', self.data.lang)

    def test_color(self):
        result = self.data.color() + '\n'
        assert result in pull('colors', self.data.lang)

    def test_company_type(self):
        result = self.data.company_type(abbreviated=True)
        assert len(result) < 7

    def test_company(self):
        result = self.data.company() + '\n'
        assert result in pull('company', self.data.lang)


class PersonalTestCase(TestCase):
    person = Personal(LANG)

    def test_age(self):
        result = self.person.age(maximum=55)
        assert result <= 55

    def test_name(self):
        result = self.person.name() + '\n'
        assert result in pull('f_names', self.person.lang)

        result = self.person.name('m') + '\n'
        assert result in pull('m_names', self.person.lang)

    def test_telephone(self):
        result = self.person.telephone()
        assert re.match(
            r'^((8|\+[1-9])[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$', result)

    def test_surname(self):
        if self.person.lang == 'ru_ru':
            result = self.person.surname('f') + '\n'
            assert result in pull('f_surnames', self.person.lang)

            result = self.person.surname('m') + '\n'
            assert result in pull('m_surnames', self.person.lang)

        result = self.person.surname() + '\n'
        assert result in pull('surnames', self.person.lang)

    def test_full_name(self):
        if self.person.lang == 'ru_ru':
            result = self.person.full_name('f').split(' ')
            f_surname = result[0] + '\n'
            assert f_surname in pull('f_surnames', self.person.lang)

            f_name = result[1] + '\n'
            assert f_name in pull('f_names', self.person.lang)

            result = self.person.full_name('m').split(' ')
            m_surname = result[0] + '\n'
            assert m_surname in pull('m_surnames', self.person.lang)

            m_name = result[1] + '\n'
            assert m_name in pull('m_names', self.person.lang)

    def test_username(self):
        result = self.person.username()
        assert re.match(r'^[a-zA-Z0-9_.-]+$', result)

    def test_password(self):
        result = self.person.password(length=10)
        assert len(result) == 10

    def test_email(self):
        result = self.person.email()
        assert re.match(
            r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", result)

    def test_home_page(self):
        result = self.person.home_page()
        assert re.match(r'http[s]?://(?:[a-zA-Z]|[0-9]|'
                        r'[$-_@.&+]|[!*\(\),]|'
                        r'(?:%[0-9a-fA-F][0-9a-fA-F]))+', result)

    def test_bitcoin(self):
        result = self.person.bitcoin()
        assert len(result) == 34

        p2pkh = self.person.bitcoin(address_format='p2pkh')
        assert p2pkh[0] == '1'
        p2sh = self.person.bitcoin(address_format='p2sh')
        assert p2sh[0] == '3'

    def test_cvv(self):
        result = self.person.cvv()
        assert (100 <= result) and (result <= 999)

    def test_credit_card_number(self):
        result = self.person.credit_card_number()
        assert re.match(r'[\d]+((-|\s)?[\d]+)+', result)

    def test_cid(self):
        result = self.person.cid()
        assert (1000 <= result) and (result <= 9999)

    def test_gender(self):
        result = self.person.gender() + '\n'
        assert result in pull('gender', self.person.lang)

        result_abbr = self.person.gender(abbreviated=True) + '\n'
        assert len(result_abbr) == 2

    def test_profession(self):
        result = self.person.profession() + '\n'
        assert result in pull('professions', self.person.lang)

    def test_university(self):
        result = self.person.university() + '\n'
        assert result in pull('university', self.person.lang)

    def test_qualification(self):
        result = self.person.qualification() + '\n'
        assert result in pull('qualifications', self.person.lang)

    def test_language(self):
        result = self.person.language() + '\n'
        assert result in pull('languages', self.person.lang)

    def test_favorite_movie(self):
        result = self.person.favorite_movie() + '\n'
        assert result in pull('favorite_movie', self.person.lang)

    def test_worldview(self):
        result = self.person.worldview() + '\n'
        assert result in pull('worldview', self.person.lang)

    def test_views_on(self):
        result = self.person.views_on() + '\n'
        assert result in pull('views_on', self.person.lang)

    def test_political_views(self):
        result = self.person.political_views() + '\n'
        assert result in pull('political_views', self.person.lang)


class DatetimeTestCase(TestCase):
    datetime = Datetime(LANG)

    def test_day_of_week(self):
        result = self.datetime.day_of_week() + '\n'
        assert len(result) > 3

        result_abbr = self.datetime.day_of_week(abbreviated=True)
        assert len(result_abbr) < 6 or '.' in result_abbr

    def test_month(self):
        result = self.datetime.month() + '\n'
        assert len(result) > 3

        result_abbr = self.datetime.month(abbreviated=True)
        assert len(result_abbr) < 6

    def test_periodicity(self):
        result = self.datetime.periodicity() + '\n'
        assert result in pull('periodicity', self.datetime.lang)

    def test_day_of_month(self):
        result = self.datetime.day_of_month()
        assert result >= 1 or result <= 31


class NetworkTestCase(TestCase):
    net = Network()

    def test_ip_v4(self):
        result = self.net.ip_v4()
        assert re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", result)

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

        assert re.match(ip_v6_pattern, result)

    def test_mac_address(self):
        result = self.net.mac_address()
        mac_pattern = r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'
        assert re.match(mac_pattern, result)

    def test_user_agent(self):
        result = self.net.user_agent() + '\n'
        assert result in pull('useragents', LANG)


class FileTestCase(TestCase):
    file = File()

    def test_extension(self):
        source = self.file.extension('source')
        assert len(source) < 8

        other = self.file.extension()
        text = ['.doc', '.docx', '.log',
                '.rtf', '.md', '.pdf',
                '.odt', '.txt'
                ]
        assert other in text


class ScienceTestCase(TestCase):
    science = Science(LANG)

    def test_math_formula(self):
        result = self.science.math_formula() + '\n'
        assert result in pull('math_formula', 'en_us')

    def test_physical_law(self):
        result = self.science.physical_law() + '\n'
        assert result in pull('physical_law', self.science.lang)

    def test_article_on_wiki(self):
        result = self.science.article_on_wiki() + '\n'
        assert result in pull('science_wiki')

    def test_scientist(self):
        result = self.science.scientist() + '\n'
        assert result in pull('scientist')

    def test_chemical_element(self):
        result = self.science.chemical_element(name_only=True)
        assert len(result) > 2

        not_reuslt = self.science.chemical_element(name_only=False)
        assert isinstance(not_reuslt, dict)


class DevelopmentTestCase(TestCase):
    dev = Development()

    def test_license(self):
        _license = [
            'Apache License, 2.0 (Apache-2.0)',
            'The BSD 3-Clause License',
            'The BSD 2-Clause License',
            'GNU General Public License (GPL)',
            'General Public License (LGPL),'
            'MIT license (MIT)',
            'Mozilla Public License 2.0 (MPL-2.0)',
            'Common Development and Distribution License (CDDL-1.0)',
            'Eclipse Public License (EPL-1.0)'
        ]

        result = self.dev.license()
        assert result in _license

    def test_programming_language(self):
        result = self.dev.programming_language() + '\n'
        assert result in pull('pro_lang', 'en_us')

    def test_database(self):
        _sql = ['MariaDB', 'MySQL', 'PostgreSQL', 'Oracle DB', 'SQLite']

        result = self.dev.database()
        assert result in _sql

        _nosql = ['MongoDB', 'RethinkDB',
                  'Couchbase', 'CouchDB',
                  'Aerospike', 'MemcacheDB',
                  'MUMPS,  Riak', 'Redis',
                  'AllegroGraph', 'Neo4J',
                  'InfiniteGraph'
                  ]
        _result = self.dev.database(nosql=True)
        assert _result in _nosql

    def test_other(self):
        _list = ['Docker', 'Rkt',
                 'LXC', 'Vagrant',
                 'Elasticsearch',
                 'Nginx', 'Git',
                 'Mercurial', 'Jira',
                 'REST', 'Apache Hadoop',
                 'Scrum', 'Redmine',
                 ]
        result = self.dev.other()
        assert result in _list

    def test_framework(self):
        result = self.dev.framework(_type='front') + '\n'
        assert result in pull('front_frmwk')

        _result = self.dev.framework(_type='back') + '\n'
        assert _result in pull('back_frmwk')

    def test_stack_of_tech(self):
        result = self.dev.stack_of_tech(nosql=True)
        assert isinstance(result, dict)

    def test_github_repo(self):
        url = self.dev.github_repo() + '\n'
        assert url in pull('github_repos')