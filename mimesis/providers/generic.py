"""Provides all at one."""

import inspect
import typing as t

from mimesis.locales import Locale
from mimesis.providers.address import Address
from mimesis.providers.base import BaseDataProvider, BaseProvider
from mimesis.providers.binaryfile import BinaryFile
from mimesis.providers.choice import Choice
from mimesis.providers.code import Code
from mimesis.providers.cryptographic import Cryptographic
from mimesis.providers.date import Datetime
from mimesis.providers.development import Development
from mimesis.providers.file import File
from mimesis.providers.finance import Finance
from mimesis.providers.food import Food
from mimesis.providers.hardware import Hardware
from mimesis.providers.internet import Internet
from mimesis.providers.numeric import Numeric
from mimesis.providers.path import Path
from mimesis.providers.payment import Payment
from mimesis.providers.person import Person
from mimesis.providers.science import Science
from mimesis.providers.text import Text
from mimesis.providers.transport import Transport
from mimesis.types import MissingSeed, Seed

__all__ = ["Generic"]

DEFAULT_PROVIDERS = (
    Address,
    BinaryFile,
    Finance,
    Choice,
    Code,
    Choice,
    Datetime,
    Development,
    File,
    Food,
    Hardware,
    Internet,
    Numeric,
    Path,
    Payment,
    Person,
    Science,
    Text,
    Transport,
    Cryptographic,
)


class Generic(BaseProvider):
    """Class which contain all providers at one."""

    def __init__(
        self,
        locale: Locale = Locale.DEFAULT,
        seed: Seed = MissingSeed,
    ) -> None:
        """Initialize attributes lazily."""
        super().__init__(seed=seed)
        self.locale = locale

        for provider in DEFAULT_PROVIDERS:
            name = getattr(provider.Meta, "name")  # type: ignore

            # Check if a provider is locale-dependent.
            if issubclass(provider, BaseDataProvider):
                setattr(self, f"_{name}", provider)
            elif issubclass(provider, BaseProvider):
                setattr(self, name, provider(seed=self.seed))

    class Meta:
        """Class for metadata."""

        name: t.Final[str] = "generic"

    def __getattr__(self, attrname: str) -> t.Any:
        """Get attribute without an underscore.

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

    def __dir__(self) -> t.List[str]:
        """Available data providers.

        :return: List of attributes.
        """
        attributes = []
        exclude = list(BaseProvider().__dict__.keys())
        # Exclude locale explicitly because
        # it is not a provider.
        exclude.append("locale")

        for attr in self.__dict__:
            if attr not in exclude:
                if attr.startswith("_"):
                    attribute = attr.replace("_", "", 1)
                    attributes.append(attribute)
                else:
                    attributes.append(attr)
        return attributes

    def reseed(self, seed: Seed = MissingSeed) -> None:
        """Reseed the internal random generator.

        Overrides method `BaseProvider.reseed()`.

        :param seed: Seed for random.
        :return: None.
        """
        # Make sure to reseed the random generator on Generic itself.
        super().reseed(seed)

        for attr in self.__dir__():
            try:
                provider = getattr(self, attr)
                provider.reseed(seed)
            except AttributeError:
                continue

    def add_provider(self, cls: t.Type[BaseProvider], **kwargs: t.Any) -> None:
        """Add a custom provider to a Generic() object.

        :param cls: Custom provider.
        :param kwargs: Keyword arguments for provider.
        :raises TypeError: if cls is Generic, if cls is not
            class or is not a subclass of BaseProvider.
        :return: Absolutely none.
        """

        if inspect.isclass(cls):
            if not issubclass(cls, BaseProvider):
                raise TypeError(
                    "The provider must be a "
                    "subclass of mimesis.providers.BaseProvider"
                )
            try:
                name = cls.Meta.name
            except AttributeError:
                name = cls.__name__.lower()

            # Enforce the same seed is used across all providers.
            kwargs.pop("seed", None)

            instance = cls(seed=self.seed, **kwargs)
            if isinstance(instance, Generic):
                raise TypeError("Cannot add Generic instance to itself.")
            setattr(self, name, instance)
        else:
            raise TypeError("The provider must be a class")

    def add_providers(self, *providers: t.Type[BaseProvider]) -> None:
        """Add numerous custom providers to the :class:`Generic` object.

        This method is a convenience method for adding multiple providers
        at once. It is equivalent to calling :meth:`add_provider` for each
        provider in the list of providers.

        Example:

        >>> from mimesis import Generic
        >>> from myproviders import ProviderA, ProviderB
        >>> g = Generic()
        >>> g.add_providers(ProviderA, ProviderB)
        >>> g.providera.never()
        >>> g.providerb.gonna()

        If you want to pass keyword arguments to the providers, you can
        do so by using :meth:`add_provider` instead.

        :param providers: Custom providers.
        :return: None
        """
        for provider in providers:
            self.add_provider(provider)

    def __iadd__(self, other: t.Type[BaseProvider]) -> "Generic":
        """Add a custom provider to a Generic() object.

        :param other: Custom provider.
        :return: None
        :raises TypeError: if cls is not class or is not a subclass
            of BaseProvider.
        """
        self.add_provider(other)
        return self

    def __str__(self) -> str:
        """Human-readable representation of locale."""
        return f"{self.__class__.__name__} <{self.locale}>"
