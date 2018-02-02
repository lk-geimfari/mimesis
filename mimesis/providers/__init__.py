"""Contains all the available data providers."""

from mimesis.providers.base import BaseProvider, BaseDataProvider
from mimesis.providers.address import Address
from mimesis.providers.business import Business
from mimesis.providers.clothing import ClothingSize
from mimesis.providers.cryptographic import Cryptographic
from mimesis.providers.code import Code
from mimesis.providers.date import Datetime
from mimesis.providers.development import Development
from mimesis.providers.file import File
from mimesis.providers.food import Food
from mimesis.providers.hardware import Hardware
from mimesis.providers.internet import Internet
from mimesis.providers.numbers import Numbers
from mimesis.providers.path import Path
from mimesis.providers.person import Person
from mimesis.providers.payment import Payment
from mimesis.providers.science import Science
from mimesis.providers.structure import Structure
from mimesis.providers.text import Text
from mimesis.providers.transport import Transport
from mimesis.providers.units import UnitSystem
from mimesis.providers.games import Games
from mimesis.providers.generic import Generic

__all__ = [
    # The main class:
    'BaseProvider',

    # Data base class:
    'BaseDataProvider',

    # And data providers:
    'Address',
    'Business',
    'ClothingSize',
    'Code',
    'Datetime',
    'Development',
    'File',
    'Food',
    'Games',
    'Hardware',
    'Internet',
    'Numbers',
    'Path',
    'Payment',
    'Person',
    'Science',
    'Structure',
    'Text',
    'Transport',
    'UnitSystem',
    'Cryptographic',

    # Has all:
    'Generic',
]
