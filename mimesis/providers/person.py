# -*- coding: utf-8 -*-

"""Provides personal data."""

import hashlib
import re
from string import ascii_letters, digits, punctuation
from typing import Optional, Union

from mimesis.data import (
    BLOOD_GROUPS,
    CALLING_CODES,
    EMAIL_DOMAINS,
    GENDER_SYMBOLS,
    SEXUALITY_SYMBOLS,
    SOCIAL_NETWORKS,
    USERNAMES,
)
from mimesis.enums import Gender, SocialNetwork, TitleType
from mimesis.exceptions import NonEnumerableError
from mimesis.providers.base import BaseDataProvider
from mimesis.random import get_random_item

__all__ = ['Person']


class Person(BaseDataProvider):
    """Class for generating personal data."""

    def __init__(self, *args, **kwargs) -> None:
        """Initialize attributes.

        :param locale: Current locale.
        :param seed: Seed.
        """
        super().__init__(*args, **kwargs)
        self._datafile = 'person.json'
        self._pull(self._datafile)
        self._store = {
            'age': 0,
        }

    class Meta:
        """Class for metadata."""

        name = 'person'

    def age(self, minimum: int = 16, maximum: int = 66) -> int:
        """Get a random integer value.

        :param maximum: Maximum value of age.
        :param minimum: Minimum value of age.
        :return: Random integer.

        :Example:
            23.
        """
        age = self.random.randint(minimum, maximum)
        self._store['age'] = age
        return age

    def work_experience(self, working_start_age: int = 22) -> int:
        """Get a work experience.

        :param working_start_age: Age then person start to work.
        :return: Depend on previous generated age.
        """
        age = self._store['age']
        if age == 0:
            age = self.age()

        return max(age - working_start_age, 0)

    def name(self, gender: Optional[Gender] = None) -> str:
        """Generate a random name.

        :param gender: Gender's enum object.
        :return: Name.

        :Example:
            John.
        """
        key = self._validate_enum(gender, Gender)
        names = self._data['names'].get(key)
        return self.random.choice(names)

    def first_name(self, gender: Optional[Gender] = None):
        """Generate a random first name.

        ..note: An alias for self.name().

        :param gender: Gender's enum object.
        :return: First name.
        """
        return self.name(gender)

    def surname(self, gender: Optional[Gender] = None) -> str:
        """Generate a random surname.

        :param gender: Gender's enum object.
        :return: Surname.

        :Example:
            Smith.
        """
        surnames = self._data['surnames']

        # Surnames separated by gender.
        if isinstance(surnames, dict):
            key = self._validate_enum(gender, Gender)
            surnames = surnames[key]

        return self.random.choice(surnames)

    def last_name(self, gender: Optional[Gender] = None) -> str:
        """Generate a random last name.

        ..note: An alias for self.surname().

        :param gender: Gender's enum object.
        :return: Last name.
        """
        return self.surname(gender)

    def title(self, gender: Optional[Gender] = None,
              title_type: Optional[TitleType] = None) -> str:
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
        gender_key = self._validate_enum(gender, Gender)
        title_key = self._validate_enum(title_type, TitleType)

        titles = self._data['title'][gender_key][title_key]
        return self.random.choice(titles)

    def full_name(self, gender: Optional[Gender] = None,
                  reverse: bool = False) -> str:
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

        fmt = '{1} {0}' if reverse else '{0} {1}'
        return fmt.format(
            self.name(gender),
            self.surname(gender),
        )

    def username(self, template: Optional[str] = None) -> str:
        """Generate username by template.

        Supported template placeholders: (U, l, d)

        Supported separators: (-, ., _)

        Template must contain at least one "U" or "l" placeholder.

        If template is None one of the following templates is used:
        ('U_d', 'U.d', 'U-d', 'UU-d', 'UU.d', 'UU_d',
        'ld', 'l-d', 'Ud', 'l.d', 'l_d', 'default')

        :param template: Template.
        :return: Username.
        :raises ValueError: If template is not supported.

        :Example:
            Celloid1873
        """
        min_date = 1800
        max_date = 2070
        default_template = 'l.d'

        templates = ('U_d', 'U.d', 'U-d', 'UU-d', 'UU.d', 'UU_d',
                     'ld', 'l-d', 'Ud', 'l.d', 'l_d', 'default')

        if template is None:
            template = self.random.choice(templates)

        if template == 'default':
            template = default_template

        if not re.fullmatch(r'[Ul\.\-\_d]*[Ul]+[Ul\.\-\_d]*', template):
            raise ValueError(
                "Template '{}' is not supported.".format(template))

        tags = re.findall(r'[Uld\.\-\_]', template)

        username = ''
        for tag in tags:
            if tag == 'U':
                username += self.random.choice(USERNAMES).capitalize()
            elif tag == 'l':
                username += self.random.choice(USERNAMES)
            elif tag == 'd':
                username += str(self.random.randint(min_date, max_date))
            elif tag in '-_.':
                username += tag

        return username

    def password(self, length: int = 8, hashed: bool = False) -> str:
        """Generate a password or hash of password.

        :param length: Length of password.
        :param hashed: MD5 hash.
        :return: Password or hash of password.

        :Example:
            k6dv2odff9#4h
        """
        text = ascii_letters + digits + punctuation
        password = ''.join([self.random.choice(text) for _ in range(length)])

        if hashed:
            md5 = hashlib.md5()
            md5.update(password.encode())
            return md5.hexdigest()

        return password

    def email(self, domains: Union[tuple, list] = None,
              unique: bool = False) -> str:
        """Generate a random email.

        :param domains: List of custom domains for emails.
        :param unique: Makes email addresses unique.
        :return: Email address.
        :raises ValueError: if «unique» is True and the provider was seeded.

        :Example:
            foretime10@live.com
        """
        if unique and self.seed is not None:
            raise ValueError('You cannot use «unique» '
                             'parameter with a seeded provider')

        if not domains:
            domains = EMAIL_DOMAINS

        domain = self.random.choice(domains)

        if not domain.startswith('@'):
            domain = '@' + domain

        if unique:
            name = self.random.randstr(unique)
        else:
            name = self.username(template='ld')

        return '{name}{domain}'.format(
            name=name,
            domain=domain,
        )

    def social_media_profile(self,
                             site: Optional[SocialNetwork] = None) -> str:
        """Generate profile for random social network.

        :return: Profile in some network.

        :Example:
            http://facebook.com/some_user
        """
        key = self._validate_enum(site, SocialNetwork)
        website = SOCIAL_NETWORKS[key]
        url = 'https://' + website
        return url.format(self.username())

    def gender(self, iso5218: bool = False,
               symbol: bool = False) -> Union[str, int]:
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

        return self.random.choice(self._data['gender'])

    def sex(self, *args, **kwargs):
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
        return '{:0.2f}'.format(h)

    def weight(self, minimum: int = 38, maximum: int = 90) -> int:
        """Generate a random weight in Kg.

        :param minimum: min value
        :param maximum: max value
        :return: Weight.

        :Example:
            48.
        """
        weight = self.random.randint(minimum, maximum)
        return weight

    def blood_type(self) -> str:
        """Get a random blood type.

        :return: Blood type (blood group).

        :Example:
            A+
        """
        return self.random.choice(BLOOD_GROUPS)

    def sexual_orientation(self, symbol: bool = False) -> str:
        """Get a random sexual orientation.

        Obviously, this option will be useful for various
        dating sites and so on.

        :param symbol: Unicode symbol.
        :return: Sexual orientation.

        :Example:
            Heterosexuality.
        """
        if symbol:
            return self.random.choice(SEXUALITY_SYMBOLS)

        sexuality = self._data['sexuality']
        return self.random.choice(sexuality)

    def occupation(self) -> str:
        """Get a random job.

        :return: The name of job.

        :Example:
            Programmer.
        """
        jobs = self._data['occupation']
        return self.random.choice(jobs)

    def political_views(self) -> str:
        """Get a random political views.

        :return: Political views.

        :Example:
            Liberal.
        """
        views = self._data['political_views']
        return self.random.choice(views)

    def worldview(self) -> str:
        """Get a random worldview.

        :return: Worldview.

        :Example:
            Pantheism.
        """
        views = self._data['worldview']
        return self.random.choice(views)

    def views_on(self) -> str:
        """Get a random views on.

        :return: Views on.

        :Example:
            Negative.
        """
        views = self._data['views_on']
        return self.random.choice(views)

    def nationality(self, gender: Optional[Gender] = None) -> str:
        """Get a random nationality.

        :param gender: Gender.
        :return: Nationality.

        :Example:
            Russian
        """
        nationalities = self._data['nationality']

        # Separated by gender
        if isinstance(nationalities, dict):
            key = self._validate_enum(gender, Gender)
            nationalities = nationalities[key]

        return self.random.choice(nationalities)

    def university(self) -> str:
        """Get a random university.

        :return: University name.

        :Example:
            MIT.
        """
        universities = self._data['university']
        return self.random.choice(universities)

    def academic_degree(self) -> str:
        """Get a random academic degree.

        :return: Degree.

        :Example:
            Bachelor.
        """
        degrees = self._data['academic_degree']
        return self.random.choice(degrees)

    def language(self) -> str:
        """Get a random language.

        :return: Random language.

        :Example:
            Irish.
        """
        languages = self._data['language']
        return self.random.choice(languages)

    def telephone(self, mask: str = '', placeholder: str = '#') -> str:
        """Generate a random phone number.

        :param mask: Mask for formatting number.
        :param placeholder: A placeholder for a mask (default is #).
        :return: Phone number.

        :Example:
            +7-(963)-409-11-22.
        """
        if not mask:
            code = self.random.choice(CALLING_CODES)
            default = '{}-(###)-###-####'.format(code)
            masks = self._data.get('telephone_fmt', [default])
            mask = self.random.choice(masks)

        return self.random.custom_code(mask=mask, digit=placeholder)

    def avatar(self, size: int = 256) -> str:
        """Generate a random avatar..

        :param size: Size of avatar.
        :return: Link to avatar.
        """
        url = 'https://api.adorable.io/avatars/{0}/{1}.png'
        return url.format(size, self.password(hashed=True))

    def identifier(self, mask: str = '##-##/##') -> str:
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
