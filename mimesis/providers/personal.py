import re
from string import ascii_letters, digits, punctuation

from mimesis.data import (BLOOD_GROUPS, EMAIL_DOMAINS, ENGLISH_LEVEL,
                          FAVORITE_MUSIC_GENRE, GENDER_SYMBOLS,
                          SEXUALITY_SYMBOLS, USERNAMES)
from mimesis.exceptions import WrongArgument
from mimesis.providers import BaseProvider, Code
from mimesis.providers.cryptographic import Cryptographic
from mimesis.settings import SURNAMES_SEPARATED_BY_GENDER
from mimesis.utils import luhn_checksum, pull

__all__ = ['Personal']


class Personal(BaseProvider):
    """Class for generate personal data, i.e names, surnames,
    age and another."""

    def __init__(self, *args, **kwargs):
        """
        :param locale: Current locale.
        """
        super().__init__(*args, **kwargs)
        self.data = pull('personal.json', self.locale)
        self._store = {
            'age': 0,
        }

    def age(self, minimum=16, maximum=66):
        """Get a random integer value.

        :param maximum: max age
        :param minimum: min age
        :return: Random integer (from minimum=16 to maximum=66)
        :Example:
            23.
        """
        a = self.random.randint(int(minimum), int(maximum))
        self._store['age'] = a
        return a

    def child_count(self, max_childs=5):
        """Get a count of child's.

        :param max_childs: Maximum count of child's.
        :return: Ints. Depend on previous generated age.
        """
        a = self._store['age']
        if a == 0:
            a = self.age()

        cc = 0 if a < 18 else self.random.randint(0, max_childs)
        return cc

    def work_experience(self, working_start_age=22):
        """Get a work experience.

        :param working_start_age: Age then person start to work.
        :return: Int. Depend on previous generated age.
        """
        a = self._store['age']
        if a == 0:
            a = self.age()

        return max(a - working_start_age, 0)

    def name(self, gender='female'):
        """Get a random name.

        :param gender: if 'male' then will getting male name else female name.
        :return: Name.
        :Example:
            John.
        """
        # TODO: Add function for checking gender.
        try:
            names = self.data['names'][gender]
        except KeyError:
            raise WrongArgument('gender must be "female" or "male"')
        return self.random.choice(names)

    def surname(self, gender='female'):
        """Get a random surname.

        :param gender: The gender of person.
        :return: Surname.
        :Example:
            Smith.
        """
        # Separated by gender.
        if self.locale in SURNAMES_SEPARATED_BY_GENDER:
            try:
                return self.random.choice(self.data['surnames'][gender])
            except KeyError:
                raise WrongArgument('gender must be "female" or "male"')

        surname = self.random.choice(self.data['surnames'])
        return surname

    def title(self, gender='female', title_type='typical'):
        """Get a random title (prefix/suffix) for name.

        :param gender: The gender.
        :param title_type:  The type of title ('typical' and 'academic').
        :return: The title.
        :Example:
            PhD.
        """
        try:
            titles = self.data['title'][gender][title_type]
        except KeyError:
            raise WrongArgument('Wrong value of argument.')

        title = self.random.choice(titles)
        return title

    def full_name(self, gender='female', reverse=False):
        """Generate a random full name.

        :param reverse: if true: surname/name else name/surname
        :param gender: if gender='male' then will be returned male name else
            female name.
        :return: Full name.
        :Example:
            Johann Wolfgang.
        """
        gender = gender.lower()

        fmt = '{1} {0}' if reverse else '{0} {1}'
        return fmt.format(
            self.name(gender),
            self.surname(gender),
        )

    def username(self, template=None):
        """Generate username by template.

        :param template: Template ('U_d', 'U.d', 'U-d', 'ld', 'l-d', 'Ud',
        'l.d', 'l_d', 'default')
        :return: Username.
        :Example:
            Celloid1873
        """
        name = self.random.choice(USERNAMES)
        date = str(self.random.randint(1800, 2070))

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

        if template is not None:
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

    def password(self, length=8, algorithm=None):
        """Generate a password or hash of password.

        :param length: Length of password.
        :param algorithm: Hashing algorithm.
        :return: Password or hash of password.
        :Example:
            k6dv2odff9#4h (without hashing).
        """
        password = ''.join([self.random.choice(
            ascii_letters + digits + punctuation) for _ in range(int(length))])

        if algorithm is not None:
            return Cryptographic().hash(algorithm=algorithm)

        return password

    def email(self, domains=None):
        """Generate a random email.

        :param domains: Custom domain for email.
        :type domains: list, tuple
        :return: Email address.
        :Example:
            foretime10@live.com
        """
        host = domains if domains else EMAIL_DOMAINS

        email = self.username(template='ld') + self.random.choice(host)
        return email

    def bitcoin(self):
        """Generate a random bitcoin address. Currently supported only two
        address formats that are most popular: 'P2PKH' and 'P2SH'

        :return: Bitcoin address.
        :Example:
            3EktnHQD7RiAE6uzMj2ZifT9YgRrkSgzQX
        """
        fmt = self.random.choice(['1', '3'])
        fmt += ''.join([self.random.choice(ascii_letters + digits)
                        for _ in range(33)])
        return fmt

    def cvv(self):
        """Generate a random card verification value (CVV).

        :return: CVV code.
        :rtype: int
        :Example:
            324
        """
        return self.random.randint(100, 999)

    def credit_card_number(self, card_type='visa'):
        """Generate a random credit card number.

        :param card_type: Issuing Network. Default is Visa.
        :return: Credit card number.
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

        number = str(number)
        while len(number) < length - 1:
            number += self.random.choice(digits)

        card = ' '.join(regex.search(number + luhn_checksum(number)).groups())
        return card

    def credit_card_expiration_date(self, minimum=16, maximum=25):
        """Generate a random expiration date for credit card.

        :param minimum: Date of issue.
        :param maximum: Maximum of expiration_date.
        :return: Expiration date of credit card.
        :rtype: str
        :Example:
            03/19.
        """
        month, year = [self.random.randint(1, 12),
                       self.random.randint(minimum, maximum)]
        month = '0' + str(month) if month < 10 else month
        return '{0}/{1}'.format(month, year)

    def cid(self):
        """Generate a random CID code.

        :return: CID code.
        :Example:
            7452
        """
        return self.random.randint(1000, 9999)

    def paypal(self):
        """Generate a random PayPal account.

        :return: Email of PapPal user.
        :Example:
            wolf235@gmail.com
        """
        return self.email()

    def social_media_profile(self):
        """Generate profile for random social network.

        :param gender: Gender of user.
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

    def gender(self, iso5218=False, symbol=False):
        """Get a random title of gender, code for the representation
        of human sexes is an international standard that defines a
        representation of human sexes through a language-neutral single-digit
        code or symbol of gender.

        :param iso5218:
            Codes for the representation of human sexes is an international
            standard.
        :param symbol: Symbol of gender.
        :return: Title of gender.
        :rtype: str
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

    def height(self, minimum=1.5, maximum=2.0):
        """Generate a random height in M (Meter).

        :param minimum: Minimum value.
        :param maximum: Maximum value.
        :return: Height.
        :Example:
            1.85.
        """
        h = self.random.uniform(float(minimum), float(maximum))
        return '{:0.2f}'.format(h)

    def weight(self, minimum=38, maximum=90):
        """Generate a random weight in Kg.

        :param minimum: min value
        :param maximum: max value
        :return: Weight.
        :Example:
            48.
        """
        weight = self.random.randint(int(minimum), int(maximum))
        return weight

    def blood_type(self):
        """Get a random blood type.

        :return: Blood type (blood group).
        :Example:
            A+
        """
        return self.random.choice(BLOOD_GROUPS)

    def sexual_orientation(self, symbol=False):
        """Get a random (LOL) sexual orientation.

        :param symbol: Unicode symbol.
        :return: Sexual orientation.
        :Example:
            Heterosexuality.
        """
        if symbol:
            return self.random.choice(SEXUALITY_SYMBOLS)

        sexuality = self.data['sexuality']
        return self.random.choice(sexuality)

    def occupation(self):
        """Get a random job.

        :return: The name of job.
        :Example:
            Programmer.
        """
        jobs = self.data['occupation']
        return self.random.choice(jobs)

    def political_views(self):
        """Get a random political views.

        :return: Political views.
        :Example:
            Liberal.
        """
        views = self.data['political_views']
        return self.random.choice(views)

    def worldview(self):
        """Get a random worldview.

        :return: Worldview.
        :Example:
            Pantheism.
        """
        views = self.data['worldview']
        return self.random.choice(views)

    def views_on(self):
        """
        Get a random views on.

        :return: Views on.
        :Example:
            Negative.
        """
        views = self.data['views_on']
        return self.random.choice(views)

    def nationality(self, gender='female'):
        """Get a random nationality.

        :param gender: female or male
        :return: Nationality.
        :Example:
            Russian.
        """
        # Subtleties of the orthography.
        separated_locales = ['ru', 'uk', 'kk']

        if self.locale in separated_locales:
            nations = self.data['nationality'][gender]
            return self.random.choice(nations)

        return self.random.choice(self.data['nationality'])

    def university(self):
        """
        Get a random university.

        :return: University name.
        :Example:
            MIT.
        """
        universities = self.data['university']
        return self.random.choice(universities)

    def academic_degree(self):
        """Get a random academic degree.

        :return: Degree.
        :Example:
            Bachelor.
        """
        degrees = self.data['academic_degree']
        return self.random.choice(degrees)

    def language(self):
        """Get a random language.

        :return: Random language.
        :Example:
            Irish.
        """
        languages = self.data['language']
        return self.random.choice(languages)

    def favorite_movie(self):
        """Get a random movie for current locale.

        :return: The name of the movie.
        :Example:
            Interstellar.
        """
        movies = self.data['favorite_movie']
        return self.random.choice(movies)

    def favorite_music_genre(self):
        """Get a random music genre.

        :return: A music genre.
        :Example:
            Ambient.
        """
        return self.random.choice(FAVORITE_MUSIC_GENRE)

    def telephone(self, mask=None, placeholder='#'):
        """Generate a random phone number.

        :param mask: Mask for formatting number.
        :param placeholder: A placeholder for a mask (default is #).
        :return: Phone number.
        :Example:
            +7-(963)-409-11-22.
        """
        # Default
        default = '+#-(###)-###-####'

        if not mask:
            masks = self.data.get('telephone_fmt', default)
            mask = self.random.choice(masks)

        return Code(self.locale).custom_code(mask=mask, digit=placeholder)

    def avatar(self, size=256):
        """Generate a random avatar (link to avatar) using API of  Adorable.io.

        :return: Link to avatar.
        :Example:
            https://api.adorable.io/avatars/64/875ed3de1604812b3c2b592c05863f47.png
        """
        url = 'https://api.adorable.io/avatars/{0}/{1}.png'
        return url.format(size, self.password(algorithm='md5'))

    def identifier(self, mask='##-##/##'):
        """Generate a random identifier by mask. With this method you can generate
        any identifiers that you need. Simply select the mask that you need.

        :param mask:
            The mask. Here '@' is a placeholder for characters and '#' is
            placeholder for digits.
        :return: An identifier.
        :Example:
            07-97/04
        """
        return Code(self.locale).custom_code(mask=mask)

    def level_of_english(self):
        """Get a random level of English.

        :return: Level of english.
        :Example:
            Intermediate.
        """
        return self.random.choice(ENGLISH_LEVEL)
