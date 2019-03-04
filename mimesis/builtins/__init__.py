# -*- coding: utf-8 -*-

"""Builtin specific data providers."""

from .en import USASpecProvider
from .ru import RussiaSpecProvider
from .pt_br import BrazilSpecProvider
from .de import GermanySpecProvider
from .nl import NetherlandsSpecProvider
from .uk import UkraineSpecProvider
from .pl import PolandSpecProvider
from .da import DenmarkSpecProvider

__all__ = [
    'USASpecProvider',
    'RussiaSpecProvider',
    'BrazilSpecProvider',
    'GermanySpecProvider',
    'NetherlandsSpecProvider',
    'UkraineSpecProvider',
    'PolandSpecProvider',
    'DenmarkSpecProvider',
]
