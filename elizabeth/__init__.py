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
    Food, Hardware, Text, Business, Generic
)

# Data for setup.py
__version__ = '0.2.8'
__author__ = 'Likid Geimfari'

__all__ = ['Address', 'Personal',
           'Text', 'Network',
           'Datetime', 'File',
           'Science', 'Development',
           'Food', 'Hardware',
           'Numbers', 'Business',
           'Generic',
           ]
