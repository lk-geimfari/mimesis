# -*- coding: utf-8 -*-

"""Elizabeth is a fast and easy to use Python library for generating dummy data
for a variety of purposes.

This data can be particularly useful during software development and testing.
For example, it could be used to populate a testing database for a web application with
user information such as email addresses, usernames, first names, last names, etc.
Elizabeth uses a JSON-based datastore and does not require any modules that are not in the Python
standard library. There are over nineteen different data providers available,
which can produce data related to food, people, computer hardware, transportation, addresses, and more.

Copyright (c) 2016 Likid Geimfari (Isaak Uchakaev)  <likid.geimfari@gmail.com>
Repository: https://github.com/lk-geimfari/elizabeth
"""

from elizabeth.core import *

__version__ = '0.3.30'
__author__ = 'Likid Geimfari'

__all__ = [
    'Address',
    'Business',
    'ClothingSizes',
    'Code',
    'Datetime',
    'Development',
    'File',
    'Food',
    'Hardware',
    'Internet',
    'Numbers',
    'Path',
    'Personal',
    'Science',
    'Structured',
    'Text',
    'Transport',
    'UnitSystem',
    'Generic'
]
