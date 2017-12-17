# -*- coding: utf-8 -*-

import re

import pytest

from mimesis import Personal, config
from mimesis.data import (BLOOD_GROUPS, ENGLISH_LEVEL, GENDER_SYMBOLS,
                          MUSIC_GENRE, SEXUALITY_SYMBOLS)
from mimesis.enums import Gender, SocialNetwork, TitleType
from mimesis.exceptions import NonEnumerableError

from ._patterns import EMAIL_REGEX, STR_REGEX, USERNAME_REGEX


@pytest.fixture
def _personal():
    return Personal()


@pytest.fixture
def _seeded_personal():
    return Personal(seed=42)


def test_str(personal):
    assert re.match(STR_REGEX, str(personal))


def test_age(_personal):
    result = _personal.age(maximum=55)
    assert result <= 55


def test_seeded_age(_seeded_personal):
    result = _seeded_personal.age(maximum=42)
    assert result == 36
    result = _seeded_personal.age()
    assert result == 23
    result = _seeded_personal.age()
    assert result == 17


def test_age_store(_personal):
    result = _personal._store['age']
    assert result == 0


def test_age_update(_personal):
    result = _personal.age() - _personal._store['age']
    assert result == 0


def test_child_count(_personal):
    result = _personal.child_count(max_childs=10)
    assert result <= 10


def test_seeded_child_count(_seeded_personal):
    result = _seeded_personal.child_count(max_childs=100)
    assert result == 14
    result = _seeded_personal.child_count()
    assert result == 0
    result = _seeded_personal.child_count()
    assert result == 5


def test_work_experience(_personal):
    result = _personal.work_experience(
        working_start_age=0) - _personal._store['age']
    assert result == 0


def test_seeded_work_experience(_seeded_personal):
    result = _seeded_personal.work_experience(working_start_age=11)
    assert result == 45
    result = _seeded_personal.work_experience()
    assert result == 34
    age = _seeded_personal.age()
    result = _seeded_personal.work_experience()
    assert result == 1
    age = _seeded_personal.age()
    result = _seeded_personal.work_experience()
    assert result == 0


def test_work_experience_store(_personal):
    result = _personal.work_experience() - _personal.work_experience()
    assert result == 0


def test_work_experience_extreme(_personal):
    result = _personal.work_experience(working_start_age=100000)
    assert result == 0


def test_password(_personal):
    result = _personal.password(length=15)
    assert len(result) == 15

    result = _personal.password(hashed=True)
    assert len(result) == 32


def test_seeded_password(_seeded_personal):
    result = _seeded_personal.password(length=15)
    assert result == '>odJFCrn](l.2ed'
    result = _seeded_personal.password()
    assert result == 'lBD#:d*z'
    result = _seeded_personal.password()
    assert result == '|@`(1C5.'


@pytest.mark.parametrize(
    'template', [
        'U-d', 'U.d',
        'U_d', 'Ud',
        'l-d', 'l.d',
        'l_d', 'ld',

        # Default is ld
        'default',
        None,
    ],
)
def test_username(_personal, template):
    result = _personal.username(template=template)
    assert re.match(USERNAME_REGEX, result)


def test_seeded_username(_seeded_personal):
    result = _seeded_personal.username(template='l.d')
    assert result == 'imagining.1857'
    result = _seeded_personal.username()
    assert result == 'Afterfuture1940'
    result = _seeded_personal.username()
    assert result == 'Boons.1871'


def test_username_unsupported_template(_personal):
    with pytest.raises(KeyError):
        _personal.username(template=':D')


def test_email(_personal):
    result = _personal.email()
    assert re.match(EMAIL_REGEX, result)

    domains = ['@example.com']
    result = _personal.email(domains=domains)
    assert re.match(EMAIL_REGEX, result)
    assert result.split('@')[1] == 'example.com'


def test_seeded_email(_seeded_personal):
    result = _seeded_personal.email()
    assert result == 'afterfuture1940@gmail.com'
    result = _seeded_personal.email()
    assert result == 'boons1871@yandex.com'


def test_height(_personal):
    result = _personal.height(minimum=1.60, maximum=1.90)
    assert result.startswith('1')
    assert isinstance(result, str)


