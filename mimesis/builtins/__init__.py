"""Builtin specific data providers."""

from .da import DenmarkSpecProvider
from .en import USASpecProvider
from .it import ItalySpecProvider
from .nl import NetherlandsSpecProvider
from .pl import PolandSpecProvider
from .pt_br import BrazilSpecProvider
from .ru import RussiaSpecProvider

__all__ = [
    "USASpecProvider",
    "RussiaSpecProvider",
    "BrazilSpecProvider",
    "NetherlandsSpecProvider",
    "PolandSpecProvider",
    "DenmarkSpecProvider",
    "ItalySpecProvider",
]
