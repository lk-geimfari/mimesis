# -*- coding: utf-8 -*-

"""Builtin specific data providers."""

from .da import DenmarkSpecProvider
from .de import GermanySpecProvider
from .en import USASpecProvider
from .it import ItalySpecProvider
from .nl import NetherlandsSpecProvider
from .pl import PolandSpecProvider
from .pt_br import BrazilSpecProvider
from .ru import RussiaSpecProvider
from .uk import UkraineSpecProvider

__all__ = [
    'USASpecProvider',
    'RussiaSpecProvider',
    'BrazilSpecProvider',
    'GermanySpecProvider',
    'NetherlandsSpecProvider',
    'UkraineSpecProvider',
    'PolandSpecProvider',
    'DenmarkSpecProvider',
    'ItalySpecProvider',
]
