from enum import Enum, EnumMeta
from random import choice
from typing import Any


class AllowRandom(EnumMeta):
    """This metaclass allows method ``get_random_item()`` which
    returns random field of enum.
    """

    def get_random_item(self) -> Any:
        return choice(list(self))


class PortRange(Enum):
    """Value for a method ``Internet.port()`` which
    takes parameter``port_range``.

    Example:

    >>> internet.port(port_range=PortRange.REGISTERED)
    '8080'
    """
    ALL = (1, 65535)
    WELL_KNOWN = (1, 1023)
    EPHEMERAL = (49152, 65535)
    REGISTERED = (1024, 49151)


class Gender(Enum, metaclass=AllowRandom):
    """Value for a lot of methods which
    takes argument ``gender``.

    Example:

    >>> personal.full_name(gender=Gender.FEMALE)
    'Jessica Larson'
    """
    FEMALE = 'female'
    MALE = 'male'


class TitleType(Enum, metaclass=AllowRandom):
    """Value for a method ``Personal.title()`` which
    takes parameter``title_type``.

    Example:

    >>> personal.title(title_type=TitleType.TYPICAL)
    'Mr.'
    """
    TYPICAL = 'typical'
    ACADEMIC = 'academic'


class CardType(Enum, metaclass=AllowRandom):
    """Value for a method ``Payment.credit_card_number()`` which
    takes parameter ``card_type``.

    Example:

    >>> payment.credit_card_number(card_type=CardType.VISA)
    '4116 9018 7744 0125'
    """
    MASTER_CARD = 'MasterCard'
    VISA = 'Visa'
    AMERICAN_EXPRESS = 'American Express'


class Algorithm(Enum, metaclass=AllowRandom):
    """Value for methods which take argument ``algorithm``.

    Example:

    >>> cryptographic.hash(algorithm=Algorithm.MD5)
    '6023658e8cc9c97edfd51cf2fabf1faf'
    """
    MD5 = 'md5'
    SHA1 = 'sha1'
    SHA224 = 'sha224'
    SHA256 = 'sha256'
    SHA384 = 'sha384'
    SHA512 = 'sha512'


class TLDType(Enum, metaclass=AllowRandom):
    """Value for a method ``Internet.top_level_domain()`` which
    takes parameter ``tld_type``.

    Example:

    >>> internet.top_level_domain(tld_type=TLDType.GEOTLD)
    '.moscow'
    """
    CCTLD = 'cctld'
    GTLD = 'gtld'
    GEOTLD = 'geotld'
    UTLD = 'utld'
    STLD = 'stld'


class Layer(Enum, metaclass=AllowRandom):
    """Value for method ``Internet.network_protocol()`` which
    takes parameter ``layer``.

    Example:

    >>> internet.network_protocol(layer=Layer.APPLICATION)
    'BitTorrent'
    """
    APPLICATION = 'application'
    DATA_LINK = 'data_link'
    NETWORK = 'network'
    PHYSICAL = 'physical'
    PRESENTATION = 'presentation'
    SESSION = 'session'
    TRANSPORT = 'transport'


class FileType(Enum, metaclass=AllowRandom):
    """Value for methods which takes parameter ``file_type``.

    Example:

    >>> file.extension(file_type=FileType.SOURCE)
    '.py'
    """
    SOURCE = 'source'
    TEXT = 'text'
    DATA = 'data'
    AUDIO = 'audio'
    VIDEO = 'video'
    IMAGE = 'image'
    EXECUTABLE = 'executable'
    COMPRESSED = 'compressed'


class MimeType(Enum, metaclass=AllowRandom):
    """Value for method ``File.mime_type()`` which
    takes parameter ``type_``.

    Example:

    >>> file.mime_type(type_=MimeType.APPLICATION)
    'application/alto-directory+json'
    """
    APPLICATION = 'application'
    AUDIO = 'audio'
    IMAGE = 'image'
    MESSAGE = 'message'
    TEXT = 'text'
    VIDEO = 'video'


class PrefixSign(Enum, metaclass=AllowRandom):
    """Value for method ``UnitSystem.prefix()`` which
    takes parameter ``sign``.

    Example:

    >>> unitsystem.prefix(sign=PrefixSign.NEGATIVE)
    'yocto'
    """
    POSITIVE = 'positive'
    NEGATIVE = 'negative'


class CountryCode(Enum, metaclass=AllowRandom):
    """Value for method ``Address.country_iso_code()`` which
    takes parameter ``fmt``.

    Example:

    >>> address.country_iso_code(fmt=CountryCode.ISO3)
    'AND'
    """
    ISO2 = 'iso2'
    ISO3 = 'iso3'
    NUMERIC = 'numeric'


class ISBNFormat(Enum, metaclass=AllowRandom):
    """Value for method ``Code.isbn()`` which
    takes parameter ``fmt``.

    Example:

    >>> code.isbn(fmt=ISBNFormat.ISBN10)
    '1-64396-236-2'
    """
    ISBN13 = 'isbn-13'
    ISBN10 = 'isbn-10'


class EANFormat(Enum, metaclass=AllowRandom):
    """Value for method ``Code.ean()`` which
    takes parameter ``fmt``.

    Example:

    >>> code.ean(fmt=EANFormat.EAN8)
    '09959590'
    """
    EAN8 = 'ean-8'
    EAN13 = 'ean-13'


class SocialNetwork(Enum, metaclass=AllowRandom):
    """Value for method ``Personal.social_media_profile()`` which
    takes parameter ``site``.

    Example:

    >>> personal.social_media_profile(site=SocialNetwork.INSTAGRAM)
    'https://www.instagram.com/cacara_1844'
    """
    FACEBOOK = 'facebook'
    TWITTER = 'twitter'
    INSTAGRAM = 'instagram'
    VK = 'vk'


class UnitName(Enum, metaclass=AllowRandom):
    """Value for method ``UnitSystem.unit()`` which
    takes parameter ``name``.

    Example:

    >>> unitsystem.unit(name=UnitName.MASS)
    'gramm'
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
