from enum import Enum, EnumMeta
from random import choice
from typing import Any


class AllowRandom(EnumMeta):
    """This metaclass allow method get_random_item() which
    equal to random field of enum for his subclasses.
    """

    def get_random_item(self) -> Any:
        return choice(list(self))


class PortRange(Enum):
    ALL = (1, 65535)
    WELL_KNOWN = (1, 1023)
    EPHEMERAL = (49152, 65535)
    REGISTERED = (1024, 49151)


class Gender(Enum, metaclass=AllowRandom):
    FEMALE = 'female'
    MALE = 'male'


class TitleType(Enum, metaclass=AllowRandom):
    TYPICAL = 'typical'
    ACADEMIC = 'academic'


class CardType(Enum, metaclass=AllowRandom):
    MASTER_CARD = 'MasterCard'
    VISA = 'Visa'
    AMERICAN_EXPRESS = 'American Express'


class Algorithm(Enum, metaclass=AllowRandom):
    MD5 = 'md5'
    SHA1 = 'sha1'
    SHA224 = 'sha224'
    SHA256 = 'sha256'
    SHA384 = 'sha384'
    SHA512 = 'sha512'


class TLDType(Enum, metaclass=AllowRandom):
    CCTLD = 'cctld'
    GTLD = 'gtld'
    GEOTLD = 'geotld'
    UTLD = 'utld'
    STLD = 'stld'


class Layer(Enum, metaclass=AllowRandom):
    APPLICATION = 'application'
    DATA_LINK = 'data_link'
    NETWORK = 'network'
    PHYSICAL = 'physical'
    PRESENTATION = 'presentation'
    SESSION = 'session'
    TRANSPORT = 'transport'


class FileType(Enum, metaclass=AllowRandom):
    SOURCE = 'source'
    TEXT = 'text'
    DATA = 'data'
    AUDIO = 'audio'
    VIDEO = 'video'
    IMAGE = 'image'
    EXECUTABLE = 'executable'
    COMPRESSED = 'compressed'


class MimeType(Enum, metaclass=AllowRandom):
    APPLICATION = 'application'
    AUDIO = 'audio'
    IMAGE = 'image'
    MESSAGE = 'message'
    TEXT = 'text'
    VIDEO = 'video'


class PrefixSign(Enum, metaclass=AllowRandom):
    POSITIVE = 'positive'
    NEGATIVE = 'negative'


class CountryCode(Enum, metaclass=AllowRandom):
    ISO2 = 'iso2'
    ISO3 = 'iso3'
    NUMERIC = 'numeric'


class ISBNFormat(Enum, metaclass=AllowRandom):
    ISBN13 = 'isbn-13'
    ISBN10 = 'isbn-10'


class EANFormat(Enum, metaclass=AllowRandom):
    EAN8 = 'ean-8'
    EAN13 = 'ean-13'


class SocialNetwork(Enum, metaclass=AllowRandom):
    FACEBOOK = 'facebook'
    TWITTER = 'twitter'
    INSTAGRAM = 'instagram'
    VK = 'vk'


class UnitName(Enum, metaclass=AllowRandom):
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
