# -*- coding: utf-8 -*-

import re

import pytest

import mimesis
from mimesis import config
from mimesis.data import (
    BLOOD_GROUPS,
    ENGLISH_LEVEL,
    FAVORITE_MUSIC_GENRE,
    GENDER_SYMBOLS,
    SEXUALITY_SYMBOLS,
)
from mimesis.enums import Gender, TitleType
from mimesis.exceptions import (
    UnexpectedGender,
    UnsupportedAlgorithm,
    WrongArgument,
)
from mimesis.utils import check_gender

from ._patterns import (
    USERNAME_REGEX,
    STR_REGEX,
    CREDIT_CARD_REGEX,
    EMAIL_REGEX,
)


@pytest.fixture
def _personal():
    return mimesis.Personal()


def test_str(personal):
    assert re.match(STR_REGEX, str(personal))


def test_age(_personal):
    result = _personal.age(maximum=55)
    assert result <= 55


def test_age_store(_personal):
    result = _personal._store['age']
    assert result == 0


def test_age_update(_personal):
    result = _personal.age() - _personal._store['age']
    assert result == 0


def test_child_count(_personal):
    result = _personal.child_count(max_childs=10)
    assert result <= 10


def test_work_experience(_personal):
    result = _personal.work_experience(
        working_start_age=0) - _personal._store['age']
    assert result == 0


def test_work_experience_store(_personal):
    result = _personal.work_experience() - _personal.work_experience()
    assert result == 0


def test_work_experience_extreme(_personal):
    result = _personal.work_experience(working_start_age=100000)
    assert result == 0


def test_paypal(_personal):
    result = _personal.paypal()
    assert result is not None


@pytest.mark.parametrize(
    'algorithm, length', [
        ('md5', 32),
        ('sha1', 40),
        ('sha256', 64),
        ('sha512', 128),
    ],
)
def test_password(_personal, algorithm, length):
    result = _personal.password(length=15)
    assert len(result) == 15

    result = _personal.password(algorithm=algorithm)
    assert len(result) == length

    with pytest.raises(UnsupportedAlgorithm):
        _personal.password(algorithm='sha42')


@pytest.mark.parametrize(
    'template', [
        'U-d', 'U.d',
        'U_d', 'Ud',
        'l-d', 'l.d',
        'l_d', 'ld',

        # Default is ld
        'default',
    ],
)
def test_username(_personal, template):
    result = _personal.username(template=template)
    assert re.match(USERNAME_REGEX, result)

    with pytest.raises(WrongArgument):
        _personal.username(template=':D')


def test_email(_personal):
    result = _personal.email()
    assert re.match(EMAIL_REGEX, result)

    domains = ['@example.com']
    result = _personal.email(domains=domains)
    assert re.match(EMAIL_REGEX, result)
    assert result.split('@')[1] == 'example.com'


def test_bitcoin(_personal):
    result = _personal.bitcoin()
    assert len(result) == 34


def test_cvv(_personal):
    result = _personal.cvv()
    assert 100 <= result
    assert result <= 999


@pytest.mark.parametrize(
    'card_type', [
        # Visa
        'visa', 'vi', 'v',

        # MasterCard
        'master_card', 'master', 'mc', 'm',

        # American Express
        'american_express', 'amex', 'ax', 'a',
    ],
)
def test_credit_card_number(_personal, card_type):
    result = _personal.credit_card_number(card_type=card_type)
    assert re.match(CREDIT_CARD_REGEX, result)

    with pytest.raises(NotImplementedError):
        _personal.credit_card_number(card_type='discover')


def test_expiration_date(_personal):
    result = _personal.credit_card_expiration_date(
        minimum=16, maximum=25)

    year = result.split('/')[1]
    assert int(year) >= 16
    assert int(year) <= 25


def test_cid(_personal):
    result = _personal.cid()
    assert 1000 <= result
    assert result <= 9999


def test_height(_personal):
    result = _personal.height(minimum=1.60, maximum=1.90)
    assert result.startswith('1')
    assert isinstance(result, str)


def test_weight(_personal):
    result = _personal.weight(minimum=40, maximum=60)
    assert result >= 40
    assert result <= 60


def test_blood_type(_personal):
    result = _personal.blood_type()
    assert result in BLOOD_GROUPS


def test_favorite_movie(personal):
    result = personal.favorite_movie()
    assert result in personal.data['favorite_movie']


def test_favorite_music_genre(_personal):
    result = _personal.favorite_music_genre()
    assert result in FAVORITE_MUSIC_GENRE


