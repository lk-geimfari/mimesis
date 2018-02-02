"""Provides all at one."""

import inspect
from typing import List

from mimesis.providers.address import Address
from mimesis.providers.base import BaseDataProvider
from mimesis.providers.business import Business
from mimesis.providers.clothing import ClothingSize
from mimesis.providers.code import Code
from mimesis.providers.cryptographic import Cryptographic
from mimesis.providers.date import Datetime
from mimesis.providers.development import Development
from mimesis.providers.file import File
from mimesis.providers.food import Food
from mimesis.providers.games import Games
from mimesis.providers.hardware import Hardware
from mimesis.providers.internet import Internet
from mimesis.providers.numbers import Numbers
from mimesis.providers.path import Path
from mimesis.providers.payment import Payment
from mimesis.providers.person import Person
from mimesis.providers.science import Science
from mimesis.providers.structure import Structure
from mimesis.providers.text import Text
from mimesis.providers.transport import Transport
from mimesis.providers.units import UnitSystem

__all__ = ['Generic']


class Generic(BaseDataProvider):
    """Class which contain all providers at one."""

    def __init__(self, *args, **kwargs):
        """Initialize attributes lazily.

        :param args: Arguments.
        :param kwargs: Keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self._person = Person
        self._address = Address
        self._datetime = Datetime
        self._business = Business
        self._text = Text
        self._food = Food
        self._science = Science
        self._code = Code
        self._transport = Transport
        self.unit_system = UnitSystem(seed=self.seed)
        self.file = File(seed=self.seed)
        self.numbers = Numbers(seed=self.seed)
        self.development = Development(seed=self.seed)
        self.hardware = Hardware(seed=self.seed)
        self.clothing_size = ClothingSize(seed=self.seed)
        self.internet = Internet(seed=self.seed)
        self.path = Path(seed=self.seed)
        self.payment = Payment(seed=self.seed)
        self.games = Games(seed=self.seed)
        self.cryptographic = Cryptographic(seed=self.seed)
        self.structure = Structure(seed=self.seed)

    def __getattr__(self, attrname: str):
        """Get attribute without underscore.

        :param attrname: Attribute name.
        :return: An attribute.
        """
        attribute = object.__getattribute__(self, '_' + attrname)
        if attribute and callable(attribute):
            self.__dict__[attrname] = attribute(
                locale=self.locale,
                seed=self.seed,
            )
            return self.__dict__[attrname]

    def __dir__(self) -> List[str]:
        """Available data providers.

        :return: List of attributes.
        """
        attributes = []
        exclude = BaseDataProvider().__dict__.keys()

        for a in self.__dict__:
            if a not in exclude:
                if a.startswith('_'):
                    attribute = a.replace('_', '', 1)
                    attributes.append(attribute)
                else:
                    attributes.append(a)
        return attributes

    def add_provider(self, cls) -> None:
        """Add a custom provider to Generic() object.

        :param cls: Custom provider.
        :return: None
        :raises TypeError: if cls is not class.
        """
        if inspect.isclass(cls):
            name = ''
            if hasattr(cls, 'Meta'):
                if inspect.isclass(cls.Meta) and hasattr(cls.Meta, 'name'):
                    name = cls.Meta.name
            else:
                name = cls.__name__.lower()
            setattr(self, name, cls())
        else:
            raise TypeError('Provider must be a class')

    def add_providers(self, *providers) -> None:
        """Add a lot of custom providers to Generic() object.

        :param providers: Custom providers.
        :return: None
        """
        for provider in providers:
            self.add_provider(provider)