def test_seeded_height(_seeded_personal):
    result = _seeded_personal.height(minimum=1.60, maximum=1.90)
    assert result == '1.79'
    result = _seeded_personal.height()
    assert result == '1.51'
    result = _seeded_personal.height()
    assert result == '1.64'


def test_weight(_personal):
    result = _personal.weight(minimum=40, maximum=60)
    assert result >= 40
    assert result <= 60


def test_seeded_weight(_seeded_personal):
    result = _seeded_personal.weight(minimum=40, maximum=60)
    assert result == 60
    result = _seeded_personal.weight()
    assert result == 45
    result = _seeded_personal.weight()
    assert result == 39


def test_blood_type(_personal):
    result = _personal.blood_type()
    assert result in BLOOD_GROUPS


def test_seeded_blood_type(_seeded_personal):
    result = _seeded_personal.blood_type()
    assert result == 'A+'
    result = _seeded_personal.blood_type()
    assert result == 'O+'


def test_favorite_movie(personal):
    result = personal.favorite_movie()
    assert result in personal._data['favorite_movie']


def test_seeded_favorite_movie(_seeded_personal):
    result = _seeded_personal.favorite_movie()
    assert result == 'Creature'
    result = _seeded_personal.favorite_movie()
    assert result == 'Air Bud'


def test_favorite_music_genre(_personal):
    result = _personal.favorite_music_genre()
    assert result in MUSIC_GENRE


def test_seeded_favorite_music_genre(_seeded_personal):
    result = _seeded_personal.favorite_music_genre()
    assert result == 'Ambient house'
    result = _seeded_personal.favorite_music_genre()
    assert result == 'Rhythm & Blues (R&B)'


@pytest.mark.parametrize(
    'site', [
        SocialNetwork.INSTAGRAM,
        SocialNetwork.FACEBOOK,
        SocialNetwork.TWITTER,
        SocialNetwork.VK,
        None,
    ],
)
def test_social_media_profile(_personal, site):
    result = _personal.social_media_profile(site=site)
    assert result is not None


def test_seeded_social_media_profile(_seeded_personal):
    result = _seeded_personal.social_media_profile(site=SocialNetwork.TWITTER)
    assert result == 'https://www.twitter.com/Imagining-1857'
    result = _seeded_personal.social_media_profile()
    assert result == 'https://www.instagram.com/Briolette_1914'
    result = _seeded_personal.social_media_profile()
    assert result == 'https://www.facebook.com/mitten.1844'


def test_avatar(_personal):
    result = _personal.avatar(size=512)
    img, size, *__ = result.split('/')[::-1]
    assert int(size) == 512
    assert 32 == len(img.split('.')[0])


def test_seeded_avatar(_seeded_personal):
    result = _seeded_personal.avatar(size=128)
    assert result.endswith('c5d90f155b758732c7da3f614e9783ce.png')
    result = _seeded_personal.avatar()
    assert result.endswith('a66ff795b40c9d5cffcaa98374f03d4d.png')
    result = _seeded_personal.avatar()
    assert result.endswith('9290813a752fd4550f710567e564b474.png')


def test_identifier(_personal):
    result = _personal.identifier()
    mask = '##-##/##'
    assert len(mask) == len(result)

    result = _personal.identifier(mask='##-##/## @@')
    suffix = result.split(' ')[1]
    assert suffix.isalpha()


def test_seeded_identifier(_seeded_personal):
    result = _seeded_personal.identifier(mask='##-##/## @@')
    assert result == '10-43/32 XD'
    result = _seeded_personal.identifier()
    assert result == '81-96/00'
    result = _seeded_personal.identifier()
    assert result == '13-38/90'


def test_level_of_english(_personal):
    result = _personal.level_of_english()
    assert result in ENGLISH_LEVEL


def test_seeded_level_of_english(_seeded_personal):
    result = _seeded_personal.level_of_english()
    assert result == 'Advanced'
    result = _seeded_personal.level_of_english()
    assert result == 'Beginner'


@pytest.mark.parametrize(
    'gender', [
        Gender.FEMALE,
        Gender.MALE,
    ],
)
def test_name(personal, gender):
    result = personal.name(gender=gender)
    assert result in personal._data['names'][gender.value]


