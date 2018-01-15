"""Builtin specific data providers."""

from .en import USASpecProvider
from .ja import JapanSpecProvider
from .ru import RussiaSpecProvider
from .pt_br import BrazilSpecProvider
from .de import GermanySpecProvider
from .nl import NetherlandsSpecProvider
from .uk import UkraineSpecProvider

__all__ = [
    'USASpecProvider',
    'JapanSpecProvider',
    'RussiaSpecProvider',
    'BrazilSpecProvider',
    'GermanySpecProvider',
    'NetherlandsSpecProvider',
    'UkraineSpecProvider',
]
