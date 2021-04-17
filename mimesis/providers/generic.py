# -*- coding: utf-8 -*-

"""Provides all at one."""

import inspect
from typing import Any, List, Optional, Type

from mimesis.locales import DEFAULT_LOCALE
from mimesis.providers.address import Address
from mimesis.providers.base import BaseDataProvider, BaseProvider
from mimesis.providers.binaryfile import BinaryFile
from mimesis.providers.choice import Choice
from mimesis.providers.clothing import Clothing
from mimesis.providers.code import Code
from mimesis.providers.cryptographic import Cryptographic
from mimesis.providers.date import Datetime
from mimesis.providers.development import Development
from mimesis.providers.file import File
from mimesis.providers.finance import Finance
from mimesis.providers.food import Food
from mimesis.providers.hardware import Hardware
from mimesis.providers.internet import Internet
from mimesis.providers.numbers import Numbers
from mimesis.providers.path import Path
from mimesis.providers.payment import Payment
from mimesis.providers.person import Person
from mimesis.providers.science import Science
from mimesis.providers.text import Text
from mimesis.providers.transport import Transport
from mimesis.typing import Seed

__all__ = ["Generic"]


class Generic(BaseProvider):
    """Class which contain all providers at one."""

    _DEFAULT_PROVIDERS = (
        Address,
        BinaryFile,
        Finance,
        Choice,
        Clothing,
        Code,
        Choice,
        Datetime,
        Development,
        File,
        Food,
        Hardware,
        Internet,
        Numbers,
        Path,
        Payment,
        Person,
        Science,
        Text,
        Transport,
        Cryptographic,
    )

    def __init__(
        self, locale: str = DEFAULT_LOCALE, seed: Optional[Seed] = None
    ) -> None:
        """Initialize attributes lazily."""
        super().__init__(seed=seed)
        self.locale = locale

        for provider in self._DEFAULT_PROVIDERS:
            name = getattr(provider.Meta, "name")  # type: ignore

            # Check if a provider is locale dependent.
            if hasattr(provider, "_data"):
                setattr(self, f"_{name}", provider)
            else:
                setattr(self, name, provider(seed=self.seed))

    class Meta:
        """Class for metadata."""

        name = "generic"

    def __getattr__(self, attrname: str) -> Any:
        """Get attribute without underscore.

        :param attrname: Attribute name.
        :return: An attribute.
        """
        attribute = object.__getattribute__(self, "_" + attrname)
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
                if a.startswith("_"):
                    attribute = a.replace("_", "", 1)
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
                raise TypeError(
                    "The provider must be a "
                    "subclass of mimesis.providers.BaseProvider"
                )
            try:
                meta = getattr(cls, "Meta")
                name = getattr(meta, "name")
            except AttributeError:
                name = cls.__name__.lower()
            setattr(self, name, cls(seed=self.seed))
        else:
            raise TypeError("The provider must be a class")

    def add_providers(self, *providers: Type[BaseProvider]) -> None:
        """Add a lot of custom providers to Generic() object.

        :param providers: Custom providers.
        :return: None
        """
        for provider in providers:
            self.add_provider(provider)

    def __str__(self) -> str:
        """Human-readable representation of locale."""
        return "{} <{}>".format(self.__class__.__name__, self.locale)
