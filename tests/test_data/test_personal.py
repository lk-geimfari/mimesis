# -*- coding: utf-8 -*-

import re

import pytest

from mimesis import Personal
from mimesis.data import (BLOOD_GROUPS, ENGLISH_LEVEL, GENDER_SYMBOLS,
                          MUSIC_GENRE, SEXUALITY_SYMBOLS)
from mimesis.enums import Gender, SocialNetwork, TitleType
from mimesis.exceptions import NonEnumerableError

from ._patterns import EMAIL_REGEX, STR_REGEX, USERNAME_REGEX


class TestPersonal(object):
    @pytest.fixture
    def _personal(self):
        return Personal()

    def test_str(self, personal):
        assert re.match(STR_REGEX, str(personal))

    @pytest.mark.parametrize(
        'minimum, maximum', [
            (16, 18),
            (18, 21),
            (22, 28),
        ],
    )
    def test_age(self, _personal, minimum, maximum):
        result = _personal.age(minimum, maximum)
        assert (result >= minimum) and (result <= maximum)

    def test_age_store(self, _personal):
        result = _personal._store['age']
        assert result == 0

    def test_age_update(self, _personal):
        result = _personal.age() - _personal._store['age']
        assert result == 0

    def test_child_count(self, _personal):
        result = _personal.child_count(max_childs=10)
        assert result <= 10

    def test_work_experience(self, _personal):
        result = _personal.work_experience(
            working_start_age=0) - _personal._store['age']
        assert result == 0

    def test_work_experience_store(self, _personal):
        result = _personal.work_experience() - _personal.work_experience()
        assert result == 0

    def test_work_experience_extreme(self, _personal):
        result = _personal.work_experience(working_start_age=100000)
        assert result == 0

    def test_password(self, _personal):
        result = _personal.password(length=15)
        assert len(result) == 15

        result = _personal.password(hashed=True)
        assert len(result) == 32

    @pytest.mark.parametrize(
        'template', [
            'U-d', 'U.d', 'UU-d',
            'UU.d', 'UU_d', 'U_d',
            'Ud', 'default', 'l-d',
            'l.d', 'l_d', 'ld',
            None,
        ],
    )
    def test_username(self, _personal, template):
        result = _personal.username(template=template)
        assert re.match(USERNAME_REGEX, result)

    def test_username_unsupported_template(self, _personal):
        with pytest.raises(KeyError):
            _personal.username(template=':D')

    def test_email(self, _personal):
        result = _personal.email()
        assert re.match(EMAIL_REGEX, result)

        domains = ['@example.com']
        result = _personal.email(domains=domains)
        assert re.match(EMAIL_REGEX, result)
        assert result.split('@')[1] == 'example.com'

    def test_height(self, _personal):
        result = _personal.height(minimum=1.60, maximum=1.90)
        assert result.startswith('1')
        assert isinstance(result, str)

    def test_weight(self, _personal):
        result = _personal.weight(minimum=40, maximum=60)
        assert result >= 40
        assert result <= 60

    def test_blood_type(self, _personal):
        result = _personal.blood_type()
        assert result in BLOOD_GROUPS

    def test_favorite_movie(self, personal):
        result = personal.favorite_movie()
        assert result in personal._data['favorite_movie']

    def test_favorite_music_genre(self, _personal):
        result = _personal.favorite_music_genre()
        assert result in MUSIC_GENRE

    @pytest.mark.parametrize(
        'site', [
            SocialNetwork.INSTAGRAM,
            SocialNetwork.FACEBOOK,
            SocialNetwork.TWITTER,
            SocialNetwork.VK,
            None,
        ],
    )
    def test_social_media_profile(self, _personal, site):
        result = _personal.social_media_profile(site=site)
        assert result is not None

    def test_avatar(self, _personal):
        result = _personal.avatar(size=512)
        img, size, *__ = result.split('/')[::-1]
        assert int(size) == 512
        assert 32 == len(img.split('.')[0])

    def test_identifier(self, _personal):
        result = _personal.identifier()
        mask = '##-##/##'
        assert len(mask) == len(result)

        result = _personal.identifier(mask='##-##/## @@')
        suffix = result.split(' ')[1]
        assert suffix.isalpha()

    def test_level_of_english(self, _personal):
        result = _personal.level_of_english()
        assert result in ENGLISH_LEVEL

    @pytest.mark.parametrize(
        'gender', [
            Gender.FEMALE,
            Gender.MALE,
        ],
    )
    def test_name(self, personal, gender):
        result = personal.name(gender=gender)
        assert result in personal._data['names'][gender.value]

    def test_name_with_none(self, _personal):
        result = _personal.name(gender=None)
        names = _personal._data['names']

        females = names['female']
        males = names['male']
        assert result is not None
        assert (result in females) or (result in males)

    def test_name_unexpected_gender(self, personal):
        with pytest.raises(NonEnumerableError):
            personal.name(gender='nil')

    def test_telephone(self, personal):
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
        ],
    )
    def test_surname(self, personal, gender):
        surnames = personal._data['surnames']

        # Surnames separated by gender.
        if isinstance(surnames, dict):
            result = personal.surname(gender=gender)
            assert result in surnames[gender.value]
        else:
            result = personal.surname()
            assert result in surnames

    @pytest.mark.parametrize(
        'gender', [
            Gender.FEMALE,
            Gender.MALE,
        ],
    )
    def test_full_name(self, personal, gender):
        result = personal.full_name(gender=gender)

        result = result.split(' ')
        assert result[0] is not None
        assert result[1] is not None

        result = personal.full_name(reverse=True)
        assert result is not None

    def test_gender(self, personal):
        result = personal.gender()
        assert result in personal._data['gender']

        result = personal.gender(symbol=True)
        assert result in GENDER_SYMBOLS

        # The four codes specified in ISO/IEC 5218 are:
        # 0 = not known, 1 = male, 2 = female, 9 = not applicable.
        codes = [0, 1, 2, 9]
        iso5218 = personal.gender(iso5218=True)
        assert iso5218 in codes

    def test_sexual_orientation(self, personal):
        result = personal.sexual_orientation()
        assert result in personal._data['sexuality']

        symbol = personal.sexual_orientation(symbol=True)
        assert symbol in SEXUALITY_SYMBOLS

    def test_profession(self, personal):
        result = personal.occupation()
        assert result in personal._data['occupation']

    def test_university(self, personal):
        result = personal.university()
        assert result in personal._data['university']

    def test_academic_degree(self, personal):
        result = personal.academic_degree()
        assert result in personal._data['academic_degree']

    def test_language(self, personal):
        result = personal.language()
        assert result in personal._data['language']

    def test_worldview(self, personal):
        result = personal.worldview()
        assert result in personal._data['worldview']

    def test_views_on(self, personal):
        result = personal.views_on()
        assert result in personal._data['views_on']

    def test_political_views(self, personal):
        result = personal.political_views()
        assert result in personal._data['political_views']

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
    def test_title(self, personal, gender, title_type):
        result = personal.title(gender=gender, title_type=title_type)
        assert result is not None

        with pytest.raises(NonEnumerableError):
            personal.title(title_type='nil')
            personal.title(gender='nil')

    @pytest.mark.parametrize(
        'gender', [
            Gender.FEMALE,
            Gender.MALE,
        ],
    )
    def test_nationality(self, personal, gender):
        nationality = personal._data['nationality']
        if isinstance(nationality, dict):
            result = personal.nationality(gender=gender)
            assert result in personal._data['nationality'][gender.value]

        result = personal.nationality()
        assert result is not None


