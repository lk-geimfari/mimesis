"""Mimesis is a Python library, which helps generate synthetic data.

Copyright (c) 2016 - 2018 Likid Geimfari (Isaak Uchakaev)
Repository: https://github.com/lk-geimfari/mimesis
Email: <likid.geimfari@gmail.com>
"""

from mimesis.providers import *

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

    # Meta:
    '__version__',
    '__title__',
    '__description__',
    '__url__',
    '__author__',
    '__author_email__',
    '__license__',
]

__version__ = '3.0.0'
__title__ = 'mimesis'
__description__ = 'Mimesis: fake data generator.'
__url__ = 'https://github.com/lk-geimfari/mimesis'
__author__ = 'Likid Geimfari (Isaak Uchakaev)'
__author_email__ = 'likid.geimfari@gmail.com'
__license__ = 'MIT License'
