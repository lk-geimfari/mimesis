"""Provides personal data."""

import hashlib
import re
import typing as t
from string import ascii_letters, digits, punctuation

from mimesis.data import (
    BLOOD_GROUPS,
    CALLING_CODES,
    EMAIL_DOMAINS,
    GENDER_SYMBOLS,
    USERNAMES,
)
from mimesis.enums import Gender, TitleType
from mimesis.exceptions import NonEnumerableError
from mimesis.providers.base import BaseDataProvider
from mimesis.random import get_random_item

__all__ = ["Person"]


class Person(BaseDataProvider):
    """Class for generating personal data."""

    def __init__(self, *args: t.Any, **kwargs: t.Any) -> None:
        """Initialize attributes.

        :param locale: Current locale.
        :param seed: Seed.
        """
        super().__init__(*args, **kwargs)
        self._datafile = "person.json"
        self._load_datafile(self._datafile)
        self._store = {
            "age": 0,
        }

    class Meta:
        """Class for metadata."""

        name: t.Final[str] = "person"

    def age(self, minimum: int = 16, maximum: int = 66) -> int:
        """Get a random integer value.

        :param maximum: Maximum value of age.
        :param minimum: Minimum value of age.
        :return: Random integer.

        :Example:
            23.
        """
        age = self.random.randint(minimum, maximum)
        self._store["age"] = age
        return age

    def work_experience(self, working_start_age: int = 22) -> int:
        """Get a work experience.

        :param working_start_age: Age then person start to work.
        :return: Depend on previous generated age.
        """
        age = self._store["age"]
        if age == 0:
            age = self.age()

        return max(age - working_start_age, 0)

    def name(self, gender: t.Optional[Gender] = None) -> str:
        """Generate a random name.

        :param gender: Gender's enum object.
        :return: Name.

        :Example:
            John.
        """
        key = self.validate_enum(gender, Gender)
        names: t.List[str] = self.extract(["names", key])
        return self.random.choice(names)

    def first_name(self, gender: t.Optional[Gender] = None) -> str:
        """Generate a random first name.

        ..note: An alias for self.name().

        :param gender: Gender's enum object.
        :return: First name.
        """
        return self.name(gender)

    def surname(self, gender: t.Optional[Gender] = None) -> str:
        """Generate a random surname.

        :param gender: Gender's enum object.
        :return: Surname.

        :Example:
            Smith.
        """
        surnames: t.Sequence[str] = self.extract(["surnames"])

        # Surnames separated by gender.
        if isinstance(surnames, dict):
            key = self.validate_enum(gender, Gender)
            surnames = surnames[key]

        return self.random.choice(surnames)

    def last_name(self, gender: t.Optional[Gender] = None) -> str:
        """Generate a random last name.

        ..note: An alias for self.surname().

        :param gender: Gender's enum object.
        :return: Last name.
        """
        return self.surname(gender)

    def title(
        self,
        gender: t.Optional[Gender] = None,
        title_type: t.Optional[TitleType] = None,
    ) -> str:
        """Generate a random title for name.

        You can generate random prefix or suffix
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

        titles: t.List[str] = self.extract(["title", gender_key, title_key])
        return self.random.choice(titles)

    def full_name(
        self, gender: t.Optional[Gender] = None, reverse: bool = False
    ) -> str:
        """Generate a random full name.

        :param reverse: Return reversed full name.
        :param gender: Gender's enum object.
        :return: Full name.

        :Example:
            Johann Wolfgang.
        """
        if gender is None:
            gender = get_random_item(Gender, rnd=self.random)

        if gender and isinstance(gender, Gender):
            gender = gender
        else:
            raise NonEnumerableError(Gender)

        name = self.name(gender)
        surname = self.surname(gender)
        return f"{surname} {name}" if reverse else f"{name} {surname}"

    def username(
        self, mask: t.Optional[str] = None, drange: t.Tuple[int, int] = (1800, 2100)
    ) -> str:
        """Generate username by template.

        You can create many different usernames using masks.

        - **C** stands for capitalized username.
        - **U** stands for uppercase username.
        - **l** stands for lowercase username.
        - **d** stands for digits in username.

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
        """Generate a password or hash of password.

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
        domains: t.Optional[t.Sequence[str]] = None,
        unique: bool = False,
    ) -> str:
        """Generate a random email.

        :param domains: List of custom domains for emails.
        :param unique: Makes email addresses unique.
        :return: Email address.
        :raises ValueError: if «unique» is True and the provider was seeded.

        :Example:
            foretime10@live.com
        """
        if unique and self.seed is not None:
            raise ValueError(
                "You cannot use «unique» parameter with the seeded provider"
            )

        if not domains:
            domains = EMAIL_DOMAINS

        domain = self.random.choice(domains)

        if not domain.startswith("@"):
            domain = "@" + domain

        if unique:
            name = self.random.randstr(unique)
        else:
            name = self.username(mask="ld")

        return f"{name}{domain}"

    def gender(self, iso5218: bool = False, symbol: bool = False) -> t.Union[str, int]:
        """Get a random gender.

        Get a random title of gender, code for the representation
        of human sexes is an international standard that defines a
        representation of human sexes through a language-neutral single-digit
        code or symbol of gender.

        :param iso5218:
            Codes for the representation of human sexes is an international
            standard (0 - not known, 1 - male, 2 - female, 9 - not applicable).
        :param symbol: Symbol of gender.
        :return: Title of gender.

        :Example:
            Male
        """
        if iso5218:
            return self.random.choice([0, 1, 2, 9])

        if symbol:
            return self.random.choice(GENDER_SYMBOLS)

        genders: t.List[str] = self.extract(["gender"])
        return self.random.choice(genders)

    def sex(self, *args: t.Any, **kwargs: t.Any) -> t.Union[str, int]:
        """An alias for method self.gender().

        See docstrings of method self.gender() for details.

        :param args: Positional arguments.
        :param kwargs: Keyword arguments.
        :return: Sex
        """
        return self.gender(*args, **kwargs)

    def height(self, minimum: float = 1.5, maximum: float = 2.0) -> str:
        """Generate a random height in meters.

        :param minimum: Minimum value.
        :param float maximum: Maximum value.
        :return: Height.

        :Example:
            1.85.
        """
        h = self.random.uniform(minimum, maximum)
        return f"{h:0.2f}"

    def weight(self, minimum: int = 38, maximum: int = 90) -> int:
        """Generate a random weight in Kg.

        :param minimum: min value
        :param maximum: max value
        :return: Weight.

        :Example:
            48.
        """
        return self.random.randint(minimum, maximum)

    def blood_type(self) -> str:
        """Get a random blood type.

        :return: Blood type (blood group).

        :Example:
            A+
        """
        return self.random.choice(BLOOD_GROUPS)

    def occupation(self) -> str:
        """Get a random job.

        :return: The name of job.

        :Example:
            Programmer.
        """
        jobs: t.List[str] = self.extract(["occupation"])
        return self.random.choice(jobs)

    def political_views(self) -> str:
        """Get a random political views.

        :return: Political views.

        :Example:
            Liberal.
        """
        views: t.List[str] = self.extract(["political_views"])
        return self.random.choice(views)

    def worldview(self) -> str:
        """Get a random worldview.

        :return: Worldview.

        :Example:
            Pantheism.
        """
        views: t.List[str] = self.extract(["worldview"])
        return self.random.choice(views)

    def views_on(self) -> str:
        """Get a random views on.

        :return: Views on.

        :Example:
            Negative.
        """
        views: t.List[str] = self.extract(["views_on"])
        return self.random.choice(views)

    def nationality(self, gender: t.Optional[Gender] = None) -> str:
        """Get a random nationality.

        :param gender: Gender.
        :return: Nationality.

        :Example:
            Russian
        """
        nationalities: t.List[str] = self.extract(["nationality"])

        # Separated by gender
        if isinstance(nationalities, dict):
            key = self.validate_enum(gender, Gender)
            nationalities = nationalities[key]

        return self.random.choice(nationalities)

    def university(self) -> str:
        """Get a random university.

        :return: University name.

        :Example:
            MIT.
        """
        universities: t.List[str] = self.extract(["university"])
        return self.random.choice(universities)

    def academic_degree(self) -> str:
        """Get a random academic degree.

        :return: Degree.

        :Example:
            Bachelor.
        """
        degrees: t.List[str] = self.extract(["academic_degree"])
        return self.random.choice(degrees)

    def language(self) -> str:
        """Get a random language.

        :return: Random language.

        :Example:
            Irish.
        """
        languages: t.List[str] = self.extract(["language"])
        return self.random.choice(languages)

    def telephone(self, mask: str = "", placeholder: str = "#") -> str:
        """Generate a random phone number.

        :param mask: Mask for formatting number.
        :param placeholder: A placeholder for a mask (default is #).
        :return: Phone number.

        :Example:
            +7-(963)-409-11-22.
        """
        if not mask:
            code = self.random.choice(CALLING_CODES)
            default = f"{code}-(###)-###-####"
            masks = self.extract(["telephone_fmt"], default=[default])
            mask = self.random.choice(masks)

        return self.random.custom_code(mask=mask, digit=placeholder)

    def identifier(self, mask: str = "##-##/##") -> str:
        """Generate a random identifier by mask.

        With this method you can generate any identifiers that
        you need. Simply select the mask that you need.

        :param mask:
            The mask. Here ``@`` is a placeholder for characters and ``#`` is
            placeholder for digits.
        :return: An identifier.

        :Example:
            07-97/04
        """
        return self.random.custom_code(mask=mask)
