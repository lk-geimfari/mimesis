# -*- coding: utf-8 -*-

import re
from unittest import TestCase

from elizabeth import Personal
import elizabeth.core.interdata as common

from tests.test_data import DummyCase
from ._patterns import *


class PersonalBaseTest(TestCase):
    def setUp(self):
        self.personal = Personal()

    def tearDown(self):
        del self.personal

    def test_age(self):
        result = self.personal.age(maximum=55)
        self.assertTrue(result <= 55)

    def test_paypal(self):
        result = self.personal.paypal()
        self.assertIsNotNone(result)

    def test_password(self):
        plain = self.personal.password(length=15)
        self.assertEqual(len(plain), 15)

        md5 = self.personal.password(algorithm='md5')
        self.assertEqual(len(md5), 32)

        sha1 = self.personal.password(algorithm='sha1')
        self.assertEqual(len(sha1), 40)

        sha256 = self.personal.password(algorithm='sha256')
        self.assertEqual(len(sha256), 64)

        sha512 = self.personal.password(algorithm='sha512')
        self.assertEqual(len(sha512), 128)

    def test_username(self):
        result = self.personal.username()
        self.assertTrue(re.match(USERNAME_REGEX, result))

    def test_email(self):
        result = self.personal.email()
        self.assertTrue(re.match(EMAIL_REGEX, result))

    def test_bitcoin(self):
        result = self.personal.bitcoin()
        self.assertEqual(len(result), 34)

    def test_cvv(self):
        result = self.personal.cvv()
        self.assertTrue((100 <= result) and (result <= 999))

    def test_credit_card_number(self):
        result = self.personal.credit_card_number()
        self.assertTrue(re.match(CREDIT_CARD_REGEX, result))

    def test_expiration_date(self):
        result = self.personal.credit_card_expiration_date(
            minimum=16, maximum=25)

        year = result.split('/')[1]
        self.assertTrue((int(year) >= 16) and (int(year) <= 25))

    def test_cid(self):
        result = self.personal.cid()
        self.assertTrue((1000 <= result) and (result <= 9999))

    def test_height(self):
        result = self.personal.height(minimum=1.60, maximum=1.90)
        self.assertTrue(result.startswith('1'))
        self.assertIsInstance(result, str)

    def test_weight(self):
        result = self.personal.weight(minimum=40, maximum=60)
        self.assertTrue((result >= 40) and (result <= 60))

    def test_blood_type(self):
        result = self.personal.blood_type()
        self.assertIn(result, common.BLOOD_GROUPS)

    def test_favorite_movie(self):
        result = self.personal.favorite_movie()
        self.assertIn(result, self.personal.data['favorite_movie'])

    def test_favorite_music_genre(self):
        result = self.personal.favorite_music_genre()
        self.assertIn(result, common.FAVORITE_MUSIC_GENRE)

    def test_avatar(self):
        result = self.personal.avatar()
        self.assertTrue(len(result) > 20)

    def test_identifier(self):
        result = self.personal.identifier()
        mask = '##-##/##'
        self.assertEqual(len(mask), len(result))

        result = self.personal.identifier(mask='##', suffix=True)
        lst = result.split()
        _id, sfx = lst[0], lst[1]
        self.assertEqual(len(_id), 2)
        self.assertEqual(len(sfx), 2)

        result = self.personal.identifier(suffix=True)
        suffix = result.split(' ')[1]
        self.assertTrue(suffix.isalpha())


class PersonalTestCase(DummyCase):
    def test_name(self):
        result = self.generic.personal.name(gender='female')
        self.assertIn(result, self.generic.personal.data['names']['female'])

        result = self.generic.personal.name(gender='male')
        self.assertIn(result, self.generic.personal.data['names']['male'])

    def test_telephone(self):
        result = self.generic.personal.telephone()
        self.assertTrue(len(result) >= 11)

        mask = '+5 (###)-###-##-##'
        result2 = self.generic.personal.telephone(mask=mask)
        head = result2.split(' ')[0]
        self.assertEqual(head, '+5')

    def test_surname(self):
        diff_surnames = ('ru', 'is')
        if self.generic.personal.locale in diff_surnames:

            result = self.generic.personal.surname(gender='female')
            self.assertIn(
                result, self.generic.personal.data['surnames']['female'])

            result = self.generic.personal.surname(gender='male')
            self.assertIn(
                result, self.generic.personal.data['surnames']['male'])
        else:
            result = self.generic.personal.surname()
            self.assertIn(result, self.generic.personal.data['surnames'])

    def test_full_name(self):
        result = self.generic.personal.full_name(gender='female')
        _result = result.split(' ')
        self.assertIsInstance(_result, list)

    def test_gender(self):
        result = self.generic.personal.gender()
        self.assertIn(result, self.generic.personal.data['gender'])

        symbol = self.generic.personal.gender(symbol=True)
        self.assertIn(symbol, common.GENDER_SYMBOLS)

    def test_sexual_orientation(self):
        result = self.generic.personal.sexual_orientation()
        self.assertIn(result, self.generic.personal.data['sexuality'])

        symbol = self.generic.personal.sexual_orientation(symbol=True)
        self.assertIn(symbol, common.SEXUALITY_SYMBOLS)

    def test_profession(self):
        result = self.generic.personal.occupation()
        self.assertIn(result, self.generic.personal.data['occupation'])

    def test_university(self):
        result = self.generic.personal.university()
        self.assertIn(result, self.generic.personal.data['university'])

    def test_academic_degree(self):
        result = self.generic.personal.academic_degree()
        self.assertIn(result, self.generic.personal.data['academic_degree'])

    def test_language(self):
        result = self.generic.personal.language()
        self.assertIn(result, self.generic.personal.data['language'])

    def test_worldview(self):
        result = self.generic.personal.worldview()
        self.assertIn(result, self.generic.personal.data['worldview'])

    def test_views_on(self):
        result = self.generic.personal.views_on()
        self.assertIn(result, self.generic.personal.data['views_on'])

    def test_political_views(self):
        result = self.generic.personal.political_views()
        self.assertIn(result, self.generic.personal.data['political_views'])

    def test_title(self):
        result = self.generic.personal.title(type_='typical')
        self.assertIsInstance(result, str)

        result2 = self.generic.personal.title(type_='academic')
        self.assertIsInstance(result2, str)
