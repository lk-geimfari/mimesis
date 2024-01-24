import re
from datetime import date, datetime

import pytest

from mimesis import Person, random
from mimesis.data import BLOOD_GROUPS, GENDER_CODES, GENDER_SYMBOLS
from mimesis.enums import Gender, TitleType
from mimesis.exceptions import NonEnumerableError

from . import patterns


class TestPerson:
    @pytest.fixture
    def _person(self):
        return Person()

    def test_str(self, person):
        assert re.match(patterns.DATA_PROVIDER_STR_REGEX, str(person))

    @pytest.mark.parametrize(
        "min_year, max_year",
        [
            (1900, 1950),
            (1951, 2001),
            (2001, 2023),
        ],
    )
    def test_birthdate(self, _person, min_year, max_year):
        birthdate = _person.birthdate(min_year, max_year)
        assert min_year <= birthdate.year <= max_year
        assert isinstance(birthdate, date)

    @pytest.mark.parametrize(
        "min_year, max_year",
        [
            (1899, 1950),
            (datetime.now().year + 1, datetime.now().year + 3),
        ],
    )
    def test_birthdate_with_invalid_params(self, _person, min_year, max_year):
        with pytest.raises(ValueError):
            _person.birthdate(min_year, max_year)

    def test_is_leap_year(self, _person):
        assert _person._is_leap_year(2024)

    def test_password(self, _person):
        result = _person.password(length=15)
        assert len(result) == 15

        result = _person.password(hashed=True)
        assert len(result) == 64

    @pytest.mark.parametrize(
        "mask",
        [
            "C-d",
            "C.d",
            "C_d",
            "CC-d",
            "CC.d",
            "CC_d",
            "Cd",
            "l-d",
            "l.d",
            "l_d",
            "ld",
            None,
        ],
    )
    def test_username(self, _person, mask):
        template_patterns = {
            "C-d": r"^[A-Z][a-z]+-[0-9]+$",
            "C.d": r"^[A-Z][a-z]+\.[0-9]+$",
            "C_d": r"^[A-Z][a-z]+_[0-9]+$",
            "CC-d": r"^[A-Z][a-z]+[A-Z][a-z]+-[0-9]+$",
            "CC.d": r"^[A-Z][a-z]+[A-Z][a-z]+\.[0-9]+$",
            "CC_d": r"^[A-Z][a-z]+[A-Z][a-z]+_[0-9]+$",
            "Cd": r"^[A-Z][a-z]+[0-9]+$",
            "l-d": r"^[a-z]+-[0-9]+$",
            "l.d": r"^[a-z]+\.[0-9]+$",
            "l_d": r"^[a-z]+_[0-9]+$",
            "ld": r"^[a-z]+[0-9]+$",
            None: r"^[A-Za-z]{2,}[\.\-\_]?[0-9]+$",
        }

        result = _person.username(mask=mask)
        assert re.match(template_patterns[mask], result)

    def test_username_drange(self, _person):
        username = _person.username(mask="U.d", drange=(1000, 2000))
        username, digits = username.split(".")
        assert 1000 <= int(digits.strip()) <= 2000

        with pytest.raises(ValueError):
            _person.username(drange=(1000, 2000, 3000))  # type: ignore

    def test_username_unsupported_mask(self, _person):
        with pytest.raises(ValueError):
            _person.username(mask="cda")

    @pytest.mark.parametrize(
        "unique",
        [
            False,
            True,
        ],
    )
    def test_email(self, _person, unique, monkeypatch):
        if unique:
            # We need to prepare the env to remove seeds:
            monkeypatch.setattr(random, "global_seed", None)

        result = _person.email()
        assert re.match(patterns.EMAIL_REGEX, result)

        domains = ["@example.com", "example.com"]
        result = _person.email(domains=domains)
        assert re.match(patterns.EMAIL_REGEX, result)
        assert result.split("@")[1] == "example.com"

        if unique:
            count = 1000000
            generated = set()

            for i in range(count):
                email = _person.email(
                    domains=["example.com"],
                    unique=unique,
                )
                email_username = email.split("@")[0].strip()
                generated.add(email_username)

            assert len(generated) == count

    def test_email_unique_seed(self):
        person = Person(seed=1)
        with pytest.raises(ValueError):
            person.email(unique=True)

    def test_height(self, _person):
        result = _person.height(minimum=1.60, maximum=1.90)
        assert 1.6 <= float(result) <= 1.9
        assert isinstance(result, str)

    def test_weight(self, _person):
        result = _person.weight(minimum=40, maximum=60)
        assert 40 <= result <= 60

    def test_blood_type(self, _person):
        result = _person.blood_type()
        assert result in BLOOD_GROUPS

    def test_identifier(self, _person):
        result = _person.identifier()
        mask = "##-##/##"
        assert len(mask) == len(result)

        result = _person.identifier(mask="##-##/## @@")
        suffix = result.split(" ")[1]
        assert suffix.isalpha()

    @pytest.mark.parametrize(
        "gender",
        [
            Gender.FEMALE,
            Gender.MALE,
        ],
    )
    def test_name(self, person, gender):
        result = person.name(gender=gender)
        assert result in person._data["names"][gender.value]

    @pytest.mark.parametrize(
        "gender",
        [
            Gender.FEMALE,
            Gender.MALE,
        ],
    )
    def test_first_name(self, person, gender):
        result = person.first_name(gender=gender)
        assert result in person._data["names"][gender.value]

    def test_name_with_none(self, _person):
        result = _person.name(gender=None)
        names = _person._data["names"]

        females = names["female"]
        males = names["male"]
        assert result is not None
        assert (result in females) or (result in males)

    def test_name_unexpected_gender(self, person):
        with pytest.raises(NonEnumerableError):
            person.name(gender="nil")

    def test_telephone(self, person):
        result = person.telephone()
        assert result is not None

        mask = "+5 (###)-###-##-##"
        result = person.telephone(mask=mask)
        head = result.split(" ")[0]
        assert head == "+5"

    @pytest.mark.parametrize(
        "gender",
        [
            Gender.FEMALE,
            Gender.MALE,
        ],
    )
    def test_surname(self, person, gender):
        surnames = person._data["surnames"]

        # Surnames separated by gender.
        if isinstance(surnames, dict):
            result = person.surname(gender=gender)
            assert result in surnames[gender.value]
        else:
            result = person.surname()
            assert result in surnames
            result = person.last_name()
            assert result in surnames

    @pytest.mark.parametrize(
        "gender",
        [
            Gender.FEMALE,
            Gender.MALE,
        ],
    )
    def test_full_name(self, person, gender):
        result = person.full_name(gender=gender)

        result = result.split(" ")
        assert result[0] is not None
        assert result[1] is not None

        result = person.full_name(reverse=True)
        assert result is not None

        with pytest.raises(NonEnumerableError):
            person.full_name(gender="nil")

    def test_gender_code(self, _person):
        code = _person.gender_code()
        assert code in GENDER_CODES

    def test_gender_symbol(self, _person):
        symbol = _person.gender_symbol()
        assert symbol in GENDER_SYMBOLS

    def test_gender(self, person):
        result = person.gender()
        assert result in person._data["gender"]

    def test_sex(self, person):
        result = person.sex()
        assert result in person._data["gender"]

    def test_profession(self, person):
        result = person.occupation()
        assert result in person._data["occupation"]

    def test_university(self, person):
        result = person.university()
        assert result in person._data["university"]

    def test_academic_degree(self, person):
        result = person.academic_degree()
        assert result in person._data["academic_degree"]

    def test_language(self, person):
        result = person.language()
        assert result in person._data["language"]

    def test_worldview(self, person):
        result = person.worldview()
        assert result in person._data["worldview"]

    def test_views_on(self, person):
        result = person.views_on()
        assert result in person._data["views_on"]

    def test_political_views(self, person):
        result = person.political_views()
        assert result in person._data["political_views"]

    @pytest.mark.parametrize(
        "title_type",
        [
            TitleType.ACADEMIC,
            TitleType.TYPICAL,
            None,
        ],
    )
    @pytest.mark.parametrize(
        "gender",
        [
            Gender.FEMALE,
            Gender.MALE,
            None,
        ],
    )
    def test_title(self, person, gender, title_type):
        result = person.title(gender=gender, title_type=title_type)
        assert result is not None

        with pytest.raises(NonEnumerableError):
            person.title(title_type="nil")
            person.title(gender="nil")

    @pytest.mark.parametrize(
        "gender",
        [
            Gender.FEMALE,
            Gender.MALE,
        ],
    )
    def test_nationality(self, person, gender):
        nationality = person._data["nationality"]
        if isinstance(nationality, dict):
            result = person.nationality(gender=gender)
            assert result in person._data["nationality"][gender.value]

        result = person.nationality()
        assert result is not None