def test_seeded_name(_seeded_personal):
    result = _seeded_personal.name(gender=Gender.FEMALE)
    assert result == 'Darlena'
    result = _seeded_personal.name()
    assert result == 'Krystin'
    result = _seeded_personal.name()
    assert result == 'Jenee'


def test_name_with_none(_personal):
    result = _personal.name(gender=None)
    names = _personal._data['names']

    females = names['female']
    males = names['male']
    assert result is not None
    assert (result in females) or (result in males)


def test_name_unexpected_gender(personal):
    with pytest.raises(NonEnumerableError):
        personal.name(gender='nil')


def test_telephone(personal):
    result = personal.telephone()
    assert result is not None

    mask = '+5 (###)-###-##-##'
    result = personal.telephone(mask=mask)
    head = result.split(' ')[0]
    assert head == '+5'


def test_seeded_telephone(_seeded_personal):
    result = _seeded_personal.telephone(mask='+5 (###)-###-##-##')
    assert result == '+5 (104)-332-18-19'
    result = _seeded_personal.telephone()
    assert result == '013-389-0838'
    result = _seeded_personal.telephone()
    assert result == '794.026.5423'


@pytest.mark.parametrize(
    'gender', [
        Gender.FEMALE,
        Gender.MALE,
    ],
)
def test_surname(personal, gender):
    surnames = personal._data['surnames']

    # Surnames separated by gender.
    if isinstance(surnames, dict):
        result = personal.surname(gender=gender)
        assert result in surnames[gender.value]
    else:
        result = personal.surname()
        assert result in surnames


def test_seeded_surname(_seeded_personal):
    result = _seeded_personal.surname(gender=Gender.FEMALE)
    assert result == 'Mullins'
    result = _seeded_personal.surname()
    assert result == 'Buckner'
    result = _seeded_personal.surname()
    assert result == 'Avila'


@pytest.mark.parametrize(
    'gender', [
        Gender.FEMALE,
        Gender.MALE,
    ],
)
def test_full_name(personal, gender):
    result = personal.full_name(gender=gender)

    result = result.split(' ')
    assert result[0] is not None
    assert result[1] is not None

    result = personal.full_name(reverse=True)
    assert result is not None


def test_seeded_full_name(_seeded_personal):
    result = _seeded_personal.full_name(gender=Gender.MALE, reverse=True)
    assert result == 'Avila Cornelius'
    result = _seeded_personal.full_name()
    assert result == 'Hank Day'
    result = _seeded_personal.full_name()
    assert result == 'Crystle Osborn'


def test_gender(personal):
    result = personal.gender()
    assert result in personal._data['gender']

    result = personal.gender(symbol=True)
    assert result in GENDER_SYMBOLS

    # The four codes specified in ISO/IEC 5218 are:
    # 0 = not known, 1 = male, 2 = female, 9 = not applicable.
    codes = [0, 1, 2, 9]
    iso5218 = personal.gender(iso5218=True)
    assert iso5218 in codes


def test_seeded_gender(_seeded_personal):
    result = _seeded_personal.gender(iso5218=True, symbol=True)
    assert result == 0
    result = _seeded_personal.gender()
    assert result == 'Male'
    result = _seeded_personal.gender()
    assert result == 'Fluid'


def test_sexual_orientation(personal):
    result = personal.sexual_orientation()
    assert result in personal._data['sexuality']

    symbol = personal.sexual_orientation(symbol=True)
    assert symbol in SEXUALITY_SYMBOLS


def test_seeded_sexual_orientation(_seeded_personal):
    result = _seeded_personal.sexual_orientation(symbol=True)
    assert result == '⚪'
    result = _seeded_personal.sexual_orientation()
    assert result == 'Asexual'
    result = _seeded_personal.sexual_orientation()
    assert result == 'Asexual'
    result = _seeded_personal.sexual_orientation()
    assert result == 'Heterosexual'


def test_occupation(personal):
    result = personal.occupation()
    assert result in personal._data['occupation']


def test_seeded_occupation(_seeded_personal):
    result = _seeded_personal.occupation()
    assert result == 'Coroner'
    result = _seeded_personal.occupation()
    assert result == 'Architect'


