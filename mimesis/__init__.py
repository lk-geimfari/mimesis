# -*- coding: utf-8 -*-

"""Mimesis is a Python library, which helps generate fake data.

Copyright (c) 2016 - 2020 Isaak Uchakaev (Likid Geimfari)
Repository: https://github.com/lk-geimfari/mimesis
Email: <likid.geimfari@gmail.com>
"""

from .providers import Address
from .providers import BaseDataProvider
from .providers import BaseProvider
from .providers import Business
from .providers import Choice
from .providers import Clothing
from .providers import Code
from .providers import Cryptographic
from .providers import Datetime
from .providers import Development
from .providers import File
from .providers import Food
from .providers import Generic
from .providers import Hardware
from .providers import Internet
from .providers import Numbers
from .providers import Path
from .providers import Payment
from .providers import Person
from .providers import Science
from .providers import Text
from .providers import Transport

__all__ = [
    'Address',
    'BaseDataProvider',
    'BaseProvider',
    'Business',
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
    'Text',
    'Transport',
    'Cryptographic',

    # Has all:
    'Generic',

    # Meta:
    '__version__',
    '__title__',
    '__description__',
    '__url__',
    '__author__',
    '__author_email__',
    '__license__',
]

__version__ = '5.0.0'
__title__ = 'mimesis'
__description__ = 'Mimesis: fake data generator.'
__url__ = 'https://github.com/lk-geimfari/mimesis'
__author__ = 'Isaak Uchakaev (Likid Geimfari)'
__author_email__ = 'likid.geimfari@gmail.com'
__license__ = 'MIT License'
