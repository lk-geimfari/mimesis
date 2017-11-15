import re
from string import ascii_letters, digits, punctuation
from typing import Union

from mimesis.data import (CALLING_CODES, BLOOD_GROUPS, EMAIL_DOMAINS,
                          ENGLISH_LEVEL, FAVORITE_MUSIC_GENRE, GENDER_SYMBOLS,
                          SEXUALITY_SYMBOLS, USERNAMES)
from mimesis.exceptions import WrongArgument
from mimesis.providers.base import BaseProvider
from mimesis.providers.cryptographic import Cryptographic
from mimesis.config import SURNAMES_SEPARATED_BY_GENDER
from mimesis.utils import check_gender, luhn_checksum, pull, custom_code
from mimesis.typing import Gender

__all__ = ['Personal']


class Personal(BaseProvider):
    """Class for generate personal data, i.e names, surnames,
    age and another."""

    def __init__(self, *args, **kwargs):
        """
        :param str locale: Current locale.
        """
        super().__init__(*args, **kwargs)
        self.data = pull('personal.json', self.locale)
        self._store = {
            'age': 0,
        }

    def age(self, minimum: int = 16, maximum: int = 66) -> int:
        """Get a random integer value.

        :param int maximum: Maximum value of age.
        :param int minimum: Minimum value of age.
        :return: Random integer.

        :Example:
            23.
        """
        a = self.random.randint(int(minimum), int(maximum))
        self._store['age'] = a
        return a

    def child_count(self, max_childs: int = 5) -> int:
        """Get a count of child's.

        :param int max_childs: Maximum count of child's.
        :return: Ints. Depend on previous generated age.
        """
        a = self._store['age']
        if a == 0:
            a = self.age()

        cc = 0 if a < 18 else self.random.randint(0, max_childs)
        return cc

    def work_experience(self, working_start_age: int = 22) -> int:
        """Get a work experience.

        :param int working_start_age: Age then person start to work.
        :return: Int. Depend on previous generated age.
        """
        a = self._store['age']
        if a == 0:
            a = self.age()

        return max(a - working_start_age, 0)

    def name(self, gender: Gender = 0) -> str:
        """Get a random name.

        :param gender: if 'male' then will returned male name,
            if 'female' then female name,  if None return random from ones.
        :type gender: int or str
        :return: Name.

        :Example:
            John.
        """
        gender = check_gender(gender)
        names = self.data['names'].get(gender)
        return self.random.choice(names)

    def surname(self, gender: Gender = 0) -> str:
        """Get a random surname.

        :param gender: The gender of person.
        :type gender: int of str
        :return: Surname.

        :Example:
            Smith.
        """
        surnames = self.data['surnames']

        # Separated by gender.
        if self.locale in SURNAMES_SEPARATED_BY_GENDER:
            gender = check_gender(gender)
            return self.random.choice(
                surnames.get(gender),
            )

        return self.random.choice(surnames)

    def last_name(self, gender: Gender = 0) -> str:
        return self.surname(gender)

    def title(self, gender: Gender = 0,
              title_type: str = 'typical') -> str:
        """Get a random title (prefix/suffix) for name.

        :param gender: The gender.
        :type gender: int or str
        :param str title_type:  The type of title ('typical' and 'academic').
        :return: The title.
        :raises WrongArgument: if gender in incorrect format.

        :Example:
            PhD.
        """
        try:
            gender = check_gender(gender)
            titles = self.data['title'].get(
                gender).get(title_type)
        except KeyError:
            raise WrongArgument('Wrong value of argument.')

        title = self.random.choice(titles)
        return title

    def full_name(self, gender: Gender = 0, reverse: bool = False) -> str:
        """Generate a random full name.

        :param bool reverse: Return reversed full name.
        :param gender: Gender.
        :type gender: int or str
        :return: Full name.

        :Example:
            Johann Wolfgang.
        """
        gender = check_gender(gender)

        fmt = '{1} {0}' if reverse else '{0} {1}'
        return fmt.format(
            self.name(gender),
            self.surname(gender),
        )

    def username(self, template: str = '') -> str:
        """Generate username by template.

        :param str template: Template ('U_d', 'U.d', 'U-d', 'ld', 'l-d', 'Ud',
            'l.d', 'l_d', 'default')
        :return: Username.
        :raises WrongArgument: if template is not supported.

        :Example:
            Celloid1873
        """
        name = self.random.choice(USERNAMES)
        date = self.random.randint(1800, 2070)

        templates = {
            # UppercaseDate
            'Ud': '{U}{d}'.format(
                U=name.capitalize(),
                d=date,
            ),
            # Uppercase.Date
            'U.d': '{U}.{d}'.format(
                U=name.capitalize(),
                d=date,
            ),
            # lowercaseDate
            'ld': '{l}{d}'.format(
                l=name,
                d=date,
            ),
            # Uppercase-date
            'U-d': '{U}-{d}'.format(
                U=name.title(),
                d=date,
            ),
            # Uppercase_date
            'U_d': '{U}_{d}'.format(
                U=name.title(),
                d=date,
            ),
            # lowercase-date
            'l-d': '{l}-{d}'.format(
                l=name,
                d=date,
            ),
            # lowercase_date
            'l_d': '{l}_{d}'.format(
                l=name,
                d=date,
            ),
            # lowercase.date
            'l.d': '{l}.{d}'.format(
                l=name,
                d=date,
            ),
            # Default is ld
            'default': '{l}{d}'.format(
                l=name,
                d=date,
            ),
        }

        supported = list(templates.keys())

        if template:
            try:
                return templates[template]
            except KeyError:
                raise WrongArgument(
                    'Unsupported template {unsupported}.'
                    'Use one of: {supported}'.format(
                        unsupported=template,
                        supported=', '.join(supported),
                    ),
                )

        templ = self.random.choice(supported)
        return templates[templ]

    def password(self, length: int = 8, algorithm: str = None) -> str:
        """Generate a password or hash of password.

        :param int length: Length of password.
        :param str algorithm: Hashing algorithm.
        :return: Password or hash of password.

        :Example:
            k6dv2odff9#4h (without hashing).
        """
        text = ascii_letters + digits + punctuation
        password = ''.join([self.random.choice(text) for _ in range(length)])

        if algorithm is not None:
            crypto = Cryptographic()
            return crypto.hash(algorithm)

        return password

    def email(self, domains: Union[tuple, list] = None) -> str:
        """Generate a random email.

        :param domains: List of custom domains for emails.
        :type domains: list or tuple
        :return: Email address.

        :Example:
            foretime10@live.com
        """
        if not domains:
            domains = EMAIL_DOMAINS

        domain = self.random.choice(domains)
        name = self.username(template='ld')
        return '{name}{domain}'.format(
            name=name,
            domain=domain,
        )

    def bitcoin(self) -> str:
        """Generate a random bitcoin address.

        :return: Bitcoin address.

        :Example:
            3EktnHQD7RiAE6uzMj2ZifT9YgRrkSgzQX
        """
        letters = ascii_letters + digits
        address = [self.random.choice(letters) for _ in range(33)]
        return '3' + ''.join(address)

    def cvv(self) -> int:
        """Generate a random card verification value (CVV).

        :return: CVV code.

        :Example:
            324
        """
        return self.random.randint(100, 999)

    def credit_card_number(self, card_type: str = 'visa') -> str:
        """Generate a random credit card number.

        :param str card_type: Issuing Network. Default is Visa.
        :return: Credit card number.
        :raises NotImplementedError: if cart_type is not supported.

        :Example:
            4455 5299 1152 2450
        """
        length = 16
        regex = re.compile('(\d{4})(\d{4})(\d{4})(\d{4})')

        if card_type in ('visa', 'vi', 'v'):
            number = self.random.randint(4000, 4999)
        elif card_type in ('master_card', 'mc', 'master', 'm'):
            number = self.random.choice([self.random.randint(2221, 2720),
                                         self.random.randint(5100, 5500)])
        elif card_type in ('american_express', 'amex', 'ax', 'a'):
            number = self.random.choice([34, 37])
            length = 15
            regex = re.compile('(\d{4})(\d{6})(\d{5})')
        else:
            raise NotImplementedError(
                'Card type {} is not supported.'.format(card_type))

        str_num = str(number)
        while len(str_num) < length - 1:
            str_num += self.random.choice(digits)

        groups = regex.search(str_num + luhn_checksum(str_num))
        card = ' '.join(groups.groups())
        return card

    def credit_card_expiration_date(self, minimum: int = 16,
                                    maximum: int = 25) -> str:
        """Generate a random expiration date for credit card.

        :param int minimum: Date of issue.
        :param int maximum: Maximum of expiration_date.
        :return: Expiration date of credit card.

        :Example:
            03/19.
        """
        month = self.random.randint(1, 12)
        year = self.random.randint(minimum, maximum)
        return '{0:02d}/{1}'.format(month, year)

    def cid(self) -> int:
        """Generate a random CID code.

        :return: CID code.

        :Example:
            7452
        """
        return self.random.randint(1000, 9999)

    def paypal(self) -> str:
        """Generate a random PayPal account.

        :return: Email of PapPal user.

        :Example:
            wolf235@gmail.com
        """
        return self.email()

    def social_media_profile(self) -> str:
        """Generate profile for random social network.

        :return: Profile in some network.

        :Example:
            http://facebook.com/some_user
        """
        urls = [
            'facebook.com/{}',
            'twitter.com/{}',
            'medium.com/@{}',
        ]
        url = 'http://' + self.random.choice(urls)
        username = self.username(template='U_d')

        return url.format(username)

    def gender(self, iso5218: bool = False,
               symbol: bool = False) -> Union[str, int]:
        """Get a random title of gender, code for the representation
        of human sexes is an international standard that defines a
        representation of human sexes through a language-neutral single-digit
        code or symbol of gender.

        :param bool iso5218:
            Codes for the representation of human sexes is an international
            standard.
        :param bool symbol: Symbol of gender.
        :return: Title of gender.
        :rtype: str or int

        :Example:
            Male
        """
        # The four codes specified in ISO/IEC 5218 are:
        #     0 = not known,
        #     1 = male,
        #     2 = female,
        #     9 = not applicable.
        codes = [0, 1, 2, 9]

        if iso5218:
            return self.random.choice(codes)

        if symbol:
            return self.random.choice(GENDER_SYMBOLS)

        gender = self.random.choice(self.data['gender'])
        return gender

    def height(self, minimum: float = 1.5, maximum: float = 2.0) -> str:
        """Generate a random height in M (Meter).

        :param float minimum: Minimum value.
        :param float maximum: Maximum value.
        :return: Height.

        :Example:
            1.85.
        """
        h = self.random.uniform(minimum, maximum)
        return '{:0.2f}'.format(h)

    def weight(self, minimum: int = 38, maximum: int = 90) -> int:
        """Generate a random weight in Kg.

        :param int minimum: min value
        :param int maximum: max value
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
        """Get a random (LOL) sexual orientation.

        :param bool symbol: Unicode symbol.
        :return: Sexual orientation.

        :Example:
            Heterosexuality.
        """
        if symbol:
            return self.random.choice(SEXUALITY_SYMBOLS)

        sexuality = self.data['sexuality']
        return self.random.choice(sexuality)

    def occupation(self) -> str:
        """Get a random job.

        :return: The name of job.

        :Example:
            Programmer.
        """
        jobs = self.data['occupation']
        return self.random.choice(jobs)

    def political_views(self) -> str:
        """Get a random political views.

        :return: Political views.

        :Example:
            Liberal.
        """
        views = self.data['political_views']
        return self.random.choice(views)

    def worldview(self) -> str:
        """Get a random worldview.

        :return: Worldview.

        :Example:
            Pantheism.
        """
        views = self.data['worldview']
        return self.random.choice(views)

    def views_on(self) -> str:
        """
        Get a random views on.

        :return: Views on.

        :Example:
            Negative.
        """
        views = self.data['views_on']
        return self.random.choice(views)

    def nationality(self, gender: Gender = 0) -> str:
        """Get a random nationality.

        :param gender: Gender.
        :type gender: str or int
        :return: Nationality.

        :Example:
            Russian.
        """
        # Subtleties of the orthography.
        separated_locales = ['cs', 'ru', 'uk', 'kk']

        nationalities = self.data['nationality']

        if self.locale in separated_locales:
            gender = check_gender(gender)
            nations = nationalities[gender]
            return self.random.choice(nations)

        return self.random.choice(nationalities)

    def university(self) -> str:
        """Get a random university.

        :return: University name.

        :Example:
            MIT.
        """
        universities = self.data['university']
        return self.random.choice(universities)

    def academic_degree(self) -> str:
        """Get a random academic degree.

        :return: Degree.

        :Example:
            Bachelor.
        """
        degrees = self.data['academic_degree']
        return self.random.choice(degrees)

    def language(self) -> str:
        """Get a random language.

        :return: Random language.

        :Example:
            Irish.
        """
        languages = self.data['language']
        return self.random.choice(languages)

    def favorite_movie(self) -> str:
        """Get a random movie for current locale.

        :return: The name of the movie.

        :Example:
            Interstellar.
        """
        movies = self.data['favorite_movie']
        return self.random.choice(movies)

    def favorite_music_genre(self) -> str:
        """Get a random music genre.

        :return: A music genre.

        :Example:
            Ambient.
        """
        return self.random.choice(FAVORITE_MUSIC_GENRE)

    def telephone(self, mask: str = '', placeholder: str = '#') -> str:
        """Generate a random phone number.

        :param str mask: Mask for formatting number.
        :param str placeholder: A placeholder for a mask (default is #).
        :return: Phone number.

        :Example:
            +7-(963)-409-11-22.
        """
        if not mask:
            code = self.random.choice(CALLING_CODES)
            default = [
                '{}-(###)-###-####'.format(code),
            ]

            masks = self.data.get('telephone_fmt', default)
            mask = self.random.choice(masks)

        return custom_code(mask=mask, digit=placeholder)

    def avatar(self, size: int = 256) -> str:
        """Generate a random avatar (link to avatar) using API of  Adorable.io.

        :param int size: Size of avatar.
        :return: Link to avatar.
        """
        url = 'https://api.adorable.io/avatars/{0}/{1}.png'
        return url.format(size, self.password(algorithm='md5'))

    @staticmethod
    def identifier(mask: str = '##-##/##') -> str:
        """Generate a random identifier by mask. With this method you can generate
        any identifiers that you need. Simply select the mask that you need.

        :param str mask:
            The mask. Here '@' is a placeholder for characters and '#' is
            placeholder for digits.
        :return: An identifier.

        :Example:
            07-97/04
        """
        return custom_code(mask=mask)

    def level_of_english(self) -> str:
        """Get a random level of English.

        :return: Level of english.

        :Example:
            Intermediate.
        """
        return self.random.choice(ENGLISH_LEVEL)