def test_university(personal):
    result = personal.university()
    assert result in personal._data['university']


def test_seeded_university(_seeded_personal):
    result = _seeded_personal.university()
    assert result == 'University of South Florida (USF)'
    result = _seeded_personal.university()
    assert result == 'California State University, Chico (Chico State)'


def test_academic_degree(personal):
    result = personal.academic_degree()
    assert result in personal._data['academic_degree']


def test_seeded_academic_degree(_seeded_personal):
    result = _seeded_personal.academic_degree()
    assert result == 'PhD'
    result = _seeded_personal.academic_degree()
    assert result == 'Bachelor'


def test_language(personal):
    result = personal.language()
    assert result in personal._data['language']


def test_seeded_language(_seeded_personal):
    result = _seeded_personal.language()
    assert result == 'Sotho'
    result = _seeded_personal.language()
    assert result == 'Catalan'


def test_worldview(personal):
    result = personal.worldview()
    assert result in personal._data['worldview']


def test_seeded_worldview(_seeded_personal):
    result = _seeded_personal.worldview()
    assert result == 'Agnosticism'
    result = _seeded_personal.worldview()
    assert result == 'Atheism'


def test_views_on(personal):
    result = personal.views_on()
    assert result in personal._data['views_on']


def test_seeded_views_on(_seeded_personal):
    result = _seeded_personal.views_on()
    assert result == 'Negative'
    result = _seeded_personal.views_on()
    assert result == 'Negative'
    result = _seeded_personal.views_on()
    assert result == 'Positive'


def test_political_views(personal):
    result = personal.political_views()
    assert result in personal._data['political_views']


def test_seeded_political_views(_seeded_personal):
    result = _seeded_personal.political_views()
    assert result == 'Anarchism'
    result = _seeded_personal.political_views()
    assert result == 'Apathetic'


@pytest.mark.parametrize(
    'title_type', [
        TitleType.ACADEMIC,
        TitleType.TYPICAL,
        None,
    ],
)
@pytest.mark.parametrize(
    'gender', [
        Gender.FEMALE,
        Gender.MALE,
        None,
    ],
)
def test_title(personal, gender, title_type):
    result = personal.title(gender=gender, title_type=title_type)
    assert result is not None

    with pytest.raises(NonEnumerableError):
        personal.title(title_type='nil')
        personal.title(gender='nil')


def test_seeded_title(_seeded_personal):
    result = _seeded_personal.title(
        gender=Gender.FEMALE, title_type=TitleType.ACADEMIC,
    )
    assert result == 'PhD'
    result = _seeded_personal.title()
    assert result == 'B.A.'
    result = _seeded_personal.title()
    assert result == 'Mrs.'


@pytest.mark.parametrize(
    'gender', [
        Gender.FEMALE,
        Gender.MALE,
    ],
)
def test_nationality(personal, gender):
    nationality = personal._data['nationality']
    if isinstance(nationality, dict):
        result = personal.nationality(gender=gender)
        assert result in personal._data['nationality'][gender.value]

    result = personal.nationality()
    assert result is not None


def test_seeded_nationality(_seeded_personal):
    result = _seeded_personal.nationality(gender=Gender.FEMALE)
    assert result == 'Russian'
    result = _seeded_personal.nationality()
    assert result == 'Cameroonian'
    result = _seeded_personal.nationality()
    assert result == 'Argentinian'


@pytest.mark.parametrize(
    'gender', [
        Gender.FEMALE,
        Gender.MALE,
    ],
)
def test_last_name(personal, gender):
    if personal.locale in config.SURNAMES_SEPARATED_BY_GENDER:
        result = personal.last_name(gender=gender)
        assert result in personal.data['surnames'][gender.value]
    else:
        result = personal.last_name()
        assert result in personal.data['surnames']


def test_seeded_last_name(_seeded_personal):
    result = _seeded_personal.last_name(gender=Gender.FEMALE)
    assert result == 'Mullins'
    result = _seeded_personal.last_name()
    assert result == 'Buckner'
    result = _seeded_personal.last_name()
    assert result == 'Avila'
