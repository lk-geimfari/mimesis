from enum import Enum, EnumMeta
import random

from mimesis.data import GENDER_SYMBOLS


class AllowRandom(EnumMeta):
    """This metaclass allow method get_random_item() which
    equal to random field of enum for his subclasses.
    """

    def get_random_item(self):
        return random.choice(list(self))


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
