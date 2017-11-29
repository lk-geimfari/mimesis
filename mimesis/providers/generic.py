import inspect

from mimesis.providers.address import Address
from mimesis.providers.base import BaseProvider
from mimesis.providers.business import Business
from mimesis.providers.clothing import ClothingSizes
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
from mimesis.providers.personal import Personal
from mimesis.providers.science import Science
from mimesis.providers.text import Text
from mimesis.providers.transport import Transport
from mimesis.providers.units import UnitSystem

GENERIC_ATTRS = [
    'address',
    'business',
    'clothing_sizes',
    'code',
    'cryptographic',
    'datetime',
    'development',
    'file',
    'food',
    'games',
    'hardware',
    'internet',
    'numbers',
    'path',
    'payment',
    'personal',
    'science',
    'text',
    'transport',
    'unit_system',
]


class Generic(BaseProvider):
    """A lazy initialization of locale for all classes that have locales."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._personal = Personal
        self._address = Address
        self._datetime = Datetime
        self._business = Business
        self._text = Text
        self._food = Food
        self._science = Science
        self._code = Code
        self._transport = Transport
        self.unit_system = UnitSystem()
        self.file = File()
        self.numbers = Numbers()
        self.development = Development()
        self.hardware = Hardware()
        self.clothing_sizes = ClothingSizes()
        self.internet = Internet()
        self.path = Path()
        self.payment = Payment()
        self.games = Games()
        self.cryptographic = Cryptographic()

    def __getattr__(self, attrname):
        """Get _attribute without underscore

        :param attrname: Attribute name.
        :return: An attribute.
        """
        attribute = object.__getattribute__(self, '_' + attrname)
        if attribute and callable(attribute):
            return attribute(self.locale)

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
