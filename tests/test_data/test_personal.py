# -*- coding: utf-8 -*-

import re

import pytest

from mimesis.data import (BLOOD_GROUPS, ENGLISH_LEVEL, FAVORITE_MUSIC_GENRE,
                          GENDER_SYMBOLS, SEXUALITY_SYMBOLS)
from mimesis.exceptions import UnsupportedAlgorithm, WrongArgument

from . import _patterns as p


def test_str(personal):
    assert re.match(p.STR_REGEX, str(personal))


def test_age(personal):
    result = personal.age(maximum=55)
    assert result <= 55


def test_age_store(personal):
    result = personal._store['age']
    assert result == 0


def test_age_update(personal):
    result = personal.age() - personal._store['age']
    assert result == 0


def test_child_count(personal):
    result = personal.child_count(max_childs=10)
    assert result <= 10


def test_work_experience(personal):
    result = personal.work_experience(
        working_start_age=0) - personal._store['age']
    assert result == 0


def test_work_experience_store(personal):
    result = personal.work_experience() - personal.work_experience()
    assert result == 0


def test_work_experience_extreme(personal):
    result = personal.work_experience(working_start_age=100000)
    assert result == 0


def test_paypal(personal):
    result = personal.paypal()
    assert result is not None


def test_password(personal):
    plain = personal.password(length=15)
    assert len(plain) == 15

    md5 = personal.password(algorithm='md5')
    assert len(md5) == 32

    sha1 = personal.password(algorithm='sha1')
    assert len(sha1) == 40

    sha256 = personal.password(algorithm='sha256')
    assert len(sha256) == 64

    sha512 = personal.password(algorithm='sha512')
    assert len(sha512) == 128

    with pytest.raises(UnsupportedAlgorithm):
        personal.password(algorithm='sha42')


def test_username(personal):
    result = personal.username()
    assert re.match(p.USERNAME_REGEX, result)

    with pytest.raises(WrongArgument):
        personal.username(gender='nil')


def test_email(personal):
    result = personal.email()
    assert re.match(p.EMAIL_REGEX, result)

    domains = ['@example.com']
    result = personal.email(domains=domains)
    assert re.match(p.EMAIL_REGEX, result)
    assert result.split('@')[1] == 'example.com'


def test_bitcoin(personal):
    result = personal.bitcoin()
    assert len(result) == 34


def test_cvv(personal):
    result = personal.cvv()
    assert 100 <= result
    assert result <= 999


def test_credit_card_number(personal):
    result = personal.credit_card_number()
    assert re.match(p.CREDIT_CARD_REGEX, result)

    result_mc = personal.credit_card_number(card_type='master_card')
    assert re.match(p.CREDIT_CARD_REGEX, result_mc)

    result_ax = personal.credit_card_number(card_type='amex')
    assert re.match(p.CREDIT_CARD_REGEX, result_ax)

    with pytest.raises(NotImplementedError):
        personal.credit_card_number(card_type='discover')


def test_expiration_date(personal):
    result = personal.credit_card_expiration_date(
        minimum=16, maximum=25)

    year = result.split('/')[1]
    assert int(year) >= 16
    assert int(year) <= 25


def test_cid(personal):
    result = personal.cid()
    assert 1000 <= result
    assert result <= 9999


def test_height(personal):
    result = personal.height(minimum=1.60, maximum=1.90)
    assert result.startswith('1')
    assert isinstance(result, str)


def test_weight(personal):
    result = personal.weight(minimum=40, maximum=60)
    assert result >= 40
    assert result <= 60


def test_blood_type(personal):
    result = personal.blood_type()
    assert result in BLOOD_GROUPS


def test_favorite_movie(personal):
    result = personal.favorite_movie()
    assert result in personal.data['favorite_movie']


def test_favorite_music_genre(personal):
    result = personal.favorite_music_genre()
    assert result in FAVORITE_MUSIC_GENRE


def test_social_media_profile(personal):
    result = personal.social_media_profile(gender='female')
    assert result is not None

    _result = personal.social_media_profile(gender='male')
    assert _result is not None