class TestSeededPersonal(object):
    TIMES = 5

    @pytest.fixture
    def _personals(self, seed):
        return Personal(seed=seed), Personal(seed=seed)

    def test_age(self, _personals):
        p1, p2 = _personals
        for _ in range(self.TIMES):
            assert p1.age() == p2.age()
            assert p1.age(minimum=12, maximum=42) == \
                p2.age(minimum=12, maximum=42)

    def test_child_count(self, _personals):
        p1, p2 = _personals
        for _ in range(self.TIMES):
            assert p1.child_count() == p2.child_count()
            assert p1.child_count(max_childs=42) == \
                p2.child_count(max_childs=42)

    def test_work_experience(self, _personals):
        p1, p2 = _personals
        for _ in range(self.TIMES):
            assert p1.work_experience() == p2.work_experience()
            assert p1.work_experience(working_start_age=19) == \
                p2.work_experience(working_start_age=19)

    def test_password(self, _personals):
        p1, p2 = _personals
        for _ in range(self.TIMES):
            assert p1.password() == p2.password()
            assert p1.password(length=12, hashed=True) == \
                p2.password(length=12, hashed=True)

    def test_username(self, _personals):
        p1, p2 = _personals
        for _ in range(self.TIMES):
            assert p1.username() == p2.username()
            assert p1.username(template='l_d') == p2.username(template='l_d')

    def test_email(self, _personals):
        p1, p2 = _personals
        for _ in range(self.TIMES):
            assert p1.email() == p2.email()
            assert p1.email(domains=['@mimesis.io', ]) == \
                p2.email(domains=['@mimesis.io', ])

    def test_height(self, _personals):
        p1, p2 = _personals
        for _ in range(self.TIMES):
            assert p1.height() == p2.height()
            assert p1.height(minimum=1.0, maximum=2.1) == \
                p2.height(minimum=1.0, maximum=2.1)

    def test_weight(self, _personals):
        p1, p2 = _personals
        for _ in range(self.TIMES):
            assert p1.weight() == p2.weight()
            assert p1.weight(minimum=16, maximum=42) == \
                p2.weight(minimum=16, maximum=42)

    def test_blood_type(self, _personals):
        p1, p2 = _personals
        for _ in range(self.TIMES):
            assert p1.blood_type() == p2.blood_type()

    def test_favorite_movie(self, _personals):
        p1, p2 = _personals
        for _ in range(self.TIMES):
            assert p1.favorite_movie() == p2.favorite_movie()

    def test_favorite_music_genre(self, _personals):
        p1, p2 = _personals
        for _ in range(self.TIMES):
            assert p1.favorite_music_genre() == p2.favorite_music_genre()

    def test_social_media_profile(self, _personals):
        p1, p2 = _personals
        for _ in range(self.TIMES):
            assert p1.social_media_profile() == p2.social_media_profile()
            assert p1.social_media_profile(site=SocialNetwork.TWITTER) == \
                p2.social_media_profile(site=SocialNetwork.TWITTER)

    def test_avatar(self, _personals):
        p1, p2 = _personals
        for _ in range(self.TIMES):
            assert p1.avatar() == p2.avatar()
            assert p1.avatar(size=64) == p2.avatar(size=64)

    def test_identifier(self, _personals):
        p1, p2 = _personals
        for _ in range(self.TIMES):
            assert p1.identifier() == p2.identifier()
            assert p1.identifier(mask='##_##') == p2.identifier(mask='##_##')

    def test_level_of_english(self, _personals):
        p1, p2 = _personals
        for _ in range(self.TIMES):
            assert p1.level_of_english() == p2.level_of_english()

    def test_name(self, _personals):
        p1, p2 = _personals
        for _ in range(self.TIMES):
            assert p1.name() == p2.name()
            assert p1.name(gender=Gender.FEMALE) == \
                p2.name(gender=Gender.FEMALE)

    def test_telephone(self, _personals):
        p1, p2 = _personals
        for _ in range(self.TIMES):
            assert p1.telephone() == p2.telephone()
            assert p1.telephone(mask='(x)-xx-xxx', placeholder='x') == \
                p2.telephone(mask='(x)-xx-xxx', placeholder='x')

    def test_surname(self, _personals):
        p1, p2 = _personals
        for _ in range(self.TIMES):
            assert p1.surname() == p2.surname()
            assert p1.surname(gender=Gender.MALE) == \
                p2.surname(gender=Gender.MALE)

    def test_full_name(self, _personals):
        p1, p2 = _personals
        for _ in range(self.TIMES):
            assert p1.full_name() == p2.full_name()
            assert p1.full_name(gender=Gender.FEMALE, reverse=True) == \
                p2.full_name(gender=Gender.FEMALE, reverse=True)

    def test_gender(self, _personals):
        p1, p2 = _personals
        for _ in range(self.TIMES):
            assert p1.gender() == p2.gender()
            assert p1.gender(iso5218=True, symbol=True) == \
                p2.gender(iso5218=True, symbol=True)

    def test_sexual_orientation(self, _personals):
        p1, p2 = _personals
        for _ in range(self.TIMES):
            assert p1.sexual_orientation() == p2.sexual_orientation()
            assert p1.sexual_orientation(symbol=True) == \
                p2.sexual_orientation(symbol=True)

    def test_occupation(self, _personals):
        p1, p2 = _personals
        for _ in range(self.TIMES):
            assert p1.occupation() == p2.occupation()

    def test_university(self, _personals):
        p1, p2 = _personals
        for _ in range(self.TIMES):
            assert p1.university() == p2.university()

    def test_academic_degree(self, _personals):
        p1, p2 = _personals
        for _ in range(self.TIMES):
            assert p1.academic_degree() == p2.academic_degree()

    def test_language(self, _personals):
        p1, p2 = _personals
        for _ in range(self.TIMES):
            assert p1.language() == p2.language()

    def test_worldview(self, _personals):
        p1, p2 = _personals
        for _ in range(self.TIMES):
            assert p1.worldview() == p2.worldview()

    def test_views_on(self, _personals):
        p1, p2 = _personals
        for _ in range(self.TIMES):
            assert p1.views_on() == p2.views_on()

    def test_political_views(self, _personals):
        p1, p2 = _personals
        for _ in range(self.TIMES):
            assert p1.political_views() == p2.political_views()

    def test_title(self, _personals):
        p1, p2 = _personals
        for _ in range(self.TIMES):
            assert p1.title() == p2.title()
            assert p1.title(gender=Gender.FEMALE,
                            title_type=TitleType.TYPICAL) == \
                p2.title(gender=Gender.FEMALE,
                         title_type=TitleType.TYPICAL)

    def test_nationality(self, _personals):
        p1, p2 = _personals
        for _ in range(self.TIMES):
            assert p1.nationality() == p2.nationality()
            assert p1.nationality(gender=Gender.FEMALE) == \
                p2.nationality(gender=Gender.FEMALE)
