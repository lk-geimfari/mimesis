"""Provides personal data."""

import hashlib
import re
import typing as t
import uuid
from datetime import date, datetime
from string import ascii_letters, digits, punctuation

from mimesis.datasets import (
    BLOOD_GROUPS,
    CALLING_CODES,
    EMAIL_DOMAINS,
    GENDER_CODES,
    GENDER_SYMBOLS,
    USERNAMES,
)
from mimesis.enums import Gender, TitleType
from mimesis.providers.base import BaseDataProvider
from mimesis.types import Date

__all__ = ["Person"]


class Person(BaseDataProvider):
    """Class for generating personal data."""

    def __init__(self, *args: t.Any, **kwargs: t.Any) -> None:
        """Initialize attributes.

        :param locale: Current locale.
        :param seed: Seed.
        """
        super().__init__(*args, **kwargs)

    class Meta:
        name = "person"
        datafile = f"{name}.json"

    def _validate_birth_year_params(self, min_year: int, max_year: int) -> None:
        if min_year > max_year:
            raise ValueError("min_year must be less than or equal to max_year")

        if min_year < 1900:
            raise ValueError("min_year must be greater than or equal to 1900")

        if max_year > datetime.now().year:
            raise ValueError(
                "The max_year must be less than or equal to the current year"
            )

    def _is_leap_year(self, year: int) -> bool:
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def birthdate(self, min_year: int = 1980, max_year: int = 2023) -> Date:
        """Generates a random birthdate as a :py:class:`datetime.date` object.

        :param min_year: Maximum birth year.
        :param max_year: Minimum birth year.
        :return: Random date object.
        """
        self._validate_birth_year_params(min_year, max_year)
        year = self.random.randint(min_year, max_year)
        feb_days = 29 if self._is_leap_year(year) else 28

        month_days_map = {
            1: 31,
            2: feb_days,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31,
        }

        month = self.random.randint(1, 12)
        max_day = month_days_map[month]
        day = self.random.randint(1, max_day)
        return date(year=year, month=month, day=day)

    def name(self, gender: Gender | None = None) -> str:
        """Generates a random name.

        :param gender: Gender's enum object.
        :return: Name.

        :Example:
            John.
        """
        key = self.validate_enum(gender, Gender)
        names: list[str] = self._extract(["names", key])
        return self.random.choice(names)

    def first_name(self, gender: Gender | None = None) -> str:
        """Generates a random first name.

        ..note: An alias for :meth:`~.name`.

        :param gender: Gender's enum object.
        :return: First name.
        """
        return self.name(gender)

    def surname(self, gender: Gender | None = None) -> str:
        """Generates a random surname.

        :param gender: Gender's enum object.
        :return: Surname.

        :Example:
            Smith.
        """
        surnames: t.Sequence[str] = self._extract(["surnames"])

        # Surnames separated by gender.
        if isinstance(surnames, dict):
            key = self.validate_enum(gender, Gender)
            surnames = surnames[key]

        return self.random.choice(surnames)

    def last_name(self, gender: Gender | None = None) -> str:
        """Generates a random last name.

        ..note: An alias for :meth:`~.surname`.

        :param gender: Gender's enum object.
        :return: Last name.
        """
        return self.surname(gender)

    def title(
        self,
        gender: Gender | None = None,
        title_type: TitleType | None = None,
    ) -> str:
        """Generates a random title for name.

        You can generate a random prefix or suffix
        for name using this method.

        :param gender: The gender.
        :param title_type: TitleType enum object.
        :return: The title.
        :raises NonEnumerableError: if gender or title_type in incorrect format.

        :Example:
            PhD.
        """
        gender_key = self.validate_enum(gender, Gender)
        title_key = self.validate_enum(title_type, TitleType)

        titles: list[str] = self._extract(["title", gender_key, title_key])
        return self.random.choice(titles)

    def full_name(
        self,
        gender: Gender | None = None,
        reverse: bool = False,
    ) -> str:
        """Generates a random full name.

        :param reverse: Return reversed full name.
        :param gender: Gender's enum object.
        :return: Full name.

        :Example:
            Johann Wolfgang.
        """
        name = self.name(gender)
        surname = self.surname(gender)
        return f"{surname} {name}" if reverse else f"{name} {surname}"

    def username(
        self, mask: str | None = None, drange: tuple[int, int] = (1800, 2100)
    ) -> str:
        """Generates a username by mask.

        Masks allow you to generate a variety of usernames.

        - **C** stands for capitalized username.
        - **U** stands for uppercase username.
        - **l** stands for lowercase username.
        - **d** stands for digits in the username.

        You can also use symbols to separate the different parts
        of the username: **.** **_** **-**

        :param mask: Mask.
        :param drange: Digits range.
        :raises ValueError: If template is not supported.
        :return: Username as string.

        Example:
            >>> username(mask='C_C_d')
            Cotte_Article_1923
            >>> username(mask='U.l.d')
            ELKINS.wolverine.2013
            >>> username(mask='l_l_d', drange=(1900, 2021))
            plasmic_blockader_1907
        """
        if len(drange) != 2:
            raise ValueError("The drange parameter must contain only two integers.")

        if mask is None:
            mask = "l_d"

        required_tags = "CUl"
        tags = re.findall(r"[CUld.\-_]", mask)

        if not any(tag in tags for tag in required_tags):
            raise ValueError(
                "Username mask must contain at least one of these: (C, U, l)."
            )

        final_username = ""
        for tag in tags:
            username = self.random.choice(USERNAMES)
            if tag == "C":
                final_username += username.capitalize()
            if tag == "U":
                final_username += username.upper()
            elif tag == "l":
                final_username += username.lower()
            elif tag == "d":
                final_username += str(self.random.randint(*drange))
            elif tag in "-_.":
                final_username += tag

        return final_username

    def password(self, length: int = 8, hashed: bool = False) -> str:
        """Generates a password or hash of password.

        :param length: Length of password.
        :param hashed: SHA256 hash.
        :return: Password or hash of password.

        :Example:
            k6dv2odff9#4h
        """
        characters = ascii_letters + digits + punctuation
        password = "".join(self.random.choices(characters, k=length))

        if hashed:
            sha256 = hashlib.sha256()
            sha256.update(password.encode())
            return sha256.hexdigest()

        return password

    def email(
        self,
        domains: t.Sequence[str] | None = None,
        unique: bool = False,
    ) -> str:
        """Generates a random email.

        :param domains: List of custom domains for emails.
        :param unique: Makes email addresses unique.
        :return: Email address.
        :raises ValueError: if «unique» is True and the provider was seeded.

        :Example:
            foretime10@live.com
        """
        if unique and self._has_seed():
            raise ValueError(
                "You cannot use «unique» parameter with the seeded provider"
            )

        if not domains:
            domains = EMAIL_DOMAINS

        domain = self.random.choice(domains)

        if not domain.startswith("@"):
            domain = "@" + domain

        if unique:
            name = str(uuid.uuid4().hex)
        else:
            name = self.username(mask="ld")

        return f"{name}{domain}"

    def gender_symbol(self) -> str:
        """Generate a random sex symbol.

        :Example:
            ♂
        """
        return self.random.choice(GENDER_SYMBOLS)

    def gender_code(self) -> int:
        """Generate a random ISO/IEC 5218 gender code.

        Generate a random title of gender code for the representation
        of human sexes is an international standard that defines a
        representation of human sexes through a language-neutral single-digit
        code or symbol of gender.

        Codes for the representation of human sexes is an international
        standard (0 - not known, 1 - male, 2 - female, 9 - not applicable).

        :return:
        """
        return self.random.choice(GENDER_CODES)

    def gender(self) -> str:
        """Generates a random gender title.

        :Example:
            Male
        """
        genders: list[str] = self._extract(["gender"])
        return self.random.choice(genders)

    def sex(self) -> str:
        """An alias for method :meth:`~.gender`.

        :return: Sex.
        """
        return self.gender()

    def height(self, minimum: float = 1.5, maximum: float = 2.0) -> str:
        """Generates a random height in meters.

        :param minimum: Minimum value.
        :param float maximum: Maximum value.
        :return: Height.

        :Example:
            1.85.
        """
        h = self.random.uniform(minimum, maximum)
        return f"{h:0.2f}"

    def weight(self, minimum: int = 38, maximum: int = 90) -> int:
        """Generates a random weight in Kg.

        :param minimum: min value
        :param maximum: max value
        :return: Weight.

        :Example:
            48.
        """
        return self.random.randint(minimum, maximum)

    def blood_type(self) -> str:
        """Generates a random blood type.

        :return: Blood type (blood group).

        :Example:
            A+
        """
        return self.random.choice(BLOOD_GROUPS)

    def occupation(self) -> str:
        """Generates a random job.

        :return: The name of job.

        :Example:
            Programmer.
        """
        jobs: list[str] = self._extract(["occupation"])
        return self.random.choice(jobs)

    def political_views(self) -> str:
        """Get a random political views.

        :return: Political views.

        :Example:
            Liberal.
        """
        views: list[str] = self._extract(["political_views"])
        return self.random.choice(views)

    def worldview(self) -> str:
        """Generates a random worldview.

        :return: Worldview.

        :Example:
            Pantheism.
        """
        views: list[str] = self._extract(["worldview"])
        return self.random.choice(views)

    def views_on(self) -> str:
        """Get a random views on.

        :return: Views on.

        :Example:
            Negative.
        """
        views: list[str] = self._extract(["views_on"])
        return self.random.choice(views)

    def nationality(self, gender: Gender | None = None) -> str:
        """Generates a random nationality.

        :param gender: Gender.
        :return: Nationality.

        :Example:
            Russian
        """
        nationalities: list[str] = self._extract(["nationality"])

        # Separated by gender
        if isinstance(nationalities, dict):
            key = self.validate_enum(gender, Gender)
            nationalities = nationalities[key]

        return self.random.choice(nationalities)

    def university(self) -> str:
        """Generates a random university name.

        :return: University name.

        :Example:
            MIT.
        """
        universities: list[str] = self._extract(["university"])
        return self.random.choice(universities)

    def academic_degree(self) -> str:
        """Generates a random academic degree.

        :return: Degree.

        :Example:
            Bachelor.
        """
        degrees: list[str] = self._extract(["academic_degree"])
        return self.random.choice(degrees)

    def language(self) -> str:
        """Generates a random language name.

        :return: Random language.

        :Example:
            Irish.
        """
        languages: list[str] = self._extract(["language"])
        return self.random.choice(languages)

    def phone_number(self, mask: str = "", placeholder: str = "#") -> str:
        """Generates a random phone number.

        :param mask: Mask for formatting number.
        :param placeholder: A placeholder for a mask (default is #).
        :return: Phone number.

        :Example:
            +7-(963)-409-11-22.
        """
        if not mask:
            code = self.random.choice(CALLING_CODES)
            default = f"{code}-(###)-###-####"
            masks = self._extract(["telephone_fmt"], default=[default])
            mask = self.random.choice(masks)

        return self.random.generate_string_by_mask(mask=mask, digit=placeholder)

    def telephone(self, *args: t.Any, **kwargs: t.Any) -> str:
        """An alias for :meth:`~.phone_number`."""
        return self.phone_number(*args, **kwargs)

    def identifier(self, mask: str = "##-##/##") -> str:
        """Generates a random identifier by mask.

        With this method, you can generate any identifiers that
        you need by specifying the mask.

        :param mask:
            The mask. Here ``@`` is a placeholder for characters and ``#`` is
            placeholder for digits.
        :return: An identifier.

        :Example:
            07-97/04
        """
        return self.random.generate_string_by_mask(mask=mask)
