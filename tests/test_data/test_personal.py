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
    # assert result ==
    result = _seeded_personal.child_count()
    # assert result ==
    result = _seeded_personal.child_count()
    # assert result ==
    pass


def test_work_experience(_personal):
    result = _personal.work_experience(
        working_start_age=0) - _personal._store['age']
    assert result == 0


def test_seeded_work_experience(_seeded_personal):
    result = _seeded_personal.work_experience(working_start_age=11)
    # assert result ==
    result = _seeded_personal.work_experience()
    # assert result ==
    result = _seeded_personal.work_experience()
    # assert result ==
    pass


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
    # assert result ==
    result = _seeded_personal.password()
    # assert result ==
    result = _seeded_personal.password()
    # assert result ==
    pass


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
    # assert result ==
    result = _seeded_personal.username()
    # assert result ==
    result = _seeded_personal.username()
    # assert result ==
    pass


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
    # assert result ==
    result = _seeded_personal.email()
    # assert result ==
    pass


def test_height(_personal):
    result = _personal.height(minimum=1.60, maximum=1.90)
    assert result.startswith('1')
    assert isinstance(result, str)


def test_seeded_height(_seeded_personal):
    result = _seeded_personal.height(minimum=1.60, maximum=1.90)
    # assert result ==
    result = _seeded_personal.height()
    # assert result ==
    result = _seeded_personal.height()
    # assert result ==
    pass


def test_weight(_personal):
    result = _personal.weight(minimum=40, maximum=60)
    assert result >= 40
    assert result <= 60


def test_seeded_weight(_seeded_personal):
    result = _seeded_personal.weight(minimum=40, maximum=60)
    # assert result ==
    result = _seeded_personal.weight()
    # assert result ==
    result = _seeded_personal.weight()
    # assert result ==
    pass


def test_blood_type(_personal):
    result = _personal.blood_type()
    assert result in BLOOD_GROUPS


def test_seeded_blood_type(_seeded_personal):
    result = _seeded_personal.blood_type()
    # assert result ==
    result = _seeded_personal.blood_type()
    # assert result ==
    pass


def test_favorite_movie(personal):
    result = personal.favorite_movie()
    assert result in personal.data['favorite_movie']


def test_seeded_favorite_movie(_seeded_personal):
    result = _seeded_personal.favorite_movie()
    # assert result ==
    result = _seeded_personal.favorite_movie()
    # assert result ==
    pass


def test_favorite_music_genre(_personal):
    result = _personal.favorite_music_genre()
    assert result in MUSIC_GENRE


def test_seeded_favorite_music_genre(_seeded_personal):
    result = _seeded_personal.favorite_music_genre()
    # assert result ==
    result = _seeded_personal.favorite_music_genre()
    # assert result ==
    pass


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
    # assert result ==
    result = _seeded_personal.social_media_profile()
    # assert result ==
    result = _seeded_personal.social_media_profile()
    # assert result ==
    pass


def test_avatar(_personal):
    result = _personal.avatar(size=512)
    img, size, *__ = result.split('/')[::-1]
    assert int(size) == 512
    assert 32 == len(img.split('.')[0])


def test_seeded_avatar(_seeded_personal):
    result = _seeded_personal.avatar(size=128)
    # assert result ==
    result = _seeded_personal.avatar()
    # assert result ==
    result = _seeded_personal.avatar()
    # assert result ==
    pass


def test_identifier(_personal):
    result = _personal.identifier()
    mask = '##-##/##'
    assert len(mask) == len(result)

    result = _personal.identifier(mask='##-##/## @@')
    suffix = result.split(' ')[1]
    assert suffix.isalpha()


def test_seeded_identifier(_seeded_personal):
    result = _seeded_personal.identifier(mask='##-##/## @@')
    # assert result ==
    result = _seeded_personal.identifier()
    # assert result ==
    result = _seeded_personal.identifier()
    # assert result ==
    pass


def test_level_of_english(_personal):
    result = _personal.level_of_english()
    assert result in ENGLISH_LEVEL


def test_seeded_level_of_english(_seeded_personal):
    result = _seeded_personal.level_of_english()
    # assert result ==
    result = _seeded_personal.level_of_english()
    # assert result ==
    pass


@pytest.mark.parametrize(
    'gender', [
        Gender.FEMALE,
        Gender.MALE,
    ],
)
def test_name(personal, gender):
    result = personal.name(gender=gender)
    assert result in personal.data['names'][gender.value]


def test_seeded_name(_seeded_personal):
    result = _seeded_personal.name(gender=Gender.FEMALE)
    # assert result ==
    result = _seeded_personal.name()
    # assert result ==
    result = _seeded_personal.name()
    # assert result ==
    pass


