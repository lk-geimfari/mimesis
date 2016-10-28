# -*- coding: utf-8 -*-

"""
:copyright: (c) 2016 by Likid Geimfari <likid.geimfari@gmail.com>.
:software_license: MIT, see LICENSES for more details.
:repository: https://github.com/lk-geimfari/church
:contributors: https://github.com/lk-geimfari/church/blob/master/CONTRIBUTORS.md
"""

from .church import (
    Address, Personal, Network, Datetime,
    Development, File, Science, Numbers,
    Food, Hardware, Text, Business, Church
)

# Data for setup.py
__version__ = '0.2.7'
__author__ = 'Likid Geimfari'

__all__ = ['Address', 'Personal',
           'Text', 'Network',
           'Datetime', 'File',
           'Science', 'Development',
           'Food', 'Hardware',
           'Numbers', 'Business',
           'Church',
           ]
