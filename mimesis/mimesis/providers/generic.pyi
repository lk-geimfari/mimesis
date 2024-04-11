import typing as t

from mimesis import providers
from mimesis.locales import Locale
from mimesis.providers.base import BaseProvider
from mimesis.types import Seed

__all__ = ["Generic"]

class Generic(BaseProvider):
    locale: Locale
    # Locale-dependent providers
    person: providers.Person
    text: providers.Text
    address: providers.Address
    finance: providers.Finance
    datetime: providers.Datetime
    food: providers.Food

    # Locale-independent providers
    cryptographic: providers.Cryptographic
    binaryfile: providers.BinaryFile
    file: providers.File
    code: providers.Code
    path: providers.Path
    choice: providers.Choice
    numeric: providers.Numeric
    payment: providers.Payment
    hardware: providers.Hardware
    development: providers.Development
    internet: providers.Internet
    science: providers.Science
    transport: providers.Transport

    def __init__(self, locale: Locale = ..., seed: Seed = ...) -> None: ...

    class Meta:
        name: t.Final[str]
    def __getattr__(self, attrname: str) -> t.Any: ...
    def __dir__(self) -> list[str]: ...
    def reseed(self, seed: Seed = ...) -> None: ...
    def add_provider(self, cls: t.Type[BaseProvider], **kwargs: t.Any) -> None: ...
    def add_providers(self, *providers: t.Type[BaseProvider]) -> None: ...
    def __iadd__(self, other: t.Type[BaseProvider]) -> Generic: ...
