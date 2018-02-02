"""Implements enums for a lot of methods.

Enums from this module are used in a lot of methods.
You should always import enums from this module if you want
behavior for the methods that differ from the default behavior.

You should never use your own enums in methods because in this case,
there no guarantee that you will get the result which you actually expected.

Below you can see an example of usage enums in methods of data providers.

Example:
    >>> from mimesis import Person
    >>> from mimesis.enums import Gender
    >>> person = Person()
    >>> person.full_name(gender=Gender.FEMALE)
    'Antonetta Garrison'
"""

from enum import Enum


class PortRange(Enum):
    """Represents port ranges.

    Value for a method ``Internet.port()`` which
    takes parameter ``port_range``.
    """

    ALL = (1, 65535)
    WELL_KNOWN = (1, 1023)
    EPHEMERAL = (49152, 65535)
    REGISTERED = (1024, 49151)


class Gender(Enum):
    """Represents genders.

    Value for a lot of methods which
    takes argument ``gender``.
    """

    FEMALE = 'female'
    MALE = 'male'


class TitleType(Enum):
    """Represents title types.

    Value for a method ``Person.title()`` which
    takes parameter``title_type``.
    """

    TYPICAL = 'typical'
    ACADEMIC = 'academic'


class CardType(Enum):
    """Provides cart types.

    Value for a method ``Payment.credit_card_number()`` which
    takes parameter ``card_type``.
    """

    MASTER_CARD = 'MasterCard'
    VISA = 'Visa'
    AMERICAN_EXPRESS = 'American Express'


class Algorithm(Enum):
    """Provides algorithms which available.

    Value for methods which take argument ``algorithm``.
    """

    MD5 = 'md5'
    SHA1 = 'sha1'
    SHA224 = 'sha224'
    SHA256 = 'sha256'
    SHA384 = 'sha384'
    SHA512 = 'sha512'


class TLDType(Enum):
    """Provides top level domain types.

    Value for a method ``Internet.top_level_domain()``
    which takes parameter ``tld_type``.
    """

    CCTLD = 'cctld'
    GTLD = 'gtld'
    GEOTLD = 'geotld'
    UTLD = 'utld'
    STLD = 'stld'


class Layer(Enum):
    """Provides network protocol layers.

    Value for method ``Internet.network_protocol()`` which
    takes parameter ``layer``.
    """

    APPLICATION = 'application'
    DATA_LINK = 'data_link'
    NETWORK = 'network'
    PHYSICAL = 'physical'
    PRESENTATION = 'presentation'
    SESSION = 'session'
    TRANSPORT = 'transport'


class FileType(Enum):
    """Provides file types.

    Value for methods which takes parameter ``file_type``.
    """

    SOURCE = 'source'
    TEXT = 'text'
    DATA = 'data'
    AUDIO = 'audio'
    VIDEO = 'video'
    IMAGE = 'image'
    EXECUTABLE = 'executable'
    COMPRESSED = 'compressed'


class MimeType(Enum):
    """Provides common mime types.

    Value for method ``File.mime_type()`` which
    takes parameter ``type_``.
    """

    APPLICATION = 'application'
    AUDIO = 'audio'
    IMAGE = 'image'
    MESSAGE = 'message'
    TEXT = 'text'
    VIDEO = 'video'


class PrefixSign(Enum):
    """Provides prefix signs.

    Value for method ``UnitSystem.prefix()`` which
    takes parameter ``sign``.
    """

    POSITIVE = 'positive'
    NEGATIVE = 'negative'


class CountryCode(Enum):
    """Provides types of country codes.

    Value for method ``Address.country_code()`` which
    takes parameter ``fmt``.
    """

    A2 = 'a2'
    A3 = 'a3'
    NUMERIC = 'numeric'
    IOC = 'ioc'
    FIFA = 'fifa'


class ISBNFormat(Enum):
    """Provides formats of ISBN.

    Value for method ``Code.isbn()`` which
    takes parameter ``fmt``.
    """

    ISBN13 = 'isbn-13'
    ISBN10 = 'isbn-10'


class EANFormat(Enum):
    """Provides formats of EAN.

    Value for method ``Code.ean()`` which
    takes parameter ``fmt``.
    """

    EAN8 = 'ean-8'
    EAN13 = 'ean-13'


class SocialNetwork(Enum):
    """Provides most popular social networks.

    Value for method ``Person.social_media_profile()`` which
    takes parameter ``site``.
    """

    FACEBOOK = 'facebook'
    TWITTER = 'twitter'
    INSTAGRAM = 'instagram'
    VK = 'vk'


class UnitName(Enum):
    """Provide unit names.

    Value for method ``UnitSystem.unit()`` which
    takes parameter ``name``.
    """

    MASS = ('gram', 'gr')
    INFORMATION = ('byte', 'b')
    THERMODYNAMIC_TEMPERATURE = ('kelvin', 'K')
    AMOUNT_OF_SUBSTANCE = ('mole', 'mol')
    ANGLE = ('radian', 'r')
    SOLID_ANGLE = ('steradian', '㏛')
    FREQUENCY = ('hertz', 'Hz')
    FORCE = ('newton', 'N')
    PRESSURE = ('pascal', 'P')
    ENERGY = ('joule', 'J')
    POWER = ('watt', 'W')
    FLUX = ('watt', 'W')
    ELECTRIC_CHARGE = ('coulomb', 'C')
    VOLTAGE = ('volt', 'V')
    ELECTRIC_CAPACITANCE = ('farad', 'F')
    ELECTRIC_RESISTANCE = ('ohm', 'Ω')
    ELECTRICAL_CONDUCTANCE = ('siemens', 'S')
    MAGNETIC_FLUX = ('weber', 'Wb')
    MAGNETIC_FLUX_DENSITY = ('tesla', 'T')
    INDUCTANCE = ('henry', 'H')
    TEMPERATURE = ('Celsius', '°C')
    RADIOACTIVITY = ('becquerel', 'Bq')