def test_social_media_profile(_personal):
    result = _personal.social_media_profile()
    assert result is not None


def test_avatar(_personal):
    result = _personal.avatar(size=512)
    img, size, *__ = result.split('/')[::-1]
    assert int(size) == 512
    assert 32 == len(img.split('.')[0])


def test_identifier(_personal):
    result = _personal.identifier()
    mask = '##-##/##'
    assert len(mask) == len(result)

    result = _personal.identifier(mask='##-##/## @@')
    suffix = result.split(' ')[1]
    assert suffix.isalpha()


def test_level_of_english(_personal):
    result = _personal.level_of_english()
    assert result in ENGLISH_LEVEL


@pytest.mark.parametrize(
    'gender', [
        Gender.FEMALE,
        Gender.MALE,
        Gender.RANDOM,
    ],
)
def test_name(personal, gender):
    result = personal.name(gender=gender)
    checked = check_gender(gender)
    assert result in personal.data['names'][checked.value]


def test_name_unexpected_gender(personal):
    with pytest.raises(UnexpectedGender):
        personal.name(gender=None)


def test_telephone(personal):
    result = personal.telephone()
    assert result is not None

    mask = '+5 (###)-###-##-##'
    result = personal.telephone(mask=mask)
    head = result.split(' ')[0]
    assert head == '+5'


@pytest.mark.parametrize(
    'gender', [
        Gender.FEMALE,
        Gender.MALE,
        Gender.RANDOM,
    ],
)
def test_surname(personal, gender):
    if personal.locale in config.SURNAMES_SEPARATED_BY_GENDER:

        result = personal.surname(gender=gender)
        checked = check_gender(gender)
        assert result in personal.data['surnames'][checked.value]
    else:
        result = personal.surname()
        assert result in personal.data['surnames']


@pytest.mark.parametrize(
    'gender', [
        Gender.FEMALE,
        Gender.MALE,
        Gender.RANDOM,
    ],
)
def test_full_name(personal, gender):
    result = personal.full_name(gender=gender)

    result = result.split(' ')
    assert result[0] is not None
    assert result[1] is not None

    result = personal.full_name(reverse=True)
    assert result is not None


def test_gender(personal):
    result = personal.gender()
    assert result in personal.data['gender']

    result = personal.gender(symbol=True)
    assert result in GENDER_SYMBOLS

    # The four codes specified in ISO/IEC 5218 are:
    # 0 = not known, 1 = male, 2 = female, 9 = not applicable.
    codes = [0, 1, 2, 9]
    iso5218 = personal.gender(iso5218=True)
    assert iso5218 in codes


def test_sexual_orientation(personal):
    result = personal.sexual_orientation()
    assert result in personal.data['sexuality']

    symbol = personal.sexual_orientation(symbol=True)
    assert symbol in SEXUALITY_SYMBOLS


def test_profession(personal):
    result = personal.occupation()
    assert result in personal.data['occupation']


def test_university(personal):
    result = personal.university()
    assert result in personal.data['university']


def test_academic_degree(personal):
    result = personal.academic_degree()
    assert result in personal.data['academic_degree']


def test_language(personal):
    result = personal.language()
    assert result in personal.data['language']


def test_worldview(personal):
    result = personal.worldview()
    assert result in personal.data['worldview']


def test_views_on(personal):
    result = personal.views_on()
    assert result in personal.data['views_on']


def test_political_views(personal):
    result = personal.political_views()
    assert result in personal.data['political_views']


@pytest.mark.parametrize(
    'title_type', [
        TitleType.ACADEMIC,
        TitleType.TYPICAL,
        TitleType.RANDOM,
    ],
)
@pytest.mark.parametrize(
    'gender', [
        Gender.FEMALE,
        Gender.MALE,
        Gender.RANDOM,
    ],
)
def test_title(personal, gender, title_type):
    result = personal.title(gender=gender, title_type=title_type)
    assert result is not None

    with pytest.raises(ValueError):
        personal.title(title_type=None)
        personal.title(gender=None)


@pytest.mark.parametrize(
    'gender', [
        Gender.FEMALE,
        Gender.MALE,
        Gender.RANDOM,
    ],
)
def test_nationality(personal, gender):
    if personal.locale in ['ru', 'uk', 'kk']:
        result = personal.nationality(gender=gender)
        checked = check_gender(gender)
        assert result in personal.data['nationality'][checked.value]

    result = personal.nationality()
    assert result is not None
