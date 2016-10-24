# -*- coding: utf-8 -*-

import re
from unittest import TestCase

import church._common as common
from church.church import Personal
from tests import LANG


class PersonalTestCase(TestCase):
    def setUp(self):
        self.person = Personal(LANG)
        self.db = self.person.data

    def tearDown(self):
        del self.person

    def test_age(self):
        result = self.person.age(mx=55)
        self.assertTrue(result <= 55)

    def test_name(self):
        result = self.person.name(gender='female')
        self.assertIn(result, self.db['names']['female'])

        result = self.person.name(gender='male')
        self.assertIn(result, self.db['names']['male'])

    def test_telephone(self):
        result = self.person.telephone()
        self.assertTrue(len(result) >= 11)

        mask = '+5 (###)-###-##-##'
        result2 = self.person.telephone(mask=mask)
        head = result2.split(' ')[0]
        self.assertEqual(head, '+5')

    def test_surname(self):
        if self.person.lang == 'ru':
            result = self.person.surname(gender='female')
            self.assertIn(result, self.db['surnames']['female'])

            result = self.person.surname(gender='male')
            self.assertIn(result, self.db['surnames']['male'])
        else:
            result = self.person.surname()
            self.assertIn(result, self.db['surnames'])

    def test_full_name(self):
        result = self.person.full_name(gender='female')
        _result = result.split(' ')
        self.assertIsInstance(_result, list)

    def test_username(self):
        result = self.person.username()
        self.assertTrue(re.match(r'^[a-zA-Z0-9_.-]+$', result))

    def test_twitter(self):
        result = self.person.twitter(gender='female')
        self.assertIsNotNone(result)

        _result = self.person.twitter(gender='male')
        self.assertIsNotNone(_result)

    def test_facebook(self):
        result = self.person.facebook(gender='female')
        self.assertIsNotNone(result)

        _result = self.person.facebook(gender='female')
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
        result = self.person.gender()
        self.assertIn(result, self.db['gender'])

        symbol = self.person.gender(symbol=True)
        self.assertIn(symbol, common.GENDER_SYMBOLS)

    def test_height(self):
        result = self.person.height(from_=1.60, to=1.90)
        self.assertTrue(result.startswith('1'))
        self.assertIsInstance(result, str)

    def test_weight(self):
        result = self.person.weight(from_=40, to=60)
        self.assertTrue((result >= 40) and (result <= 60))

    def test_blood_type(self):
        result = self.person.blood_type()
        self.assertIn(result, common.BLOOD_GROUPS)

    def test_sexual_orientation(self):
        result = self.person.sexual_orientation()
        self.assertIn(result, self.db['sexuality'])

        symbol = self.person.sexual_orientation(symbol=True)
        self.assertIn(symbol, common.SEXUALITY_SYMBOLS)

    def test_profession(self):
        result = self.person.occupation()
        self.assertIn(result, self.db['occupation'])

    def test_university(self):
        result = self.person.university()
        self.assertIn(result, self.db['university'])

    def test_academic_degree(self):
        result = self.person.academic_degree()
        self.assertIn(result, self.db['academic_degree'])

    def test_language(self):
        result = self.person.language()
        self.assertIn(result, self.db['language'])

    def test_favorite_movie(self):
        result = self.person.favorite_movie()
        self.assertIn(result, self.db['favorite_movie'])

    def test_favorite_music_genre(self):
        result = self.person.favorite_music_genre()
        self.assertIn(result, common.FAVORITE_MUSIC_GENRE)

    def test_worldview(self):
        result = self.person.worldview()
        self.assertIn(result, self.db['worldview'])

    def test_views_on(self):
        result = self.person.views_on()
        self.assertIn(result, self.db['views_on'])

    def test_political_views(self):
        result = self.person.political_views()
        self.assertIn(result, self.db['political_views'])

    def test_avatar(self):
        result = self.person.avatar()
        self.assertTrue(len(result) > 20)

    def test_vehicle(self):
        result = self.person.vehicle()
        self.assertIn(result, common.THE_VEHICLES)
