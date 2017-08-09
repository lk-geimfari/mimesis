import inspect

from mimesis.providers import (Address, BaseProvider, Business, ClothingSizes,
                               Code, Datetime, Development, File, Food, Games,
                               Hardware, Internet, Numbers, Path, Personal,
                               Science, Text, Transport, UnitSystem,
                               Cryptographic)


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
            raise TypeError('Provider must be a class')

    def add_providers(self, *providers):
        """Add a lot of custom providers to Generic() object.

        :param providers: Custom providers.
        :return: None
        """
        for provider in providers:
            self.add_provider(provider)