def test_avatar(personal):
    result = personal.avatar(size=512)
    img, size, *__ = result.split('/')[::-1]
    assert int(size) == 512
    assert 32 == len(img.split('.')[0])


def test_identifier(personal):
    result = personal.identifier()
    mask = '##-##/##'
    assert len(mask) == len(result)

    result = personal.identifier(mask='##-##/## @@')
    suffix = result.split(' ')[1]
    assert suffix.isalpha()


def test_level_of_english(personal):
    result = personal.level_of_english()
    assert result in ENGLISH_LEVEL


def test_name(generic):
    result = generic.personal.name(gender='female')
    assert result in generic.personal.data['names']['female']

    result = generic.personal.name(gender='male')
    assert result in generic.personal.data['names']['male']

    with pytest.raises(WrongArgument):
        generic.personal.name(gender='other')


def test_telephone(generic):
    result = generic.personal.telephone()
    assert result is not None

    mask = '+5 (###)-###-##-##'
    result2 = generic.personal.telephone(mask=mask)
    head = result2.split(' ')[0]
    assert head == '+5'


def test_surname(generic):
    diff_surnames = ('ru', 'is', 'uk', 'kk')
    if generic.personal.locale in diff_surnames:

        result = generic.personal.surname(gender='female')
        assert result in generic.personal.data['surnames']['female']

        result = generic.personal.surname(gender='male')
        assert result in generic.personal.data['surnames']['male']

        with pytest.raises(WrongArgument):
            generic.personal.surname(gender='other')
    else:
        result = generic.personal.surname()
        assert result in generic.personal.data['surnames']


def test_full_name(generic):
    result = generic.personal.full_name(gender='female')
    _result = result.split(' ')
    assert isinstance(_result, list)
    assert _result is not None

    result = generic.personal.full_name(reverse=True)
    assert result is not None


def test_gender(generic):
    result = generic.personal.gender()
    assert result in generic.personal.data['gender']

    symbol = generic.personal.gender(symbol=True)
    assert symbol in GENDER_SYMBOLS

    # The four codes specified in ISO/IEC 5218 are:
    # 0 = not known, 1 = male, 2 = female, 9 = not applicable.
    codes = [0, 1, 2, 9]
    iso5218 = generic.personal.gender(iso5218=True)
    assert iso5218 in codes


def test_sexual_orientation(generic):
    result = generic.personal.sexual_orientation()
    assert result in generic.personal.data['sexuality']

    symbol = generic.personal.sexual_orientation(symbol=True)
    assert symbol in SEXUALITY_SYMBOLS


def test_profession(generic):
    result = generic.personal.occupation()
    assert result in generic.personal.data['occupation']


def test_university(generic):
    result = generic.personal.university()
    assert result in generic.personal.data['university']


def test_academic_degree(generic):
    result = generic.personal.academic_degree()
    assert result in generic.personal.data['academic_degree']


def test_language(generic):
    result = generic.personal.language()
    assert result in generic.personal.data['language']


def test_worldview(generic):
    result = generic.personal.worldview()
    assert result in generic.personal.data['worldview']


def test_views_on(generic):
    result = generic.personal.views_on()
    assert result in generic.personal.data['views_on']


def test_political_views(generic):
    result = generic.personal.political_views()
    assert result in generic.personal.data['political_views']


def test_title(generic):
    result = generic.personal.title(title_type='typical')
    assert isinstance(result, str)

    result2 = generic.personal.title(title_type='academic')
    assert isinstance(result2, str)

    result_fem = generic.personal.title(gender='female')
    assert result_fem is not None

    result_fem = generic.personal.title(gender='male')
    assert result_fem is not None

    with pytest.raises(WrongArgument):
        generic.personal.title(gender='other', title_type='religious')


def test_nationality(generic):
    if generic.personal.locale in ['ru', 'uk', 'kk']:
        result = generic.personal.nationality(gender='female')
        assert result in generic.personal.data['nationality']['female']

        result = generic.personal.nationality(gender='male')
        assert result in generic.personal.data['nationality']['male']

    result = generic.personal.nationality()
    assert result is not None