def test_name_with_none(_personal):
    result = _personal.name(gender=None)
    names = _personal.data['names']

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
    # assert result ==
    result = _seeded_personal.telephone()
    # assert result ==
    result = _seeded_personal.telephone()
    # assert result ==
    pass


@pytest.mark.parametrize(
    'gender', [
        Gender.FEMALE,
        Gender.MALE,
    ],
)
def test_surname(personal, gender):
    if personal.locale in config.SURNAMES_SEPARATED_BY_GENDER:

        result = personal.surname(gender=gender)
        assert result in personal.data['surnames'][gender.value]
    else:
        result = personal.surname()
        assert result in personal.data['surnames']


def test_seeded_surname(_seeded_personal):
    result = _seeded_personal.surname(gender=Gender.FEMALE)
    # assert result ==
    result = _seeded_personal.surname()
    # assert result ==
    result = _seeded_personal.surname()
    # assert result ==
    pass


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
    # assert result ==
    result = _seeded_personal.full_name()
    # assert result ==
    result = _seeded_personal.full_name()
    # assert result ==
    pass


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


def test_seeded_gender(_seeded_personal):
    result = _seeded_personal.gender(iso5218=True, symbol=True)
    # assert result ==
    result = _seeded_personal.gender()
    # assert result ==
    result = _seeded_personal.gender()
    # assert result ==
    pass


def test_sexual_orientation(personal):
    result = personal.sexual_orientation()
    assert result in personal.data['sexuality']

    symbol = personal.sexual_orientation(symbol=True)
    assert symbol in SEXUALITY_SYMBOLS


def test_seeded_sexual_orientation(_seeded_personal):
    result = _seeded_personal.sexual_orientation(symbol=True)
    # assert result ==
    result = _seeded_personal.sexual_orientation()
    # assert result ==
    result = _seeded_personal.sexual_orientation()
    # assert result ==
    pass


def test_occupation(personal):
    result = personal.occupation()
    assert result in personal.data['occupation']


def test_seeded_occupation(_seeded_personal):
    result = _seeded_personal.occupation()
    # assert result ==
    result = _seeded_personal.occupation()
    # assert result ==
    pass


def test_university(personal):
    result = personal.university()
    assert result in personal.data['university']


def test_seeded_university(_seeded_personal):
    result = _seeded_personal.university()
    # assert result ==
    result = _seeded_personal.university()
    # assert result ==
    pass


def test_academic_degree(personal):
    result = personal.academic_degree()
    assert result in personal.data['academic_degree']


def test_seeded_academic_degree(_seeded_personal):
    result = _seeded_personal.academic_degree()
    # assert result ==
    result = _seeded_personal.academic_degree()
    # assert result ==
    pass


def test_language(personal):
    result = personal.language()
    assert result in personal.data['language']


def test_seeded_language(_seeded_personal):
    result = _seeded_personal.language()
    # assert result ==
    result = _seeded_personal.language()
    # assert result ==
    pass


def test_worldview(personal):
    result = personal.worldview()
    assert result in personal.data['worldview']


def test_seeded_worldview(_seeded_personal):
    result = _seeded_personal.worldview()
    # assert result ==
    result = _seeded_personal.worldview()
    # assert result ==
    pass


def test_views_on(personal):
    result = personal.views_on()
    assert result in personal.data['views_on']


def test_seeded_views_on(_seeded_personal):
    result = _seeded_personal.views_on()
    # assert result ==
    result = _seeded_personal.views_on()
    # assert result ==
    pass


def test_political_views(personal):
    result = personal.political_views()
    assert result in personal.data['political_views']


def test_seeded_political_views(_seeded_personal):
    result = _seeded_personal.political_views()
    # assert result ==
    result = _seeded_personal.political_views()
    # assert result ==
    pass


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
    # assert result ==
    result = _seeded_personal.title()
    # assert result ==
    result = _seeded_personal.title()
    # assert result ==
    pass


@pytest.mark.parametrize(
    'gender', [
        Gender.FEMALE,
        Gender.MALE,
    ],
)
def test_nationality(personal, gender):
    if personal.locale in ['ru', 'uk', 'kk']:
        result = personal.nationality(gender=gender)
        assert result in personal.data['nationality'][gender.value]

    result = personal.nationality()
    assert result is not None


def test_seeded_nationality(_seeded_personal):
    result = _seeded_personal.nationality(gender=Gender.FEMALE)
    # assert result ==
    result = _seeded_personal.nationality()
    # assert result ==
    result = _seeded_personal.nationality()
    # assert result ==
    pass


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
    # assert result ==
    result = _seeded_personal.last_name()
    # assert result ==
    result = _seeded_personal.last_name()
    # assert result ==
    pass
