import inspect

from .base import BaseProvider
from .address import Address
from .business import Business
from .clothing import ClothingSizes
from .code import Code
from .date import Datetime
from .development import Development
from .file import File
from .food import Food
from .hardware import Hardware
from .internet import Internet
from .numbers import Numbers
from .path import Path
from .personal import Personal
from .science import Science
from .text import Text
from .transport import Transport
from .units import UnitSystem


class Generic(BaseProvider):
    """A lazy initialization of locale for all classes that have locales."""

    def __init__(self, locale):
        """
        :param locale: Current locale.
        """
        self.locale = locale
        self._personal = Personal
        self._address = Address
        self._datetime = Datetime
        self._business = Business
        self._text = Text
        self._food = Food
        self._science = Science
        self._code = Code
        self.unit_system = UnitSystem()
        self.file = File()
        self.numbers = Numbers()
        self.development = Development()
        self.hardware = Hardware()
        self.clothing_sizes = ClothingSizes()
        self.internet = Internet()
        self.transport = Transport()
        self.path = Path()

    def __getattr__(self, attrname):
        """Get _attribute without underscore

        :param attrname: Attribute name.
        :return: An attribute.
        """
        attribute = object.__getattribute__(self, '_' + attrname)
        if attribute and callable(attribute):
            attribute = attribute(self.locale)
            return attribute

    def add_provider(self, cls):
        """Add a custom provider to Generic() object.

        :param cls: Custom provider.
        :return: None
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
            raise TypeError("Provider must be a class")

    def add_providers(self, *providers):
        """Add a lot of custom providers to Generic() object.

        :param providers: Custom providers.
        :return: None
        """
        for provider in providers:
            self.add_provider(provider)
