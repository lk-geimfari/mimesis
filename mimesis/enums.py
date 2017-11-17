from enum import Enum, EnumMeta
from random import choice


class clsproperty(object):
    """Based on answer from StackOverFlow.
    """

    def __init__(self, mget):
        self.mget = mget

    def __get__(self, obj, klass=None):
        if klass is None:
            klass = type(obj)
        return self.mget.__get__(obj, klass)()

    def __set__(self, obj, value):
        raise AttributeError("Can't set attribute")


class AllowRandom(EnumMeta):
    """This metaclass allows an attribute `RANDOM` which
    equal to random field of enum for his subclasses.
    """

    @clsproperty
    def RANDOM(self) -> Enum:
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
