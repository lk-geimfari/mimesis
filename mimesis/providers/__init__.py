# -*- coding: utf-8 -*-

"""Contains all the available data providers."""

from mimesis.providers.address import Address
from mimesis.providers.base import BaseDataProvider, BaseProvider
from mimesis.providers.business import Business
from mimesis.providers.choice import Choice
from mimesis.providers.clothing import Clothing
from mimesis.providers.code import Code
from mimesis.providers.cryptographic import Cryptographic
from mimesis.providers.date import Datetime
from mimesis.providers.development import Development
from mimesis.providers.file import File
from mimesis.providers.food import Food
from mimesis.providers.generic import Generic
from mimesis.providers.hardware import Hardware
from mimesis.providers.internet import Internet
from mimesis.providers.numbers import Numbers
from mimesis.providers.path import Path
from mimesis.providers.payment import Payment
from mimesis.providers.person import Person
from mimesis.providers.science import Science
from mimesis.providers.structure import Structure
from mimesis.providers.text import Text
from mimesis.providers.transport import Transport
from mimesis.providers.units import UnitSystem

__all__ = [
    # The main class:
    'BaseProvider',

    # Data base class:
    'BaseDataProvider',

    # Data providers:
    'Address',
    'Business',
    'Choice',
    'Clothing',
    'Code',
    'Choice',
    'Datetime',
    'Development',
    'File',
    'Food',
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
    'Generic',
]
