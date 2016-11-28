# -*- coding: utf-8 -*-

"""
:copyright: (c) 2016 by Likid Geimfari <likid.geimfari@gmail.com>.
:software_license: MIT, see LICENSES for more details.
:repository: https://github.com/lk-geimfari/elizabeth
:contributors: https://github.com/lk-geimfari/elizabeth/blob/master/CONTRIBUTORS.md
"""

from .elizabeth import (
    Address, Personal, Network, Datetime,
    Development, File, Science, Numbers,
    Food, Hardware, Text, Business, Code,
    ClothingSizes, Internet, Transport,
    Generic
)

# Data for setup.py
__version__ = '0.3.0'
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
    'Network',
    'Numbers',
    'Path',
    'Personal',
    'Science',
    'Text',
    'Transport',
    'Generic'
]
