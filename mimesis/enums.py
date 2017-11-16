from enum import Enum
from random import choice


class PortRange(Enum):
    DEFAULT = (1, 65535)
    WELL_KNOWN = (1, 1023)
    EPHEMERAL = (49152, 65535)
    REGISTERED = (1024, 49151)


class Gender(Enum):
    FEMALE = 'female'
    MALE = 'male'
    RANDOM = choice([FEMALE, MALE])


class TitleType(Enum):
    TYPICAL = 'typical'
    ACADEMIC = 'academic'
    RANDOM = choice([TYPICAL, ACADEMIC])
