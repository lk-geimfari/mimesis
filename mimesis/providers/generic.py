# -*- coding: utf-8 -*-

"""Provides all at one."""

import inspect
from typing import Any, List, Type

from mimesis.providers.address import Address
from mimesis.providers.base import BaseDataProvider, BaseProvider
from mimesis.providers.business import Business
from mimesis.providers.choice import Choice
from mimesis.providers.clothing import Clothing
from mimesis.providers.code import Code
from mimesis.providers.cryptographic import Cryptographic
from mimesis.providers.date import Datetime
from mimesis.providers.development import Development
from mimesis.providers.file import File
from mimesis.providers.food import Food
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

    def __init__(self, *args, **kwargs) -> None:
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
        self.transport = Transport(seed=self.seed)
        self.code = Code(seed=self.seed)
        self.unit_system = UnitSystem(seed=self.seed)
        self.file = File(seed=self.seed)
        self.numbers = Numbers(seed=self.seed)
        self.development = Development(seed=self.seed)
        self.hardware = Hardware(seed=self.seed)
        self.clothing = Clothing(seed=self.seed)
        self.internet = Internet(seed=self.seed)
        self.path = Path(seed=self.seed)
        self.payment = Payment(seed=self.seed)
        self.cryptographic = Cryptographic(seed=self.seed)
        self.structure = Structure(seed=self.seed)
        self.choice = Choice(seed=self.seed)

    class Meta:
        """Class for metadata."""

        name = 'generic'

    def __getattr__(self, attrname: str) -> Any:
        """Get attribute without underscore.

        :param attrname: Attribute name.
        :return: An attribute.
        """
        attribute = object.__getattribute__(
            self, '_' + attrname)
        if attribute and callable(attribute):
            self.__dict__[attrname] = attribute(
                self.locale,
                self.seed,
            )
            return self.__dict__[attrname]

    def __dir__(self) -> List[str]:
        """Available data providers.

        The list of result will be used in AbstractField to
        determine method's class.

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

    def add_provider(self, cls: Type[BaseProvider]) -> None:
        """Add a custom provider to Generic() object.

        :param cls: Custom provider.
        :return: None
        :raises TypeError: if cls is not class or is not a subclass
            of BaseProvider.
        """
        if inspect.isclass(cls):
            if not issubclass(cls, BaseProvider):
                raise TypeError('The provider must be a '
                                'subclass of BaseProvider')
            try:
                meta = getattr(cls, 'Meta')
                name = getattr(meta, 'name')
            except AttributeError:
                name = cls.__name__.lower()
            setattr(self, name, cls(seed=self.seed))
        else:
            raise TypeError('The provider must be a class')

    def add_providers(self, *providers: Type[BaseProvider]) -> None:
        """Add a lot of custom providers to Generic() object.

        :param providers: Custom providers.
        :return: None
        """
        for provider in providers:
            self.add_provider(provider)