class TestSeededPerson:
    @pytest.fixture
    def p1(self, seed):
        return Person(seed=seed)

    @pytest.fixture
    def p2(self, seed):
        return Person(seed=seed)

    def test_password(self, p1, p2):
        assert p1.password() == p2.password()
        assert p1.password(length=12, hashed=True) == p2.password(
            length=12, hashed=True
        )

    def test_username(self, p1, p2):
        assert p1.username() == p2.username()
        assert p1.username(mask="l_d") == p2.username(mask="l_d")

    def test_email(self, p1, p2):
        assert p1.email() == p2.email()
        assert p1.email(domains=["@mimesis.io"]) == p2.email(domains=["@mimesis.io"])

        with pytest.raises(ValueError):
            p1.email(unique=True)

    def test_height(self, p1, p2):
        assert p1.height() == p2.height()
        assert p1.height(1.7, 2.1) == p2.height(1.7, 2.1)

    def test_weight(self, p1, p2):
        assert p1.weight() == p2.weight()
        assert p1.weight(16, 42) == p2.weight(16, 42)

    def test_blood_type(self, p1, p2):
        assert p1.blood_type() == p2.blood_type()

    def test_identifier(self, p1, p2):
        assert p1.identifier() == p2.identifier()
        assert p1.identifier(mask="##") == p2.identifier(mask="##")

    def test_name(self, p1, p2):
        assert p1.name() == p2.name()
        assert p1.name(gender=Gender.FEMALE) == p2.name(gender=Gender.FEMALE)

    def test_first_name(self, p1, p2):
        assert p1.first_name() == p2.first_name()
        assert p1.first_name(gender=Gender.FEMALE) == p2.first_name(
            gender=Gender.FEMALE
        )

    def test_telephone(self, p1, p2):
        assert p1.telephone() == p2.telephone()
        assert p1.telephone(mask="(x)-xx-xxx", placeholder="x") == p2.telephone(
            mask="(x)-xx-xxx", placeholder="x"
        )

    def test_surname(self, p1, p2):
        assert p1.surname() == p2.surname()
        assert p1.last_name(gender=Gender.MALE) == p2.last_name(gender=Gender.MALE)

    def test_full_name(self, p1, p2):
        assert p1.full_name() == p2.full_name()
        assert p1.full_name(gender=Gender.FEMALE, reverse=True) == p2.full_name(
            gender=Gender.FEMALE, reverse=True
        )

    def test_gender_code(self, p1, p2):
        assert p1.gender_code() == p2.gender_code()

    def test_birthdate(self, p1, p2):
        assert p1.birthdate() == p2.birthdate()
        assert p1.birthdate(min_year=1900, max_year=2023) == p2.birthdate(
            min_year=1900, max_year=2023
        )

    def test_gender_symbol(self, p1, p2):
        assert p1.gender_symbol() == p2.gender_symbol()

    def test_gender(self, p1, p2):
        assert p1.gender() == p2.gender()

    def test_sex(self, p1, p2):
        assert p1.sex() == p2.sex()

    def test_occupation(self, p1, p2):
        assert p1.occupation() == p2.occupation()

    def test_university(self, p1, p2):
        assert p1.university() == p2.university()

    def test_academic_degree(self, p1, p2):
        assert p1.academic_degree() == p2.academic_degree()

    def test_language(self, p1, p2):
        assert p1.language() == p2.language()

    def test_worldview(self, p1, p2):
        assert p1.worldview() == p2.worldview()

    def test_views_on(self, p1, p2):
        assert p1.views_on() == p2.views_on()

    def test_political_views(self, p1, p2):
        assert p1.political_views() == p2.political_views()

    def test_title(self, p1, p2):
        assert p1.title() == p2.title()
        assert p1.title(gender=Gender.FEMALE, title_type=TitleType.TYPICAL) == p2.title(
            gender=Gender.FEMALE, title_type=TitleType.TYPICAL
        )

    def test_nationality(self, p1, p2):
        assert p1.nationality() == p2.nationality()
        assert p1.nationality(Gender.FEMALE) == p2.nationality(Gender.FEMALE)
